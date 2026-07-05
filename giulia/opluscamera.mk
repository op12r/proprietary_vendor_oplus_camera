LOCAL_PATH := vendor/oplus/camera/giulia

# Blob dependencies
PRODUCT_PACKAGES += \
    android.hardware.graphics.common-V3-ndk.vendor

# Framework
# PRODUCT_BOOT_JARS += \
#    oplus-framework

# Init
#PRODUCT_PACKAGES += \
#    init.oplus.camera.rc

# Permissions
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/permissions/oplus_google_lens_config.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/permissions/oplus_google_lens_config.xml \
    $(LOCAL_PATH)/configs/permissions/privapp-permissions-oplus.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/permissions/privapp-permissions-oplus.xml \
    $(LOCAL_PATH)/configs/sysconfig/hiddenapi-package-oplus-whitelist.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/sysconfig/hiddenapi-package-oplus-whitelist.xml

# Properties
PRODUCT_PRODUCT_PROPERTIES += \
    persist.vendor.camera.privapp.list=com.oplus.camera \
    ro.com.google.lens.oem_camera_package=com.oplus.camera \
    ro.com.google.lens.oem_image_package=com.oneplus.gallery \
    ro.oplus.system.camera.name=com.oplus.camera \
    ro.camera.disableHeicUltraHDR=1 \
    oplus.software.camera.10bit=1 \
    vendor.camera.skip_unconfigure.packagelist=com.oplus.camera \
    ro.oplus.camera.facing.front.need.disable.nfc=1 \
    ro.oplus.camera.speechassist=true \
    ro.camera.privileged.3rdpartyApp=com.mediatek.expert.mtkcamhelper;com.aiunit.aon; \
    persist.logd.log.load.camerahalserver.lower_limit=1000 \
    persist.logd.log.load.camerahalserver.threshold=800000 \
    persist.logd.log.load.camerahalserver.upper_limit=3000 \
    persist.logd.log.load.com.oplus.camera.lower_limit=1000 \
    persist.logd.log.load.com.oplus.camera.threshold=800000 \
    persist.logd.log.load.com.oplus.camera.upper_limit=3000 \
    persist.logd.log.load.vendor.qti.camera.provider-service_64.lower_limit=500 \
    persist.logd.log.load.vendor.qti.camera.provider-service_64.threshold=400000 \
    persist.logd.log.load.vendor.qti.camera.provider-service_64.upper_limit=1500 \

# Camera
$(call soong_config_set,camera,target_ships_oplus_cam,true)
$(call soong_config_set,cameraservice,allow_nonincreasing_timestamps,true)
$(call soong_config_set,libgui,num_buffer_slots,96)

# OPlus FWK
$(call inherit-product, hardware/oplus/oplus-fwk/oplus-fwk.mk)

# Photo
$(call soong_config_set,camera,package_name,com.oplus.packageName)

# Video
$(call soong_config_set_bool,camera,override_format_from_reserved,true)

# Inherit from camera-vendor.mk
$(call inherit-product, vendor/oplus/camera/giulia/blobs/blobs-vendor.mk)

# Common SEpolicy
include vendor/oplus/camera/sepolicy/SEPolicy.mk
