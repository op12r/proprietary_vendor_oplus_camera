# Giulia repeated-photo failure: sensor readiness experiment

This is a test candidate, not a device-verified fix.

## Evidence

In `/home/omar/ai/crash.txt`, the sixth photo uses feature 50 / `TRZP_S`,
five requests with two RAW exposure streams. Frame 61 returns a successful
buffer at 13:50:26.852. At 13:50:27.033,
`CreateInputResourceForOffline()` reports `pChiShortBufferHandle is NULL`.
The HAL returns error buffers, including the stream already returned.
CameraService reports `Too many buffers returned for frame 61`, the app
receives camera-device error 4, and deliberately sends itself SIGKILL.

This establishes the failure chain, but not why the short buffer is absent.
The user also reports crashes with HDR and Live Photo disabled. A log of that
case is needed to establish whether the same internal DOL path still runs.

The SDK patch previously forced `BaseMode.isSensorModeNeedWait(II)` to return
false. The shipped JAR was decoded to confirm it contains this bypass.
Stock logic returns true if either argument is 3. PhotoMode compares actual
and requested modes, polling up to 30 times with 30 ms sleeps when they differ
and that check is true. It rejects the capture if the mismatch persists.
The bypass disables both that wait and the associated rejection.

The SDK first reads `com.oplus.DolIsStaggerState`; it falls back to
`com.oplus.sensor.mode.list.result` on IllegalArgumentException. The existing
framework probe only examines the latter, using a hardcoded tag ID on final
results. Its absence messages do not establish that all sensor-mode feedback
is missing.

## Changes

- Remove the readiness-bypass hunk from `patches-sdk/0001-fixes.patch` so
  extraction preserves the stock check.
- Add `patches-sdk/0003-log-sensor-mode-readiness.patch`, which logs the
  resolved actual mode, requested mode, and poll count once after the
  PhotoMode wait loop, including timeout. The tag is `OplusSensorMode`.
  It uses Android Log directly so OEM verbose-log settings are unnecessary.

These changes are limited to giulia. If feedback is missing or incorrect,
some photos may now be rejected after approximately 900 ms. That outcome
is diagnostic; it is not a completed fix for the feedback path.

## Build and test

The local generated blob at
`giulia/blobs/proprietary/system_ext/framework/com.oplus.camera.unit.sdk.jar`
is updated with the rebuilt candidate. The tracked patch series reproduces
the change on the next extraction from stock. Do not reapply the stock patch
series directly to an already patched JAR.

Use the normal giulia ROM build and flash workflow so the system_ext SDK and
any generated dex-preopt artifacts are installed together. The Soong module
name is `com.oplus.camera.unit.sdk`. Building only that module does not install
it on the phone. A raw JAR replacement with stale odex/vdex artifacts is not
the recommended test procedure.

Start a full log capture before opening the camera:

```sh
adb logcat -b all -v threadtime > giulia-readiness.txt
```

Take at least 30 photos, repeating the sequence that previously failed
(including opening Gallery and returning to Camera if applicable). Test
HDR/Live Photo off first, then the previous settings. Stop logcat with Ctrl-C.
Keep the full log; this command selects relevant lines for a quick review:

```sh
rg 'OplusSensorMode|isAllowedToTakePicture|pChiShortBufferHandle|Too many buffers|killCameraProcess' giulia-readiness.txt
```

Interpretation:

- `polls=30` with differing modes involving 3, followed by a timeout:
  the restored guard rejected the capture. Investigate sensor-mode feedback
  and transition handling; do not treat the lack of a process death as a fix.
- `current=-1`: the SDK could not resolve the current mode. Inspect both
  metadata keys and their delivery to ConsumerImpl.
- Matching modes followed by the same short-buffer failure: readiness is
  insufficient to explain the bug; investigate the HAL's offline/ZSL buffer
  selection and lifetime with that capture's request metadata.
- Repeated successful captures: evidence that the guard helps, subject to
  testing across lenses, lighting, and camera-session restarts.

Do not suppress CameraService's buffer-count error or the app's self-kill as
a substitute for fixing the invalid HAL result.

## Local validation

The previous two patches were reversed from a copy of the decoded shipped
SDK, then the revised three-patch series was applied with `git apply --check`
for every patch. Apktool assembled the JAR successfully. A fresh decode of
the rebuilt JAR was checked for the stock readiness logic, the diagnostic
call, and changes limited to BaseMode and PhotoMode smali.

No ROM build, ART runtime verification, flash, or device capture test was
performed here.
