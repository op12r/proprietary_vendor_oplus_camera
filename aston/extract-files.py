#!/usr/bin/env -S PYTHONPATH=../../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2016 The CyanogenMod Project
# SPDX-FileCopyrightText: 2017-2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import List, NamedTuple, Tuple

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.utils import Color, color_print, run_cmd
from native_winbuff_fixup import patch_native_win_buff_exchange_file

def lib_fixup_system_ext_suffix(lib: str, partition: str, *args, **kwargs):
    if partition != 'system_ext':
        return None

    system_ext_libs = {
        'libSuperTextWrapper',
        'libXDocProcessSDK',
        'libYTCommon',
        'libmpbase',
        'libextendfile',
    }

    return f'{lib}_system_ext' if lib in system_ext_libs else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libSuperTextWrapper',
        'libXDocProcessSDK',
        'libYTCommon',
        'libmpbase',
        'libextendfile',
    ): lib_fixup_system_ext_suffix,
}

def blob_fixup_native_winbuff_exchange(ctx, file, file_path, *args, **kwargs):
    patch_native_win_buff_exchange_file(file_path)

def blob_fixup_opluscamera_privapp_linker_ns(
    ctx, file, file_path, *args, tmp_dir=None, **kwargs
):
    """
    Keep OplusCamera on the system_ext priv-app linker path that can resolve
    libvndksupport for libJniMetaTransform (capture APS meta path).

    When OplusCamera gets installed as an update under /data/app, its JNI
    libs are extracted to lib/arm64/ and the app classloader namespace can't
    see /system/lib64/libvndksupport.so, so still capture throws
    UnsatisfiedLinkError. Loading from the system_ext priv-app APK goes
    through the shared namespace and works.

    Hardening applied on every extract:
      1) android:extractNativeLibs="false" so PackageManager loads the libs
         straight from the APK.
      2) Drop android.permission.CONTROL_KEYGUARD. PackageManager refuses
         uninstall-system-updates for packages holding it, which traps an
         accidental adb-installed update in the broken /data state. The
         secure camera still works through showWhenLocked and
         SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE.
    """
    if tmp_dir is None:
        return

    manifest = Path(tmp_dir) / 'AndroidManifest.xml'
    if not manifest.exists():
        print('OplusCamera: warning: AndroidManifest.xml missing for linker-ns fixup')
        return

    data = manifest.read_text(encoding='utf-8')
    original = data
    changed = []

    # Force extractNativeLibs=false on <application ...>
    if re.search(r'android:extractNativeLibs\s*=\s*"true"', data):
        data = re.sub(
            r'android:extractNativeLibs\s*=\s*"true"',
            'android:extractNativeLibs="false"',
            data,
            count=1,
        )
        changed.append('extractNativeLibs=false')
    elif 'android:extractNativeLibs=' not in data:
        # Insert on the application tag (first match).
        new_data, n = re.subn(
            r'(<application\b)(\s)',
            r'\1 android:extractNativeLibs="false"\2',
            data,
            count=1,
        )
        if n:
            data = new_data
            changed.append('extractNativeLibs=false (inserted)')
    # else already false, leave it alone

    # Remove the CONTROL_KEYGUARD uses-permission (self-closing or paired).
    perm_re = re.compile(
        r'[ \t]*<uses-permission\b[^>]*android:name\s*=\s*'
        r'"android\.permission\.CONTROL_KEYGUARD"[^>]*/>\s*\n?'
        r'|[ \t]*<uses-permission\b[^>]*android:name\s*=\s*'
        r'"android\.permission\.CONTROL_KEYGUARD"[^>]*>\s*'
        r'</uses-permission>\s*\n?',
        re.MULTILINE,
    )
    data2, n = perm_re.subn('', data)
    if n:
        data = data2
        changed.append(f'removed CONTROL_KEYGUARD (x{n})')

    if data != original:
        manifest.write_text(data, encoding='utf-8')
        print('OplusCamera: priv-app linker ns fixup: ' + ', '.join(changed))
    else:
        print('OplusCamera: priv-app linker ns fixup already applied')

# =====================================================================
# Post-patch verification
#
# A rejected hunk already raises: patch_dir runs `git apply`, and run_cmd
# turns a non-zero exit into ValueError. What nothing catches is the silent
# case: a .call() fixup whose anchor drifted finds nothing, returns, and the
# blob ships unpatched while the extract reports success. So every patch
# below asserts a marker in the decoded tree just before it is packed.
# Failures are collected, not raised, so one run reports every broken patch.
#
# Adding a patch means adding its marker here. Pick something the patch
# itself introduces (a label, an injected const-string, a new class), not
# something that merely sits near it. Every marker below is taken from a
# line our aston patches add or remove.
# =====================================================================

