---
title: MPP
---

# MPP

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/MPP 媒体处理软件 V5.0 FAQ/MPP 媒体处理软件 V5.0 FAQ.md
--- # Preface
**Overview** This document is written for programmers developing with the MPP media processing software. Its purpose is to provide solutions and assistance for problems encountered during development. > **Note:**

> Unless otherwise specified, the content for is identical to Hi3403V100. **Product Version** The product version corresponding to this document is as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Target Audience** This document is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document. Their meanings are as follows.

| Symbol | Description |
| --- | --- |
| | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Register Access Type Conventions**

| Type | Description | Type | Description |
| --- | --- | --- | --- |
| RO | Read only, not writable. | RW | Readable and writable. |

**Numeric Unit Conventions** The representation of data capacity, frequency, data rate, etc., is described as follows.

| Category | Symbol | Corresponding Value |
| --- | --- | --- |
| Data capacity (e.g., RAM capacity) | 1K | 1024 |
| Frequency, data rate, etc. | 1k | 1000 |

Address and data representations are described as follows.

| Symbol | Example | Description |
| --- | --- | --- |
| 0x | 0x FE04, 0x18 | Hexadecimal data values and address values. |

**Revision History** The revision history accumulates update descriptions for each document version. The latest version of this document contains updates from all previous versions.

| Document Version | Release Date | Revision Description |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim release. |

# System Control

## Log Information ### How to View MPP Log Information [Phenomenon] Need to view logs and adjust log levels. [Analysis] Log records record the causes of SDK runtime errors, approximate locations, and some system running status information. Therefore, viewing logs can assist in error localization. Currently, logs have 7 levels. The default setting is level 3. The higher the level setting, the more information is recorded in the log. When the level is 7, the entire system running status is recorded in real time. The amount of information at this level is very large and will significantly reduce overall system performance. Therefore, under normal circumstances, level 3 is recommended, because at this level, information is only recorded when an error occurs, helping to locate most errors. [Solution] Commands for obtaining logs or modifying log levels are as follows: - To view the log level of each module, use **cat /proc/umap/logmpp**. This command lists all module log levels.[¶](#log-information-how-to-view-mpp-log-information-phenomenon-need-to-view-logs-and-adjust-log-levels-analysis-log-records-record-the-causes-of-sdk-runtime-errors-approximate-locations-and-some-system-running-status-information-therefore-viewing-logs-can-assist-in-error-localization-currently-logs-have-7-levels-the-default-setting-is-level-3-the-higher-the-level-setting-the-more-information-is-recorded-in-the-log-when-the-level-is-7-the-entire-system-running-status-is-recorded-in-real-time-the-amount-of-information-at-this-level-is-very-large-and-will-significantly-reduce-overall-system-performance-therefore-under-normal-circumstances-level-3-is-recommended-because-at-this-level-information-is-only-recorded-when-an-error-occurs-helping-to-locate-most-errors-solution-commands-for-obtaining-logs-or-modifying-log-levels-are-as-follows-to-view-the-log-level-of-each-module-use-cat-procumaplogmpp-this-command-lists-all-module-log-levels "锚链接")

