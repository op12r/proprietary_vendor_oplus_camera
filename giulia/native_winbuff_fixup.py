# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

"""
libNativeWinBuffExchange.so fixup for AOSP-17 buffer queue ABI.

The blob calls IGraphicBufferConsumer::releaseBuffer through the vtable
using the legacy 5-argument ABI (slot, frameNumber, eglDisplay, eglFence,
fence) where the Fence reference lives in x5. AOSP 17 (with
bq_gl_fence_cleanup enabled) ships the modern 3-argument ABI where the
Fence reference lives in x3.

This patch rewrites the argument setup so the fence pointer lands in x3:
    mov x3, xzr   ->   mov x3, x5

The surrounding instruction sequence is content-verified so the patch
fails loudly if a firmware update changes the blob's code generation.
"""

from pathlib import Path
from typing import Final


# The call-site sequence in attachHardwareBufferToBufferQ leading up to the
# vtable dispatch of releaseBuffer (28 bytes, unique within the blob).
#
#   add x5, sp, #0          ; x5 = &fakeFence (legacy fence position)
#   mov x0, x20             ; this
#   mov x2, xzr             ; frameNumber = 0
#   mov x3, xzr             ; legacy eglDisplay = 0   <-- byte 15 patched
#   ldr x8, [x8, #0x48]    ; vtable slot: releaseBuffer
#   mov x4, xzr             ; legacy eglFence = 0
#   blr  x8                 ; dispatch
_CALL_SEQUENCE: Final = bytes.fromhex(
    "e5030091"
    "e00314aa"
    "e2031faa"
    "e3031faa"
    "082540f9"
    "e4031faa"
    "00013fd6"
)

# Byte offset within _CALL_SEQUENCE of the Rm register field in the
# `mov x3, ...` instruction (instruction starts at offset 12, Rm is in
# byte 2 of the little-endian encoding).
_PATCH_OFFSET: Final = 14

_STOCK_BYTE: Final = 0x1F  # xzr (legacy: eglDisplay = null)
_PATCHED_BYTE: Final = 0x05  # x5  (modern: fence reference)


class NativeWinBuffExchangeFixupError(RuntimeError):
    pass


def patch_native_win_buff_exchange(blob: bytes) -> bytes:
    """Patch releaseBuffer call from legacy 5-arg ABI to modern 3-arg ABI."""

    count = blob.count(_CALL_SEQUENCE)
    if count == 0:
        raise NativeWinBuffExchangeFixupError(
            "libNativeWinBuffExchange: releaseBuffer call sequence not found"
        )
    if count > 1:
        raise NativeWinBuffExchangeFixupError(
            f"libNativeWinBuffExchange: call sequence found {count} times "
            "(expected exactly 1)"
        )

    offset = blob.index(_CALL_SEQUENCE) + _PATCH_OFFSET
    if blob[offset] != _STOCK_BYTE:
        raise NativeWinBuffExchangeFixupError(
            f"libNativeWinBuffExchange: byte at {offset:#x} is "
            f"{blob[offset]:#04x}, expected {_STOCK_BYTE:#04x}"
        )

    patched = bytearray(blob)
    patched[offset] = _PATCHED_BYTE
    return bytes(patched)


def patch_native_win_buff_exchange_file(file_path: str) -> None:
    path = Path(file_path)
    path.write_bytes(patch_native_win_buff_exchange(path.read_bytes()))