VERIFY_RESULTS: List[Tuple[str, str, bool]] = []

class Check(NamedTuple):
    what: str
    needle: str
    # Basename glob (searched recursively) or a concrete path under tmp_dir.
    where: str = '*.smali'
    present: bool = True

def _check_hit(root: Path, chk: Check) -> bool:
    # Concrete path: read it. Covers binary AXML too (--no-res extracts leave
    # AndroidManifest.xml packed), hence the utf-16 fallback for its string pool.
    if '*' not in chk.where and '?' not in chk.where:
        target = root / chk.where
        if not target.is_file():
            return False
        raw = target.read_bytes()
        return (
            chk.needle.encode() in raw or chk.needle.encode('utf-16-le') in raw
        )

    try:
        out = run_cmd([
            'grep',
            '-rlaF',
            '--include',
            chk.where,
            '-e',
            chk.needle,
            str(root),
        ])
    except ValueError:
        return False  # grep exits 1 when nothing matches

    return bool(out.strip())

def verify(label: str, *checks: Check):
    def impl(ctx, file, file_path, *args, tmp_dir=None, **kwargs):
        if tmp_dir is None:
            return
        root = Path(tmp_dir)
        for chk in checks:
            ok = _check_hit(root, chk) == chk.present
            # A missing file can't prove a removal: without this, an absence
            # check on AndroidManifest.xml passes when the manifest was never
            # decoded at all.
            concrete = '*' not in chk.where and '?' not in chk.where
            if not chk.present and concrete and not (root / chk.where).is_file():
                ok = False
            VERIFY_RESULTS.append((label, chk.what, ok))

    return impl

OPLUSCAMERA_CHECKS = (
    # patches/0001: OPlus fonts swapped for the system default typeface.
    Check(
        '0001 default font',
        'Landroid/graphics/Typeface;->DEFAULT:Landroid/graphics/Typeface;',
        'smali/d6/t3.smali',
    ),
    # patches/0002: the oplus-only android:permission attributes are removed.
    Check(
        '0002 oplus perms stripped',
        'android:permission="oplus.permission.OPLUS_COMPONENT_SAFE"',
        'AndroidManifest.xml',
        False,
    ),
    # patches/0003: the AnyGallery helper class it adds.
    Check('0003 any gallery', 'Lco/aospa/camera/AnyGallery;'),
    # patches/0004: the labels it adds in module/a, jh/t0 and h8/c.
    Check('0004 120fps high speed session', ':cond_fps120_passthru'),
    Check('0004 120fps recorder rate', ':cond_fps_not_high'),
    Check('0004 120fps fps helper', ':cond_fps120_ok'),
    Check('0005 120fps features reported', ':goto_aston_120fps_done'),
    # blob_fixup_opluscamera_privapp_linker_ns
    Check(
        'linker-ns extractNativeLibs=false',
        'android:extractNativeLibs="false"',
        'AndroidManifest.xml',
    ),
    Check(
        'linker-ns CONTROL_KEYGUARD dropped',
        'android.permission.CONTROL_KEYGUARD',
        'AndroidManifest.xml',
        False,
    ),
)

SDK_CHECKS = (
    # patches-sdk/0001: library load guard field in ApsHelper and friends.
    Check('0001 fixes', '.field private static sLibraryLoaded:Z'),
    # patches-sdk/0002: facebeauty probes the system_ext lib path.
    Check(
        '0002 facebeauty probe path',
        '/system_ext/lib64/libApsFaceBeautyPreviewProductJni.so',
    ),
    # patches-sdk/0003: video_120fps skipped in isFeatureConfigLegal. The
    # string itself exists in the stock class, so match the comment the
    # patch adds instead.
    Check(
        '0003 120fps unlock',
        '# The 12R camera HAL exposes 1080p and 4K constrained high speed at',
        'smali/com/oplus/ocs/camera/producer/decision/OperationModeDecision.smali',
    ),
)

GALLERY_CHECKS = (
    # patches-gallery/0001: oppo-only android:permission attributes removed.
    Check(
        '0001 oppo perms stripped',
        'android:permission="oppo.permission.OPPO_COMPONENT_SAFE"',
        'AndroidManifest.xml',
        False,
    ),
    # patches-gallery/0002: RECEIVER_NOT_EXPORTED injection label.
    Check('0002 RECEIVER_NOT_EXPORTED', ':cond_no_or'),
    # patches-gallery/0003: PhotoEditor theme items.
    Check(
        '0003 PhotoEditor theme items',
        'de_toolkit_stroke_size_tint',
        'res/values/styles.xml',
    ),
    # patches-gallery/0004: live photo key handling.
    Check(
        '0004 live photos',
        '# Save original key (p0) into v3 before it gets overwritten',
        'smali/com/oplus/aiunit/vision/f4a.smali',
    ),
)