- To modify the log level of a specific module, use **echo "venc=4" > /proc/umap/logmpp**, where venc is the module name, matching the module names listed by the cat command.
- To modify the log level of all modules, use **echo "all=4" > /proc/umap/logmpp**.
- To obtain log records, use **cat /dev/logmpp**. This command prints all log information. If the logs have been read, the command blocks and waits for new log information. Use Ctrl+C to exit. To avoid blocking and waiting, use **echo wait=0 > /proc/umap/logmpp** to cancel blocking wait. You can also use system calls such as open and read to operate the /dev/logmpp device node. ## Memory Usage ### OS Reserved Memory and Thread Stack Size Adjustment [Phenomenon] Linux system running business programs shows oom-killer. [Analysis] Possible causes include: - Insufficient OS memory
- System reserved memory too small [Solution] - Increase OS memory
- Increase system reserved memory. Add the following commands to /etc/profile to set the system reserved memory to 4MB (adjustable): echo 2 > /proc/sys/kernel/randomize\_va\_space echo 4096 > /proc/sys/vm/min\_free\_kbytes [Phenomenon] The system shows thread creation failure with error: pthread\_create: Resource temporarily unavailable. [Analysis] Possible causes include: - Insufficient OS memory
- Thread stack space too large [Solution] - Increase OS memory
- Adjust the maximum thread stack space size. There are 2 methods: - Use `ulimit -s` to modify the thread stack size in Linux, e.g., set to 1MB: `ulimit -s 1024`. Add this command to /etc/profile to set the stack size at boot. - Use `pthread_attr_setstacksize` to change the thread stack size in the program. ### How to Adjust Media Business Memory Based on Specific Products [Phenomenon] Media services require a certain amount of memory (mainly MMZ memory) to support normal operation. The MPP platform allocates memory based on typical business patterns. When product memory usage is tight, users can try related strategies to adjust memory allocation based on actual conditions. [Analysis] For products with tight memory usage, the SDK software in the delivery package provides some methods to adjust memory allocation. This section only briefly describes memory reduction measures. Refer to related documents for specific usage. [Solution] 1. Confirm OS and MMZ memory allocation. See the "Address Space Allocation and Usage" section in the document "S Sxxxx SDK Installation and Upgrade Instructions". 2. Adjust SDK-related business memory usage based on actual conditions. - All resolution image sizes should be integer multiples of each other. For example, 1080P is 1920x1080, 960H is 960x480. Situations like 960H being 960x756 should not occur. Also, the case where VI captures 1920x1088 images but VENC encodes 1920x1080 should not occur. - Minimum buffer configuration for each module: refer to "MPP Media Processing Software V5.0 Development Reference". - Public VB pool should be exactly sufficient. Related interface: ss\_mpi\_vb\_set\_cfg. Refer to the "System Control" chapter of "MPP Media Processing Software V5.0 Development Reference". **Special note: the calculation of VB size for each module's output data is complex. Refer to the ot\_buffer.h code for specific formulas.** How to confirm sufficiency: In the VB proc information, pools with "is\_comm =1" are public VB pools. Ensure min\_free = 0 for the public VB pool and no module prints that VB cannot be obtained in logmpp. - Use compact segment compression to save memory and bandwidth. For example, VI and VPSS channels can use compact segment compression for writing. - DDR miniaturization measures per module. Refer to the "DDR Miniaturization Guide". ### MMZ Information Customers can use `cat /proc/umap/media-mem` to view current system MMZ information and usage: ---ZONE: PHYS(0x64100000, 0x BFFFFFFF), GFP=0, n BYTES=1506304KB, NAME="anonymous" This indicates MMZ zone 0, named anonymous, MMZ range (0x64100000, 0x BFFFFFFF), size 1506304KB. If MMZ is divided into multiple ranges, there will be multiple ZON Es. ---MMZ\_USE\_INFO: total size=1512448KB(1477MB), used=86564KB(84MB + 548KB), remain=1425884KB(1392MB + 476KB), zone\_number=2, block\_number=16 This indicates overall MMZ statistics, including total MMZ size, used size, remaining size, number of ZON Es, etc. ### CMA Related In projects such as Hi3403V100, CMA is enabled by default. When CMA is enabled, the system reserves a portion of memory by default. Only part of this reserved memory may be used. Therefore, to save memory, customers can use the following two methods: 1. Adjust the system reserved memory. Use `cat /proc/meminfo` to view the current system reserved CMA memory and its usage. Cma Total is the total reserved CMA memory, and Cma Free is the remaining memory: Cma Total: 16384 kB Cma Free: 16068 kB Customers can adjust the reserved memory size by modifying the kernel configuration: Device Drivers -> Generic Driver Options -> Size in Mega Bytes After modifying the kernel configuration, please recompile the kernel. 2. Disable CMA. If customers do not need the CMA feature, they can disable it by modifying the kernel configuration: Kernel Features -> Contiguous Memory Allocator After modifying the kernel configuration, please recompile the kernel and ot\_osal.ko. ## Performance Related ### Effect and Impact of Adjusting USB Priority On XVR platforms, if the mouse cursor drifts automatically, this can be resolved by increasing the USB module priority. The method for adjusting USB module priority is as follows: ### CPU Performance Top Statistics Fluctuation Issue [Phenomenon] Using top for CPU utilization statistics is not very accurate and may show fluctuations, especially in low-load scenarios where top CPU utilization can fluctuate significantly. [Analysis] The Linux kernel version defaults to HZ=100 (10ms scheduling statistics). The statistical time granularity is coarse, resulting in insufficient accuracy and larger fluctuations. [Solution] For more accurate CPU utilization statistics, modify kernel HZ to 1000 to improve statistical precision. ### Precautions for Binding Interrupts to Different CPUs The following recommendations apply to binding interrupts to CP Us: - Bind CP Us before business operations start, do not dynamically switch during operation.
- Multiple cores of the same module should be bound to the same CPU.
- VPSS and VGS modules should be bound to the same CPU, because VPSS may call VGS for rotation, overlayex, coverex, mosaicex, line, brightness, and other functions.
- Identify modules with many interrupts and bind them to different CP Us. For example, if network interrupts are numerous, separate them from media services. ## Miniaturization ### Static Library Usage [Phenomenon] Applications only use a small portion of functions from libss\_mpi.a, but need to link library files such as vqev2 in addition to the mpi library, resulting in excessively large application files. [Analysis] By default, the linker needs to link all defined function tables in the library, thus referencing other libraries associated with the mpi library. [Solution] When generating the MPP version library, add the -ffunction-sections compilation option to Makefile.param. When the customer links to generate the application, add -Wl,--gc-sections. This effectively reduces the application size by removing unused functions. ## Where to Configure Pin Multiplexing, Clock Gating, and System Control? In the single Linux multi-core solution, pinmux, pin drive capability, clock gating (clk), and system control (sysctl) configurations are concentrated in interdrv/sysconfig/sys\_config.c. Users can modify them based on their product needs, compile them into sys\_config.ko, and the configuration takes effect after loading the ko. ## Video Cascade Configuration Precautions - During video cascading, VO outputs standard timing signals, and VI parses the timing, thus completing data transmission.
- When VI parses BT.1120 standard timing, it uses 0xff 00 00 as the sync header signal data. When VO generates timing signals, it writes status information in the blanking area for software management of cascade status. Note that during data transmission, sync header values should not appear in the blanking area, otherwise VI will parse the timing incorrectly, ultimately causing transmission failure.
- When calling ss\_mpi\_vo\_set\_cas\_pattern, users should avoid using pattern=0x7f, as it may cause the 0xff 00 00 sync header to appear. ## Fast Frame Buffer Rotation Scheme Usage [Phenomenon] For all self-encoded streams, implement fast frame buffer rotation, saving one VB per decoding channel. [Usage Notes] - Call ss\_mpi\_vdec\_set\_chn\_param to set display frame count to 0.
- Call ss\_mpi\_vpss\_disable\_backup\_frame to disable backup frames. ## Recompiling KO Process After Modifying Kernel Options [Phenomenon] Customers need to modify kernel options. After recompiling the kernel, driver K Os need to be recompiled. [Solution] - Modify kernel options and recompile the kernel. Refer to the readme\_cn.txt/readme\_en.txt files in the osdrv directory of the delivery package.
- After changing kernel options, all business drivers need to be recompiled and relinked. - For Hi3403V100, enter the mpp/out/obj directory, run: make clean; make. ipcm.ko and virt-tty.ko need to be compiled in osdrv to be updated. [Precautions] - The generated driver ko is automatically copied to the mpp/ko (Hi3403V100 copies to mpp/out/ko) directory, overwriting the old driver ko.
- The default kernel source path is open\_source/linux/linux-4.x.y in the delivery package (x is the kernel version). To specify a kernel path, use: make clean; make KERNEL\_ROOT=. ## Quick Schedule Precautions Quick schedule is an overall optimization scheme for VDEC-VPSS-VO, requiring end-to-end coordination to achieve optimal memory savings. The specific operations are as follows: 1. Use ss\_mpi\_vb\_set\_mod\_pool\_cfg and ss\_mpi\_vb\_init\_mod\_common\_pool to create VDEC VB (supports module VB and user VB, module VB recommended).
- Use ss\_mpi\_sys\_set\_schedule\_mode to set system schedule mode to OT\_SCHEDULE\_QUICK.
- Use ss\_mpi\_vdec\_set\_mod\_param to set vb\_src to OT\_VB\_SRC\_MOD (module VB recommended).
- Set VDEC mark mode to fast mark mode via ss\_mpi\_vdec\_set\_chn\_param (quick\_mark\_mode = OT\_QUICK\_MARK\_ADAPT or OT\_QUICK\_MARK\_FORCE).
- Set VDEC display frame count to 0 via ss\_mpi\_vdec\_set\_chn\_param (display\_frame\_num = 0).
- Use ss\_mpi\_vpss\_enable\_quick\_send to enable channel fast send mode. Disable backup frames, and set channel mode to auto mode.
- Use ss\_mpi\_vo\_set\_less\_buf\_attr to enable VO buffer saving (enable = TD\_TRUE). Set the vtth value based on different customer scenarios. See the VO section for details.
- Use ss\_mpi\_vo\_set\_video\_layer\_attr to set display\_buf\_len to 2 buffers, partition\_mode to OT\_VO\_PARTITION\_MODE\_MULTI (MULTI mode recommended). ### VDEC - VDEC fast schedule only takes effect in VDEC-VO and VDEC-VPSS-VO binding relationships.
- When mixing bound and unbound channels, user VB mode is recommended. Unbound channels should attach to a different pool than bound channels to avoid VB starvation.
- Fast reference frame release defaults to adaptive mode (OT\_QUICK\_MARK\_ADAPT).
- Force mode (OT\_QUICK\_MARK\_FORCE) supports normalP and SmartP streams without skip-frame reference for fast frame release saving VB. However, if the encoder sets skip-frame reference or reference frame count > 2, there is a decoding compatibility risk causing decoding artifacts.
- When compound decoding of enhancement layer is enabled, fast reference frame release does not take effect.
- After enabling fast schedule, display order output, IPB decode mode, and private VB mode are not supported.
- With fast schedule enabled, if a single VDEC channel binds to multiple VO channels, playback control is disabled.
- With fast schedule and dynamic bind/unbind scenarios, to avoid stuttering, call ss\_mpi\_vpss\_reset\_grp and ss\_mpi\_vo\_clear\_chn\_buf to reset before rebinding.
- With fast schedule and skip-frame reference streams in playback control scenarios, set display frame count to 1 to avoid stuttering. ### VPSS - With fast schedule, VPSS prioritizes VO-bound Groups, affecting real-time performance of non-VO-bound Groups.
- The VPSS proc info's old undo count may increase. Multiple Groups may have uneven old undo counts, which is normal.
- VPSS fast send mode interface does not support dynamic configuration; set it before enabling the channel.
- Various platform-specific limitations exist for VPSS fast send mode (Aspect Ratio, Flip, overscaling, channel post-processing, rotation, low latency, etc.). Refer to the original Chinese documentation for the complete platform-specific details. ### VO - VO buffer saving vtth2 value range is [2, vtth1], where vtth1 is set by ss\_mpi\_vo\_set\_vtth.
- If vtth2 is close to 2, no screen tearing risk, but may cause insufficient frame rate or frame drops. If close to vtth1, frame rate is sufficient but there is screen tearing risk.
- For fewer channels with larger resolutions, set vtth2 = vtth1-1. For more channels with smaller resolutions, set vtth2 close to 2.
- MULTI mode is recommended over SINGLE mode in buffer-saving fast schedule scenarios.
- Use hide/show for screen switching, not disable/enable. If using disable/enable, destroy the disabled front-end channels to ensure sufficient VB.
- If VDEC/VPSS performance is near the bottleneck with VO 2-buf, configure 3-buf to guarantee no frame drops. ## Low Latency Low latency features reduce delay between pipeline modules (e.g., VPSS->VO/VENC), including input low latency and output low latency. Module support varies by product. See the "Low Latency" section in "MPP Media Processing Software V5.0 Development Reference". ### VDEC - H264/H265 decode channels support output low latency via ss\_mpi\_vdec\_set\_low\_delay\_attr.
- H264/H265 decode supports slice input low latency via ss\_mpi\_vdec\_set\_chn\_param (slice\_input\_en). ### VPSS - Configure output low latency via ss\_mpi\_vpss\_set\_low\_delay\_attr.
- Disable channel post-processing features (see "VPSS Data Processing Flow").
- Enable fast schedule via ss\_mpi\_vpss\_enable\_quick\_send.
- Adjust VPSS online interrupt type via ss\_mpi\_vpss\_set\_grp\_frame\_interrupt\_attr. ### VO - Configure VO as single-screen direct mode. Refer to the "Video Output" chapter in the Development Reference.
- Set the channel receive threshold. Smaller values mean lower preview latency.
- Adjust the vertical timing interrupt threshold. Smaller values reduce latency.
- For non-direct SINGLE mode low latency, enable video layer early display. ### VENC - Input low latency is only supported on Hi3403V100.
- Output low latency includes H.264/H.265 slice interrupt output and JPEGE/MJPEGE ECS interrupt output.
- Hi3403V100 support slice low latency output (ss\_mpi\_venc\_set\_slice\_split).
- Hi3403V100 support ECS interrupt output (ss\_mpi\_venc\_set\_mjpeg\_param). ### VI - Input/output low latency is only supported on Hi3403V100.
- Configure pipe output low latency via ss\_mpi\_vi\_set\_pipe\_low\_delay\_attr.
- Configure channel/channel post-processing output low latency via ss\_mpi\_vi\_set\_chn\_low\_delay\_attr.
- Adjust VI interrupt type via ss\_mpi\_vi\_set\_pipe\_frame\_interrupt\_attr. ## Pixel Format Description The byte ordering for VGS module reading and writing YUV PACKAGE 422 format is as follows. 32-bit data byte-to-memory mapping: a7~0 = Byte0 bits, b7~0 = Byte1 bits, etc. **Figure 1** 32-bit Data to Memory Byte Mapping YUV PACKAGE 422 format component-to-memory byte mapping (using YUYV as example): **Figure 2** YUV PACKAGE 422 Component to Memory Byte Mapping All YUV PACKAGE 422 formats mapping: **Table 1** Pixel Format Component to Memory Byte Mapping

