# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from typing import Final

_CALL_SEQUENCE: Final = bytes.fromhex(
    "e5030091"
    "e00314aa"
    "e2031faa"
    "e3031faa"
    "082540f9"
    "e4031faa"
    "00013fd6"
)

_PATCH_OFFSET: Final = 14

_STOCK_BYTE: Final = 0x1F
_PATCHED_BYTE: Final = 0x05

class NativeWinBuffExchangeFixupError(RuntimeError):
    pass

def patch_native_win_buff_exchange(blob: bytes) -> bytes:

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