# Repacked archives, checked after the extract as shipped in the blob repo.
# OppoGallery2 is left out: aston/proprietary-files.txt doesn't list it (we
# ship no OPlus gallery), so its fixup and GALLERY_CHECKS only run if it is
# ever added back.
PATCHED_BLOBS = (
    'system_ext/priv-app/OplusCamera/OplusCamera.apk',
    'system_ext/framework/com.oplus.camera.unit.sdk.jar',
)

def verify_packed_artifacts():
    # The in-tree checks run on the decoded tree, so they still pass if
    # apktool_pack then writes a truncated archive, or if a later re-extract
    # overwrites the patched blob with the stock one. Read the central
    # directory of what actually landed in the blob repo.
    out = Path(__file__).resolve().parent / 'blobs' / 'proprietary'
    for rel in PATCHED_BLOBS:
        name = Path(rel).name
        target = out / rel
        if not target.is_file():
            VERIFY_RESULTS.append((name, 'present in blob repo', False))
            continue
        try:
            with zipfile.ZipFile(target) as z:
                names = z.namelist()
        except (zipfile.BadZipFile, OSError):
            VERIFY_RESULTS.append((name, 'repacked archive readable', False))
            continue
        VERIFY_RESULTS.append((name, 'repacked archive readable', True))
        VERIFY_RESULTS.append((
            name,
            'contains dex',
            any(n.endswith('.dex') for n in names),
        ))

def report_verification() -> bool:
    if not VERIFY_RESULTS:
        color_print('\nno patch verification ran', color=Color.RED)
        return False

    width = max(len(f'{label}: {what}') for label, what, _ in VERIFY_RESULTS)
    failed = [r for r in VERIFY_RESULTS if not r[2]]

    print('\n=== patch verification ===')
    for label, what, ok in VERIFY_RESULTS:
        color_print(
            f'{label}: {what}'.ljust(width) + ('   OK' if ok else '   FAILED'),
            color=Color.GREEN if ok else Color.RED,
        )

    if failed:
        color_print(
            f'\n{len(failed)} of {len(VERIFY_RESULTS)} checks FAILED, the blobs '
            'above shipped without the change they are supposed to carry. Re-derive '
            'the anchor against this dump before building.',
            color=Color.RED,
        )
        return False

    color_print(
        f'\nall {len(VERIFY_RESULTS)} checks passed', color=Color.GREEN
    )
    return True

blob_fixups = {
    'system_ext/lib64/libAPSClient-cmd-jni.so': blob_fixup()
        .binary_regex_replace(b'libHeifEncoderWrapper\\.so', b'xibHeifEncoderWrapper.so')
        .binary_regex_replace(b'libNativeWinBuffExchange\\.so', b'xibNativeWinBuffExchange.so'),
    'system_ext/lib64/libNativeWinBuffExchange.so': blob_fixup()
        .call(blob_fixup_native_winbuff_exchange),
    'system_ext/lib64/libAPSClient-cmd-jni-extension.oplus.so': blob_fixup()
        .binary_regex_replace(b'libHeifEncoderWrapper\\.so', b'xibHeifEncoderWrapper.so')
        .binary_regex_replace(b'libNativeWinBuffExchange\\.so', b'xibNativeWinBuffExchange.so'),
    'system_ext/lib64/libcsextimpl.so': blob_fixup()
        .replace_needed(
            'android.hardware.camera.provider-V3-ndk.so',
            'android.hardware.camera.provider-V4-ndk.so',)
        .replace_needed(
            'android.hardware.camera.device-V3-ndk.so',
            'android.hardware.camera.device-V4-ndk.so',)
        .replace_needed('libbase.so', 'libbase-stock.so'),
    # Same as apktool_patch('patches'), split up so the linker namespace fixup
    # can edit the decoded manifest before the APK is packed again.
    'system_ext/priv-app/OplusCamera/OplusCamera.apk': blob_fixup()
        .apktool_unpack('patches')
        .patch_dir('patches')
        .call(blob_fixup_opluscamera_privapp_linker_ns)
        .call(verify('OplusCamera', *OPLUSCAMERA_CHECKS))
        .apktool_pack()
        .stripzip(),
    # apktool_patch() expanded so the patches can be verified before packing.
    'system_ext/framework/com.oplus.camera.unit.sdk.jar': blob_fixup()
        .apktool_unpack('patches-sdk')
        .patch_dir('patches-sdk')
        .call(verify('sdk.jar', *SDK_CHECKS))
        .apktool_pack()
        .stripzip(),
    # apktool_patch() expanded so the patches can be verified before packing.
    'system_ext/priv-app/OppoGallery2/OppoGallery2.apk': blob_fixup()
        .apktool_unpack('patches-gallery')
        .patch_dir('patches-gallery')
        .call(verify('OppoGallery2', *GALLERY_CHECKS))
        .apktool_pack()
        .stripzip(),
    'odm/etc/init/init.camera_process.rc': blob_fixup()
        .regex_replace(
            '''on post-fs-data
    mkdir /data/vendor/camera_process 0777 camera camera
    mkdir /data/vendor/camera_process/livephoto 0777 camera camera
    mkdir /data/vendor/cam_alog 0777 camera camera
on property:sys.camera.user.removed=*
    #delete_recursion /data/vendor/camera_process/${sys.camera.user.removed}
''',
            '''on post-fs-data
    mkdir /data/vendor/camera_process 0777 camera camera
    mkdir /data/vendor/camera_process/livephoto 0777 camera camera
    mkdir /data/vendor/cam_alog 0777 camera camera
    mkdir /data/system/camera_rus 0777 cameraserver cameraserver
    mkdir /data/vendor/camera_rus 0777 camera camera
on property:sys.camera.user.removed=*
    #delete_recursion /data/vendor/camera_process/${sys.camera.user.removed}
''',
        )
}