| Pixel Format | Byte3[7:0] | Byte2[7:0] | Byte1[7:0] | Byte0[7:0] |
| --- | --- | --- | --- | --- |
| OT\_PIXEL\_FORMAT\_YUYV\_PACKAGE\_422 | Y0 | U0 | Y1 | V0 |
| OT\_PIXEL\_FORMAT\_YVYU\_PACKAGE\_422 | Y0 | V0 | Y1 | U0 |
| OT\_PIXEL\_FORMAT\_UYVY\_PACKAGE\_422 | U0 | Y0 | V0 | Y1 |
| OT\_PIXEL\_FORMAT\_VYUY\_PACKAGE\_422 | V0 | Y0 | U0 | Y1 |

(Additional pixel format byte mappings follow the same pattern. See the original Chinese document for the complete list of 8 YUV PACKAGE 422 formats.) # VI

## Thermal Detector Interface ### T0 Type Detector Configuration #### CRG and Pin Multiplexing Configuration When loading the ko, use: load\_Hi3403V100 -a --sensor1 t0. Adjust pin multiplexing in sysconfig as needed, referring to functions thermo\_clock\_config and thermo\_sensor\_pin\_mux. #### MIPI Configuration No configuration required. #### VI Configuration #### VI DEV Attribute Configuration Only Dev1 can be used. Set intf\_mode to OT\_VI\_INTF\_MODE\_THERMO. Other configurations are the same as raw data input. Resolution set to 656x520. #### Thermal Attribute Configuration - work\_mode set to OT\_VI\_THERMO\_WORK\_MODE\_T0.[¶](#thermal-detector-interface-t0-type-detector-configuration-crg-and-pin-multiplexing-configuration-when-loading-the-ko-use-load_hi3403v100-a-sensor1-t0-adjust-pin-multiplexing-in-sysconfig-as-needed-referring-to-functions-thermo_clock_config-and-thermo_sensor_pin_mux-mipi-configuration-no-configuration-required-vi-configuration-vi-dev-attribute-configuration-only-dev1-can-be-used-set-intf_mode-to-ot_vi_intf_mode_thermo-other-configurations-are-the-same-as-raw-data-input-resolution-set-to-656x520-thermal-attribute-configuration-work_mode-set-to-ot_vi_thermo_work_mode_t0 "锚链接")

