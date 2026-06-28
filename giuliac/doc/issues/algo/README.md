# Description
There are multiple crashes at libAlgoProcess:
# [Copy metadata](https://github.com/dodge-camera-port/vendor_oplus_camera/tree/A16/doc/issues/algo/copy_metadata)
Taking a photo will cause camera HAL crash at copy metadata.  
```logcat
04-14 15:58:48.373 15763 15763 F DEBUG   : *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
04-14 15:58:48.373 15763 15763 F DEBUG   : LineageOS Version: 'unknown'
04-14 15:58:48.373 15763 15763 F DEBUG   : Build fingerprint: 'OnePlus/CPH2653EEA/OP5D55L1:16/BP2A.250605.015/V.R4T3.45a1268-22c76c3-22e1011:user/release-keys'
04-14 15:58:48.373 15763 15763 F DEBUG   : Kernel Release: '6.6.126-4k-g58bbdc043f1c'
04-14 15:58:48.373 15763 15763 F DEBUG   : Revision: '0'
04-14 15:58:48.373 15763 15763 F DEBUG   : ABI: 'arm64'
04-14 15:58:48.373 15763 15763 F DEBUG   : Timestamp: 2026-04-14 15:58:48.235953006+0800
04-14 15:58:48.373 15763 15763 F DEBUG   : Process uptime: 917s
04-14 15:58:48.373 15763 15763 F DEBUG   : Executable: /system/bin/app_process64
04-14 15:58:48.373 15763 15763 F DEBUG   : Cmdline: com.oplus.camera
04-14 15:58:48.373 15763 15763 F DEBUG   : pid: 14258, tid: 14311, name: ImageProcessThr  >>> com.oplus.camera <<<
04-14 15:58:48.373 15763 15763 F DEBUG   : uid: 10227
04-14 15:58:48.373 15763 15763 F DEBUG   : tagged_addr_ctrl: 0000000000000001 (PR_TAGGED_ADDR_ENABLE)
04-14 15:58:48.373 15763 15763 F DEBUG   : pac_enabled_keys: 000000000000000f (PR_PAC_APIAKEY, PR_PAC_APIBKEY, PR_PAC_APDAKEY, PR_PAC_APDBKEY)
04-14 15:58:48.373 15763 15763 F DEBUG   : esr: 0000000092000007 (Data Abort Exception 0x24)
04-14 15:58:48.373 15763 15763 F DEBUG   : signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0000006f7cc500bc (read)
04-14 15:58:48.373 15763 15763 F DEBUG   :     x0  0000000000000000  x1  0000000000000018  x2  0000006e51f014d2  x3  000000000000006a
04-14 15:58:48.373 15763 15763 F DEBUG   :     x4  b40000719fbd587a  x5  b40000719fbf6eda  x6  756c706f2e6d6f63  x7  61632e636e702e73
04-14 15:58:48.373 15763 15763 F DEBUG   :     x8  0000000000000000  x9  0000000000000001  x10 0000000000000000  x11 0000000000000016
04-14 15:58:48.373 15763 15763 F DEBUG   :     x12 696c61632e636e70  x13 006e6f6974617262  x14 2e6172656d616372  x15 746f6e2e6970696d
04-14 15:58:48.373 15763 15763 F DEBUG   :     x16 0000006f67b3e778  x17 00000072697068b4  x18 0000006e5a2ac000  x19 b400006fcf1eba18
04-14 15:58:48.373 15763 15763 F DEBUG   :     x20 aaaaaaaaaaaaaaab  x21 b400006f7cc500b0  x22 0000006e67ce2600  x23 ffffffffffffffff
04-14 15:58:48.373 15763 15763 F DEBUG   :     x24 0000006e67ce0e70  x25 0000006e51f014d2  x26 0000006e51f014d2  x27 0000000000000000
04-14 15:58:48.373 15763 15763 F DEBUG   :     x28 00000000ffffffff  x29 0000006e67ce02d0
04-14 15:58:48.373 15763 15763 F DEBUG   :     lr  0000006e520dc410  sp  0000006e67cdfeb0  pc  0000006e520dc410  pst 0000000060001000
04-14 15:58:48.373 15763 15763 F DEBUG   :     esr 0000000092000007
04-14 15:58:48.373 15763 15763 F DEBUG   : 30 total frames
04-14 15:58:48.373 15763 15763 F DEBUG   : backtrace:
04-14 15:58:48.373 15763 15763 F DEBUG   :       #00 pc 000000000027c410  /odm/lib64/libAlgoProcess.so (android::APSMetadata::copyMetadata(camera_metadata const*)+60) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #01 pc 0000000000197380  /odm/lib64/libAlgoProcess.so (DeferJob::startCapture(std::__1::vector<params_key_value_t, std::__1::allocator<params_key_value_t>> const&, android::init_info const&, std::__1::vector<params_key_value_t, std::__1::allocator<params_key_value_t>> const&)+1980) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #02 pc 00000000001795c8  /odm/lib64/libAlgoProcess.so (APSDeferJobGoverner::startCapture(std::__1::vector<params_key_value_t, std::__1::allocator<params_key_value_t>> const&, int)+1296) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #03 pc 00000000002a60e8  /odm/lib64/libAlgoProcess.so (camApsStartCapture+280) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #04 pc 00000000002c1910  /odm/lib64/libAlgoProcess.so (app_cmd_startCapture(std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>>>>&, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const, std::__1::vector<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>, std::__1::allocator<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>>>>>>&)+752) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #05 pc 00000000002b8858  /odm/lib64/libAlgoProcess.so (onTransact+240) (BuildId: 96ce373526f5141788e6050e8471b9c3)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #06 pc 000000000004adf0  /system_ext/lib64/libAPSClient-cmd-jni.so (Java_com_oplus_ocs_camera_consumer_apsAdapter_APSClient_transact+452) (BuildId: 2caf09fde14428fe4f3db36a432a2dd68a510a22)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #07 pc 000000000084024c  /system/framework/arm64/boot-framework.oat (art_jni_trampoline+140) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #08 pc 000000000066fb80  /apex/com.android.art/lib64/libart.so (nterp_helper+4016) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #09 pc 0000000000224ca6  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.APSClientWrapper$Stub$Proxy.startCapture+54)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #10 pc 0000000000670944  /apex/com.android.art/lib64/libart.so (nterp_helper+7540) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #11 pc 00000000002281b0  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.APSClient.startCapture+136)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #12 pc 000000000066fb24  /apex/com.android.art/lib64/libart.so (nterp_helper+3924) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #13 pc 00000000002445dc  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.algorithm.FullApsImpl.startCapture+4)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #14 pc 00000000006709f0  /apex/com.android.art/lib64/libart.so (nterp_helper+7712) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #15 pc 0000000000234798  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.adapter.ApsCaptureAdapterImpl.startCapture+8)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #16 pc 000000000066fb24  /apex/com.android.art/lib64/libart.so (nterp_helper+3924) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #17 pc 000000000022d15a  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.consumer.apsAdapter.adapter.ApsAdapterImpl$ImageProcessHandler.handleMessage+662)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #18 pc 00000000004d6128  /system/framework/arm64/boot-framework.oat (android.os.Handler.dispatchMessage+152) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #19 pc 000000000050d9bc  /system/framework/arm64/boot-framework.oat (android.os.Looper.loopOnce+3260) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #20 pc 000000000050cc84  /system/framework/arm64/boot-framework.oat (android.os.Looper.loop+244) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #21 pc 00000000004ffd08  /system/framework/arm64/boot-framework.oat (android.os.HandlerThread.run+472) (BuildId: cb4426455a34fd906ec4a64c1a65b390dadbb551)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #22 pc 000000000066fb80  /apex/com.android.art/lib64/libart.so (nterp_helper+4016) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #23 pc 00000000001e6c10  /system_ext/framework/com.oplus.camera.unit.sdk.jar (com.oplus.ocs.camera.common.util.CameraHandlerThread.run+48)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #24 pc 00000000002d1d94  /apex/com.android.art/lib64/libart.so (art_quick_invoke_stub+612) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #25 pc 000000000026fce0  /apex/com.android.art/lib64/libart.so (art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)+220) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #26 pc 000000000049f0b0  /apex/com.android.art/lib64/libart.so (art::Thread::CreateCallback(void*)+1176) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #27 pc 000000000049ec08  /apex/com.android.art/lib64/libart.so (art::Thread::CreateCallbackWithUffdGc(void*)+8) (BuildId: 12b5140e5736e39a8a1454d68fec373b)
04-14 15:58:48.373 15763 15763 F DEBUG   :       #28 pc 0000000000086444  /apex/com.android.runtime/lib64/bionic/libc.so (__pthread_start(void*) (.__uniq.67847048707805468364044055584648682506)+236) (BuildId: 2ee797caf5d68ce0393b5420a4310889)
04-14 15:58:48.374 15763 15763 F DEBUG   :       #29 pc 0000000000078c48  /apex/com.android.runtime/lib64/bionic/libc.so (__start_thread+64) (BuildId: 2ee797caf5d68ce0393b5420a4310889)

```