namespace_imports = [
    'vendor/oplus/camera/aston/blobs',
    'vendor/oneplus/oneplus12r',
    'hardware/oplus',
    'vendor/qcom/common/system/audio',
    'vendor/qcom/common/system/perf',
]

module = ExtractUtilsModule(
    'blobs',
    'oplus/camera/aston',
    device_rel_path='vendor/oplus/camera/aston',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

# apktool needs a lot of scratch space for this module: OppoGallery2 is ~300 MB
# with 31 dex directories, and decoding plus repacking it needs well over 10 GB
# at once. /tmp is a tmpfs on the usual build hosts and is nowhere near that.
#
# The failure is badly disguised. When the scratch filesystem fills, aapt2 does
# not report ENOSPC, it reports "failed to write entry data" and "file failed to
# compile", which reads like a corrupt resource in the APK. And extract-utils
# empties its output tree before it repopulates, so a crash partway through
# leaves the blob repo without Android.bp, the makefiles and a few hundred
# blobs. `git checkout -- .` in the blobs dir recovers it.
REQUIRED_SCRATCH_BYTES = 24 * 1024**3

def use_scratch_dir_with_space():
    """
    Point tempfile at a filesystem with room for the apktool work dirs.

    Decided purely on free space, including when TMPDIR is already set. A
    TMPDIR that is too small only reproduces the failure this exists to
    avoid, so it is reported and overridden rather than obeyed.
    """
    # gettempdir() already resolves TMPDIR/TEMP/TMP, so this covers both the
    # inherited environment and the plain /tmp case.
    default_tmp = tempfile.gettempdir()
    if shutil.disk_usage(default_tmp).free >= REQUIRED_SCRATCH_BYTES:
        return

    scratch = os.path.join(
        os.environ.get('XDG_CACHE_HOME') or os.path.expanduser('~/.cache'),
        'extract-utils',
        'scratch',
    )
    os.makedirs(scratch, exist_ok=True)

    os.environ['TMPDIR'] = scratch
    tempfile.tempdir = scratch

    # Java resolves java.io.tmpdir at startup and ignores TMPDIR, so apktool and
    # the aapt2 it spawns would still land in /tmp without this. Appended rather
    # than assigned so an existing JAVA_TOOL_OPTIONS (heap size, GC) is kept;
    # the last -D on the line wins.
    java_options = os.environ.get('JAVA_TOOL_OPTIONS', '')
    os.environ['JAVA_TOOL_OPTIONS'] = (
        f'{java_options} -Djava.io.tmpdir={scratch}'.strip()
    )

    free_gib = shutil.disk_usage(scratch).free / 1024**3
    print(
        f'{default_tmp} is too small for apktool, using {scratch} '
        f'({free_gib:.0f} GiB free)'
    )
    if shutil.disk_usage(scratch).free < REQUIRED_SCRATCH_BYTES:
        print(
            f'warning: {scratch} has under '
            f'{REQUIRED_SCRATCH_BYTES / 1024**3:.0f} GiB free either; the '
            f'OppoGallery2 repack may still fail. Set TMPDIR to somewhere '
            f'with more room.'
        )

if __name__ == '__main__':
    use_scratch_dir_with_space()

    utils = ExtractUtils.device(module)
    utils.run()

    verify_packed_artifacts()
    if not report_verification():
        sys.exit(1)
