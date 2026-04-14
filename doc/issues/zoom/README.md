# Summary
For back camera, zoom does not take effect. No matter what zoom level you set, it's always actually 1.0x.  
# Details
Zoom does not take effect in Oplus camera, when  
- [x] Camera HAL correctly loads node   `OplusVideoSATFusionOfflineReprocess`, same as on stock ROM.
```
    1. OplusVideoSATFusionOfflineReprocess is responsible for (lens seamless switch animation) and HIS(OIS+EIS) and some algorithm in preview.
    2. If camera HAL loads OplusVideoSATOfflineReprocess incorrectly (if packagaName hack not complete), zoom will work.
```
- [x] Vendor tag `com.oplus.packageName` reports `com.oplus.camera` (same as on stock ROM) and `com.oplus.is.sdk.camera.package` reports `NOT_FOUND` (same as on stock ROM)  
```
    1. com.oplus.is.sdk.camera.package tag should not be defined, according to stock ROM. It should return NOT_FOUND.
    2. When defined and returns 1, zoom will work, but (lens seamless switch animation will disappear), camera re-initialize once every second, and graphical glictches happens when super EIS enabled.
```
- [x] Oplus camera uses logical combined (0.6x - 20/120x) camera
```
    1. When Oplus camera uses single physical camera, zoom works. (For example, in Portrait/XPAN/Movie mode, or when using front camera)
```
Zoom works in Oplus camera, when  
- [x] Oplus camera uses single camera instead of logical combined one.  
- [x] Oplus camera uses front camera  
- [x] Initial zoom is not 1.0x
```
    Set zoom level, then go to camera app settings, then go back, it will apply zoom correctly.
```
# How to debug
## 1. Log inside libcamera_metadata
```
If you suspect the error happens because of missing/corrupt vendor tags, you may try logging in system/media/camera/src/camera_metadata.c.

Maybe related functions:
    find_camera_metadata_entry
    get_camera_metadata_entry
    and more.
```
## 2. Log inside VendorTagDescriptor
```
Logging here may also be helpful, since many "Tag name '%s' does not exist" logs appear when setting zoom level.

Warning: Both when zoom works and doesn't work (for exmaple, action mode enabled and not enabled), the same logs appear. Although there may be some differences.

Maybe related functions:
    VendorTagDescriptor::lookupTag
```
## 3. Pay attention to other logs
## 4. Use strace to trace process
```
strace -p $(pidof vendor.qti.camera.provider-service_64) -f -e trace=openat # Add more syscall types in demand
strace -p $(pidof cameraserver) -f -e trace=openat # Add more syscall types in demand
```
## 5. Use gdb
```
gdb -p $(pidof vendor.qti.camera.provider-service_64)
```