- ooc\_frame\_info set to 328x520, 16-bit raw data input.
- cfg\_num set to 60.
- sns\_cfg configuration (60-byte data array, see original document).
- frame\_rate set to 50 (currently invalid).
- sd\_mux set based on actual hardware routing. ### T1 Type Detector Configuration #### CRG and Pin Multiplexing Configuration Use: load\_Hi3403V100 -a -sensor0 t1. Adjust pin multiplexing as needed. #### MIPI Configuration (LVDS Configuration) 1. Configure LVDS attributes with combo\_dev\_attr\_t THERMO\_T1\_LVDS\_ATTR (devno=0, INPUT\_MODE\_LVDS, DATA\_TYPE\_RAW\_8BIT, etc.). See the original document for the full structure with sync codes and lane mapping. 2. Configure LVDS VBPLL. #### VI Configuration Set intf\_mode to OT\_VI\_INTF\_MODE\_THERMO. Resolution 164x123. #### Thermal Attribute Configuration - work\_mode set to OT\_VI\_THERMO\_WORK\_MODE\_T1.
- ooc\_frame\_info set to 82x123, 16-bit raw data.
- cfg\_num set to 60.
- frame\_rate set to 50.
- sd\_mux etc. configured based on hardware. ### T1 Aitemp Type Detector Configuration Similar to T1 LVDS but with different sync codes and register configurations. ### T1 ISC Type Detector Configuration Uses INPUT\_MODE\_MIPI with RAW data type. Similar to T1 but with MIPI instead of LVDS. ### T2 Type Detector Configuration Uses LVDS interface. Notable attributes include 160x120 resolution image rectangle. ## VI Frame Rate Readback Description The frame rate readback interface provides VICAP's internal frame rate statistics. See ss\_mpi\_vi\_get\_pipe\_fps and ss\_mpi\_vi\_get\_chn\_fps. ## VI Channel Offline Crop Invalid Issue [Phenomenon] VI channel offline crop may not take effect.
 [Solution] Ensure that the pipe's first enable is online mode. ## VI Channel Pipe Bind and Unbind VI supports dynamic bind/unbind. For different modes (online/offline), follow specific sequences for create, bind, start, and stop operations. ## VI Pipe Dynamic Frame Rate Setting Function Supports dynamic frame rate changes via ss\_mpi\_vi\_set\_pipe\_frame\_rate. Must stop dev/pipe first. ## VI Bind VPSS in Offline Mode - Scaler Performance Issue - Scale-down factor >= 16x is not supported in offline mode.
