# Description
Taking a photo will cause camera HAL crash at copy metadata.

# Log
```logcat
--------- beginning of crash
04-14 15:43:31.080 13832 13906 F libc    : Fatal signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x6f7256a0bc in tid 13906 (ImageProcessThr), pid 13832 (om.oplus.camera)
04-14 15:43:31.086  1763 13964 D vendor.qti.camera.provider-service_64: CamPerf cmd:OSENSE_ACTION_CAMERA_CAPTURE timeout:250
04-14 15:43:31.086  1763 13964 E vendor.qti.camera.provider-service_64: CamPerf get request fail!!!
04-14 15:43:31.069 14179 14179 I CAM_EXT_INFO: CAM-EXT-TOF: tof8801_app0_read_results: 1073: ams-tof capture result: distance= 33 (mm), confidence= 10/63, inc result cnt= 32
04-14 15:43:31.096  1763  3384 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.103  2149  2149 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.103  2149  2149 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.104 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.107  1763  3381 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.107  1763  3381 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.107  1763  3381 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.107  1763  3381 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.108  2149 11074 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.108  2149 11074 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.109  2149 11074 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.109  2149 11074 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.113 13832 13877 D nativeloader: Load /system_ext/priv-app/OplusCamera/OplusCamera.apk!/lib/arm64-v8a/libJniMetaTransform.so using class loader ns clns-shared-9 (caller=/system_ext/framework/com.oplus.camera.unit.sdk.jar): ok
04-14 15:43:31.113  2149  2149 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.113  2149  2149 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.116 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 79  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_buildMetadataBufferPtr()  gAPSOps.pfnAPSMemHWAcquire is NULL
04-14 15:43:31.118  2149 11074 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.118  2149 11074 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.118  2149 13830 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.118  2149 13830 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.frame.number nativeType=1 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.frame.number result=81
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.request.idx nativeType=1 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.request.idx result=1
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.sensitivity
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.sensitivity tag=917506
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.sensitivity nativeType=1 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.sensitivity result=3428
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.exposureTime
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.exposureTime tag=917504
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.exposureTime nativeType=3 data.length=8
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.exposureTime result=15994852
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.focalLength
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.focalLength tag=524290
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.focalLength nativeType=2 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.focalLength result=2.3
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.aperture
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.aperture tag=524288
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.aperture nativeType=2 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.aperture result=2.05
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.control.awbMode
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.control.awbMode tag=65547
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.control.awbMode nativeType=0 data.length=1
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.control.awbMode result=1
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.sensors.mask nativeType=1 data.length=16
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.sensors.mask result=[I@e9b82fc
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@507bd85
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.120 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@9e867da
04-14 15:43:31.120 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.120 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.121 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.jpeg.orientation
04-14 15:43:31.121 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.jpeg.orientation tag=458755
04-14 15:43:31.121 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.jpeg.orientation nativeType=1 data.length=4
04-14 15:43:31.121 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.jpeg.orientation result=90
04-14 15:43:31.122 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 79  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_buildMetadataBufferPtr()  gAPSOps.pfnAPSMemHWAcquire is NULL
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.frame.number nativeType=1 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.frame.number result=82
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.request.idx nativeType=1 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.request.idx result=2
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.sensitivity
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.sensitivity tag=917506
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.sensitivity nativeType=1 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.sensitivity result=3428
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.exposureTime
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.exposureTime tag=917504
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.exposureTime nativeType=3 data.length=8
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.exposureTime result=15994852
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.focalLength
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.focalLength tag=524290
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.focalLength nativeType=2 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.focalLength result=2.3
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.aperture
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.aperture tag=524288
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.aperture nativeType=2 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.aperture result=2.05
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.control.awbMode
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.control.awbMode tag=65547
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.control.awbMode nativeType=0 data.length=1
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.control.awbMode result=1
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.sensors.mask nativeType=1 data.length=16
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.sensors.mask result=[I@dcf3594
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@805183d
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@3bc1832
04-14 15:43:31.122 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.122 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.122  2149  2149 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.122  2149  2149 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.jpeg.orientation
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.jpeg.orientation tag=458755
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.jpeg.orientation nativeType=1 data.length=4
04-14 15:43:31.122 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.jpeg.orientation result=90
04-14 15:43:31.104  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.126 13832 13888 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]: [Event] MSFDDNetworkEngine.cpp(179)::onTcpInfoUpdate->onTcpInfoUpdate:
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_state = 2;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_ca_state = 4;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_rto = 1000 ms;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_unacked = 1;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_rttcur = 0 ms;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_rttvar = 250 ms;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_bytes_retrans = 0 bytes;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_notsent_bytes = 0 bytes;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_bytes_received = 0 bytes;
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_bytes_sent = 0 bytes 
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_last_data_sent = 598584 ms 
04-14 15:43:31.126  5843  8079 V MSF.C.MSFCore[@DD]:                      tcpi_last_data_recv = 598584 ms 
04-14 15:43:31.127  2149 13830 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.127  2149 13830 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.127 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 79  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_buildMetadataBufferPtr()  gAPSOps.pfnAPSMemHWAcquire is NULL
04-14 15:43:31.127  2149  2149 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.127  2149  2149 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.frame.number nativeType=1 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.frame.number result=83
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.request.idx nativeType=1 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.request.idx result=3
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.sensitivity
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.sensitivity tag=917506
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.sensitivity nativeType=1 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.sensitivity result=3428
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.exposureTime
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.exposureTime tag=917504
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.exposureTime nativeType=3 data.length=8
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.exposureTime result=15994852
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.focalLength
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.focalLength tag=524290
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.focalLength nativeType=2 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.focalLength result=2.3
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.aperture
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.aperture tag=524288
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.aperture nativeType=2 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.aperture result=2.05
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.control.awbMode
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.control.awbMode tag=65547
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.control.awbMode nativeType=0 data.length=1
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.control.awbMode result=1
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.sensors.mask nativeType=1 data.length=16
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.sensors.mask result=[I@f02d6d7
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@2f52bc4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.127 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@3518aad
04-14 15:43:31.127 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.127 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.128 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.jpeg.orientation
04-14 15:43:31.128 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.jpeg.orientation tag=458755
04-14 15:43:31.128 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.jpeg.orientation nativeType=1 data.length=4
04-14 15:43:31.128 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.jpeg.orientation result=90
04-14 15:43:31.139  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.131  2149  2149 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.132  1763  3378 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.133 13832 13929 D FormatConverter: dumpTextureToBitmap AndroidBitmap_getInfo result: 0, width: 192, height: 192, format: 1
04-14 15:43:31.133 13832 13929 D FormatConverter: dumpTextureToBitmap AndroidBitmap_lockPixels result: 0, inAddr: 0xb400007248ba5000
04-14 15:43:31.137  2149 11074 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.137  2149 11074 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.137  2149 11074 W qdgralloc: DataspaceHelper: Attempting to set invalid gralloc dataspace - 1
04-14 15:43:31.137  2149 11074 W qdgralloc: Unable to set metadata - metadata type 17
04-14 15:43:31.137 13832 13929 D FormatConverter: dumpTextureToBitmap glReadPixels texWidth: 192, texHeight: 192
04-14 15:43:31.137 13832 13929 D FormatConverter: dumpTextureToBitmapWithDimming AndroidBitmap_getInfo result: 0, width: 1440, height: 1920, format: 1
04-14 15:43:31.137 13832 13929 D FormatConverter: dumpTextureToBitmapWithDimming AndroidBitmap_lockPixels result: 0, inAddr: 0xb400006daa2fe000
04-14 15:43:31.140  1763  3385 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.140  1763  3385 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.140  1763  3385 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.140  1763  3385 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.144 14179 14179 I CAM_EXT_INFO: CAM-EXT-TOF: tof8801_app0_read_results: 1073: ams-tof capture result: distance= 32 (mm), confidence= 10/63, inc result cnt= 33
04-14 15:43:31.159  1815  1974 E BatteryDamageDetect: BddVoltDiffCheck begins
04-14 15:43:31.159  1815  1974 E BatteryDamageDetect: volt diff trend not changed, volt_diff_trend = 0
04-14 15:43:31.168  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.160  1763  3380 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.173 12906 12906 I CAM_INFO: CAM-CPAS: cam_cpas_util_vote_hlos_bus_client_bw: 431: Bus_client: cam_sf_0, HLOS vote [4860250567 0] is_camnoc_bw: N
04-14 15:43:31.164  5843  8069 V MSF.C.MSFCore[@PS]: [Event] MSFPacketStatistics.cpp(276)::checkBadNetwork->badNetwork state change:1, reason:1, rtts=0.000
04-14 15:43:31.164  5843  8069 V MSF.C.MSFCore[@PS]: [Event] MSFPacketStatistics.cpp(300)::DoCheckRequestTimeout->current rtts:0.000
04-14 15:43:31.164  5843  8073 D MSF.C.NewSender: [onMSFBadNetworkState], isBadNet: true, reason: 1
04-14 15:43:31.165  5843  8065 I MSF.D.NetworkProvider.NetConnInfo: refresh activeNetInfo currentAPN:. received networkInfo: BLOCKED :NetworkInfo: type: WIFI[], state: DISCONNECTED/BLOCKED, reason: (unspecified), roaming: false, failover: false, isAvailable: true, isConnectedToProvisioningNetwork: false. ExtraNetInfo: 
04-14 15:43:31.165  5843  7908 D MSF.C.MSFNetworkStateAdapter: send weakNet status change broadcast, isWeakNet: true, reason: 1
04-14 15:43:31.165  5843  7908 I MSF.C.MSFNetworkStateAdapter:  WeakNetChanged isBadNet: true, Normal to WeakNet, reason:(0, 1)
04-14 15:43:31.170 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.170 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 79  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_buildMetadataBufferPtr()  gAPSOps.pfnAPSMemHWAcquire is NULL
04-14 15:43:31.171 14219 14219 I crash_dump64: obtaining output fd from tombstoned, type: kDebuggerdTombstoneProto
04-14 15:43:31.171 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.171  1234  1234 I tombstoned: received crash request for pid 13906
04-14 15:43:31.172 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.frame.number nativeType=1 data.length=4
04-14 15:43:31.172 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.frame.number result=84
04-14 15:43:31.172 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.capture.request.idx nativeType=1 data.length=4
04-14 15:43:31.173 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.capture.request.idx result=4
04-14 15:43:31.173 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.sensitivity
04-14 15:43:31.173 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.sensitivity tag=917506
04-14 15:43:31.173 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.sensitivity nativeType=1 data.length=4
04-14 15:43:31.173 14219 14219 I crash_dump64: performing dump of process 13832 (target tid = 13906)
04-14 15:43:31.173 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.sensitivity result=3428
04-14 15:43:31.174 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.sensor.exposureTime
04-14 15:43:31.174 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.sensor.exposureTime tag=917504
04-14 15:43:31.174  1763  3379 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.174  1763  3379 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.174  1763  3379 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.174  1763  3379 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.sensor.exposureTime nativeType=3 data.length=8
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.sensor.exposureTime result=15994852
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.focalLength
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.focalLength tag=524290
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.focalLength nativeType=2 data.length=4
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.focalLength result=2.3
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.lens.aperture
04-14 15:43:31.175 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.lens.aperture tag=524288
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.lens.aperture nativeType=2 data.length=4
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.lens.aperture result=2.05
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.control.awbMode
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.control.awbMode tag=65547
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.control.awbMode nativeType=0 data.length=1
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.control.awbMode result=1
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.sensors.mask nativeType=1 data.length=16
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.sensors.mask result=[I@85123c7
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@65d0df4
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=com.oplus.aps.sat.snapshot.master.pipeline nativeType=1 data.length=4
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=com.oplus.aps.sat.snapshot.master.pipeline result=[I@e97791d
04-14 15:43:31.176 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.176 13832 13877 E APS_CORE: [ERROR][ ALGO_JNI ] com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult.cpp: 118  Java_com_oplus_ocs_camera_consumer_apsAdapter_adapter_ApsTotalResult_getMetaValue()  ApsTotalResult_getTagValue getMetadata, res: -2
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: getMetadataTag: key=android.jpeg.orientation
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: getMetadataTag OK key=android.jpeg.orientation tag=458755
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert: key=android.jpeg.orientation nativeType=1 data.length=4
04-14 15:43:31.176 13832 13877 D OplusCameraManagerExt: metaDataValueConvert OK key=android.jpeg.orientation result=90
04-14 15:43:31.175  1771  1771 W LightningLaunc: type=1400 audit(0.0:507): avc:  denied  { search } for  name="14219" dev="proc" ino=1068610 scontext=u:r:vendor_hal_perf_default:s0 tcontext=u:r:crash_dump:s0:c227,c256,c512,c768 tclass=dir permissive=0
04-14 15:43:31.173 12906 12906 I CAM_INFO: CAM-PERF: cam_soc_bus_client_update_bw: 182: Bus client=[cam_sf_0] [BUS_PATH_HLOS] :ab[4860250567] ib[0]
04-14 15:43:31.183 13832 13929 D FormatConverter: dumpTextureToBitmapWithDimming glReadPixels texWidth: 1440, texHeight: 1920
04-14 15:43:31.184  4812 13289 E WakeLock: CryptauthEnroller ** IS FORCE-RELEASED ON TIMEOUT ** [CONTEXT service_id=259 ]
04-14 15:43:31.187 13832 13929 D FormatConverter: dumpTextureToBitmapWithDimming, dimming: 1.000000, costTime: 3.936000 ms
04-14 15:43:31.206  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.211 12906 12906 I CAM_INFO: CAM-CPAS: cam_cpas_util_vote_hlos_bus_client_bw: 431: Bus_client: cam_sf_0, HLOS vote [4858309386 0] is_camnoc_bw: N
04-14 15:43:31.199  1763  3380 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.211 12906 12906 I CAM_INFO: CAM-PERF: cam_soc_bus_client_update_bw: 182: Bus client=[cam_sf_0] [BUS_PATH_HLOS] :ab[4858309386] ib[0]
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.205 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.206  1763  3383 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.206  1763  3383 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.206  1763  3383 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.206  1763  3383 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.207 13832 13838 W System  : A resource failed to call HardwareBuffer.close. 
04-14 15:43:31.210  5471  5490 W MediaProvider: isAppCloneUserPair for user 0: false
04-14 15:43:31.212  2855  4210 W Thanox-Core: resolveProviderName fail resolve provider for name: com.open.gallery.smart.provider, providerInfo is null
04-14 15:43:31.212  2855  4210 W Thanox-Core: getContentProviderImpl checkContentProvider, can not resolve provider name: com.open.gallery.smart.provider
04-14 15:43:31.212 13832 13899 E ActivityThread: Failed to find provider info for com.open.gallery.smart.provider
04-14 15:43:31.207 13832 13832 W pool-11-thread-: type=1400 audit(0.0:508): avc:  denied  { rename } for  name=".tmp" dev="dm-46" ino=721211 scontext=u:r:opluscamera_app:s0:c227,c256,c512,c768 tcontext=u:object_r:vendor_data_file:s0:c227,c256,c512,c768 tclass=file permissive=0 app=com.oplus.camera
04-14 15:43:31.216 14179 14179 I CAM_EXT_INFO: CAM-EXT-TOF: tof8801_app0_read_results: 1073: ams-tof capture result: distance= 33 (mm), confidence= 10/63, inc result cnt= 34
04-14 15:43:31.222 13832 13900 D nativeloader: Load /system_ext/priv-app/OplusCamera/OplusCamera.apk!/lib/arm64-v8a/libIccProfileJni.so using class loader ns clns-shared-10 (caller=/system_ext/priv-app/OplusCamera/OplusCamera.apk!classes19.dex): ok
04-14 15:43:31.222 13832 13900 I WriteIccProfile: inputBufferSize 27675 outPutBufferSize 28239 iccSize 562
04-14 15:43:31.222 13832 13900 I WriteIccProfile: writeSize 28241
04-14 15:43:31.222 13832 13900 I WriteIccProfile: writeJpegIccProfileFd, close fd: 139 
04-14 15:43:31.238  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.243 12906 12906 I CAM_INFO: CAM-CPAS: cam_cpas_util_vote_hlos_bus_client_bw: 431: Bus_client: cam_sf_0, HLOS vote [4857182003 0] is_camnoc_bw: N
04-14 15:43:31.230  1763  3377 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.236 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.239  1763  3385 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.239  1763  3385 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.239  1763  3385 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.239  1763  3385 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.243 12906 12906 I CAM_INFO: CAM-PERF: cam_soc_bus_client_update_bw: 182: Bus client=[cam_sf_0] [BUS_PATH_HLOS] :ab[4857182003] ib[0]
04-14 15:43:31.255  1763  3385 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.261  1763  3379 E ChiX    : [ERROR][ChiMeta] chxmetadata.cpp:3123 ReleaseAndroidFrameworkOutputMetadata() [CMB_ERROR] Cannot release metadata 0xb400007528225fd0
04-14 15:43:31.261  1763  3379 E ChiX    : [ERROR][ChiMeta] chxmetadata.cpp:3123 ReleaseAndroidFrameworkOutputMetadata() [CMB_ERROR] Cannot release metadata 0xb400007528225fd0
04-14 15:43:31.262  1763  3379 E ChiX    : [ERROR][ChiMeta] chxmetadata.cpp:3123 ReleaseAndroidFrameworkOutputMetadata() [CMB_ERROR] Cannot release metadata 0xb400007528225fd0
04-14 15:43:31.262  1763  3379 E ChiX    : [ERROR][ChiMeta] chxmetadata.cpp:3123 ReleaseAndroidFrameworkOutputMetadata() [CMB_ERROR] Cannot release metadata 0xb400007528225fd0
04-14 15:43:31.262 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.263  1763  1987 I camx-service.device.camera_device_session.cpp: repeatingRequestEnd: frameNumber:90, stream[0/1], id:1, pStream:0xb400007528131198, hdrProfile:1
04-14 15:43:31.262  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.273  1763  3378 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.273  1763  3378 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.273  1763  3378 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.273  1763  3378 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.288 14179 14179 I CAM_EXT_INFO: CAM-EXT-TOF: tof8801_app0_read_results: 1073: ams-tof capture result: distance= 33 (mm), confidence= 10/63, inc result cnt= 36
04-14 15:43:31.290  1763  3377 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.299 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.306  1763  3381 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.306  1763  3381 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.306  1763  3381 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.306  1763  3381 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.298  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.329  1763  3378 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.340  1763  3380 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.340  1763  3380 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.340  1763  3380 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.340  1763  3380 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.340 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.337  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.363 14179 14179 I CAM_EXT_INFO: CAM-EXT-TOF: tof8801_app0_read_results: 1073: ams-tof capture result: distance= 33 (mm), confidence= 10/63, inc result cnt= 37
04-14 15:43:31.369  1763  3380 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.370  4178 13727 I NetworkScheduler.Stats: (REDACTED) Task %s/%s started execution. cause:%s exec_start_elapsed_seconds: %s
04-14 15:43:31.367 14219 14219 W crash_dump64: type=1400 audit(0.0:509): avc:  denied  { search } for  name="com.oplus.camera" dev="dm-46" ino=6073 scontext=u:r:crash_dump:s0:c227,c256,c512,c768 tcontext=u:object_r:opluscamera_app_data_file:s0:c227,c256,c512,c768 tclass=dir permissive=0 app=com.oplus.camera
04-14 15:43:31.367 14219 14219 W crash_dump64: type=1400 audit(0.0:510): avc:  denied  { search } for  name="com.oplus.camera" dev="dm-46" ino=6073 scontext=u:r:crash_dump:s0:c227,c256,c512,c768 tcontext=u:object_r:opluscamera_app_data_file:s0:c227,c256,c512,c768 tclass=dir permissive=0 app=com.oplus.camera
04-14 15:43:31.367 14219 14219 W crash_dump64: type=1400 audit(0.0:511): avc:  denied  { search } for  name="com.oplus.camera" dev="dm-46" ino=6073 scontext=u:r:crash_dump:s0:c227,c256,c512,c768 tcontext=u:object_r:opluscamera_app_data_file:s0:c227,c256,c512,c768 tclass=dir permissive=0 app=com.oplus.camera
04-14 15:43:31.367 14219 14219 W crash_dump64: type=1400 audit(0.0:512): avc:  denied  { search } for  name="com.oplus.camera" dev="dm-46" ino=6073 scontext=u:r:crash_dump:s0:c227,c256,c512,c768 tcontext=u:object_r:opluscamera_app_data_file:s0:c227,c256,c512,c768 tclass=dir permissive=0 app=com.oplus.camera
04-14 15:43:31.367 14219 14219 W crash_dump64: type=1400 audit(0.0:513): avc:  denied  { search } for  name="com.oplus.camera" dev="dm-46" ino=6073 scontext=u:r:crash_dump:s0:c227,c256,c512,c768 tcontext=u:object_r:opluscamera_app_data_file:s0:c227,c256,c512,c768 tclass=dir permissive=0 app=com.oplus.camera
04-14 15:43:31.367 14219 14219 W crash_dump64: type=1400 audit(0.0:514): avc:  denied  { search } for  name="com.oplus.camera" dev="dm-46" ino=6073 scontext=u:r:crash_dump:s0:c227,c256,c512,c768 tcontext=u:object_r:opluscamera_app_data_file:s0:c227,c256,c512,c768 tclass=dir permissive=0 app=com.oplus.camera
04-14 15:43:31.372  1763  3377 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.372  1763  3377 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.372  1763  3377 E S5KJN5_DBG : framelength lines:6408, linecount: 1273, a reg gain:2560, d reg gain:256
04-14 15:43:31.372  1763  3377 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.377  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.388 14219 14219 W audit   : audit_lost=348 audit_rate_limit=5 audit_backlog_limit=64
04-14 15:43:31.388 14219 14219 E audit   : rate limit exceeded
04-14 15:43:31.380 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.394  1763  3385 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.402 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.405  1763  3380 E S5KJN5_DBG : framelength lines:6408, linecount: 1394, a reg gain:2373, d reg gain:256
04-14 15:43:31.405  1763  3380 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.405  1763  3380 E S5KJN5_DBG : framelength lines:6408, linecount: 1394, a reg gain:2373, d reg gain:256
04-14 15:43:31.405  1763  3380 E S5KJN5_DBG : Normal exposure, longFrameLengthLines:6408, shortFrameLengthLines:6408
04-14 15:43:31.410 14219 14219 F DEBUG   : *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
04-14 15:43:31.410 14219 14219 F DEBUG   : LineageOS Version: 'unknown'
04-14 15:43:31.410 14219 14219 F DEBUG   : Build fingerprint: 'OnePlus/CPH2653EEA/OP5D55L1:16/BP2A.250605.015/V.R4T3.45a1268-22c76c3-22e1011:user/release-keys'
04-14 15:43:31.410 14219 14219 F DEBUG   : Kernel Release: '6.6.126-4k-g58bbdc043f1c'
04-14 15:43:31.410 14219 14219 F DEBUG   : Revision: '0'
04-14 15:43:31.410 14219 14219 F DEBUG   : ABI: 'arm64'
04-14 15:43:31.410 14219 14219 F DEBUG   : Timestamp: 2026-04-14 15:43:31.189017314+0800
04-14 15:43:31.410 14219 14219 F DEBUG   : Process uptime: 4s
04-14 15:43:31.410 14219 14219 F DEBUG   : Executable: /system/bin/app_process64
04-14 15:43:31.410 14219 14219 F DEBUG   : Cmdline: com.oplus.camera
04-14 15:43:31.410 14219 14219 F DEBUG   : pid: 13832, tid: 13906, name: ImageProcessThr  >>> com.oplus.camera <<<
04-14 15:43:31.410 14219 14219 F DEBUG   : uid: 10227
04-14 15:43:31.410 14219 14219 F DEBUG   : tagged_addr_ctrl: 0000000000000001 (PR_TAGGED_ADDR_ENABLE)
04-14 15:43:31.410 14219 14219 F DEBUG   : pac_enabled_keys: 000000000000000f (PR_PAC_APIAKEY, PR_PAC_APIBKEY, PR_PAC_APDAKEY, PR_PAC_APDBKEY)
04-14 15:43:31.410 14219 14219 F DEBUG   : esr: 0000000092000007 (Data Abort Exception 0x24)
04-14 15:43:31.411 14219 14219 F DEBUG   : signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0000006f7256a0bc (read)
04-14 15:43:31.411 14219 14219 F DEBUG   :     x0  0000000000000000  x1  0000000000000018  x2  0000006e38d0e4d2  x3  000000000000006a
04-14 15:43:31.411 14219 14219 F DEBUG   :     x4  b40000719fbf243a  x5  b40000719f1e08fa  x6  756c706f2e6d6f63  x7  61632e636e702e73
04-14 15:43:31.411 14219 14219 F DEBUG   :     x8  0000000000000000  x9  0000000000000001  x10 0000000000000000  x11 0000000000000016
04-14 15:43:31.411 14219 14219 F DEBUG   :     x12 696c61632e636e70  x13 006e6f6974617262  x14 2e6172656d616372  x15 746f6e2e6970696d
04-14 15:43:31.411 14219 14219 F DEBUG   :     x16 0000006f67b3e778  x17 00000072697068b4  x18 0000006e40968000  x19 b400006fcf1bbef8
04-14 15:43:31.411 14219 14219 F DEBUG   :     x20 aaaaaaaaaaaaaaab  x21 b400006f7256a0b0  x22 0000006e41067600  x23 ffffffffffffffff
04-14 15:43:31.411 14219 14219 F DEBUG   :     x24 0000006e41065e70  x25 0000006e38d0e4d2  x26 0000006e38d0e4d2  x27 0000000000000000
04-14 15:43:31.411 14219 14219 F DEBUG   :     x28 00000000ffffffff  x29 0000006e410652d0
04-14 15:43:31.411 14219 14219 F DEBUG   :     lr  0000006e38ee9410  sp  0000006e41064eb0  pc  0000006e38ee9410  pst 0000000060001000
04-14 15:43:31.411 14219 14219 F DEBUG   :     esr 0000000092000007
04-14 15:43:31.411 14219 14219 F DEBUG   : 30 total frames
04-14 15:43:31.411 14219 14219 F DEBUG   : backtrace:
04-14 15:43:31.411 14219 14219 F DEBUG   :       #00 pc 000000000027c410  /odm/lib64/libAlgoProcess.so (android::APSMetadata::copyMetadata(camera_metadata const*)+60) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #01 pc 0000000000197380  /odm/lib64/libAlgoProcess.so (DeferJob::startCapture(std::__1::vector<params_key_value_t, std::__1::allocator<params_key_value_t>> const&, android::init_info const&, std::__1::vector<params_key_value_t, std::__1::allocator<params_key_value_t>> const&)+1980) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #02 pc 00000000001795c8  /odm/lib64/libAlgoProcess.so (APSDeferJobGoverner::startCapture(std::__1::vector<params_key_value_t, std::__1::allocator<params_key_value_t>> const&, int)+1296) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #03 pc 00000000002a60e8  /odm/lib64/libAlgoProcess.so (camApsStartCapture+280) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #04 pc 00000000002c1910  /odm/lib64/libAlgoProcess.so (app_cmd_startCapture(std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>>>>&, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>>>>&)+752) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #05 pc 00000000002b8858  /odm/lib64/libAlgoProcess.so (onTransact+240) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #06 pc 000000000004adf0  /system_ext/lib64/libAPSClient-cmd-jni.so (Java_com_oplus_ocs_camera_consumer_apsAdapter_APSClient_transact+452) (BuildId: 2caf09fde14428fe4f3db36a432a2dd68a510a22)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #07 pc 000000000084024c  /system/framework/arm64/boot-framework.oat (art_jni_trampoline+140) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #08 pc 000000000066fb80  /apex/com.android.art/lib64/libart.so (nterp_helper+4016) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #09 pc 0000000000224ca6  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.APSClientWrapper$Stub$Proxy.startCapture+54)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #10 pc 0000000000670944  /apex/com.android.art/lib64/libart.so (nterp_helper+7540) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #11 pc 00000000002281b0  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.APSClient.startCapture+136)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #12 pc 000000000066fb24  /apex/com.android.art/lib64/libart.so (nterp_helper+3924) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #13 pc 00000000002445dc  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.algorithm.FullApsImpl.startCapture+4)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #14 pc 00000000006709f0  /apex/com.android.art/lib64/libart.so (nterp_helper+7712) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #15 pc 0000000000234798  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.adapter.ApsCaptureAdapterImpl.startCapture+8)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #16 pc 000000000066fb24  /apex/com.android.art/lib64/libart.so (nterp_helper+3924) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #17 pc 000000000022d15a  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.adapter.ApsAdapterImpl$ImageProcessHandler.handleMessage+662)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #18 pc 00000000004d6128  /system/framework/arm64/boot-framework.oat (android.os.Handler.dispatchMessage+152) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #19 pc 000000000050d9bc  /system/framework/arm64/boot-framework.oat (android.os.Looper.loopOnce+3260) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #20 pc 000000000050cc84  /system/framework/arm64/boot-framework.oat (android.os.Looper.loop+244) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #21 pc 00000000004ffd08  /system/framework/arm64/boot-framework.oat (android.os.HandlerThread.run+472) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #22 pc 000000000066fb80  /apex/com.android.art/lib64/libart.so (nterp_helper+4016) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #23 pc 00000000001e6c10  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.common.util.CameraHandlerThread.run+48)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #24 pc 00000000002d1d94  /apex/com.android.art/lib64/libart.so (art_quick_invoke_stub+612) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #25 pc 000000000026fce0  /apex/com.android.art/lib64/libart.so (art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)+220) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #26 pc 000000000049f0b0  /apex/com.android.art/lib64/libart.so (art::Thread::CreateCallback(void*)+1176) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #27 pc 000000000049ec08  /apex/com.android.art/lib64/libart.so (art::Thread::CreateCallbackWithUffdGc(void*)+8) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #28 pc 0000000000086444  /apex/com.android.runtime/lib64/bionic/libc.so (__pthread_start(void*) (.__uniq.67847048707805468364044055584648682506)+236) (BuildId: 2ee797caf5d68ce0393b5420a4310889)
04-14 15:43:31.411 14219 14219 F DEBUG   :       #29 pc 0000000000078c48  /apex/com.android.runtime/lib64/bionic/libc.so (__start_thread+64) (BuildId: 2ee797caf5d68ce0393b5420a4310889)
04-14 15:43:31.401  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.431  1336  1336 I CAM_INFO: CAM-ICP: cam_icp_mgr_process_dbg_buf: 3408: [icp]: FW_DBG:CICP_FW_E : [ICP]  HWDRV_:DMI_STATUS polling timed out at hardwaredriver_ipebps.c:419 QC_IMAGE_VERSION_STRING=CICP.FW.8.0-00009 OEM_IMAGE_VERSION_STRING=CRM
04-14 15:43:31.423  1763  3383 I CV      : File: vendor/qcom/proprietary/cv-noship/eva/4.0/src/cpu/evaOpticalFlow.cpp Line: 2676 Function: evaOFExt_Sync() Msg: evaOFExt_Sync: pConfigList is NOT NULL then call evaOFSetFrameConfig
04-14 15:43:31.428 13832 13890 W CameraMetadataJV: Expect face scores and rectangles to be non-null
04-14 15:43:31.433  1234  1234 E tombstoned: Tombstone written to: tombstone_07

```
These errors are suspecious, but need to check log in stock ROM:
```
W qdgralloc: Unable to set metadata - metadata type 17
```

# How to debug
## Check ABI mismatch
Try to replace some needed lib with stock one.
## Check oplus-fwk
Some java side code in oplus-fwk is called before using JNI and getting crash.  
Check oplus-fwk/src/android/hardware/camera2/OplusCameraManager.java,  
specifically `metaDataValueConvert` and `getMetadataTag`.