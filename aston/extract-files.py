#!/usr/bin/env -S PYTHONPATH=../../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2016 The CyanogenMod Project
# SPDX-FileCopyrightText: 2017-2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import os
import re
import shutil
import tempfile
from pathlib import Path

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
        .apktool_pack()
        .stripzip(),
    'system_ext/framework/com.oplus.camera.unit.sdk.jar': blob_fixup()
        .apktool_patch('patches-sdk'),
    'system_ext/priv-app/OppoGallery2/OppoGallery2.apk': blob_fixup()
        .apktool_patch('patches-gallery'),
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