- Scale-down factor >= 8x may cause performance bottlenecks. ## VI Intf Sync Horizontal Pixel Count Not Aligned to 16 For BT.1120/BT.656 interfaces, ensure horizontal pixel count is aligned to 16 to avoid image shift. ## VI Ringing Green Border Issue [Phenomenon] Green border ringing on images.
 [Solution] Adjust VI module filter coefficients. # VO ## Static Logo Loading Flicker Issue [Phenomenon] Static logo loading causes flicker.
 [Solution] Set the channel layer to VGS layer before sending the logo. Logo configuration timing differs between HD and SD. ## Hi3403V100 Cascade VO Part Screen Flicker [Phenomenon] Flicker on cascaded VO partial screens.
 [Solution] Enable BTA for BT.1120 output. ## VO BT.1120 Clock Phase Setting [Phenomenon] Data sampling errors due to BT.1120 clock phase.
 [Solution] Use the debug register or sample delay interface ss\_mpi\_vo\_set\_sample\_delay to adjust delay. ## VO Compositing Graphical Layers and Video Layers [Phenomenon] Composited display of graphical layers over video layers may show only the graphical layer.
 [Analysis] Graphical layers have higher overlay priority and may completely cover the video layer if alpha transparency is not properly configured.
 [Solution] Set proper alpha values for the overlay operation. ## VO Channel Does Not Display Images [Phenomenon] After configuring all VO parameters per the document, no image is displayed.
 [Analysis] Possible issues with device enable timing and channel enable sequence.
 [Solution] - Enable the device before enabling channels.
- After enabling channels, delay at least 2 frames before sending images. ## VO Crop Feature Does Not Cover Entire Screen After Configuring Compositing Parameters [Phenomenon] After setting VO compositing parameters, configuring crop overlay area results in incomplete screen coverage.
 [Solution] Configure the compositing attribute bord\_en to set a border area and ensure the crop area dimensions are correct. ## VO Layer Extended Configuration Method Use ss\_mpi\_vo\_set\_video\_layer\_ext\_para to set custom timing parameters for the video layer. ## MIPI DSI Read Data Register Check Method [Phenomenon] Need to check MIPI DSI register data.
 [Solution] Use 'himdL' to read registers at mipi\_tx\_base + specific offsets for command packet, RX DATA, and payload. ## VO Cascading Common Issues - Confirm VO BT.1120 is outputting correct timing.
- Confirm VI can lock onto BT.1120 timing.
- Check for MIPI\_TX signal using an oscilloscope.
- Check cascade register configuration. # VENC ## JPEG Quantization Table Configuration Precautions Use ss\_mpi\_venc\_set\_jpeg\_param to set quantization tables. The luminance and chrominance tables should be configured separately. ## JPEG Dull/Gray Issue [Phenomenon] JPEG images appear dull or gray.
 [Solution] Adjust quantization tables and enable JPEG quality enhancement features. ## P-frame Intra Refresh Causes Visible Screen Scrolling [Phenomenon] P-frame intra refresh produces a visible scrolling effect.
 [Solution] Reduce the intra refresh cycle or use a different refresh mode. ## H.264 AVBR Bitrate Differences Compared to Other Platforms [Phenomenon] H.264 AVBR bitrates differ from other platforms.
 [Solution] Use VBV buffer size adjustment to fine-tune bitrate control. # VDEC ## MDC Decode Memory Usage When DDR > 3GB Configure VB pool properly for MDC decode mode. Memory mapping differs for DDR configurations exceeding 3GB. ## MDC Decode Module VB Usage Precautions Use module VB pool for MDC decode. Ensure VB size meets MDC requirements. ## VO Display Differences When Destroying VDEC Channels in Different Scenarios Destroying VDEC channels may cause different VO display behaviors depending on the pipeline configuration (direct display vs. VPSS processing). ## Decode Timeliness Optimization Optimize decode latency by adjusting decode buffer count and thread priority. # Pipeline Debugging Guide

## VI Pipeline Debugging ### I2C Errors Check I2C communication: verify pull-up resistors, clock frequency, and device address. Use i2c-tools for debugging. ### No Output Image or Black Screen [Phenomenon] No image output or black screen.[¶](#vi-pipeline-debugging-i2c-errors-check-i2c-communication-verify-pull-up-resistors-clock-frequency-and-device-address-use-i2c-tools-for-debugging-no-output-image-or-black-screen-phenomenon-no-image-output-or-black-screen "锚链接")

[Analysis] Possible causes: incorrect sensor configuration, MIPI/LVDS setup issues, clock problems.
[Solution] Check sensor initialization, verify MIPI/LVDS configuration, check clock signals. ### CC Error [Phenomenon] CC (Code Correction) errors reported by VI.
[Solution] Check signal integrity and adjust equalizer settings. ### Lost Interrupts [Phenomenon] VI interrupts being lost.
[Solution] Check interrupt binding, CPU load, and interrupt priority settings. ### Color Bar Debug Use built-in color bar to verify video pipeline without an external sensor. ## VO Pipeline Debugging ### VO Color Bar Usage Enable built-in VO color bar to verify output timing. ### VO Color Bar Configuration Configure specific color bar patterns and modes via the VO color bar interface. ## HDMI Pipeline Debugging ### Color Bar Usage Enable HDMI color bar to verify the HDMI output path. ### HDMI Color Bar HDMI color bar configuration details. # Other

## Dynamic Library ### Why Can't Static Compilation Applications Use Dynamic Libraries [Phenomenon] Statically compiled applications cannot link dynamic libraries.[¶](#dynamic-library-why-cant-static-compilation-applications-use-dynamic-libraries-phenomenon-statically-compiled-applications-cannot-link-dynamic-libraries "锚链接")

[Solution] Use dynamic linking or ensure all required libraries are statically linked. ### Why Does Dynamic Compilation with libss\_upvqe.a and libss\_dnvqe.a Cause Redefinition [Phenomenon] Redefinition errors when linking both upvqe and dnvqe libraries.
[Solution] Use --allow-multiple-definition or ensure only one VQE library is linked. ## Encoding Block Effect in IR Mode [Phenomenon] Visible block artifacts in IR mode encoding.
[Solution] Adjust encoding parameters for IR-specific noise characteristics. ## DVR Front-end 3840x480 Interlaced Scene Performance Optimization Optimize performance for interlaced 3840x480 capture on DVR front-end. ### Module KO Dependencies List of module driver dependencies and correct loading order. ## HDMI Hot Plug and Power Consumption HDMI hot plug detection may affect power consumption. Optimize by managing HDMI PHY power states. ## OSD Transparency and Color Issues OSD overlay transparency and color configuration guidelines. ## Partial VI Channel Startup Black Screen [Phenomenon] Starting some VI channels results in black screen.
[Solution] Check channel enable sequence and VB allocation. ## VDEC Backpressure Failure in Playback Mode [Phenomenon] Backpressure to VDEC fails during playback.
[Solution] Adjust buffer pool sizes or use alternative flow control. ## MIPI\_RX Pin Multiplexing Configuration Issue [Phenomenon] Incorrect MIPI\_RX pin multiplexing.
[Solution] Verify pinmux configuration for specific MIPI lanes in sysconfig. ## Hardware Timer Used for VI User Image Modification Using hardware timers to control VI user image update timing. ## EARLY/EARLY\_END Mode Early\_Line Configuration Suggestions Recommendations for configuring early\_line in EARLY and EARLY\_END modes for latency optimization. ## HNR/Smart Business Switching Process Switching between HNR (High Noise Reduction) and smart business modes. Follow the documented sequence to avoid configuration conflicts. ## VO Interrupt Delay Issue [Phenomenon] VO interrupt delays causing display issues.
[Solution] Check interrupt handling and CPU affinity settings. ## Hi3403V100 VI Buffer Overflow Interrupt Frame Drop Issue [Phenomenon] VI reporting buffer overflow interrupt and dropping frames.
[Solution] Increase VB pool size or reduce VI input load.