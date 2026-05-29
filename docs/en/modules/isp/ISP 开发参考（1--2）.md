---
title: Chapter 1–2
---

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ISP Development Reference/ISP Development Reference (1-2).md
--- # Preface
**Overview** This document is written for programmers using ISP development, aiming to provide solutions and assistance for issues encountered during development. > **Note:** >This document uses Hi3403V100 as the description example. Unless otherwise specified, the content for is the same as Hi3403V100. **Product Version** The product version corresponding to this document is as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Target Audience** This document (guide) is mainly applicable to the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document, and their meanings are as follows.

| Symbol | Description |
| --- | --- |
| | Indicates a high-risk hazard which, if not avoided, will result in death or serious injury. |

**Revision History** The revision history accumulates descriptions of each document update. The latest version of the document contains the updates from all previous document versions.

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# Overview

## Overview ISP completes the processing of digital image effects through a series of digital image processing algorithms. It mainly includes 3A, bad pixel correction, denoising, highlight suppression, backlight compensation, color enhancement, lens shading correction, and other processing. ISP consists of a logic part and the firmware running on it. This section mainly introduces the ISP user interface. ## Function Description The ISP control structure is shown in [Figure 1](#fig19534124782113). After the lens projects the light signal onto the sensor's photosensitive area, the sensor performs photoelectric conversion and sends the original Bayer format image to the ISP. The ISP processes it through algorithms and outputs an RGB space domain image to the backend video capture unit. During this process, the ISP controls the ISP logic, lens, and sensor through the firmware running on it, thereby implementing functions such as auto iris, auto exposure, and auto white balance. The firmware operation is driven by interrupts from the video capture unit. The PQ Tools tool performs online image quality adjustment of the ISP through the network port or serial port. The ISP consists of ISP logic and the firmware running on it. In addition to completing part of the algorithm processing, the logic unit can also collect real-time information about the current image. The firmware obtains image statistics from the ISP logic, recalculates, and provides feedback control to the lens, sensor, and ISP logic to achieve automatic image quality adjustment. **Figure 1** ISP Control Structure Diagram For the main ISP logic flow, specific concepts, and functional points, please refer to the chip manual. ### Architecture The ISP firmware consists of three parts: one part is the ISP control unit and basic algorithm library, one part is the AE/AWB algorithm library, and one part is the sensor library. The basic idea of the firmware design is to provide the 3A algorithm library separately, with the ISP control unit scheduling the basic algorithm library and the 3A algorithm library, while the sensor library registers function callbacks to the ISP basic algorithm library and the 3A algorithm library respectively, to achieve differentiated sensor adaptation. The ISP firmware architecture is shown in [Figure 1](#fig1959110622411). **Figure 1** ISP Firmware Architecture Different sensors all register control functions with the ISP algorithm library in the form of callback functions. When the ISP control unit schedules the basic algorithm library and the 3A algorithm library, it will obtain initialization parameters through these callback functions and control the sensor, such as adjusting exposure time, analog gain, digital gain, and controlling lens step focusing or iris rotation. ### Development Mode The SDK supports users using multiple development modes: 1. Users use the SDK's 3A algorithm library. In this case, users need to adapt different sensors according to the sensor adaptation interfaces provided by the ISP basic algorithm library and the 3A algorithm library. Each sensor corresponds to a folder, which contains two main files: - sensor\_cmos.c This file mainly implements the callback functions required by ISP. These callback functions contain the sensor adaptation algorithm, which may vary for different sensors. - sensor\_ctrl.c The sensor's low-level control driver, mainly implementing sensor read/write and initialization operations. Users can develop these two files based on the sensor's datasheet, and can seek support from the sensor manufacturer when necessary. 2. Users implement their own 3A algorithm library development based on the 3A algorithm registration interface provided by the ISP library. In this case, users need to adapt different sensors according to the sensor adaptation interfaces provided by the ISP basic algorithm library and the user's 3A algorithm library.[¶](#overview-isp-completes-the-processing-of-digital-image-effects-through-a-series-of-digital-image-processing-algorithms-it-mainly-includes-3a-bad-pixel-correction-denoising-highlight-suppression-backlight-compensation-color-enhancement-lens-shading-correction-and-other-processing-isp-consists-of-a-logic-part-and-the-firmware-running-on-it-this-section-mainly-introduces-the-isp-user-interface-function-description-the-isp-control-structure-is-shown-in-figure-1-after-the-lens-projects-the-light-signal-onto-the-sensors-photosensitive-area-the-sensor-performs-photoelectric-conversion-and-sends-the-original-bayer-format-image-to-the-isp-the-isp-processes-it-through-algorithms-and-outputs-an-rgb-space-domain-image-to-the-backend-video-capture-unit-during-this-process-the-isp-controls-the-isp-logic-lens-and-sensor-through-the-firmware-running-on-it-thereby-implementing-functions-such-as-auto-iris-auto-exposure-and-auto-white-balance-the-firmware-operation-is-driven-by-interrupts-from-the-video-capture-unit-the-pq-tools-tool-performs-online-image-quality-adjustment-of-the-isp-through-the-network-port-or-serial-port-the-isp-consists-of-isp-logic-and-the-firmware-running-on-it-in-addition-to-completing-part-of-the-algorithm-processing-the-logic-unit-can-also-collect-real-time-information-about-the-current-image-the-firmware-obtains-image-statistics-from-the-isp-logic-recalculates-and-provides-feedback-control-to-the-lens-sensor-and-isp-logic-to-achieve-automatic-image-quality-adjustment-figure-1-isp-control-structure-diagram-for-the-main-isp-logic-flow-specific-concepts-and-functional-points-please-refer-to-the-chip-manual-architecture-the-isp-firmware-consists-of-three-parts-one-part-is-the-isp-control-unit-and-basic-algorithm-library-one-part-is-the-aeawb-algorithm-library-and-one-part-is-the-sensor-library-the-basic-idea-of-the-firmware-design-is-to-provide-the-3a-algorithm-library-separately-with-the-isp-control-unit-scheduling-the-basic-algorithm-library-and-the-3a-algorithm-library-while-the-sensor-library-registers-function-callbacks-to-the-isp-basic-algorithm-library-and-the-3a-algorithm-library-respectively-to-achieve-differentiated-sensor-adaptation-the-isp-firmware-architecture-is-shown-in-figure-1-figure-1-isp-firmware-architecture-different-sensors-all-register-control-functions-with-the-isp-algorithm-library-in-the-form-of-callback-functions-when-the-isp-control-unit-schedules-the-basic-algorithm-library-and-the-3a-algorithm-library-it-will-obtain-initialization-parameters-through-these-callback-functions-and-control-the-sensor-such-as-adjusting-exposure-time-analog-gain-digital-gain-and-controlling-lens-step-focusing-or-iris-rotation-development-mode-the-sdk-supports-users-using-multiple-development-modes-1-users-use-the-sdks-3a-algorithm-library-in-this-case-users-need-to-adapt-different-sensors-according-to-the-sensor-adaptation-interfaces-provided-by-the-isp-basic-algorithm-library-and-the-3a-algorithm-library-each-sensor-corresponds-to-a-folder-which-contains-two-main-files-sensor_cmosc-this-file-mainly-implements-the-callback-functions-required-by-isp-these-callback-functions-contain-the-sensor-adaptation-algorithm-which-may-vary-for-different-sensors-sensor_ctrlc-the-sensors-low-level-control-driver-mainly-implementing-sensor-readwrite-and-initialization-operations-users-can-develop-these-two-files-based-on-the-sensors-datasheet-and-can-seek-support-from-the-sensor-manufacturer-when-necessary-2-users-implement-their-own-3a-algorithm-library-development-based-on-the-3a-algorithm-registration-interface-provided-by-the-isp-library-in-this-case-users-need-to-adapt-different-sensors-according-to-the-sensor-adaptation-interfaces-provided-by-the-isp-basic-algorithm-library-and-the-users-3a-algorithm-library "锚链接")

1. Users partially use the 3A algorithm library from the SDK and partially implement their own 3A algorithm library. For example, AE uses libot\_ae.a, and AWB uses its own 3A algorithm library. The SDK provides flexible and diverse support methods. ### Internal Flow The firmware internal flow is divided into two parts, as shown in [Figure 1](#fig39021449132613). One part is the initialization task, which mainly completes the initialization of the ISP control unit, ISP basic algorithm library, and 3A algorithm library, including calling sensor callbacks to obtain sensor-specific initialization parameters. The other part is the dynamic adjustment process, during which the ISP control unit in the firmware schedules the ISP basic algorithm library and the 3A algorithm library, performing real-time calculations and corresponding control. The firmware software structure is shown in [Figure 2](#fig81434122714). **Figure 1** ISP Firmware Internal Flow **Figure 2** ISP Firmware Software Structure ### Software Flow As the front-end capture component, ISP needs to work together with the Video Input Unit (VIU). After ISP initialization and basic configuration, the VIU needs to perform interface timing matching. This is done first to match the input timing of different sensors, and second to configure the correct input timing for the ISP. Once the timing configuration is complete, the ISP can start running to perform dynamic image quality adjustment. The output image is then captured by the VIU and sent for display or encoding. The software usage flow is shown in [Figure 1](#fig796617213110). The PQ Tools tool mainly performs dynamic image quality adjustment on the PC side, allowing adjustment of multiple factors that affect image quality, such as denoising strength, color conversion matrix, and saturation. **Figure 1** ISP Firmware Usage Flow After the user has debugged the image effect, they can use the configuration file save function provided by the PQ Tools tool to save the configuration parameters. On the next startup, the system can use the configuration file loading function provided by the PQ Tools tool to load the already adjusted image parameters. Code Example: ```[¶](#software-flow-as-the-front-end-capture-component-isp-needs-to-work-together-with-the-video-input-unit-viu-after-isp-initialization-and-basic-configuration-the-viu-needs-to-perform-interface-timing-matching-this-is-done-first-to-match-the-input-timing-of-different-sensors-and-second-to-configure-the-correct-input-timing-for-the-isp-once-the-timing-configuration-is-complete-the-isp-can-start-running-to-perform-dynamic-image-quality-adjustment-the-output-image-is-then-captured-by-the-viu-and-sent-for-display-or-encoding-the-software-usage-flow-is-shown-in-figure-1-the-pq-tools-tool-mainly-performs-dynamic-image-quality-adjustment-on-the-pc-side-allowing-adjustment-of-multiple-factors-that-affect-image-quality-such-as-denoising-strength-color-conversion-matrix-and-saturation-figure-1-isp-firmware-usage-flow-after-the-user-has-debugged-the-image-effect-they-can-use-the-configuration-file-save-function-provided-by-the-pq-tools-tool-to-save-the-configuration-parameters-on-the-next-startup-the-system-can-use-the-configuration-file-loading-function-provided-by-the-pq-tools-tool-to-load-the-already-adjusted-image-parameters-code-example "锚链接")

td\_s32 ret;
ot\_isp\_3a\_alg\_lib ae\_lib;
ot\_isp\_3a\_alg\_lib awb\_lib;
ot\_isp\_pub\_attr pub\_attr;
pthread\_t isp\_pid;
ot\_vi\_pipe vi\_pipe = 0;
/ *Register sensor library* /
ret = sensor\_register\_callback(vi\_pipe, &ae\_lib, &awb\_lib);
if (ret != TD\_SUCCESS) {
printf(”register sensor failed!\n”);
return ret;
} / *Register AE algorithm library* /
ae\_lib.id = 0;
strncpy(ae\_lib.lib\_name, OT\_AE\_LIB\_NAME, sizeof(OT\_AE\_LIB\_NAME));
ret = ss\_mpi\_ae\_register(isp\_dev, &ae\_lib);
if (ret != TD\_SUCCESS) { printf("ss\_mpi\_ae\_register failed with %#x!\n", ret); return ret;
} / *Register AWB algorithm library* /
awb\_lib.id = isp\_dev;
strncpy(awb\_lib.lib\_name, OT\_AWB\_LIB\_NAME, sizeof(OT\_AWB\_LIB\_NAME)); ret = ss\_mpi\_awb\_register(isp\_dev, &awb\_lib);
if (ret != TD\_SUCCESS) { printf("ss\_mpi\_awb\_register failed with %#x!\n", ret); return ret;
} / *Initialize ISP external registers* / ret = ss\_mpi\_isp\_mem\_init(vi\_pipe); if (ret != TD\_SUCCESS) { printf("ss\_mpi\_isp\_mem\_init failed with %#x!\n", ret); return ret; } / *Configure image common attributes* / ret = ss\_mpi\_isp\_set\_pub\_attr (vi\_pipe, & pub\_attr); if (ret != TD\_SUCCESS) {
printf("ss\_mpi\_isp\_set\_pub\_attr failed with %#x!\n", ret); return ret; }
/ *Initialize ISP Firmware* /
ret = ss\_mpi\_isp\_init(vi\_pipe);
if (ret != TD\_SUCCESS) {
printf(”isp init failed!\n”);
return ret;
} / *Start ss\_mpi\_isp\_run in a separate thread* /
if (0 != pthread\_create(&isp\_pid, 0, ISP\_Run, NULL))
{ printf("create isp running thread failed!\n"); return TD\_FAILURE;
} / *Start VI/VO and other services* / …… / *Stop VI/VO and other services* /
ret = ss\_mpi\_isp\_exit (vi\_pipe);
if (TD\_SUCCESS != ret) {
printf(”isp exit failed!\n”);
return ret;
} pthread\_join(isp\_pid, 0);
return TD\_SUCCESS; ``` > **Note:** >The AE library uses the standard C math library. Please add the -lm compilation flag in the Makefile. ### File Organization The file organization structure of the ISP firmware is shown in [Figure 1](#fig142122515335). The ISP library, 3A library, sensor library, dehaze library, ldci library, and drc library are each independent. The driver generated by drv in the firmware reports ISP interrupts to user space and drives the ISP control unit of the firmware to operate using these interrupts. The ISP control unit obtains statistics from the driver program and schedules the basic algorithm unit and 3A algorithm library, finally configuring registers through the driver. The Src folder contains the ISP control unit and basic algorithm unit, which are compiled to generate libss\_isp.a and libot\_isp.a, i.e., the ISP library. The 3a folder contains the AE/AWB algorithm library; users can also develop their own 3A algorithms based on a unified interface. The Sensor folder contains driver programs for each sensor; this code is open source. The dehaze folder corresponds to the dehazing algorithm program, the ldci folder corresponds to the local automatic contrast enhancement algorithm program, and the drc folder corresponds to the dynamic range compression algorithm program; these parts are not open source. **Figure 1** ISP Firmware File Organization # System Control[¶](#system-control "锚链接")

<a name="ZH-CN_TOPIC_0000002471084920"></a>## Function Overview The system control section includes ISP public attribute configuration, initializing the ISP firmware, running the ISP firmware, exiting the ISP firmware, and setting ISP modules and other functions. ## API Reference The interfaces in this document, unless otherwise specified, support multi-process. - [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920): Initialize the ISP external registers.[¶](#function-overview-the-system-control-section-includes-isp-public-attribute-configuration-initializing-the-isp-firmware-running-the-isp-firmware-exiting-the-isp-firmware-and-setting-isp-modules-and-other-functions-api-reference-the-interfaces-in-this-document-unless-otherwise-specified-support-multi-process-ss_mpi_isp_mem_init-initialize-the-isp-external-registers "锚链接")

<a name="ZH-CN_TOPIC_0000002471085190"></a>- [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190): Initialize the ISP firmware.
<a name="ZH-CN_TOPIC_0000002470925164"></a>- [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164): Run the ISP firmware.
<a name="ZH-CN_TOPIC_0000002470925158"></a>- [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000002470925158): Run the ISP firmware once.
<a name="ZH-CN_TOPIC_0000002503964923"></a>- [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923): Exit the ISP firmware.
<a name="ZH-CN_TOPIC_0000002503964829"></a>- [ss\_mpi\_isp\_set\_pub\_attr](#ZH-CN_TOPIC_0000002503964829): Set the ISP public attributes.
<a name="ZH-CN_TOPIC_0000002504085055"></a>- [ss\_mpi\_isp\_get\_pub\_attr](#ZH-CN_TOPIC_0000002504085055): Get the ISP public attributes.
<a name="ZH-CN_TOPIC_0000002503964889"></a>- [ss\_mpi\_isp\_set\_fmw\_state](#ZH-CN_TOPIC_0000002503964889): Set the ISP firmware state.
<a name="ZH-CN_TOPIC_0000002503965107"></a>- [ss\_mpi\_isp\_get\_fmw\_state](#ZH-CN_TOPIC_0000002503965107): Get the ISP firmware state.
<a name="ZH-CN_TOPIC_0000002503965133"></a>- [ss\_mpi\_isp\_set\_sns\_slave\_attr](#ZH-CN_TOPIC_0000002503965133): Set the slave mode sensor H/V sync signal.
<a name="ZH-CN_TOPIC_0000002503964929"></a>- [ss\_mpi\_isp\_get\_sns\_slave\_attr](#ZH-CN_TOPIC_0000002503964929): Get the slave mode sensor H/V sync signal.
<a name="ZH-CN_TOPIC_0000002504084719"></a>- [ss\_mpi\_isp\_set\_module\_ctrl](#ZH-CN_TOPIC_0000002504084719): Set the ISP function module control.
<a name="ZH-CN_TOPIC_0000002503964897"></a>- [ss\_mpi\_isp\_get\_module\_ctrl](#ZH-CN_TOPIC_0000002503964897): Get the ISP function module control.
<a name="ZH-CN_TOPIC_0000002504085017"></a>- [ss\_mpi\_isp\_get\_vd\_time\_out](#ZH-CN_TOPIC_0000002504085017): Get the ISP interrupt information.
<a name="ZH-CN_TOPIC_0000002503964973"></a>- [ss\_mpi\_isp\_sensor\_reg\_callback](#ZH-CN_TOPIC_0000002503964973): ISP sensor registration callback interface.
<a name="ZH-CN_TOPIC_0000002504084971"></a>- [ss\_mpi\_isp\_sensor\_unreg\_callback](#ZH-CN_TOPIC_0000002504084971): ISP sensor unregistration callback interface.
<a name="ZH-CN_TOPIC_0000002470925170"></a>- [ss\_mpi\_isp\_ae\_lib\_reg\_callback](#ZH-CN_TOPIC_0000002470925170): ISP AE library registration callback interface.
<a name="ZH-CN_TOPIC_0000002504085045"></a>- [ss\_mpi\_isp\_ae\_lib\_unreg\_callback](#ZH-CN_TOPIC_0000002504085045): ISP AE library unregistration callback interface.
<a name="ZH-CN_TOPIC_0000002471084946"></a>- [ss\_mpi\_isp\_awb\_lib\_reg\_callback](#ZH-CN_TOPIC_0000002471084946): ISP AWB library registration callback interface.
<a name="ZH-CN_TOPIC_0000002470924890"></a>- [ss\_mpi\_isp\_awb\_lib\_unreg\_callback](#ZH-CN_TOPIC_0000002470924890): ISP AWB library unregistration callback interface.
<a name="ZH-CN_TOPIC_0000002503964869"></a>- [ss\_mpi\_isp\_set\_bind\_attr](#ZH-CN_TOPIC_0000002503964869): Set the binding relationship between the ISP library, 3A library, and sensor.
<a name="ZH-CN_TOPIC_0000002504085091"></a>- [ss\_mpi\_isp\_get\_bind\_attr](#ZH-CN_TOPIC_0000002504085091): Get the binding relationship between the ISP library, 3A library, and sensor.
<a name="ZH-CN_TOPIC_0000002471084974"></a>- [ss\_mpi\_isp\_set\_dcf\_info](#ZH-CN_TOPIC_0000002471084974): Set the DCF parameters.
<a name="ZH-CN_TOPIC_0000002504085077"></a>- [ss\_mpi\_isp\_get\_dcf\_info](#ZH-CN_TOPIC_0000002504085077): Get the DCF parameters.
<a name="ZH-CN_TOPIC_0000002504084755"></a>- [ss\_mpi\_isp\_set\_pipe\_differ\_attr](#ZH-CN_TOPIC_0000002504084755): Set the multi-channel ISP Pipe difference attributes.
<a name="ZH-CN_TOPIC_0000002503964909"></a>- [ss\_mpi\_isp\_get\_pipe\_differ\_attr](#ZH-CN_TOPIC_0000002503964909): Get the multi-channel ISP Pipe difference attributes.
<a name="ZH-CN_TOPIC_0000002504084839"></a>- [ss\_mpi\_isp\_set\_ctrl\_param](#ZH-CN_TOPIC_0000002504084839): Set the ISP control parameters.
<a name="ZH-CN_TOPIC_0000002471085186"></a>- [ss\_mpi\_isp\_get\_ctrl\_param](#ZH-CN_TOPIC_0000002471085186): Get the ISP control parameters.
<a name="ZH-CN_TOPIC_0000002503965069"></a>- [ss\_mpi\_isp\_set\_mod\_param](#ZH-CN_TOPIC_0000002503965069): Set the ISP module parameters.
<a name="ZH-CN_TOPIC_0000002503964891"></a>- [ss\_mpi\_isp\_get\_mod\_param](#ZH-CN_TOPIC_0000002503964891): Get the ISP module parameters.
<a name="ZH-CN_TOPIC_0000002470924926"></a>- [ss\_mpi\_isp\_set\_smart\_info](#ZH-CN_TOPIC_0000002470924926): Set the ISP module smart information.
<a name="ZH-CN_TOPIC_0000002503964955"></a>- [ss\_mpi\_isp\_get\_smart\_info](#ZH-CN_TOPIC_0000002503964955): Get the ISP module smart information.
<a name="ZH-CN_TOPIC_0000002470924968"></a>- [ss\_mpi\_isp\_get\_lightbox\_gain](#ZH-CN_TOPIC_0000002470924968): Get the gain structure obtained from AWB online calibration.
<a name="ZH-CN_TOPIC_0000002470925130"></a>- [ss\_mpi\_isp\_ir\_auto\_run\_once](#ZH-CN_TOPIC_0000002470925130): Run the IR auto-switch function.
<a name="ZH-CN_TOPIC_0000002470924938"></a>- [ss\_mpi\_isp\_set\_be\_frame\_attr](#ZH-CN_TOPIC_0000002470924938): Set the ISP BE frame attributes.
<a name="ZH-CN_TOPIC_0000002470924858"></a>- [ss\_mpi\_isp\_get\_be\_frame\_attr](#ZH-CN_TOPIC_0000002470924858): Get the ISP BE frame attributes.
<a name="ZH-CN_TOPIC_0000002503964825"></a>- [ss\_mpi\_isp\_get\_noise\_calibration](#ZH-CN_TOPIC_0000002503964825): Get the noise model calibration parameters.
<a name="ZH-CN_TOPIC_0000002471085032"></a>- [ss\_mpi\_isp\_set\_frame\_info](#ZH-CN_TOPIC_0000002471085032): Set the ISP real-time information.
<a name="ZH-CN_TOPIC_0000002503965017"></a>- [ss\_mpi\_isp\_get\_frame\_info](#ZH-CN_TOPIC_0000002503965017): Get the ISP real-time information.
<a name="ZH-CN_TOPIC_0000002504084749"></a>- [ss\_mpi\_isp\_mem\_share](#ZH-CN_TOPIC_0000002504084749): Share ISP-related mmz buffer with a specific process ID.
<a name="ZH-CN_TOPIC_0000002470925018"></a>- [ss\_mpi\_isp\_mem\_unshare](#ZH-CN_TOPIC_0000002470925018): Unshare ISP-related mmz buffer from the process ID.
<a name="ZH-CN_TOPIC_0000002470924996"></a>- [ss\_mpi\_isp\_mem\_share\_all](#ZH-CN_TOPIC_0000002470924996): Share ISP-related mmz buffer with all processes without process ID restriction.
<a name="ZH-CN_TOPIC_0000002470924886"></a>- [ss\_mpi\_isp\_mem\_unshare\_all](#ZH-CN_TOPIC_0000002470924886): Cancel sharing of ISP-related mmz buffer with all processes. ### ss\_mpi\_isp\_mem\_init [Description] Initialize the ISP external registers. **Syntax** `td_s32 ss_mpi_isp_mem_init(ot_vi_pipe vi_pipe);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Before initializing the external registers, ensure that the ko is loaded and the sensor has registered the callback function with the ISP.
- Only after calling This interface can you call [ss\_mpi\_isp\_set\_pub\_attr](#ZH-CN_TOPIC_0000002503964829) to set the image public attributes.
- Not supported for multi-process. Must be called in the same process as sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164), and [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923).
- This interface cannot be called while [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164) is running.
- It is recommended to call [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923) first, then call This interface for re-initialization.
- Lite OS does not have the concept of kernel module loading. The Linux ko loading process corresponds to the relevant process executed in sdk\_init.c under LiteOS release/ko.
<a name="ZH-CN_TOPIC_0000001174819160"></a>- Not supported for multi-threaded ISP creation and destruction on the same vi\_pipe (multi-threaded simultaneous calls to sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000001174819160), [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923))
- After ISP initialization, one frame time is needed for the hardware to read the algorithm coefficient table. Therefore, within one frame time after [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), the [ss\_mpi\_vi\_stop\_pipe](#ss_mpi_vi_stop_pipe) interface cannot be called to stop the pipe. ss\_mpi\_vi\_stop\_pipe See the "Video Input" chapter of the "MPP Media Processing Software V5.0 Development Reference") **Example** None **Related Topics** [ss\_mpi\_isp\_exit](#ss_mpi_isp_exit) ### ss\_mpi\_isp\_init [Description] Initialize the ISP firmware. **Syntax** `td_s32 ss_mpi_isp_init(ot_vi_pipe vi_pipe);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Before initialization, ensure that the ko is loaded and the sensor has registered the callback function with the ISP.
- Before initialization, ensure that [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920) has been called to initialize the ISP external registers.
- Before initialization, ensure that [ss\_mpi\_isp\_set\_pub\_attr](#ZH-CN_TOPIC_0000002503964829) has been called to set the image public attributes.
- Not supported for multi-process. Must be called in the same process as sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164), and [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923).
- Not supported for repeated calls to This interface.
- It is recommended to call [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923) first, then call This interface for re-initialization.
- Lite OS does not have the concept of kernel module loading. The Linux ko loading process corresponds to the relevant process executed in sdk\_init.c under LiteOS release/ko.
- Not supported for multi-threaded ISP creation and destruction on the same vi\_pipe (multi-threaded simultaneous calls to sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923))
- After ISP initialization, one frame time is needed for the hardware to read the algorithm coefficient table. Therefore, within one frame time after [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), the ss\_mpi\_vi\_stop\_pipe interface cannot be called to stop the pipe. ss\_mpi\_vi\_stop\_pipe See the "Video Input" chapter of the "MPP Media Processing Software V5.0 Development Reference". **Example** None **Related Topics** [ss\_mpi\_isp\_exit](#ss_mpi_isp_exit) ### ss\_mpi\_isp\_run [Description] Run the ISP firmware. **Syntax** `td_s32 ss_mpi_isp_run(ot_vi_pipe vi_pipe);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Before running, ensure that the sensor has been initialized and has registered the callback function with the ISP.
- Before running, ensure that [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190) has been called to initialize the ISP.
- Not supported for multi-process. Must be called in the same process as sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), and [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923).
- This interface is a blocking interface. It is recommended that users use a real-time thread for processing. **Example** None **Related Topics** [ss\_mpi\_isp\_init](#ss_mpi_isp_init) ### ss\_mpi\_isp\_run\_once [Description] Run the ISP firmware once. **Syntax** `td_s32 ss_mpi_isp_run_once(ot_vi_pipe vi_pipe);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Before running, ensure that the sensor has been initialized and has registered the callback function with the ISP.
- Before running, ensure that [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190) has been called to initialize the ISP.
- Not supported for multi-process. Must be called in the same process as sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), and [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923).
- This interface is a blocking interface. It is recommended that users use a real-time thread for processing.
<a name="ZH-CN_TOPIC_0000001219938931"></a>- This interface works in offline mode when users feed RAW data to BE. When using it, you must wait for the previously sent RAW data to be processed before making the next [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000001219938931) call and sending RAW data (this can be achieved by calling ss\_mpi\_vi\_get\_chn\_frame after ss\_mpi\_vi\_send\_pipe\_raw. For more details, see the VI chapter of the "MPP Media Processing Software V5.0 Development Reference"). Refer to the pseudocode in **Example** for details.
- When processing video streams using [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000001219938931) mode, mode switching and resolution switching are supported. The switching process is similar to processing video streams using [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164): the ISP module does not need to exit during switching, but the VI module needs to be destroyed and recreated. The difference is that when using [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000001219938931) to process video streams, users need to create a thread. Refer to the pseudocode in the example.
- [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164) and [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000001219938931) cannot be used simultaneously on the same vi\_pipe.
- This interface does not support frame-combining WDR mode.
- This interface configures the sensor time only after being called. This differs from [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164), which configures the sensor at frame start or frame end.
<a name="ZH-CN_TOPIC_0000002470925008"></a>- For pipes using This interface, when using the [ss\_mpi\_isp\_get\_vd\_time\_out](#ZH-CN_TOPIC_0000002504085017) interface, the [ot\_isp\_vd\_type](#ZH-CN_TOPIC_0000002470925008) variable only supports the OT\_ISP\_VD\_BE\_END type.
- This interface does not support stitching mode. **Example** 1. Only after the previously sent RAW data has been fully processed can the next call to [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000001219938931) be made: `……
ret = ss_mpi_isp_run_once(vi_pipe); if (TD_SUCCESS != ret) { SAMPLE_PRT("ss_mpi_isp_run_once failed with %#x\n", ret); return ret; } ret = ss_mpi_vi_send_pipe_raw(vi_pipe, frame_info, frame_num, milli_sec); if (TD_SUCCESS != ret) { SAMPLE_PRT("ss_mpi_vi_send_pipe_raw failed with %#x\n", ret); return ret; } ret = ss_mpi_vi_get_chn_frame(vi_pipe, vi_chn, &yuv_frame_info, milli_sec); if (TD_SUCCESS != ret) { SAMPLE_PRT("ss_mpi_vi_get_chn_frame failed with %#x\n", ret); return ret;
} ret = ss_mpi_vi_release_chn_frame(vi_pipe, vi_chn, &yuv_frame_info); if (TD_SUCCESS != ret) { SAMPLE_PRT("ss_mpi_vi_release_chn_frame failed with %#x\n", ret); return ret;
}` 2. When using [ss\_mpi\_isp\_run\_once](#ZH-CN_TOPIC_0000001219938931) to process a video stream, the user must create a separate thread: `…
st Vi Config.ast Vi Info[s32Sns Id].stSnsInfo.enSnsType = SENSOR_NAME_MIPI_8M_30FPS_12BIT, st Vi Config.ast Vi Info[s32SnsId].stDevInfo.enWDRMode = WDR_MODE_3To1_LINE;
… pthread_t thread; ret = pthread_create(&thread, NULL, Ot_Vi_SendWDRFrameProc, (ot_void*)&stSendRawThreadInfo); if (0 == ret) { pthread_detach(thread); } SAMPLE_COMM_VI_SwitchMode_StopVI(&stViConfig); g_u32RunOnceSwitch =1; g_enWDRMode = WDR_MODE_NONE; st Vi Config.ast Vi Info[s32Sns Id].stSnsInfo.enSnsType = SENSOR_NAME_MIPI_8M_30FPS_12BIT; st Vi Config.ast Vi Info[s32SnsId].stDevInfo.enWDRMode = WDR_MODE_NONE; st Vi Config.ast Vi Info[0].st Pipe Info.a Pipe[0] = Vi Raw Out Pipe; st Vi Config.ast Vi Info[0].st Pipe Info.a Pipe[1] = -1; st Vi Config.ast Vi Info[0].st Pipe Info.a Pipe[2] = -1; st Vi Config.ast Vi Info[0].st Pipe Info.a Pipe[3] = -1; SAMPLE_RunonceSwitch_StartVi(&stViConfig); SAMPLE_COMM_VI_SwitcotSPMode(&stViConfig); g_u32RunOnceSwitch =0; static void *Ot_Vi_SendWDRFrameProc(void *pArgs)
{
……
while(1) { td_s32 s32MilliSec = 100; i++; if(g_u32RunOnceSwitch ==1) { ss_mpi_isp_run_once(ViRawOutPipe); } if ( g_enWDRMode == WDR_MODE_3To1_LINE ) { ret = SS_MPI_VI_GetPipeFrame(ViRawOutPipe, &stRaw Info[0], s32Milli Sec); if (TD_SUCCESS != ret) { SAMPLE_PRT("SS_MPI_VI_GetPipeFrame failed with %#x\n", ret); continue; } ret = SAMPLE_Capture_VideoWDRFrameProc(ViRawOutPipe, &st Raw Info[0], &st Raw Info[1], &st Raw Info[2]); if (TD_SUCCESS != ret) { break; } ret = SS_MPI_VI_ReleasePipeFrame(ViRawOutPipe, &st Raw Info[0]); if (TD_SUCCESS != ret) { SAMPLE_PRT("SS_MPI_VI_ReleasePipeFrame failed with %#x\n", ret); goto EXIT5; } } if ( g_enWDRMode == WDR_MODE_NONE ) { ret = SS_MPI_VI_GetPipeFrame(ViRawOutPipe, &stRaw Info[0], s32Milli Sec); if (TD_SUCCESS != ret) { SAMPLE_PRT("SS_MPI_VI_GetPipeFrame failed with %#x\n", ret); continue; } ret = SAMPLE_Capture_VideoFrameProc(ViRawOutPipe, &st Raw Info[0]); if (TD_SUCCESS != ret) { break; } ret = SS_MPI_VI_ReleasePipeFrame(ViRawOutPipe, &st Raw Info[0]); if (TD_SUCCESS != ret) { SAMPLE_PRT("SS_MPI_VI_ReleasePipeFrame failed with %#x\n", ret); goto EXIT5; } }
EXIT5: stDumpAttr.bEnable = TD_FALSE; st Dump Attr.u32Depth = 0; SS_MPI_VI_SetPipeDumpAttr(ViRawOutPipe, &st Dump Attr); return NULL;
}` **Related Topics** [ss\_mpi\_isp\_init](#ss_mpi_isp_init) ### ss\_mpi\_isp\_exit [Description] Exit the ISP firmware. **Syntax** `td_s32 ss_mpi_isp_exit(ot_vi_pipe vi_pipe);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - After calling [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190) and [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164), call This interface to exit the ISP firmware.
- Not supported for multi-process. Must be called in the same process as sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), and [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164).
- Repeated calls to This interface are supported.
- In stitching mode, the main pipe must be exited first, followed by other pipes.
<a name="ZH-CN_TOPIC_0000001220218983"></a>- Not supported for multi-threaded ISP creation and destruction on the same vi\_pipe (multi-threaded simultaneous calls to sensor\_register\_callback, ss\_mpi\_ae\_register, ss\_mpi\_awb\_register, [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000001220218983))
- It is recommended to call This interface after [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190). **Example** None **Related Topics** [ss\_mpi\_isp\_init](#ss_mpi_isp_init) ### ss\_mpi\_isp\_set\_pub\_attr [Description] Set the ISP public attributes. **Syntax** `td_s32 ss_mpi_isp_set_pub_attr(ot_vi_pipe vi_pipe, const ot_isp_pub_attr *pub_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| pub\_attr | ISP public attributes. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - The image attributes correspond to the capture attributes of the corresponding sensor.
- When ISP starts, ensure that [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920) has been called to initialize the ISP external registers.
- ISP supports dynamic cropping of the image start position during operation.
<a name="ZH-CN_TOPIC_0000001220057509"></a>- Processing flow inside ISP after calling This interface: - The ISP firmware checks whether the image WDR mode, resolution, and frame rate have changed. If none have changed, it returns directly. Otherwise, the ISP firmware calls cmos\_set\_wdr\_mode and cmos\_set\_image\_mode functions in sensor cmos.c to change the sensor mode. - If the sensor mode does not change (return value -2), it checks whether the ISP crop width and height have changed. If so, the ISP firmware switches resolution and calls the sensor\_init function to reconfigure the sensor. - If the sensor mode changes (return value 0), the ISP firmware calls the sensor\_init function to reconfigure the sensor. - The ISP firmware passes the frame rate information to the AE library and decides whether to change the frame rate. - When using This interface for dynamic resolution and frame rate switching, if the sensor mode changes, follow the switching procedure provided in the sample (stop the VI device first, then create the VI device, then set [ss\_mpi\_isp\_set\_pub\_attr](#ZH-CN_TOPIC_0000001220057509) to switch). The current system does not support frame rate switching in VI parallel mode. Additionally, when switching resolution and frame rate dynamically, at least one of the resolution or frame rate must be different (i.e., cannot switch to itself); otherwise, the sensor may not re-initialize, causing anomalies. Mode switching also cannot switch to itself. For cases where the ISP input has the same resolution and frame rate but requires different initialization sequences, different sns\_mode values can be used for mode switching.
- When using the ISP cropping function, note: Dynamic cropping of image width and height will re-initialize the sensor. Follow the switching procedure provided in the sample (stop the VI device first, then create the VI device, then set [ss\_mpi\_isp\_set\_pub\_attr](#ZH-CN_TOPIC_0000001220057509) to switch). The ISP cropping function is not supported in online WDR mode. When the input is YUV, cropping does not take effect. - Users can modify the cmos\_set\_image\_mode function in sensor cmos.c to adjust the sensor mode switching order. For example, if a sensor only provides 5M30fps and 1080P60fps initialization sequences, to run 1080P30fps, it can be obtained by cropping from 5M30fps or by reducing the frame rate from 1080P60fps by modifying the cmos\_set\_image\_mode function.
- When configuring a frame rate that exceeds the sensor's frame rate range through the [ss\_mpi\_isp\_set\_pub\_attr](#ZH-CN_TOPIC_0000001220057509) interface, the frame rate value can be configured into the ISP, but sensor\_cmos.c detects that the value is out of range and does not perform the frame rate change. If the application layer then performs mode switching (e.g., linear mode to WDR mode), the sensor re-initializes and reads the frame rate from the ISP. Since the ISP stores the out-of-range frame rate configured in the previous mode, the sensor fails to reconfigure the frame rate, causing frame rate anomalies and abnormal images in the switched mode. Therefore, when using This interface to configure the frame rate, do not configure values that exceed the sensor's frame rate range.
- Cases where This interface is not supported: switching from WDR to linear mode in different working modes, or switching resolution or frame rate in different working modes (e.g., not supported to switch from OT\_VI\_ONLINE\_VPSS\_OFFLINE WDR mode to OT\_VI\_PARALLEL\_VPSS\_OFFLINE linear mode).
- When switching between linear mode and frame WDR mode, the return value of cmos\_set\_image\_mode is also checked. Therefore, linear mode and frame WDR mode should use different image\_mode values to ensure successful switching.
- When switching between linear mode and WDR mode in online mode, the BNR temporal filter is turned off (no manual user intervention required). After mode switching, a delay of 4 frames is needed before the temporal filter takes effect again; otherwise, image anomalies may occur. Users can pre-configure the temporal filter state within the 4-frame delay after mode switching. Without pre-configuration, the temporal filter state before mode switching will be reinstated after the delay. **Example** None **Related Topics** [ss\_mpi\_isp\_get\_pub\_attr](#ss_mpi_isp_get_pub_attr) ### ss\_mpi\_isp\_get\_pub\_attr [Description] Get the ISP public attributes. **Syntax** `td_s32 ss_mpi_isp_get_pub_attr(ot_vi_pipe vi_pipe, ot_isp_pub_attr *pub_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| pub\_attr | ISP public attributes. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_pub\_attr](#ss_mpi_isp_set_pub_attr) ### ss\_mpi\_isp\_set\_fmw\_state [Description] Set the ISP firmware state. **Syntax** `td_s32 ss_mpi_isp_set_fmw_state(ot_vi_pipe vi_pipe, const ot_isp_fmw_state state);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| state | ISP firmware state. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** When the state value is OT\_ISP\_FMW\_STATE\_FREEZE, the ISP firmware's 3A algorithm, Sharpen algorithm, DRC algorithm, Crosstalk removal algorithm, NR algorithm, dehazing algorithm, demosaicing algorithm, black level algorithm, FPN removal algorithm, ACM algorithm, WDR algorithm, etc. will be frozen. The sensor registers will also stop being configured and will retain the values before freezing. When the state value is OT\_ISP\_FMW\_STATE\_RUN, the ISP firmware operates normally. **Example** None **Related Topics** [ss\_mpi\_isp\_get\_fmw\_state](#ss_mpi_isp_get_fmw_state) ### ss\_mpi\_isp\_get\_fmw\_state [Description] Get the ISP firmware state. **Syntax** `td_s32 ss_mpi_isp_get_fmw_state(ot_vi_pipe vi_pipe, ot_isp_fmw_state *state);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| state | ISP firmware state. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_fmw\_state](#ss_mpi_isp_set_fmw_state) ### ss\_mpi\_isp\_set\_sns\_slave\_attr [Description] Set the slave-mode sensor H/V sync signal. **Syntax** `td_s32 ss_mpi_isp_set_sns_slave_attr (ot_slave_dev slave_dev, const ot_isp_slave_sns_sync *sns_sync);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| slave\_dev | Slave Device number. | Input |
| sns\_sync | Sync signal configuration. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - A slave-mode sensor requires H-sync (XHS) and V-sync (XVS) signals for exposure and data readout control. This interface primarily configures the sync signal generator to output the H/V timing required by the sensor. It is generally called from within the sensor library.
- Supports setting different timing configurations for slave-mode sensors. The current sensor timing configuration is set in xxx\_cmos.c/xxx\_sensor\_ctl.c.
- There are two binding relationships for slave signals: first, a binding between pipe and vsync; second, within vsync, different signal source slaves can be selected. Different pipes can select different slave signal devices (vsync), and different slave signal devices can select different signal sources (slave).
- In stitch mode, if two channels are stitched together, it is best to use the same slave signal device. For more than two channels, different sensors must connect to different slave signal devices; in this case, all slave signal devices should use the same signal source to ensure synchronization across sensors.
- If multiple slave sensors operate independently without stitch mode, each sensor must connect to a different slave signal device, and each slave signal device must select a different signal source. **Example** 4-channel slave sensor stitch mode example: pipe I Ds are 0/2/4/6, bound to slave signal vsync0, vsync0, vsync1, vsync1 respectively. Since this is stitch mode, they must all select the same slave signal source (assumed to be slave0). The driver assignment is as follows: `td_s32 g_SlaveBindDev[ISP_MAX_PIPE_NUM] = {0, x, 0, x, 1, x, 1, x};
td_u32 g_SlaveSensorModeTime[ISP_MAX_PIPE_NUM] = {0, x, 0, x, 0, x, 0, x};` 4-channel slave sensor non-stitch mode example: pipe I Ds are 0/2/4/6, bound to vsync0, vsync1, vsync2, vsync3 respectively. Since this is non-stitch mode, they must select different signal sources: slave0, slave1, slave2, slave3. The driver assignment is as follows: `td_s32 g_SlaveBindDev[ISP_MAX_PIPE_NUM] = {0, x, 1, x, 2, x, 3, x};
td_u32 g_SlaveSensorModeTime[ISP_MAX_PIPE_NUM] = {0, x, 1, x, 2, x, 3, x};` Here x represents any value satisfying the interface requirements; it can be ignored. **Related Topics** [ss\_mpi\_isp\_get\_sns\_slave\_attr](#ss_mpi_isp_get_sns_slave_attr) ### ss\_mpi\_isp\_get\_sns\_slave\_attr [Description] Get the slave-mode sensor H/V sync signal. **Syntax** `td_s32 ss_mpi_isp_get_sns_slave_attr(ot_slave_dev slave_dev, ot_isp_slave_sns_sync *sns_sync);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| slave\_dev | Slave Device number. | Input |
| sns\_sync | Sync signal configuration. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_sns\_slave\_attr](#ss_mpi_isp_set_sns_slave_attr) ### ss\_mpi\_isp\_set\_module\_ctrl [Description] Set the ISP function module control. **Syntax** `td_s32 ss_mpi_isp_set_module_ctrl(ot_vi_pipe vi_pipe, const ot_isp_module_ctrl *mod_ctrl);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| mod\_ctrl | Module control value.Each bit controls the enabling of a function module in the ISP. 0: Enable this module; 1: Disable this module. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - This interface can control the enabling of each ISP function module.
- The register corresponding to This interface is shared with the enable registers of each module. **Example** None **Related Topics** [ss\_mpi\_isp\_get\_module\_ctrl](#ss_mpi_isp_get_module_ctrl) ### ss\_mpi\_isp\_get\_module\_ctrl [Description] Get the IS Pfunction module control. **Syntax** `td_s32 ss_mpi_isp_get_module_ctrl(ot_vi_pipe vi_pipe, ot_isp_module_ctrl *mod_ctrl);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| mod\_ctrl | Module control value. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_module\_ctrl](#ss_mpi_isp_set_module_ctrl) ### ss\_mpi\_isp\_get\_vd\_time\_out [Description] Get ISP interrupt information. **Syntax** `td_s32 ss_mpi_isp_get_vd_time_out(ot_vi_pipe vi_pipe, ot_isp_vd_type isp_vd_type, td_u32 milli_sec);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| isp\_vd\_type | Frame sync signal type. | Input |
| milli\_sec | Timeout, unit: ms | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - This interface indicates getting information related to ISP interrupt generation, including whether an interrupt occurred, the current ISP frame information at the time of the interrupt, and that the interrupt uses the frame start interrupt.
- The milli\_sec parameter is in milliseconds and refers to the timeout. If the ISP interrupt cannot be obtained within milli\_sec milliseconds, the function returns. When milli\_sec is set to 0, it means blocking mode, where the program waits until the ISP interrupt is obtained before returning.
- Using the [OT\_ISP\_VD\_FE\_END](#OT_ISP_VD_FE_END) method to get ISP interrupt information and read statistics. In extreme cases (high CPU usage, etc.), reading statistics may not be timely. It is recommended to use the [OT\_ISP\_VD\_FE\_START](#OT_ISP_VD_FE_START) method to get ISP interrupts and read statistics.
- When N processes simultaneously call This interface to get the same isp\_vd\_type, each process receives 1/N of the actual interrupt information. For example, in RAW feeding scenarios, [OT\_ISP\_VD\_FE\_START](#OT_ISP_VD_FE_START) is used to send raw data. If other processes also use [OT\_ISP\_VD\_FE\_START](#OT_ISP_VD_FE_START) to run services, the frame rate of the RAW feeding service will be halved. **Example** None **Related Topics** None ### ss\_mpi\_isp\_sensor\_reg\_callback [Description] ISP-provided callback interface for sensor registration. **Syntax** `td_s32 ss_mpi_isp_sensor_reg_callback(ot_vi_pipe vi_pipe, ot_isp_sns_attr_info *sns_attr_info , ot_isp_sensor_register *sns_register);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| sns\_attr\_info | Attributes of the sensor registered with the ISP. | Input |
| sns\_register | Sensor registrationstructure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - sensor\_id is a user-defined value within the sensor library, primarily used to verify that the sensor registered with the ISP and the sensor registered with 3A are the same sensor.
- The ISP acquires differentiated initialization parameters and controls the sensor through a series of callback interfaces registered by the sensor.
- This interfacedoes not support multi-process operation. **Figure 1** Interface between ISP library and sensor library **Example** `ot_vi_pipe vi_pipe = 0;
td_s32 ret;
ot_isp_sensor_register isp_register;
ot_isp_sns_attr_info sns_attr_info;
ot_isp_sensor_exp_func * sensor_exp_func = &isp_register.sns_exp;
(ot_void)memset_s(sensor_exp_func, sizeof(ot_isp_sensor_exp_func), 0, sizeof(ot_isp_sensor_exp_func)); sensor_exp_func->pfn_cmos_sensor_init = sensor_init;
sensor_exp_func->pfn_cmos_sensor_exit = sensor_exit;
sensor_exp_func->pfn_cmos_sensor_global_init = sensor_global_init;
sensor_exp_func->pfn_cmos_set_image_mode = cmos_set_image_mode;
sensor_exp_func->pfn_cmos_set_wdr_mode = cmos_set_wdr_mode;
sensor_exp_func->pfn_cmos_get_isp_default = cmos_get_isp_default;
sensor_exp_func->pfn_cmos_get_isp_black_level = cmos_get_isp_black_level;
sensor_exp_func->pfn_cmos_set_pixel_detect = cmos_set_pixel_detect;
sensor_exp_func->pfn_cmos_get_sns_reg_info = cmos_get_sns_regs_info; sns_attr_info.sensor_id= SENSOR_NAME_ID;
ret = ss_mpi_isp_sensor_reg_callback(vi_pipe, &sensor_id, &isp_register);
if (ret) {
printf("sensor register callback function failed!\n");
return ret;
}` **Related Topics** [ss\_mpi\_isp\_sensor\_unreg\_callback](#ss_mpi_isp_sensor_unreg_callback) ### ss\_mpi\_isp\_sensor\_unreg\_callback [Description] ISP-provided callback interface for sensor unregistration. **Syntax** `td_s32 ss_mpi_isp_sensor_unreg_callback(ot_vi_pipe vi_pipe, ot_sensor_id sensor_id);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| sensor\_id | ID of the sensor registered with the ISP. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - sensor\_id is a custom value in the sensor library, mainly used to verify whether the sensor being unregistered from ISP and the sensor being unregistered from 3A are the same sensor.
- This interface does not support multi-process operation. **Example** `ot_vi_pipe vi_pipe = 0; ret = ss_mpi_isp_sensor_unreg_callback(vi_pipe, SENSOR_NAME_ID); if (ret) { printf("sensor unregister callback function failed!\n"); return ret; }` **Related Topics** [ss\_mpi\_isp\_sensor\_reg\_callback](#ss_mpi_isp_sensor_reg_callback) ### ss\_mpi\_isp\_ae\_lib\_reg\_callback [Description] ISP callback interface for AE library registration. **Syntax** `td_s32 ss_mpi_isp_ae_lib_reg_callback(ot_vi_pipe vi_pipe, const ot_isp_3a_alg_lib *ae_lib, const ot_isp_ae_register *ae_register);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_lib | AE librarystructure pointer. | Input |
| ae\_register | AE libraryregistration structure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - The ISP provides a unified AE algorithm library interface for initializing, running, controlling, and destroying the AE library. When using the SDK's AE algorithm library, this interface does not need to be called. When using a custom AE algorithm library, this interface must be used to register callback functions.
- This interfacedoes not support multi-process operation.
- A maximum of 2 AE libraries can be registered. **Figure 1** Interface between ISP library and AE library **Example** `ot_isp_ae_register ae_register;
td_s32 ret = TD_SUCCESS;
ae_register.ae_exp_func.pfn_ae_init = ae_init;
ae_register.ae_exp_func.pfn_ae_run = ae_run;
ae_register.ae_exp_func.pfn_ae_ctrl = ae_ctrl;
ae_register.ae_exp_func.pfn_ae_exit = ae_exit;
ret = ss_mpi_isp_ae_lib_reg_callback(vi_pipe, ae_lib, &ae_register);
if (TD_SUCCESS != ret) {
printf("Ot_ae register failed!\n");
}` **Related Topics** [ss\_mpi\_isp\_ae\_lib\_unreg\_callback](#ss_mpi_isp_ae_lib_unreg_callback) ### ss\_mpi\_isp\_ae\_lib\_unreg\_callback [Description] ISP callback interface for AE library unregistration. **Syntax** `td_s32 ss_mpi_isp_ae_lib_unreg_callback(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *ae_lib);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_lib | AE librarystructure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - When using the SDK's AE algorithm library, you do not need to pay attention to this interface；When using your own AE algorithm library, you need to call this interface tounregister the callback function from the ISP.
- This interfacedoes not support multi-process operation. **Example** `td_s32 ret = TD_SUCCESS;
ret = ss_mpi_isp_ae_lib_unreg_callback(vi_pipe, ae_lib);
if (TD_SUCCESS != ret) {
printf("Ot_ae unregister failed!\n");
}
return ret;` **Related Topics** [ss\_mpi\_isp\_ae\_lib\_reg\_callback](#ss_mpi_isp_ae_lib_reg_callback) ### ss\_mpi\_isp\_awb\_lib\_reg\_callback [Description] ISP callback interface for AWB library registration. **Syntax** `td_s32 ss_mpi_isp_awb_lib_reg_callback(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *awb_lib, ot_isp_awb_register *awb_register);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| awb\_lib | AWB library structure pointer. | Input |
| awb\_register | AWB library registration structure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - ISP provides a unified AWB algorithm library interface for initializing, running, controlling, and destroying the AWB algorithm library. When using the SDK's AWB algorithm library, you do not need to pay attention to this interface. When using your own AWB algorithm library, you need to call this interface to register the callback function with the ISP.
- This interface does not support multi-process operation.
- Supports a maximum of 2 AWB library registrations. **Figure 1** Interface between ISP library and AWB library **Example** None **Related Topics** [ss\_mpi\_isp\_awb\_lib\_unreg\_callback](#ss_mpi_isp_awb_lib_unreg_callback) ### ss\_mpi\_isp\_awb\_lib\_unreg\_callback [Description] ISP callback interface for AWB library unregistration. **Syntax** `td_s32 ss_mpi_isp_awb_lib_unreg_callback(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *awb_lib);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| awb\_lib | AWB library structure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** - When using the SDK-provided AWB algorithm library, this interface does not need to be called. When using a custom AWB algorithm library, this interface must be used to unregister the callback function from the ISP.
- This interfacedoes not support multi-process operation. **Related Topics** [ss\_mpi\_isp\_awb\_lib\_reg\_callback](#ss_mpi_isp_awb_lib_reg_callback) ### ss\_mpi\_isp\_set\_bind\_attr [Description] Set the binding relationship between the ISP library, 3A library, and sensor. **Syntax** `td_s32 ss_mpi_isp_set_bind_attr(ot_vi_pipe vi_pipe, const ot_isp_bind_attr *bind_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| bind\_attr | Binding structure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - This interface is not mandatory. It is only needed when registering multiple AE/AWB libraries and wanting to switch between algorithm libraries. When multiple AE/AWB libraries are registered, the default binding is the last registered AE library and AWB library.
- This interface does not support multi-process operation. **Example** None **Related Topics** [ss\_mpi\_isp\_get\_bind\_attr](#ss_mpi_isp_get_bind_attr) ### ss\_mpi\_isp\_get\_bind\_attr [Description] Get the binding relationship between the ISP library, 3A library, and sensor. **Syntax** `td_s32 ss_mpi_isp_get_bind_attr(ot_vi_pipe vi_pipe, ot_isp_bind_attr *bind_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| bind\_attr | Binding structure pointer. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** This interfacedoes not support multi-process operation. **Example** None **Related Topics** [ss\_mpi\_isp\_set\_bind\_attr](#ss_mpi_isp_set_bind_attr) ### ss\_mpi\_isp\_set\_dcf\_info [Description] Set DCF parameters. **Syntax** `td_s32 ss_mpi_isp_set_dcf_info(ot_vi_pipe vi_pipe, const ot_isp_dcf_info *isp_dcf);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| isp\_dcf | DCF parameter structure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** Before calling this interface, ss\_mpi\_vb\_set\_supplement\_cfg must be called (see the “System Control” section of the MPP Media Processing Software V5.0 Developer Reference) with supplement\_cfg set to OT\_VB\_SUPPLEMENT\_JPEG\_MASK. **Example** `ot_vb_supplement_cfg supplement_conf = {0}; supplement_conf.supplement_cfg = OT_VB_SUPPLEMENT_JPEG_MASK;
ret=ss_mpi_vb_set_supplement_cfg(&supplement_conf); if(ret != TD_SUCCESS) { printf("ss_mpi_vb_set_supplement_conf err 0x%x\n",ret);
} ...... ret=ss_mpi_vb_init; if(ret != TD_SUCCESS) { printf("ss_mpi_vb_init err 0x%x\n",ret);
} ...... ot_vi_pipe vi_pipe;
ret=ss_mpi_isp_init(vi_pipe); ...... ot_isp_dcf_info isp_dcf;
/will:119 105 108 108
isp_dcf.isp_dcf_const_info.image_description[0]=119;
isp_dcf.isp_dcf_const_info.image_description[1]=105;
isp_dcf.isp_dcf_const_info.image_description[2]=108;
isp_dcf.isp_dcf_const_info.image_description[3]=108;
isp_dcf.isp_dcf_const_info.image_description[4]=0;
/otsi: 104 105 115 105
isp_dcf.isp_dcf_const_info.make[0]=104;
isp_dcf.isp_dcf_const_info.make[1]=105;
isp_dcf.isp_dcf_const_info.make[2]=115;
isp_dcf.isp_dcf_const_info.make[3]=105;
isp_dcf.isp_dcf_const_info.make[4]=0;
/funy：102 117 110 121
isp_dcf.isp_dcf_const_info.model[0]=102;
isp_dcf.isp_dcf_const_info.model[1]=117;
isp_dcf.isp_dcf_const_info.model[2]=110;
isp_dcf.isp_dcf_const_info.model[3]=121;
isp_dcf.isp_dcf_const_info.model[4]=0;
/v.1.1.0: 118 46 49 46 49 46 48
isp_dcf.isp_dcf_const_info.software[0] = 118;
isp_dcf.isp_dcf_const_info.software[1] = 46;
isp_dcf.isp_dcf_const_info.software[2] = 49;
isp_dcf.isp_dcf_const_info.software[3] = 46;
isp_dcf.isp_dcf_const_info.software[4] = 49;
isp_dcf.isp_dcf_const_info.software[5] = 46;
isp_dcf.isp_dcf_const_info.software[6] = 48;
isp_dcf.isp_dcf_const_info.software[7] = 0; isp_dcf.isp_dcf_update_info.iso_speed_ratings = 500;
isp_dcf.isp_dcf_update_info.exposure_bias_value = 5;
isp_dcf.isp_dcf_update_info.exposure_time = 0x00010004;
isp_dcf.isp_dcf_update_info.f_number = 0x0001000f;
isp_dcf.isp_dcf_const_info.focal_length = 0x00640001;
isp_dcf.isp_dcf_update_info.max_aperture_value = 0x00010001;
isp_dcf.isp_dcf_const_info.contrast =5;
isp_dcf.isp_dcf_const_info.custom_rendered = 0;
isp_dcf.isp_dcf_update_info.exposure_mode = 0;
isp_dcf.isp_dcf_const_info.focal_length_in35mm_film = 0;
isp_dcf.isp_dcf_const_info.gain_control = 1;
isp_dcf.isp_dcf_const_info.light_source = 1;
isp_dcf.isp_dcf_const_info.metering_mode = 1;
isp_dcf.isp_dcf_const_info.saturation = 1;
isp_dcf.isp_dcf_const_info.scene_capture_type = 1;
isp_dcf.isp_dcf_const_info.scene_type = 0;
isp_dcf.isp_dcf_const_info.sharpness =5;
isp_dcf.isp_dcf_update_info.white_balance = 0;
ss_mpi_isp_set_dcf_info(vi_pipe,&isp_dcf);` **Related Topics** [ss\_mpi\_isp\_get\_dcf\_info](#ss_mpi_isp_get_dcf_info) ### ss\_mpi\_isp\_get\_dcf\_info [Description] Get DCF parameters. **Syntax** `td_s32 ss_mpi_isp_get_dcf_info(ot_vi_pipe vi_pipe, ot_isp_dcf_info *isp_dcf)` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| isp\_dcf | DCF parameter structure pointer. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_dcf\_info](#ss_mpi_isp_set_dcf_info) ### ss\_mpi\_isp\_set\_pipe\_differ\_attr [Description] Set multi-pipe ISP differential attributes. **Syntax** `td_s32 ss_mpi_isp_set_pipe_differ_attr(ot_vi_pipe vi_pipe, const ot_isp_pipe_diff_attr *pipe_differ);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| pipe\_differ | Multi-pipe ISP differential attribute structure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** This interface is not mandatory. It is used in multi-channel ISP stitching mode. When higher stitching quality is required, calibration tools (PQ\_Stitching\_Tool) can be used to calibrate the brightness, color, and other differences of multi-channel ISP outputs. Configuring through this interface reduces the differences between multi-channel ISP output images. This interface must be called after [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190). **Example** None **Related Topics** [ss\_mpi\_isp\_get\_pipe\_differ\_attr](#ss_mpi_isp_get_pipe_differ_attr) ### ss\_mpi\_isp\_get\_pipe\_differ\_attr [Description] Get multi-pipe ISP differential attributes. **Syntax** `td_s32 ss_mpi_isp_get_pipe_differ_attr(ot_vi_pipe vi_pipe, ot_isp_pipe_diff_attr *pipe_differ);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| pipe\_differ | Multi-pipe ISP differential attribute structure pointer. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** This interface is not mandatory. It is used in conjunction with [ss\_mpi\_isp\_set\_pipe\_differ\_attr](#ZH-CN_TOPIC_0000002504084755) to obtain the multi-channel ISP difference parameters for the corresponding configuration. **Example** None **Related Topics** [ss\_mpi\_isp\_set\_pipe\_differ\_attr](#ss_mpi_isp_set_pipe_differ_attr) ### ss\_mpi\_isp\_set\_ctrl\_param [Description] Set the IS Pcontrol parameters。 **Syntax** `td_s32 ss_mpi_isp_set_ctrl_param(ot_vi_pipe vi_pipe, const ot_isp_ctrl_param *isp_ctrl_param);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number | Input |
| isp\_ctrl\_param | IS Pcontrol parametersstructure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
<a name="ZH-CN_TOPIC_0000002503964837"></a>- Library: libss\_isp.a、libot\_isp.a **Note** For interface usage restrictions, see[ot\_isp\_ctrl\_param](#ZH-CN_TOPIC_0000002503964837)Precautions in。 **Example** None **Related Topics** [ss\_mpi\_isp\_get\_ctrl\_param](#ss_mpi_isp_get_ctrl_param) ### ss\_mpi\_isp\_get\_ctrl\_param [Description] Get the IS Pcontrol parameters。 **Syntax** `td_s32 ss_mpi_isp_get_ctrl_param(ot_vi_pipe vi_pipe, ot_isp_ctrl_param *isp_ctrl_param);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number | Input |
| isp\_ctrl\_param | IS Pcontrol parametersstructure pointer. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_ctrl\_param](#ss_mpi_isp_set_ctrl_param) ### ss\_mpi\_isp\_set\_mod\_param [Description] Set the IS Pmodule parameter。 **Syntax** `td_s32 ss_mpi_isp_set_mod_param(const ot_isp_mod_param *mod_param);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| mod\_param | IS Pmodule parameterstructure pointer. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
<a name="ZH-CN_TOPIC_0000002470925030"></a>- Library: libss\_isp.a、libot\_isp.a **Note** For interface usage restrictions, see[ot\_isp\_mod\_param](#ZH-CN_TOPIC_0000002470925030)Precautions in。 **Example** None **Related Topics** [ss\_mpi\_isp\_get\_mod\_param](#ss_mpi_isp_get_mod_param) ### ss\_mpi\_isp\_get\_mod\_param [Description] Get the IS Pmodule parameter。 **Syntax** `td_s32 ss_mpi_isp_get_mod_param(ot_isp_mod_param *mod_param);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| mod\_param | IS Pmodule parameterstructure pointer. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_mod\_param](#ss_mpi_isp_set_mod_param) ### ss\_mpi\_isp\_set\_smart\_info [Description] Set ISP module smart information. **Syntax** `td_s32 ss_mpi_isp_set_smart_info(ot_vi_pipe vi_pipe, const ot_isp_smart_info *smart_info);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| smart\_info | Smart information, including face and human form information. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
<a name="ZH-CN_TOPIC_0000002503964975"></a>- Library: libss\_isp.a、libot\_isp.a **Note** For interface usage, see[ot\_isp\_smart\_info](#ZH-CN_TOPIC_0000002503964975)description. **Example** None **Related Topics** [ss\_mpi\_isp\_get\_smart\_info](#ss_mpi_isp_get_smart_info) ### ss\_mpi\_isp\_get\_smart\_info [Description] Get ISP module smart information. **Syntax** `td_s32 ss_mpi_isp_get_smart_info(ot_vi_pipe vi_pipe, ot_isp_smart_info *smart_info);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| smart\_info | Smart information, including face and human form information. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_smart\_info](#ss_mpi_isp_set_smart_info) ### ss\_mpi\_isp\_get\_lightbox\_gain [Description] Get the gain structure from AWB online calibration. **Syntax** `td_s32 ss_mpi_isp_get_lightbox_gain(ot_vi_pipe vi_pipe, ot_isp_awb_calibration_gain *awb_calibration_gain);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| awb\_calibration\_gain | Gain structure output from AWB online calibration. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** The AWB online calibration interface is primarily intended to support consumer customers in correcting AWB parameters during mass production of camcorders on the production line. This interface is only valid under a uniform background with uniform illumination and a color temperature range of 4500K to 6500K. **Example** None **Related Topics** None ### ss\_mpi\_isp\_ir\_auto\_run\_once [Description] Run the IR auto-switching function. **Syntax** `td_s32 ss_mpi_isp_ir_auto_run_once(ot_vi_pipe vi_pipe, ot_isp_ir_auto_attr *ir_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ir\_attr | IR auto-switching attributes. | Input/Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a、libot\_ir\_auto.a **Note** When using this interface, libot\_ir\_auto.a must be included. This feature is not supported on Hi3403V100. **Example** None **Related Topics** None ### ss\_mpi\_isp\_set\_be\_frame\_attr [Description] Set BE frame attributes. **Syntax** `td_s32 ss_mpi_isp_set_be_frame_attr(ot_vi_pipe vi_pipe, const ot_isp_be_frame_attr *be_frame_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| be\_frame\_attr | BE frame attributes. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** When this interface is configured to capture RAW data after WDR synthesis, all ISP BE modules after the WDR module are bypassed. The VI channel attributes must also be configured to write RAW from the VI channel (which will interrupt the video stream). Refer to the pseudocode in the example. For ss\_mpi\_vi\_set\_chn\_attr/ss\_mpi\_vi\_get\_chn\_frame/ss\_mpi\_vi\_release\_chn\_frame, see the “Video Input 2” chapter of the MPP Media Processing Software V5.0 Developer Reference. **Example** `ot_pixel_format ori_pix_format;
ot_compress_mode ori_compress_mode;
ot_vi_chn_attr chn_attr;
ot_isp_be_frame_attr be_frame_attr; /* Set vi chn_attr to output 16-bit raw data */
ss_mpi_vi_get_chn_attr(vi_pipe, vi_chn, &chn_attr); ori_pix_format = chn_attr.pixel_format;
ori_compress_mode = chn_attr.compress_mode;
chn_attr.compress_mode = OT_COMPRESS_MODE_NONE;
chn_attr.pixel_format = OT_PIXEL_FORMAT_RGB_BAYER_16BPP;
ss_mpi_vi_set_chn_attr(vi_pipe, vi_chn, &chn_attr); /* Set dump frame position */
be_frame_attr.frame_pos = OT_ISP_DUMP_FRAME_POS_AFTER_WDR;
ss_mpi_isp_set_be_frame_attr(vi_pipe, &be_frame_attr); /* dump frame */
td_s32 milli_sec = 5000;
ot_video_frame_info frame_info;
ss_mpi_vi_get_chn_frame(vi_pipe, vi_chn, &frame_info, milli_sec); /* save frame data */
……
/* release dump frame */
ss_mpi_vi_release_chn_frame(vi_pipe, vi_chn, &frame_info); /* Restore normal output state after dump completes */
chn_attr.compress_mode = ori_compress_mode;
chn_attr.pixel_format = ori_pix_format;
ss_mpi_vi_set_chn_attr(vi_pipe, vi_chn, &chn_attr);
be_frame_attr.frame_pos = OT_ISP_DUMP_FRAME_POS_NORMAL;
ss_mpi_isp_set_be_frame_attr(vi_pipe, &be_frame_attr);` **Related Topics** [ss\_mpi\_isp\_get\_be\_frame\_attr](#ss_mpi_isp_get_be_frame_attr) ### ss\_mpi\_isp\_get\_be\_frame\_attr [Description] Get BE frame attributes. **Syntax** `td_s32 ss_mpi_isp_get_be_frame_attr(ot_vi_pipe vi_pipe, ot_isp_be_frame_attr *be_frame_attr);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| be\_frame\_attr | BE frame attributes. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** [ss\_mpi\_isp\_set\_be\_frame\_attr](#ss_mpi_isp_set_be_frame_attr) ### ss\_mpi\_isp\_get\_noise\_calibration [Description] Get noise model calibration parameters. **Syntax** `td_s32 ss_mpi_isp_get_noise_calibration(ot_vi_pipe vi_pipe, ot_isp_noise_calibration *noise_calibration);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| noise\_calibration | Noise model calibration parameters. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** None ### ss\_mpi\_isp\_set\_frame\_info [Description] Set ISP real-time information. **Syntax** `td_s32 ss_mpi_isp_set_frame_info(ot_vi_pipe vi_pipe, const ot_isp_frame_info *isp_frame);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| isp\_frame | ISP real-time information. For details on ot\_isp\_frame\_info, see the “System Control” chapter of the MPP Media Processing Software Developer Reference. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** None ### ss\_mpi\_isp\_get\_frame\_info [Description] Get ISP real-time information. **Syntax** `td_s32 ss_mpi_isp_get_frame_info(ot_vi_pipe vi_pipe, ot_isp_frame_info *isp_frame);` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| isp\_frame | ISP real-time information. For details on ot\_isp\_frame\_info, see the “System Control” chapter of the MPP Media Processing Software Developer Reference. | Output |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** None **Example** None **Related Topics** None ### ss\_mpi\_isp\_mem\_share [Description] Share ISP-related MMZ buffers with a specific process ID. **Syntax** `td_s32 ss_mpi_isp_mem_share(ot_vi_pipe vi_pipe, td_s32 pid)` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| pid | Process ID to share with. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Only the process that allocated the MMZ buffer can register sharing; other processes attempting to register sharing will receive a failure return.
- The process that allocated the MMZ buffer does not need to be shared with itself; if the pid parameter is the allocating process ID, the interface returns failure.
- If the MMZ buffer is already in a globally shared state (shared with all processes), the interface returns failure.
- Each MMZ buffer can be shared with a maximum of 5 process I Ds (including the allocating process ID).
- Repeatedly sharing with the same process ID returns success.
- If the MMZ module parameter mem\_process\_isolation is set to 0, this interface returns success but has no effect.
- Must be called after [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190). Other non-allocating processes must call this before invoking related interfaces; otherwise, mmap will fail. Any interface that reads or writes ISP kernel-allocated MMZ buffers requires sharing, including external register access, statistics reading, DCF info retrieval, and debug interfaces.
- The ss\_mpi\_isp\_set\_debug interface also requires mutual sharing before debug information can be written to the MMZ buffer allocated by the respective process. Example: process B calls ss\_mpi\_isp\_set\_debug to provide its allocated MMZ for the ISP master process A to write debug information: 1. ISP master process A calls [ss\_mpi\_isp\_mem\_share](#ZH-CN_TOPIC_0000002504084749)/[ss\_mpi\_isp\_mem\_share\_all](#ZH-CN_TOPIC_0000002470924996) to allow the ISP master process to write debug information to process B; 2. Process B calls ss\_mpi\_sys\_mem\_share/ss\_mpi\_sys\_mem\_share\_all to grant ISP master process A access to the debug MMZ allocated by process B; 3. Process B calls ss\_mpi\_isp\_set\_debug to pass the debug MMZ information to ISP master process A. **Example** None **Related Topics** None ### ss\_mpi\_isp\_mem\_unshare [Description] Revoke ISP-related MMZ buffer sharing from a process ID. **Syntax** `td_s32 ss_mpi_isp_mem_unshare(ot_vi_pipe vi_pipe, td_s32 pid)` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| pid | Process ID to revoke sharing from. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - The process that allocated the MMZ buffer can revoke sharing with any non-allocating process ID.
- A shared process can only revoke sharing for its own process ID.
- If the MMZ buffer is already in a globally shared state (shared with all processes), the interface returns failure.
- Repeatedly revoking sharing from the same process ID returns failure.
- Must be used in conjunction with the [ss\_mpi\_isp\_mem\_share](#ZH-CN_TOPIC_0000002504084749) interface.
- If the MMZ module parameter mem\_process\_isolation is set to 0, this interface returns success but has no effect. **Example** None **Related Topics** None ### ss\_mpi\_isp\_mem\_share\_all [Description] Share ISP-related MMZ buffers with all processes without process ID restriction. **Syntax** `td_s32 ss_mpi_isp_mem_share_all(ot_vi_pipe vi_pipe)` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Only the process that allocated the mmz buffer can register sharing. Other processes registering sharing will return failure.
- Repeated sharing with all processes, the interface returns Success.
- If the MMZ module parameter mem\_process\_isolation is set to 0, this interface will not take effect even if it returns success.
- Must be called after [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), and other non-allocating processes must call it before calling related interfaces. Otherwise, non-allocating processes will fail mmap when calling related interfaces. Any interface that involves reading or writing the ISP kernel-mode allocated mmz buffer needs to be shared, such as accessing external registers, reading statistics, getting dcf info, and debug interfaces.
- Access to the ss\_mpi\_isp\_set\_debug interface also requires sharing, and mutual sharing is needed. Only after sharing can debug information be written to the mmz buffer allocated by the corresponding process. For example, process B calls ss\_mpi\_isp\_set\_debug to provide its allocated MMZ to ISP main process A for writing debug information: 1. ISP main process A calls [ss\_mpi\_isp\_mem\_share](#ZH-CN_TOPIC_0000002504084749)/[ss\_mpi\_isp\_mem\_share\_all](#ZH-CN_TOPIC_0000002470924996) to allow ISP main process A to write debug information to process B. 2. Process B calls ss\_mpi\_sys\_mem\_share/ss\_mpi\_sys\_mem\_share\_all to grant ISP main process A access to process B's allocated debug mmz. 3. Process B calls ss\_mpi\_isp\_set\_debug to pass the debug mmz information to ISP main process A. **Example** None **Related Topics** None ### ss\_mpi\_isp\_mem\_unshare\_all [Description] Revoke ISP-related MMZ buffer sharing from all processes. **Syntax** `td_s32 ss_mpi_isp_mem_unshare_all(ot_vi_pipe vi_pipe)` **Parameters**

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |

**Return Value**

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-zero | On failure, the value is Error Code。 |

**Requirements** - Header: ot\_common\_isp.h、ss\_mpi\_isp.h
- Library: libss\_isp.a、libot\_isp.a **Note** - Only the process that allocated the mmz buffer can cancel sharing with all processes.
- Repeatedly canceling sharing with all processes, the interface returns Success.
- Used in conjunction with the [ss\_mpi\_isp\_mem\_share\_all](#ZH-CN_TOPIC_0000002470924996) interface.
- After calling this interface to cancel the shared state with all processes, the original shared state with individual process I Ds is retained.
<a name="ZH-CN_TOPIC_0000002470925096"></a>- If the MMZ module parameter mem\_process\_isolation is set to 0, this interface will not take effect even if it returns success. **Example** None **Related Topics** None ## Data Types Unless a valid range is explicitly specified for a variable in this document, the default is the valid range of the corresponding data type. For example, the valid range of a td\_u8 variable is [0, 255]. Unless a data precision is explicitly specified, the default precision is 1. - [OT\_ISP\_BAYER\_CHN\_NUM](#ZH-CN_TOPIC_0000002470925096): Defines the number of Bayer data channels.
- [OT\_ISP\_MAX\_PIPE\_NUM](#ZH-CN_TOPIC_0000002503965125): Defines the maximum number of ISP-supported pipes.
- [OT\_ISP\_WDR\_MAX\_FRAME\_NUM](#ZH-CN_TOPIC_0000002471084934): Defines the maximum number of frames for WDR synthesis.
- [OT\_ISP\_EXP\_RATIO\_NUM](#ZH-CN_TOPIC_0000002471085142): Defines the number of WDR exposure ratios.
- [OT\_ISP\_AUTO\_ISO\_NUM](#ZH-CN_TOPIC_0000002504084769): Defines the number of ISO stops.
- [OT\_ISP\_STRIPING\_MAX\_NUM](#ZH-CN_TOPIC_0000002471084874): Defines the maximum number of ISP BE offline strips.
- [OT\_ISP\_MAX\_STITCH\_NUM](#ZH-CN_TOPIC_0000002471085118): Defines the maximum number of ISP stitch groups.
- [ALG\_LIB\_NAME\_SIZE\_MAX](#ZH-CN_TOPIC_0000002503965005): Defines the maximum number of characters for the 3A algorithm library name.
- [OT\_ISP\_MAX\_SNS\_REGS](#ZH-CN_TOPIC_0000002470925146): Defines the maximum number of registers that must be configured when writing exposure results to the sensor.
- [OT\_ISP\_PEOPLE\_CLASS\_MAX](#ZH-CN_TOPIC_0000002504084879): Defines the maximum number of human body and face detection types.
- [OT\_ISP\_TUNNEL\_CLASS\_MAX](#ZH-CN_TOPIC_0000002470924904): Defines the maximum number of tunnel detection types.
- [OT\_ISP\_AE\_ZONE\_ROW](#ZH-CN_TOPIC_0000002504084767): Number of AE zones in the horizontal direction.
- [OT\_ISP\_AE\_ZONE\_COLUMN](#ZH-CN_TOPIC_0000002503964985): Number of AE zones in the vertical direction.
- [OT\_ISP\_MG\_ZONE\_ROW](#ZH-CN_TOPIC_0000002470925212): Number of MG zones in the horizontal direction.
- [OT\_ISP\_MG\_ZONE\_COLUMN](#ZH-CN_TOPIC_0000002503965087): Number of MG zones in the vertical direction.
- [OT\_ISP\_AE\_ROUTE\_MAX\_NODES](#ZH-CN_TOPIC_0000002504084699): Maximum number of AE ROUTE nodes.
- [OT\_ISP\_AE\_ROUTE\_EX\_MAX\_NODES](#ZH-CN_TOPIC_0000002471085072): Maximum number of extended AE ROUTE nodes.
- [OT\_ISP\_BAYER\_CALIBTAION\_MAX\_NUM](#ZH-CN_TOPIC_0000002504084815): Defines the maximum number of ISO stops for noise model calibration parameters.
- [OT\_BAYER\_CALIBRATION\_PARA\_NUM\_NEW](#ZH-CN_TOPIC_0000002471084890): Defines the maximum number of noise model calibration parameters.
- [OT\_ISP\_CCM\_MATRIX\_SIZE](#ZH-CN_TOPIC_0000002470924922): Number of CCM matrix parameters.
- [OT\_DCF\_DRSCRIPTION\_LENGTH](#ZH-CN_TOPIC_0000002503965029): Defines the depth of DCF description information.
- [ISP\_SNS\_SAVE\_INFO\_MAX](#ZH-CN_TOPIC_0000002503964809): Defines the maximum number of frames for recording sensor info.
- [OT\_ISP\_LSC\_GRID\_COL](#ZH-CN_TOPIC_0000002471084870): Number of points required for Mesh Shading partition in the x direction.
- [OT\_ISP\_LSC\_GRID\_ROW](#ZH-CN_TOPIC_0000002504085075): Number of points required for Mesh Shading partition in the y direction.
- [OT\_ISP\_LSC\_GRID\_POINTS](#ZH-CN_TOPIC_0000002504084759): Number of gain points in the Mesh Shading LUT table.
- [OT\_ISP\_ACS\_LIGHT\_NUM](#ZH-CN_TOPIC_0000002504084891): Number of light sources for ACS partitioning.
- [OT\_ISP\_ACS\_CHN\_NUM](#ZH-CN_TOPIC_0000002504084885): R and B channel components calibrated by ACS.
- [OT\_ISP\_PRO\_MAX\_FRAME\_NUM](#ZH-CN_TOPIC_0000002503964967): Maximum number of frames supported in photo pro mode.
- [ot\_rect](#ZH-CN_TOPIC_0000002470925086): Defines the starting position and dimensions of the crop window.
<a name="ZH-CN_TOPIC_0000002470924882"></a>- [ot\_point](#ZH-CN_TOPIC_0000002470924882): Defines coordinate information.
<a name="ZH-CN_TOPIC_0000002503964903"></a>- [ot\_isp\_bayer\_format](#ZH-CN_TOPIC_0000002503964903): Defines the input Bayer image data format.
<a name="ZH-CN_TOPIC_0000002503964885"></a>- [ot\_mipi\_crop\_attr](#ZH-CN_TOPIC_0000002503964885): MIPI crop parameters.
<a name="ZH-CN_TOPIC_0000002470925010"></a>- [ot\_isp\_bayer\_raw\_bit](#ZH-CN_TOPIC_0000002470925010): Defines the input Bayer image data bit width.
<a name="ZH-CN_TOPIC_0000002504084877"></a>- [ot\_size](#ZH-CN_TOPIC_0000002504084877): Defines the width and height of sensor output.
<a name="ZH-CN_TOPIC_0000002504084785"></a>- [ot\_color\_gamut](#ZH-CN_TOPIC_0000002504084785): Defines channel color gamut attributes.
<a name="ZH-CN_TOPIC_0000002471085026"></a>- [ot\_isp\_pub\_attr](#ZH-CN_TOPIC_0000002471085026): Defines ISP public attributes.
<a name="ZH-CN_TOPIC_0000002471084900"></a>- [ot\_op\_mode](#ZH-CN_TOPIC_0000002471084900): Defines the module operating state.
<a name="ZH-CN_TOPIC_0000002471084930"></a>- [ot\_isp\_fmw\_state](#ZH-CN_TOPIC_0000002471084930): Defines ISP firmware state.
<a name="ZH-CN_TOPIC_0000002471085028"></a>- [ot\_isp\_slave\_sns\_sync](#ZH-CN_TOPIC_0000002471085028): Defines slave-mode sensor sync signal configuration.
<a name="ZH-CN_TOPIC_0000002504085073"></a>- [ot\_isp\_wdr\_mode](#ZH-CN_TOPIC_0000002504085073): Defines ISP wide dynamic range mode.
<a name="ZH-CN_TOPIC_0000002504084745"></a>- [ot\_wdr\_mode](#ZH-CN_TOPIC_0000002504084745): Defines wide dynamic range mode.
<a name="ZH-CN_TOPIC_0000002504085031"></a>- [ot\_isp\_module\_ctrl](#ZH-CN_TOPIC_0000002504085031): Defines ISP function module control.
<a name="ZH-CN_TOPIC_0000002504084887"></a>- [ot\_isp\_dump\_frame\_pos](#ZH-CN_TOPIC_0000002504084887): Defines the position information for dumping BE frames.
<a name="ZH-CN_TOPIC_0000002504085027"></a>- [ot\_isp\_be\_frame\_attr](#ZH-CN_TOPIC_0000002504085027): Defines BE frame configuration information.
- [ot\_isp\_vd\_type](#ZH-CN_TOPIC_0000002470925008): Defines the frame sync signal type.
<a name="ZH-CN_TOPIC_0000002504084741"></a>- [ot\_isp\_sns\_attr\_info](#ZH-CN_TOPIC_0000002504084741): Defines sensor attributes.
<a name="ZH-CN_TOPIC_0000002504084795"></a>- [ot\_isp\_sensor\_register](#ZH-CN_TOPIC_0000002504084795): Defines the sensor registration structure.
<a name="ZH-CN_TOPIC_0000002503964953"></a>- [ot\_isp\_sensor\_exp\_func](#ZH-CN_TOPIC_0000002503964953): Defines the sensor callback function structure.
<a name="ZH-CN_TOPIC_0000002503965049"></a>- [ot\_isp\_cmos\_sensor\_image\_mode](#ZH-CN_TOPIC_0000002503965049): Defines sensor output width, height, and frame rate attributes.
<a name="ZH-CN_TOPIC_0000002504084813"></a>- [ot\_isp\_cmos\_lsc](#ZH-CN_TOPIC_0000002504084813): Defines LSC parameters.
<a name="ZH-CN_TOPIC_0000002503964887"></a>- [ot\_isp\_acs\_y\_shading\_lut](#ZH-CN_TOPIC_0000002503964887): Defines the correction intensity table for the luminance component of Auto Color Shading.
<a name="ZH-CN_TOPIC_0000002504084969"></a>- [ot\_isp\_acs\_color\_shading\_lut](#ZH-CN_TOPIC_0000002504084969): Defines the LUT table for the color component of Auto Color Shading.
<a name="ZH-CN_TOPIC_0000002471085078"></a>- [ot\_isp\_acs\_calib\_param](#ZH-CN_TOPIC_0000002471085078): Defines the calibration parameters for Auto Color Shading, generated by the calibration tool.
<a name="ZH-CN_TOPIC_0000002471085168"></a>- [ot\_isp\_cmos\_acs](#ZH-CN_TOPIC_0000002471085168): Defines the CMOS parameters for Auto Color Shading.
<a name="ZH-CN_TOPIC_0000002471085224"></a>- [ot\_isp\_noise\_calibration](#ZH-CN_TOPIC_0000002471085224): Defines NOISE correction parameters.
<a name="ZH-CN_TOPIC_0000002470924998"></a>- [ot\_isp\_cmos\_sensor\_max\_resolution](#ZH-CN_TOPIC_0000002470924998): Defines the sensor maximum resolution structure.
<a name="ZH-CN_TOPIC_0000002470924898"></a>- [ot\_isp\_cmos\_clut](#ZH-CN_TOPIC_0000002470924898): Defines the CLUT structure.
<a name="ZH-CN_TOPIC_0000002471085226"></a>- [ot\_isp\_cmos\_sensor\_mode](#ZH-CN_TOPIC_0000002471085226): Defines sensor mode registers.
<a name="ZH-CN_TOPIC_0000002503964927"></a>- [ot\_isp\_cmos\_dng\_color\_param](#ZH-CN_TOPIC_0000002503964927): Defines DNG white balance correction coefficients.
<a name="ZH-CN_TOPIC_0000002471084926"></a>- [ot\_isp\_cmos\_wdr\_switch\_attr](#ZH-CN_TOPIC_0000002471084926): Defines WDR switch attributes.
<a name="ZH-CN_TOPIC_0000002471084994"></a>- [ot\_isp\_cmos\_alg\_key](#ZH-CN_TOPIC_0000002471084994): Defines flag bits indicating whether each ISP algorithm uses the default CMOS configuration.
<a name="ZH-CN_TOPIC_0000002503964879"></a>- [ot\_isp\_cmos\_default](#ZH-CN_TOPIC_0000002503964879): Defines the initialization parameter structure for the ISP base algorithm library.
<a name="ZH-CN_TOPIC_0000002471085128"></a>- [ot\_isp\_sensor\_total\_size\_attr](#ZH-CN_TOPIC_0000002471085128): Defines the actual width and height of sensor output data.
<a name="ZH-CN_TOPIC_0000002503965035"></a>- [ot\_isp\_cmos\_black\_level](#ZH-CN_TOPIC_0000002503965035): Defines the sensor black level structure.
<a name="ZH-CN_TOPIC_0000002471085112"></a>- [ot\_isp\_sns\_regs\_info](#ZH-CN_TOPIC_0000002471085112): Defines sensor register information.
<a name="ZH-CN_TOPIC_0000002503965039"></a>- [ot\_isp\_3a\_alg\_lib](#ZH-CN_TOPIC_0000002503965039): Defines the AE/AWB algorithm library structure.
<a name="ZH-CN_TOPIC_0000002503965055"></a>- [ot\_isp\_bind\_attr](#ZH-CN_TOPIC_0000002503965055): Defines the structure for the binding relationship between the ISP library, sensor, and 3A library.
<a name="ZH-CN_TOPIC_0000002503964981"></a>- [ot\_isp\_ctrl\_proc\_write](#ZH-CN_TOPIC_0000002503964981): Defines ISP PROC information.
<a name="ZH-CN_TOPIC_0000002470924852"></a>- [ot\_isp\_ctrl\_cmd](#ZH-CN_TOPIC_0000002470924852): Defines ISP control commands for 3A.
<a name="ZH-CN_TOPIC_0000002503964881"></a>- [ot\_isp\_stitch\_attr](#ZH-CN_TOPIC_0000002503964881): Defines the ISP stitch structure.
<a name="ZH-CN_TOPIC_0000002471085212"></a>- [ot\_isp\_ae\_register](#ZH-CN_TOPIC_0000002471085212): Defines the AE registration structure.
<a name="ZH-CN_TOPIC_0000002503964939"></a>- [ot\_isp\_ae\_exp\_func](#ZH-CN_TOPIC_0000002503964939): Defines the AE callback function structure.
<a name="ZH-CN_TOPIC_0000002471085106"></a>- [ot\_isp\_ae\_param](#ZH-CN_TOPIC_0000002471085106): Defines the initialization parameter structure provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002470924960"></a>- [ot\_isp\_people\_roi](#ZH-CN_TOPIC_0000002470924960): Defines the human body and face statistics structure provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002471084876"></a>- [ot\_isp\_tunnel\_roi](#ZH-CN_TOPIC_0000002471084876): Defines the tunnel statistics structure provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002503965171"></a>- [ot\_isp\_face\_roi](#ZH-CN_TOPIC_0000002503965171): Defines the face fast-convergence algorithm structure provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002503965021"></a>- [ot\_isp\_people\_type](#ZH-CN_TOPIC_0000002503965021): Defines the human body and face statistics enumeration type provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002471084928"></a>- [ot\_isp\_tunnel\_type](#ZH-CN_TOPIC_0000002471084928): Defines the tunnel statistics enumeration type provided by the ISP to the AE library.
- [ot\_isp\_smart\_info](#ZH-CN_TOPIC_0000002503964975): Defines the human body and face statistics structure provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002471084964"></a>- [ot\_isp\_fe\_ae\_stat\_1](#ZH-CN_TOPIC_0000002471084964): Defines AE statistics attributes in ISP FE.
<a name="ZH-CN_TOPIC_0000002470925108"></a>- [ot\_isp\_be\_ae\_stat\_1](#ZH-CN_TOPIC_0000002470925108): Defines AE statistics attributes in ISP BE.
<a name="ZH-CN_TOPIC_0000002470925126"></a>- [ot\_isp\_ae\_info](#ZH-CN_TOPIC_0000002470925126): Defines the statistics structure provided by the ISP to the AE library.
<a name="ZH-CN_TOPIC_0000002504084881"></a>- [ot\_isp\_ae\_stat\_attr](#ZH-CN_TOPIC_0000002504084881): Defines the configuration register structure returned by the AE library to the ISP.
<a name="ZH-CN_TOPIC_0000002503965167"></a>- [ot\_isp\_ae\_result](#ZH-CN_TOPIC_0000002503965167): Defines the configuration register structure returned by the AE library to the ISP.
<a name="ZH-CN_TOPIC_0000002470924932"></a>- [ot\_isp\_awb\_register](#ZH-CN_TOPIC_0000002470924932): Defines the AWB registration structure.
<a name="ZH-CN_TOPIC_0000002471084978"></a>- [ot\_isp\_awb\_exp\_func](#ZH-CN_TOPIC_0000002471084978): Defines the AWB callback function structure.
<a name="ZH-CN_TOPIC_0000002503965117"></a>- [ot\_isp\_awb\_param](#ZH-CN_TOPIC_0000002503965117): Defines the initialization parameter structure provided by the ISP to the AWB library.
<a name="ZH-CN_TOPIC_0000002470924906"></a>- [ot\_isp\_awb\_stat\_1](#ZH-CN_TOPIC_0000002470924906): Defines the AWB statistics structure.
<a name="ZH-CN_TOPIC_0000002503965071"></a>- [ot\_isp\_awb\_stat\_result](#ZH-CN_TOPIC_0000002503965071): Defines the AWB statistics structure.
<a name="ZH-CN_TOPIC_0000002471084884"></a>- [ot\_isp\_awb\_info](#ZH-CN_TOPIC_0000002471084884): Defines the statistics structure provided by the ISP to the AWB library.
<a name="ZH-CN_TOPIC_0000002503965033"></a>- [ot\_isp\_awb\_raw\_stat\_attr](#ZH-CN_TOPIC_0000002503965033): Defines the AWB Bayer-domain statistics structure.
<a name="ZH-CN_TOPIC_0000002503964823"></a>- [ot\_isp\_awb\_result](#ZH-CN_TOPIC_0000002503964823): Defines the configuration register structure returned by the AWB library to the ISP.
<a name="ZH-CN_TOPIC_0000002504084773"></a>- [ot\_isp\_awb\_calibration\_gain](#ZH-CN_TOPIC_0000002504084773): Defines the gain structure output from AWB online calibration.
<a name="ZH-CN_TOPIC_0000002470925020"></a>- [ot\_isp\_dcf\_const\_info](#ZH-CN_TOPIC_0000002470925020): Defines user-configurable parameters in DCF information.
<a name="ZH-CN_TOPIC_0000002503964901"></a>- [ot\_isp\_dcf\_update\_info](#ZH-CN_TOPIC_0000002503964901): Defines ISP real-time update parameters in DCF information.
<a name="ZH-CN_TOPIC_0000002471085014"></a>- [ot\_isp\_dcf\_info](#ZH-CN_TOPIC_0000002471085014): Defines the DCF information parameter structure.
<a name="ZH-CN_TOPIC_0000002470925038"></a>- [ot\_isp\_pipe\_diff\_mode](#ZH-CN_TOPIC_0000002470925038): Defines the pipe diff mode.
<a name="ZH-CN_TOPIC_0000002470925120"></a>- [ot\_isp\_pipe\_diff\_param](#ZH-CN_TOPIC_0000002470925120): Defines the dual-pipe ISP differential parameter structure.
<a name="ZH-CN_TOPIC_0000002504085003"></a>- [ot\_isp\_pipe\_diff\_attr](#ZH-CN_TOPIC_0000002504085003): Defines the dual-pipe ISP differential attribute structure.
<a name="ZH-CN_TOPIC_0000002470924884"></a>- [ot\_isp\_ob\_stats\_update\_pos](#ZH-CN_TOPIC_0000002470924884): Defines the position for reading OB region statistics.
<a name="ZH-CN_TOPIC_0000002503964913"></a>- [ot\_isp\_alg\_run\_select](#ZH-CN_TOPIC_0000002503964913): Defines whether to mask algorithm modules in ISP BE.
<a name="ZH-CN_TOPIC_0000002503965109"></a>- [ot\_isp\_run\_wakeup\_select](#ZH-CN_TOPIC_0000002503965109): Defines the interrupt type that wakes up the ISP.
- [ot\_isp\_ctrl\_param](#ZH-CN_TOPIC_0000002503964837): Defines the ISP control parameters structure.
- [ot\_isp\_mod\_param](#ZH-CN_TOPIC_0000002470925030): Defines the ISP module parameter structure.
<a name="ZH-CN_TOPIC_0000002504084951"></a>- [ot\_isp\_init\_attr](#ZH-CN_TOPIC_0000002504084951): Defines the AE/AWB initialization parameter structure for ISP first startup.
<a name="ZH-CN_TOPIC_0000002503964807"></a>- [ot\_isp\_sns\_mirrorflip\_type](#ZH-CN_TOPIC_0000002503964807): Defines the sensor mirror-flip enumeration.
<a name="ZH-CN_TOPIC_0000002504084893"></a>- [ot\_isp\_sns\_blc\_clamp](#ZH-CN_TOPIC_0000002504084893): Defines the sensor black level correction enable switch.
<a name="ZH-CN_TOPIC_0000002504085065"></a>- [ot\_isp\_sns\_bus\_ex](#ZH-CN_TOPIC_0000002504085065): Defines the extended structure for sensor communication protocols.
<a name="ZH-CN_TOPIC_0000002471085122"></a>- [ot\_isp\_sns\_obj](#ZH-CN_TOPIC_0000002471085122): Defines the object pointing to the sensor.
<a name="ZH-CN_TOPIC_0000002470925066"></a>- [ot\_isp\_sns\_state](#ZH-CN_TOPIC_0000002470925066): Defines the global variable parameter structure for sensor-related data.
<a name="ZH-CN_TOPIC_0000002471084970"></a><a name="ZH-CN_TOPIC_0000002503964999"></a>- [ot\_isp\_awb\_alg](#ZH-CN_TOPIC_0000002471084970): Defines the AWB algorithm type. The following data types are for features not yet supported: - [ot\_isp\_ir\_status](#ZH-CN_TOPIC_0000002503964999): Defines the current IR state of the device.
<a name="ZH-CN_TOPIC_0000002471085082"></a>- [ot\_isp\_ir\_switch\_status](#ZH-CN_TOPIC_0000002471085082): Defines the IR switch state of the device.
<a name="ZH-CN_TOPIC_0000002470924864"></a>- [ot\_isp\_ir\_auto\_attr](#ZH-CN_TOPIC_0000002470924864): Defines the IR auto-switching attributes. ### OT\_ISP\_BAYER\_CHN\_NUM **Description** Defines the number of Bayer data channels. **Definition** ```

# define OT\_ISP\_BAYER\_CHN\_NUM 4[¶](#define-ot_isp_bayer_chn_num-4 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - [ot\_isp\_awb\_info](#ot_isp_awb_info)
- [ot\_isp\_awb\_result](#ot_isp_awb_result)
- ot\_isp\_awb\_sensor\_default
- [ot\_isp\_pipe\_diff\_attr](#ot_isp_pipe_diff_attr)
- ot\_isp\_nr\_snr\_auto\_attr
- ot\_isp\_nr\_snr\_manual\_attr
- ot\_isp\_black\_level\_manual\_attr
- ot\_isp\_inner\_state\_info
- ot\_isp\_ae\_stats
- ot\_isp\_ae\_stitch\_stats
- ot\_isp\_mg\_stats
- ot\_isp\_awb\_attr
- ot\_isp\_dng\_raw\_format
- [ot\_isp\_sns\_state](#ot_isp_sns_state) ### OT\_ISP\_MAX\_PIPE\_NUM<a name="ZH-CN_TOPIC_0000002503965125"></a> **Description** Defines the maximum number of ISP-supported pipes. **Definition**`

# define OT\_ISP\_MAX\_PHY\_PIPE\_NUM 4[¶](#define-ot_isp_max_phy_pipe_num-4 "锚链接")

# define OT\_ISP\_MAX\_VIR\_PIPE\_NUM 8[¶](#define-ot_isp_max_vir_pipe_num-8 "锚链接")

# define OT\_ISP\_MAX\_PIPE\_NUM (OT\_ISP\_MAX\_PHY\_PIPE\_NUM + OT\_ISP\_MAX\_VIR\_PIPE\_NUM)[¶](#define-ot_isp_max_pipe_num-ot_isp_max_phy_pipe_num-ot_isp_max_vir_pipe_num "锚链接")

`**Precautions** None **Related Data Types and Interfaces** ot\_isp\_ae\_stitch\_stats ### OT\_ISP\_WDR\_MAX\_FRAME\_NUM<a name="ZH-CN_TOPIC_0000002471084934"></a> **Description** Defines the maximum number of frames for WDR synthesis. **Definition**`

# define OT\_ISP\_WDR\_MAX\_FRAME\_NUM 4[¶](#define-ot_isp_wdr_max_frame_num-4 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - [ot\_isp\_ae\_result](#ot_isp_ae_result)
- ot\_isp\_ae\_sensor\_default
- ot\_isp\_fusion\_attr
- ot\_isp\_nr\_wdr\_attr
- ot\_isp\_black\_level\_manual\_attr
- ot\_isp\_inner\_state\_info
- ot\_isp\_ae\_stats
- ot\_isp\_ae\_stitch\_stats
- ot\_isp\_fe\_focus\_stats
- [ot\_isp\_sns\_state](#ot_isp_sns_state) ### OT\_ISP\_EXP\_RATIO\_NUM<a name="ZH-CN_TOPIC_0000002471085142"></a> **Description** Defines the number of WDR exposure ratios. **Definition**`

# define OT\_ISP\_EXP\_RATIO\_NUM 3[¶](#define-ot_isp_exp_ratio_num-3 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_ae\_sensor\_default
- ot\_isp\_wdr\_exposure\_attr
- [ot\_isp\_cmos\_wdr\_switch\_attr](#ot_isp_cmos_wdr_switch_attr) ### OT\_ISP\_AUTO\_ISO\_NUM<a name="ZH-CN_TOPIC_0000002504084769"></a> **Description** Defines the number of ISO stops. **Definition**`

# define OT\_ISP\_AUTO\_ISO\_NUM 16[¶](#define-ot_isp_auto_iso_num-16 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_fswdr\_auto\_attr
- ot\_isp\_ldci\_auto\_attr
- ot\_isp\_ca\_lut
- ot\_isp\_dp\_dynamic\_auto\_attr
- ot\_isp\_nr\_snr\_auto\_attr
- ot\_isp\_nr\_tnr\_auto\_attr
- ot\_isp\_sharpen\_auto\_attr
- ot\_isp\_cr\_attr
- ot\_isp\_anti\_false\_color\_auto\_attr
- ot\_isp\_demosaic\_auto\_attr
- ot\_isp\_acac\_auto\_attr
- ot\_isp\_bayershp\_auto\_attr
- ot\_isp\_awb\_cbcr\_track\_attr
- ot\_isp\_saturation\_auto ### OT\_ISP\_STRIPING\_MAX\_NUM<a name="ZH-CN_TOPIC_0000002471084874"></a> **Description** Defines the maximum number of ISP BE offline strips. **Definition**`

# define OT\_ISP\_STRIPING\_MAX\_NUM 3[¶](#define-ot_isp_striping_max_num-3 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_fpn\_frame\_info
- ot\_isp\_dp\_static\_calibrate
- ot\_isp\_dp\_static\_attr ### OT\_ISP\_MAX\_STITCH\_NUM<a name="ZH-CN_TOPIC_0000002471085118"></a> **Description** Defines the maximum number of ISP stitch groups. **Definition**`

# define OT\_ISP\_MAX\_STITCH\_NUM 4[¶](#define-ot_isp_max_stitch_num-4 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** ot\_isp\_wb\_stitch\_stats ### ALG\_LIB\_NAME\_SIZE\_MAX<a name="ZH-CN_TOPIC_0000002503965005"></a> **Description** Defines the maximum number of characters for the 3A algorithm library name. **Definition**`

# define ALG\_LIB\_NAME\_SIZE\_MAX 20[¶](#define-alg_lib_name_size_max-20 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_3a\_alg\_lib](#ot_isp_3a_alg_lib) ### OT\_ISP\_MAX\_SNS\_REGS<a name="ZH-CN_TOPIC_0000002470925146"></a> **Description** Defines the maximum number of registers that must be configured when writing exposure results to the sensor. **Definition**`

# define OT\_ISP\_MAX\_SNS\_REGS 32[¶](#define-ot_isp_max_sns_regs-32 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_sns\_regs\_info](#ot_isp_sns_regs_info) ### OT\_ISP\_PEOPLE\_CLASS\_MAX<a name="ZH-CN_TOPIC_0000002504084879"></a> **Description** Defines the maximum number of human body and face detection types. **Definition**`

# define OT\_ISP\_PEOPLE\_CLASS\_MAX 2[¶](#define-ot_isp_people_class_max-2 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_smart\_info](#ot_isp_smart_info) ### OT\_ISP\_TUNNEL\_CLASS\_MAX<a name="ZH-CN_TOPIC_0000002470924904"></a> **Description** Defines the maximum number of tunnel detection types. **Definition**`

# define OT\_ISP\_TUNNEL\_CLASS\_MAX 2[¶](#define-ot_isp_tunnel_class_max-2 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_smart\_info](#ot_isp_smart_info) ### OT\_ISP\_AE\_ZONE\_ROW<a name="ZH-CN_TOPIC_0000002504084767"></a> **Description** Number of AE zones in the horizontal direction. **Definition**`

# define OT\_ISP\_AE\_ZONE\_ROW 15[¶](#define-ot_isp_ae_zone_row-15 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - [ot\_isp\_ae\_stat\_attr](#ot_isp_ae_stat_attr)
- ot\_isp\_ae\_stats\_cfg
- ot\_isp\_ae\_grid\_info
- ot\_isp\_ae\_stats
- ot\_isp\_ae\_stitch\_stats ### OT\_ISP\_AE\_ZONE\_COLUMN<a name="ZH-CN_TOPIC_0000002503964985"></a> **Description** Number of AE zones in the vertical direction. **Definition**`

# define OT\_ISP\_AE\_ZONE\_COLUMN 17[¶](#define-ot_isp_ae_zone_column-17 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - [ot\_isp\_ae\_stat\_attr](#ot_isp_ae_stat_attr)
- ot\_isp\_ae\_stats\_cfg
- ot\_isp\_ae\_grid\_info
- ot\_isp\_ae\_stats
- ot\_isp\_ae\_stitch\_stats ### OT\_ISP\_MG\_ZONE\_ROW<a name="ZH-CN_TOPIC_0000002470925212"></a> **Description** Number of MG zones in the horizontal direction. **Definition**`

# define OT\_ISP\_MG\_ZONE\_ROW 15[¶](#define-ot_isp_mg_zone_row-15 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_mg\_grid\_info
- ot\_isp\_mg\_stats ### OT\_ISP\_MG\_ZONE\_COLUMN<a name="ZH-CN_TOPIC_0000002503965087"></a> **Description** Number of MG zones in the vertical direction. **Definition**`

# define OT\_ISP\_MG\_ZONE\_COLUMN 17[¶](#define-ot_isp_mg_zone_column-17 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_mg\_grid\_info
- ot\_isp\_mg\_stats ### OT\_ISP\_AE\_ROUTE\_MAX\_NODES<a name="ZH-CN_TOPIC_0000002504084699"></a> **Description** Maximum number of AE ROUTE nodes. **Definition**`

# define OT\_ISP\_AE\_ROUTE\_MAX\_NODES 16[¶](#define-ot_isp_ae_route_max_nodes-16 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** ot\_isp\_ae\_route ### OT\_ISP\_AE\_ROUTE\_EX\_MAX\_NODES<a name="ZH-CN_TOPIC_0000002471085072"></a> **Description** Maximum number of extended AE ROUTE nodes. **Definition**`

# define OT\_ISP\_AE\_ROUTE\_EX\_MAX\_NODES 16[¶](#define-ot_isp_ae_route_ex_max_nodes-16 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** ot\_isp\_ae\_route\_ex ### OT\_ISP\_BAYER\_CALIBTAION\_MAX\_NUM<a name="ZH-CN_TOPIC_0000002504084815"></a> **Description** Defines the maximum number of ISO stops for noise model calibration parameters. **Definition**`

# define OT\_ISP\_BAYER\_CALIBTAION\_MAX\_NUM 50[¶](#define-ot_isp_bayer_calibtaion_max_num-50 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_noise\_calibration](#ot_isp_noise_calibration) ### OT\_BAYER\_CALIBRATION\_PARA\_NUM\_NEW<a name="ZH-CN_TOPIC_0000002471084890"></a> **Description** Defines the maximum number of noise model calibration parameters. **Definition**`

# define OT\_BAYER\_CALIBRATION\_PARA\_NUM\_NEW 16[¶](#define-ot_bayer_calibration_para_num_new-16 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_noise\_calibration](#ot_isp_noise_calibration) ### OT\_ISP\_CCM\_MATRIX\_SIZE<a name="ZH-CN_TOPIC_0000002470924922"></a> **Description** Number of CCM matrix parameters. **Definition**`

# define OT\_ISP\_CCM\_MATRIX\_SIZE 9[¶](#define-ot_isp_ccm_matrix_size-9 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - [ot\_isp\_awb\_result](#ot_isp_awb_result)
- ot\_isp\_awb\_ccm\_tab
- ot\_isp\_awb\_sensor\_default
- [ot\_isp\_pipe\_diff\_attr](#ot_isp_pipe_diff_attr)
- ot\_isp\_color\_matrix\_manual
- ot\_isp\_color\_matrix\_param
- ot\_isp\_wb\_info
- [ot\_isp\_init\_attr](#ot_isp_init_attr)
- ot\_isp\_dng\_image\_static\_info ### OT\_DCF\_DRSCRIPTION\_LENGTH<a name="ZH-CN_TOPIC_0000002503965029"></a> **Description** Defines the depth of DCF description information. **Definition**`

# define OT\_DCF\_DRSCRIPTION\_LENGTH 32[¶](#define-ot_dcf_drscription_length-32 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_dcf\_const\_info](#ot_isp_dcf_const_info) ### ISP\_SNS\_SAVE\_INFO\_MAX<a name="ZH-CN_TOPIC_0000002503964809"></a> **Description** Defines the maximum number of frames for recording sensor info. **Definition**`

# define ISP\_SNS\_SAVE\_INFO\_MAX 2[¶](#define-isp_sns_save_info_max-2 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_sns\_state](#ot_isp_sns_state) ### OT\_ISP\_LSC\_GRID\_COL<a name="ZH-CN_TOPIC_0000002471084870"></a> **Description** Number of points required for Mesh Shading partition in the x direction. **Definition**`

# define OT\_ISP\_LSC\_GRID\_COL 33[¶](#define-ot_isp_lsc_grid_col-33 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_shading\_gain\_lut
- [ot\_isp\_acs\_y\_shading\_lut](#ot_isp_acs_y_shading_lut)
- [ot\_isp\_acs\_color\_shading\_lut](#ot_isp_acs_color_shading_lut) ### OT\_ISP\_LSC\_GRID\_ROW<a name="ZH-CN_TOPIC_0000002504085075"></a> **Description** Number of points required for Mesh Shading partition in the y direction. **Definition**`

# define OT\_ISP\_LSC\_GRID\_ROW 33[¶](#define-ot_isp_lsc_grid_row-33 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_shading\_gain\_lut
- [ot\_isp\_acs\_y\_shading\_lut](#ot_isp_acs_y_shading_lut)
- [ot\_isp\_acs\_color\_shading\_lut](#ot_isp_acs_color_shading_lut) ### OT\_ISP\_LSC\_GRID\_POINTS<a name="ZH-CN_TOPIC_0000002504084759"></a> **Description** Number of gain points in the Mesh Shading LUT table. **Definition**`

# define OT\_ISP\_LSC\_GRID\_POINTS (OT\_ISP\_LSC\_GRID\_COL \* OT\_ISP\_LSC\_GRID\_ROW)[¶](#define-ot_isp_lsc_grid_points-ot_isp_lsc_grid_col-ot_isp_lsc_grid_row "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** - ot\_isp\_shading\_gain\_lut
- [ot\_isp\_acs\_y\_shading\_lut](#ot_isp_acs_y_shading_lut)
- [ot\_isp\_acs\_color\_shading\_lut](#ot_isp_acs_color_shading_lut) ### OT\_ISP\_ACS\_LIGHT\_NUM<a name="ZH-CN_TOPIC_0000002504084891"></a> **Description** Number of light sources for ACS partitioning. **Definition**`

# define OT\_ISP\_ACS\_LIGHT\_NUM 32[¶](#define-ot_isp_acs_light_num-32 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_acs\_calib\_param](#ot_isp_acs_calib_param) ### OT\_ISP\_ACS\_CHN\_NUM<a name="ZH-CN_TOPIC_0000002504084885"></a> **Description** R and B channel components calibrated by ACS. **Definition**`

# define OT\_ISP\_ACS\_CHN\_NUM 2[¶](#define-ot_isp_acs_chn_num-2 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_acs\_calib\_param](#ot_isp_acs_calib_param) ### OT\_ISP\_PRO\_MAX\_FRAME\_NUM<a name="ZH-CN_TOPIC_0000002503964967"></a> **Description** Defines the maximum number of frames supported in photo pro mode. **Definition**`

# define OT\_ISP\_PRO\_MAX\_FRAME\_NUM 8[¶](#define-ot_isp_pro_max_frame_num-8 "锚链接")

`**Precautions** None. **Related Data Types and Interfaces** ss\_mpi\_snap\_set\_pipe\_attr ### ot\_rect<a name="ZH-CN_TOPIC_0000002470925086"></a> **Description** Defines the starting position and dimensions of the crop window. **Definition**`
typedef struct { td\_s32 x; td\_s32 y; td\_u32 width; td\_u32 height;
} ot\_rect;
``` **Members**

| Member Name | Description |
| --- | --- |
| x | Horizontal start position. Valid range: [0, 8072] |
| width | Image width, 4-byte aligned. Must be 4-aligned when using the shading feature, otherwise shading will not work correctly. Valid range: [120, 8192] |
| height | Image height, 4-byte aligned. Must be 4-aligned when using the shading feature, otherwise shading will not work correctly. Valid range: [120, 8192] |

**Precautions** - The sum of the horizontal start position and image width must be less than the sensor output image width.
- The sum of the vertical start position and image height must be less than the sensor output image height. Since the actual sensor output dimensions cannot be detected, the MPI does not report an error when this condition is not met.
- When the AF module is enabled, the minimum image width is 256.
- Different vi\_pipe channels on Hi3403V100 support different AE resolutions: vi\_pipe0 supports a maximum resolution of 8192\*8192, and vi\_pipe1/vi\_pipe2/vi\_pipe3 support a maximum resolution of 4096\*4096. When the resolution of vi\_pipe1/vi\_pipe2/vi\_pipe3 exceeds 4096, AE statistics are disabled for those channels. **Related Data Types and Interfaces** None ### ot\_point **Description** Defines coordinate information. **Definition** `typedef struct { td_s32 x; td_s32 y;
} ot_point;` **Members**

| Member Name | Description |
| --- | --- |
| x | X-axis coordinate. |

**Precautions** None. **Related Data Types and Interfaces** None ### ot\_isp\_bayer\_format **Description** Defines the input Bayer image data format. **Definition** `typedef enum { OT_ISP_BAYER_RGGB = 0, OT_ISP_BAYER_GRBG = 1, OT_ISP_BAYER_GBRG = 2, OT_ISP_BAYER_BGGR = 3, OT_ISP_BAYER_BUTT
} ot_isp_bayer_format;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_BAYER\_RGGB | RGGB pixel arrangement. |
| OT\_ISP\_BAYER\_GRBG | GRBG pixel arrangement. |
| OT\_ISP\_BAYER\_GBRG | GBRG pixel arrangement. |
| OT\_ISP\_BAYER\_BGGR | BGGR pixel arrangement. |

**Precautions** This format can be obtained from the sensor datasheet and is related to the crop start position. **Related Data Types and Interfaces** None ### ot\_mipi\_crop\_attr **Description** MIPI crop parameters. **Definition** `typedef struct { td_bool mipi_crop_en; ot_rect mipi_crop_offset;
} ot_mipi_crop_attr;` **Members**

| Member Name | Description |
| --- | --- |
| mipi\_crop\_en | MIPI crop enable. |
| mipi\_crop\_offset | MIPI crop range; width and height must be 4-aligned. |

**Precautions** The MIPI parameter configuration in PUB\_ATTR is used to guide the Dynamic Blc module in modifying the OB region statistics range. This parameter must be consistent with the actual MIPI crop configuration. **Related Data Types and Interfaces** None ### ot\_isp\_bayer\_raw\_bit **Description** Defines the input Bayer image data bit width. **Definition** `typedef enum { OT_ISP_BAYER_RAW_BIT_8BIT = 8, OT_ISP_BAYER_RAW_BIT_10BIT = 10, OT_ISP_BAYER_RAW_BIT_12BIT = 12, OT_ISP_BAYER_RAW_BIT_14BIT = 14, OT_ISP_BAYER_RAW_BIT_16BIT = 16, OT_ISP_BAYER_RAW_BIT_BUTT
} ot_isp_bayer_raw_bit;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_BAYER\_RAW\_BIT\_8BIT | Bayer data bit width: 8 bits. |
| OT\_ISP\_BAYER\_RAW\_BIT\_10BIT | Bayer data bit width: 10 bits. |
| OT\_ISP\_BAYER\_RAW\_BIT\_12BIT | Bayer data bit width: 12 bits. |
| OT\_ISP\_BAYER\_RAW\_BIT\_14BIT | Bayer data bit width: 14 bits. |
| OT\_ISP\_BAYER\_RAW\_BIT\_16BIT | Bayer data bit width: 16 bits. |

**Precautions** This format can be obtained from the sensor datasheet and is related to the crop start position. **Related Data Types and Interfaces** None ### ot\_size **Description** Defines the width and height of sensor output. **Definition** `typedef struct { td_u32 width; td_u32 height;
} ot_size;` **Members**

| Member Name | Description |
| --- | --- |
| width | Sensor output width. Hi3403V100Valid range: [120, 8192] |
| height | Sensor output height. Hi3403V100Valid range: [120, 8192] |

**Precautions** Image width must be less than the sensor output image width; image height must be less than the sensor output image height. **Related Data Types and Interfaces** None ### ot\_color\_gamut **Description** Defines channel color gamut attributes. **Definition** `typedef enum { OT_COLOR_GAMUT_BT601 = 0, OT_COLOR_GAMUT_BT709, OT_COLOR_GAMUT_BT2020, OT_COLOR_GAMUT_USER, OT_COLOR_GAMUT_BUTT
} ot_color_gamut;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_COLOR\_GAMUT\_BT601 | Color gamut: BT.601. |
| OT\_COLOR\_GAMUT\_BT709 | Color gamut: BT.709. |
| OT\_COLOR\_GAMUT\_BT2020 | Color gamut: BT.2020. |
| OT\_COLOR\_GAMUT\_USER | User-defined color gamut. |

**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_pub\_attr](#ot_isp_pub_attr) ### ot\_isp\_pub\_attr **Description** Defines ISP public attributes. **Definition** `typedef struct { ot_rect wnd_rect; ot_size sns_size; ot_float frame_rate; ot_isp_bayer_format bayer_format; ot_wdr_mode wdr_mode; td_u8 sns_mode; td_bool sensor_flip_en; td_bool sensor_mirror_en; ot_mipi_crop_attr mipi_crop_attr;
} ot_isp_pub_attr;` **Members**

| Member Name | Description |
| --- | --- |
| wnd\_rect | Crop window start position and image dimensions. The horizontal start position x and vertical start position y in wnd\_rect must be 2-aligned. |
| sns\_size | Sensor output image width and height. |
| frame\_rate | Input image frame rate. Valid range: (0.00, 65535.00] |
| bayer\_format | Bayer data format. |
| wdr\_mode | WDR mode selection. |
| sns\_mode | Used to select the sensor initialization sequence. When resolution and frame rate are the same, different sns\_mode values correspond to different initialization sequences. Otherwise, sns\_mode defaults to 0 and the initialization sequence is selected via sns\_size and frame\_rate. |
| sensor\_flip\_en | Used to guide the Dynamic Blc module in adjusting the OB region statistics range. Set to 1 when sensor internal flip is enabled and the OB region has moved to the bottom; set to 0 when sensor internal flip is disabled. |
| sensor\_mirror\_en | Used to guide the Dynamic Blc module in adjusting the OB region statistics range. Set to 1 when sensor internal mirror is enabled and the OB region has moved from left to right; set to 0 when sensor internal mirror is disabled. |
| mipi\_crop\_attr | Used to guide the Dynamic Blc module in adjusting the OB region statistics range. This parameter must be consistent with the MIPI crop configuration. |

**Precautions** - If sensor\_flip\_en is 0, mipi\_crop\_attr.y should be set to 0.
- If sensor\_flip\_en is 1, mipi\_crop\_attr.y plus mipi\_crop\_attr.height must equal the sensor output height. **Related Data Types and Interfaces** None ### ot\_op\_mode **Description** Defines the module operating state. **Definition** `typedef enum { OT_OP_MODE_AUTO = 0, OT_OP_MODE_MANUAL = 1, OT_OP_MODE_BUTT
} ot_op_mode;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_OP\_MODE\_AUTO | Runs in automatic mode. |
| OT\_OP\_MODE\_MANUAL | Runs in manual mode. |

**Precautions** None **Related Data Types and Interfaces** - ot\_isp\_fswdr\_mdt\_attr
- ot\_isp\_drc\_attr
- ot\_isp\_ldci\_attr
- ot\_isp\_crb\_attr
- ot\_isp\_dp\_dynamic\_attr
- ot\_isp\_nr\_attr
- ot\_isp\_sharpen\_attr
- ot\_isp\_anti\_false\_color\_attr
- ot\_isp\_demosaic\_attr
- ot\_isp\_fpn\_attr
- ot\_isp\_dehaze\_attr
- ot\_isp\_local\_cac\_attr
- ot\_isp\_acac\_attr
- ot\_isp\_bayershp\_attr
- ot\_isp\_iris\_attr
- ot\_isp\_me\_attr
- ot\_isp\_exposure\_attr
- ot\_isp\_wdr\_exposure\_attr
- ot\_isp\_hdr\_exposure\_attr
- ot\_isp\_smart\_exposure\_attr
- ot\_isp\_awb\_ct\_limit\_attr
- ot\_isp\_awb\_in\_out\_attr
- ot\_isp\_awb\_lum\_histgram\_attr
- ot\_isp\_wb\_attr
- ot\_isp\_color\_matrix\_attr
- ot\_isp\_saturation\_attr ### ot\_isp\_fmw\_state **Description** Defines ISP firmware state. **Definition** `typedef enum { OT_ISP_FMW_STATE_RUN = 0, OT_ISP_FMW_STATE_FREEZE, OT_ISP_FMW_STATE_BUTT
} ot_isp_fmw_state;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_FMW\_STATE\_RUN | Firmware is running normally. |
| OT\_ISP\_FMW\_STATE\_FREEZE | Firmware is frozen. |

**Precautions** None **Related Data Types and Interfaces** None ### ot\_isp\_slave\_sns\_sync **Description** Defines slave-mode sensor sync signal configuration. **Definition** `typedef struct { union { struct { td_u32 bit16_reserved : 16; td_u32 bit_h_inv : 1; td_u32 bit_v_inv : 1; td_u32 bit12_reserved : 12; td_u32 bit_h_enable : 1; td_u32 bit_v_enable : 1; } bits; td_u32 bytes; } cfg; td_u32 vs_time; td_u32 hs_time; td_u32 vs_cyc; td_u32 hs_cyc; td_u32 hs_dly_cyc; td_u32 slave_mode_time;
} ot_isp_slave_sns_sync;` **Members**

| Member Name | Description |
| --- | --- |
| bit16\_reserved | Reserved field. |
| bit\_h\_inv | XHS polarity configuration. - 0: positive polarity; - 1: negative polarity. |
| bit\_v\_inv | XVS polarity configuration. |
| bit12\_reserved | Reserved field. |
| bit\_h\_enable | XHS output enable. |
| bit\_v\_enable | XVS output enable. |
| vs\_time | XVS signal period, unit: sensor input clock cycles. |
| hs\_time | XHS signal period, unit: sensor input clock cycles. |
| vs\_cyc | XVS active level width, unit: sensor input clock cycles. |
| hs\_cyc | XHS active level width, unit: sensor input clock cycles. |
| hs\_dly\_cyc | XHS pulse output delay relative to XVS pulse, unit: sensor input clock cycles. |
| slave\_mode\_time | Sensor slave mode timing configuration selection register: 0: Select SENSOR0 timing configuration; 1: Select SENSOR1 timing configuration; 2: Select SENSOR2 timing configuration; 3: Select SENSOR3 timing configuration. |

**Precautions** As shown in [Figure 1](#_Ref440016125) to [Figure 3](#_Ref440016130), the meaning of each configuration parameter for the sync signal generator module is illustrated. **Figure 1** Sync signal configuration timing diagram **Figure 2** Sync signal polarity inversion **Figure 3** Sync signal enabled **Related Data Types and Interfaces** None ### ot\_isp\_wdr\_mode **Description** Defines ISP wide dynamic range mode. **Definition** `typedef struct { ot_wdr_mode wdr_mode;
} ot_isp_wdr_mode;` **Members**

| Member Name | Description |
| --- | --- |
| wdr\_mode | Wide dynamic range mode. |

**Precautions** None **Related Data Types and Interfaces** None ### ot\_wdr\_mode **Description** Defines wide dynamic range mode. **Definition** `typedef enum { OT_WDR_MODE_NONE = 0, OT_WDR_MODE_BUILT_IN, OT_WDR_MODE_QUDRA, OT_WDR_MODE_2To1_LINE, OT_WDR_MODE_2To1_FRAME, OT_WDR_MODE_3To1_LINE, OT_WDR_MODE_3To1_FRAME, OT_WDR_MODE_4To1_LINE, OT_WDR_MODE_4To1_FRAME, OT_WDR_MODE_BUTT,
} ot_wdr_mode;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_WDR\_MODE\_NONE | Linear mode. |
| OT\_WDR\_MODE\_BUILT\_IN | Sensor-synthesized WDR mode. |
| OT\_WDR\_MODE\_QUDRA | Quadra mode. |
| OT\_WDR\_MODE\_2To1\_LINE | 2-frame line-interleaved WDR mode. |
| OT\_WDR\_MODE\_2To1\_FRAME | 2-frame frame-interleaved WDR mode. |
| OT\_WDR\_MODE\_3To1\_LINE | 3-frame line-interleaved WDR mode. |
| OT\_WDR\_MODE\_3To1\_FRAME | 3-frame frame-interleaved WDR mode. |
| OT\_WDR\_MODE\_4To1\_LINE | 4-frame line-interleaved WDR mode. |
| OT\_WDR\_MODE\_4To1\_FRAME | 4-frame frame-interleaved WDR mode. |

**Precautions** OT\_WDR\_MODE\_BUILT\_IN requires sensor support. **Related Data Types and Interfaces** None ### ot\_isp\_module\_ctrl **Description** Defines ISP function module control. **Definition** `typedef union { td_u64 key; struct { td_u64 bit_bypass_isp_d_gain : 1; /* RW;[0] */ td_u64 bit_bypass_anti_false_color : 1; /* RW;[1] */ td_u64 bit_bypass_crosstalk_removal : 1; /* RW;[2] */ td_u64 bit_bypass_dpc : 1; /* RW;[3] */ td_u64 bit_bypass_nr : 1; /* RW;[4] */ td_u64 bit_bypass_dehaze : 1; /* RW;[5] */ td_u64 bit_bypass_wb_gain : 1; /* RW;[6] */ td_u64 bit_bypass_mesh_shading : 1; /* RW;[7] */ td_u64 bit_bypass_drc : 1; /* RW;[8] */ td_u64 bit_bypass_demosaic : 1; /* RW;[9] */ td_u64 bit_bypass_color_matrix : 1; /* RW;[10] */ td_u64 bit_bypass_gamma : 1; /* RW;[11] */ td_u64 bit_bypass_fswdr : 1; /* RW;[12] */ td_u64 bit_bypass_ca : 1; /* RW;[13] */ td_u64 bit_bypass_csc : 1; /* RW;[14] */ td_u64 bit_bypass_radial_crop : 1; /* RW;[15] */ td_u64 bit_bypass_sharpen : 1; /* RW;[16] */ td_u64 bit_bypass_local_cac : 1; /* RW;[17] */ td_u64 bit_bypass_acac : 1; /* RW;[18]; */ td_u64 bit2_chn_select : 2; /* RW;[19:20] */ td_u64 bit_bypass_ldci : 1; /* RW;[21] */ td_u64 bit_bypass_pregamma : 1; /* RW;[22] */ td_u64 bit_bypass_ae_stat_fe : 1; /* RW;[23] */ td_u64 bit_bypass_ae_stat_be : 1; /* RW;[24] */ td_u64 bit_bypass_mg_stat : 1; /* RW;[25] */ td_u64 bit_bypass_af_stat_fe : 1; /* RW;[26] */ td_u64 bit_bypass_af_stat_be : 1; /* RW;[27] */ td_u64 bit_bypass_awb_stat : 1; /* RW;[28] */ td_u64 bit_bypass_clut : 1; /* RW;[29] */ td_u64 bit_bypass_rgbir : 1; /* RW;[30] */ td_u64 bit_bypass_agamma : 1; /* RW;[31] */ td_u64 bit_bypass_adgamma : 1; /* RW;[32] */ td_u64 bit_bypass_crb : 1; /* RW [33] */ td_u64 bit_reserved30 : 30; /* H; [34:63] */ };
} ot_isp_module_ctrl;` **Members**

| Member Name | Description |
| --- | --- |
| key | Integer value of the struct union. |
| bit\_bypass\_isp\_d\_gain | Bypass digital gain. |
| bit\_bypass\_anti\_false\_color | Bypass anti-false-color. |
| bit\_bypass\_crosstalk\_removal | Bypass Crosstalk Removal. |
| bit\_bypass\_dpc | Bypass defective pixel correction. |
| bit\_bypass\_nr | Bypass noise reduction. |
| bit\_bypass\_dehaze | Bypass dehaze. |
| bit\_bypass\_wb\_gain | Bypass white balance gain and offset. |
| bit\_bypass\_mesh\_shading | Bypass lens shading correction. |
| bit\_bypass\_drc | Bypass DRC. |
| bit\_bypass\_demosaic | Bypass demosaic module. |
| bit\_bypass\_color\_matrix | Bypass color matrix. |
| bit\_bypass\_gamma | Bypass Gamma table. |
| bit\_bypass\_fswdr | Bypass multi-frame WDR synthesis. |
| bit\_bypass\_ca | Bypass CA. |
| bit\_bypass\_csc | Bypass CSC conversion. |
| bit\_bypass\_radial\_crop | Bypass Radial Crop |
| bit\_bypass\_sharpen | Bypass Sharpen. |
| bit\_bypass\_local\_cac | Bypass Local CAC. |
| bit\_bypass\_acac | Bypass ACAC |
| bit2\_chn\_select | WDR mode main-path data source; typically used for debug after bypassing the multi-frame WDR synthesis module. 0: Main-path data source is the ultra-short frame; 1: Main-path data source is the short frame; 2: Main-path data source is the medium frame; 3: Main-path data source is the long frame. |
| bit\_bypass\_ldci | Bypass Local DCI. |
| bit\_bypass\_pregamma | Bypass Pre Gamma. |
| bit\_bypass\_ae\_stat\_fe | Bypass AE statistics at the FE. |
| bit\_bypass\_ae\_stat\_be | Bypass AE statistics at the BE. |
| bit\_bypass\_mg\_stat | Bypass MG statistics. |
| bit\_bypass\_af\_stat\_fe | Bypass AF statistics at the FE. |
| bit\_bypass\_af\_stat\_be | Bypass AF statistics at the BE. |
| bit\_bypass\_awb\_stat | Bypass AWB statistics. |
| bit\_bypass\_clut | Bypass CLUT. |
| bit\_bypass\_rgbir | Bypass RGBIR. |
| bit\_bypass\_agamma | Bypass a Gamma. Not supported |
| bit\_bypass\_adgamma | Bypass a Dgamma. Not supported |
| bit\_bypass\_crb | Bypass CRB |
| bit\_reserved30 | Reserved. |

**Precautions** In WDR mode, toggling the WDR module enable/disable causes a few frames of abnormal color. **Related Data Types and Interfaces** None ### ot\_isp\_dump\_frame\_pos **Description** Defines the position of the captured frame data within the ISP BE. **Definition** `typedef enum { OT_ISP_DUMP_FRAME_POS_NORMAL = 0, OT_ISP_DUMP_FRAME_POS_AFTER_WDR = 1, OT_ISP_DUMP_FRAME_POS_BUTT
} ot_isp_dump_frame_pos;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_DUMP\_FRAME\_POS\_NORMAL | Capture data after processing by all ISP BE modules. |
| OT\_ISP\_DUMP\_FRAME\_POS\_AFTER\_WDR | Capture raw data after WDR synthesis. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_be\_frame\_attr](#ot_isp_be_frame_attr) ### ot\_isp\_be\_frame\_attr **Description** Defines the configuration for a BE frame. **Definition** `typedef struct { ot_isp_dump_frame_pos frame_pos;
} ot_isp_be_frame_attr;` **Members**

| Member Name | Description |
| --- | --- |
| frame\_pos | Position of the captured frame data within the ISP BE. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_dump\_frame\_pos](#ot_isp_dump_frame_pos) ### ot\_isp\_vd\_type **Description** Defines the ISP vertical-sync signal type. **Definition** `typedef enum { OT_ISP_VD_FE_START = 0, OT_ISP_VD_FE_END, OT_ISP_VD_BE_END, OT_ISP_VD_BUTT
} ot_isp_vd_type;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_VD\_FE\_START | FE frame start. |
| OT\_ISP\_VD\_FE\_END | FE frame end. |
| OT\_ISP\_VD\_BE\_END | BE frame end. |

**Precautions** [OT\_ISP\_VD\_BE\_END](#OT_ISP_VD_BE_END) is not supported in online and parallel modes. **Related Data Types and Interfaces** None ### ot\_isp\_sns\_attr\_info **Description** Defines ISP sensor attributes. **Definition** `typedef struct { ot_sensor_id sensor_id;
} ot_isp_sns_attr_info;` **Members**

| Member Name | Description |
| --- | --- |
| sensor\_id | Sensor ID number. |

**Precautions** None. **Related Data Types and Interfaces** None ### ot\_isp\_sensor\_register **Description** Defines the sensor registration struct. **Definition** `typedef struct { ot_isp_sensor_exp_func sns_exp;
} ot_isp_sensor_register;` **Members**

| Member Name | Description |
| --- | --- |
| sns\_exp | Callback function struct for sensor registration. |

**Precautions** This wrapper exists for extensibility. **Related Data Types and Interfaces** [ot\_isp\_sensor\_exp\_func](#ot_isp_sensor_exp_func) ### ot\_isp\_sensor\_exp\_func **Description** Defines the sensor callback function struct. **Definition** `typedef struct { ot_void (*pfn_cmos_sensor_init)(ot_vi_pipe vi_pipe); ot_void (*pfn_cmos_sensor_exit)(ot_vi_pipe vi_pipe); ot_void (*pfn_cmos_sensor_global_init)(ot_vi_pipe vi_pipe); td_s32 (*pfn_cmos_set_image_mode)(ot_vi_pipe vi_pipe, ot_isp_cmos_sensor_image_mode *sensor_image_mode); td_s32 (*pfn_cmos_set_wdr_mode)(ot_vi_pipe vi_pipe, td_u8 mode); td_s32 (*pfn_cmos_get_isp_default)(ot_vi_pipe vi_pipe, ot_isp_cmos_default *def); td_s32 (*pfn_cmos_get_isp_black_level)(ot_vi_pipe vi_pipe, ot_isp_cmos_black_level *black_level); td_s32 (*pfn_cmos_get_blc_clamp_info)(ot_vi_pipe vi_pipe, td_bool *clamp_en); td_s32 (*pfn_cmos_get_sns_reg_info)(ot_vi_pipe vi_pipe, ot_isp_sns_regs_info *sns_regs_info); ot_void (*pfn_cmos_set_pixel_detect)(ot_vi_pipe vi_pipe, td_bool enable); td_s32 (*pfn_cmos_get_awb_gains)(ot_vi_pipe vi_pipe, td_u32 *sensor_awb_gain);
} ot_isp_sensor_exp_func;` **Members**

| Member Name | Description |
| --- | --- |
| pfn\_cmos\_sensor\_init | Callback function pointer for sensor initialization. |
| pfn\_cmos\_sensor\_exit | Callback function pointer for sensor exit. |
| pfn\_cmos\_sensor\_global\_init | Callback function pointer for global variable initialization. |
| pfn\_cmos\_set\_image\_mode | Callback function pointer for setting resolution and frame-rate switching. Return value 0 means the sensor mode has changed and ISP will call pfn\_cmos\_sensor\_init to reconfigure the sensor; return value -2 means the sensor mode is unchanged and ISP will not reconfigure the sensor. |
| pfn\_cmos\_set\_wdr\_mode | Callback function pointer for setting the WDR mode. |
| pfn\_cmos\_get\_isp\_default | Callback function pointer to get the initial values of the ISP base algorithms. |
| pfn\_cmos\_get\_isp\_black\_level | Callback function pointer to get the sensor black level. Supports dynamically adjusting the black level based on sensor gain. If dynamic adjustment is used, the black level can only be set externally via the manual mode of ss\_mpi\_isp\_set\_black\_level\_attr. |
| pfn\_cmos\_get\_blc\_clamp\_info | Callback function pointer to get the sensor internal black-level clamp enable status. |
| pfn\_cmos\_get\_sns\_reg\_info | Callback function pointer to get sensor register information, used to configure AE information in kernel space. |
| pfn\_cmos\_set\_pixel\_detect | Callback function pointer for enabling/disabling defective pixel correction. |
| pfn\_cmos\_get\_awb\_gains | Callback function pointer to get AWB gains. |

**Precautions** - pfn\_cmos\_sensor\_init, pfn\_cmos\_get\_isp\_default, pfn\_cmos\_get\_isp\_black\_level, pfn\_cmos\_set\_pixel\_detect, and pfn\_cmos\_get\_sns\_reg\_info must be assigned. Other callback function pointers that are not needed should be set to NULL. For example, if a sensor does not support resolution switching, set pfn\_cmos\_set\_image\_mode to NULL.
- Hi3403V100 does not support configuring AWB gains on the sensor side; only reading the current AWB gains from the sensor side is supported.
- Switching the AWB gain configuration location is not supported. **Related Data Types and Interfaces** - [ot\_isp\_sensor\_register](#ot_isp_sensor_register)
- [ot\_isp\_sns\_state](#ot_isp_sns_state)
- [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_sensor\_image\_mode **Description** Defines the sensor output width, height, and frame rate attributes. **Definition** `typedef struct { td_u16 width; td_u16 height; ot_float fps; td_u8 sns_mode;
} ot_isp_cmos_sensor_image_mode;` **Members**

| Member Name | Description |
| --- | --- |
| width | Sensor output width. |
| height | Sensor output height. |
| fps | Sensor output frame rate. |
| sns\_mode | Used to select the sensor initialization sequence. When resolution and frame rate are the same, different sns\_mode values correspond to different initialization sequences; in other cases sns\_mode defaults to 0. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_sensor\_exp\_func](#ot_isp_sensor_exp_func) ### ot\_isp\_cmos\_lsc **Description** Defines LSC parameters. **Definition** `typedef struct { ot_isp_shading_attr lsc_attr; ot_isp_shading_lut_attr lsc_lut;
} ot_isp_cmos_lsc;` **Members**

| Member Name | Description |
| --- | --- |
| lsc\_attr | Mesh ShadingAlgorithm parameters. |
| lsc\_lut | Mesh ShadingGain-table attributes. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_acs\_y\_shading\_lut **Description** Defines the correction strength table for the luminance component (Gr/Gb channels) of Auto Color Shading, generated by the calibration tool. **Definition** `typedef struct { td_u16 g_param_high_ct[OT_ISP_LSC_GRID_POINTS]; td_u16 g_param_low_ct[OT_ISP_LSC_GRID_POINTS];
} ot_isp_acs_y_shading_lut;` **Members**

| Member Name | Description |
| --- | --- |
| g\_param\_high\_ct | Correction strength table for the Gr/Gb channels; higher correction strength. |
| g\_param\_low\_ct | Correction strength table for the Gr/Gb channels; lower correction strength. |

**Precautions** The algorithm interpolates between the g\_param\_high\_ct and g\_param\_low\_ct tables based on the scene. **Related Data Types and Interfaces** [ot\_isp\_cmos\_acs](#ot_isp_cmos_acs) ### ot\_isp\_acs\_color\_shading\_lut **Description** Defines the color-component LUT for Auto Color Shading, generated by the calibration tool. The algorithm dynamically generates a scene-appropriate LUT based on the R/B channel LU Ts. **Definition** `typedef struct { ot_float avg_rg_map[OT_ISP_LSC_GRID_POINTS]; ot_float avg_bg_map[OT_ISP_LSC_GRID_POINTS]; ot_float prof_rg_map[OT_ISP_LSC_GRID_POINTS]; ot_float prof_bg_map[OT_ISP_LSC_GRID_POINTS];
} ot_isp_acs_color_shading_lut;` **Members**

| Member Name | Description |
| --- | --- |
| avg\_rg\_map | Color Shading table for the R channel. |
| avg\_bg\_map | Color Shading table for the B channel. |
| prof\_rg\_map | Color Shading table for the R channel. |
| prof\_bg\_map | Color Shading table for the B channel. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_acs](#ot_isp_cmos_acs) ### ot\_isp\_acs\_calib\_param **Description** Defines the calibration parameters for Auto Color Shading, generated by the calibration tool. **Definition** `typedef struct { td_s16 light_index[OT_ISP_ACS_LIGHT_NUM * OT_ISP_ACS_CHN_NUM]; ot_float model_ar_min; ot_float model_ar_step; ot_float model_ab_min; ot_float model_ab_step; td_s16 light_type_g_high; td_s16 light_type_g_low;
} ot_isp_acs_calib_param;` **Members**

| Member Name | Description |
| --- | --- |
| light\_index | Coordinates of the calibration light source within the algorithm model. |
| model\_ar\_min | Algorithm model parameter obtained from calibration. |
| model\_ar\_step | Algorithm model parameter obtained from calibration. |
| model\_ab\_min | Algorithm model parameter obtained from calibration. |
| model\_ab\_step | Algorithm model parameter obtained from calibration. |
| light\_type\_g\_high | Corresponding light source coordinate for the g\_param\_high\_ct table. |
| light\_type\_g\_low | Corresponding light source coordinate for the g\_param\_low\_ct table. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_acs](#ot_isp_cmos_acs) ### ot\_isp\_cmos\_acs **Description** Defines the CMOS parameters for Auto Color Shading. **Definition** `typedef struct { ot_isp_acs_attr acs_attr; ot_isp_acs_calib_param acs_calib_param; ot_isp_acs_y_shading_lut acs_y_shading_lut; ot_isp_acs_color_shading_lut acs_color_shading_lut;
} ot_isp_cmos_acs;` **Members**

| Member Name | Description |
| --- | --- |
| acs\_attr | See ot\_isp\_acs\_attr. |
| acs\_calib\_param | See [ot\_isp\_acs\_calib\_param](#ZH-CN_TOPIC_0000002471085078) |
| acs\_y\_shading\_lut | See [ot\_isp\_acs\_y\_shading\_lut](#ot_isp_acs_y_shading_lut) |
| acs\_color\_shading\_lut | See [ot\_isp\_acs\_color\_shading\_lut](#ot_isp_acs_color_shading_lut) |

**Precautions** - The default configuration of the gain table is related to the bit1\_acs flag in [ot\_isp\_cmos\_alg\_key](#ZH-CN_TOPIC_0000002471084994). If bit1\_acs=1, the values from cmos\_ex.h are used as the default; otherwise all defaults are 0.
- The OTP for the ACS module is implemented via the lsc\_lut.lsc\_gain\_lut interface in [ot\_isp\_cmos\_lsc](#ZH-CN_TOPIC_0000002504084813). lsc\_lut.lsc\_gain\_lut[0] is configured as the golden-sample calibration table at D50; lsc\_lut.lsc\_gain\_lut[1] is configured as the current lens module calibration table at D50. This resolves lens-to-lens consistency issues — the smaller the difference between the module and the golden sample, the better the correction. You can also configure lsc\_gain\_lut[0] and lsc\_gain\_lut[1] via ss\_mpi\_isp\_set\_mesh\_shading\_gain\_lut\_attr after ISP start-up; usage is the same as described above. **Related Data Types and Interfaces** - [ot\_isp\_cmos\_default](#ot_isp_cmos_default)
- [ot\_isp\_acs\_y\_shading\_lut](#ot_isp_acs_y_shading_lut)
- [ot\_isp\_acs\_color\_shading\_lut](#ot_isp_acs_color_shading_lut)
- [ot\_isp\_acs\_calib\_param](#ot_isp_acs_calib_param) ### ot\_isp\_noise\_calibration **Description** Defines noise calibration parameters. **Definition** `typedef struct { td_double calibration_coef[OT_BAYER_CALIBRATION_PARA_NUM_NEW];
} ot_isp_noise_calibration;` **Members**

| Member Name | Description |
| --- | --- |
| calibration\_coef[[OT\_BAYER\_CALIBRATION\_PARA\_NUM\_NEW](#OT_BAYER_CALIBRATION_PARA_NUM_NEW)] | Noise calibration table. |

**Precautions** None **Related Data Types and Interfaces** [ss\_mpi\_isp\_get\_noise\_calibration](#ss_mpi_isp_get_noise_calibration) ### ot\_isp\_cmos\_sensor\_max\_resolution **Description** Defines the sensor maximum resolution struct. **Definition** `typedef struct { td_u32 max_width; td_u32 max_height;
} ot_isp_cmos_sensor_max_resolution;` **Members**

| Member Name | Description |
| --- | --- |
| max\_width | Maximum width. |
| max\_height | Maximum height. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_clut **Description** Defines the CLUT struct. **Definition** `typedef struct { ot_isp_clut_attr clut_attr; ot_isp_clut_lut clut_lut;
} ot_isp_cmos_clut;` **Members**

| Member Name | Description |
| --- | --- |
| clut\_attr | Defines the CLUT gain. |
| clut\_lut | Defines the CLUT lookup table. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_sensor\_mode **Description** Defines the sensor mode register. **Definition** `typedef struct { td_u32 sensor_id; td_u8 sensor_mode; td_bool valid_dng_raw_format; ot_isp_dng_raw_format dng_raw_format;
} ot_isp_cmos_sensor_mode;` **Members**

| Member Name | Description |
| --- | --- |
| sensor\_id | Sensor ID number. |
| sensor\_mode | Sensor user-defined operating mode; different resolutions and frame rates correspond to different operating modes. |
| valid\_dng\_raw\_format | Valid DNG raw format. |
| dng\_raw\_format | DNG raw format. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_dng\_color\_param **Description** Defines the DNG white balance correction coefficients. **Definition** `typedef struct { ot_isp_dng_wb_gain wb_gain1; ot_isp_dng_wb_gain wb_gain2;
} ot_isp_cmos_dng_color_param;` **Members**

| Member Name | Description |
| --- | --- |
| wb\_gain1 | DNG white balance correction coefficient 1. |
| wb\_gain2 | DNG white balance correction coefficient 2. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_wdr\_switch\_attr **Description** Defines WDR switching attributes. **Definition** `typedef struct { td_u32 exp_ratio[OT_ISP_EXP_RATIO_NUM];
} ot_isp_cmos_wdr_switch_attr;` **Members**

| Member Name | Description |
| --- | --- |
| exp\_ratio | Expected exposure ratio. |

**Precautions** Assign the default value to exp\_ratio based on the WDR mode in the cmos\_get\_isp\_default function. The value must be consistent with the AE initialization exposure ratio in cmos\_get\_ae\_default: - If ae\_sns\_dft->man\_ratio\_enable is TRUE, exp\_ratio equals ae\_sns\_dft->arr\_ratio;
- If ae\_sns\_dft->man\_ratio\_enable is FALSE, exp\_ratio is 0x40. **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_alg\_key **Description** Defines flag bits indicating whether each ISP algorithm uses the default CMOS configuration. **Definition** Definition for Hi3403V100: `typedef union { td_u64 key; struct { td_u64 bit1_drc : 1 ; /* [0] */ td_u64 bit1_demosaic : 1 ; /* [1] */ td_u64 bit1_pregamma : 1 ; /* [2] */ td_u64 bit1_gamma : 1 ; /* [3] */ td_u64 bit1_sharpen : 1 ; /* [4] */ td_u64 bit1_ldci : 1 ; /* [5] */ td_u64 bit1_dpc : 1 ; /* [6] */ td_u64 bit1_lsc : 1 ; /* [7] */ td_u64 bit1_ge : 1 ; /* [8] */ td_u64 bit1_anti_false_color : 1 ; /* [9] */ td_u64 bit1_bayer_nr : 1 ; /* [10] */ td_u64 bit1_ca : 1 ; /* [11] */ td_u64 bit1_expander : 1 ; /* [12] */ td_u64 bit1_clut : 1 ; /* [13] */ td_u64 bit1_wdr : 1 ; /* [14] */ td_u64 bit1_dehaze : 1 ; /* [15] */ td_u64 bit1_lcac : 1 ; /* [16] */ td_u64 bit1_acs : 1 ; /* [17] */ td_u64 bit1_rgbir : 1 ; /* [18] */ td_u64 bit1_bshp : 1 ; /* [19] */ td_u64 bit1_acac : 1 ; /* [20] */ td_u64 bit1_crb : 1 ; /* [21] */ td_u64 bit42_reserved : 42; /* [22:63] */ };
} ot_isp_cmos_alg_key;` **Members**

| Member Name | Description |
| --- | --- |
| bit1\_drc | Flag bit for whether the DRC module uses the CMOS default configuration. |
| bit1\_demosaic | Flag bit for whether the demosaic module uses the CMOS default configuration. |
| bit1\_pregamma | Flag bit for whether the Pre Gamma module uses the CMOS default configuration. |
| bit1\_gamma | Flag bit for whether the Gamma module uses the CMOS default configuration. |
| bit1\_sharpen | Flag bit for whether the Sharpen module uses the CMOS default configuration. |
| bit1\_ldci | Flag bit for whether the LDCI module uses the CMOS default configuration. |
| bit1\_dpc | Flag bit for whether the DPC module uses the CMOS default configuration. |
| bit1\_lsc | Flag bit for whether the LSC module uses the CMOS default configuration. |
| bit1\_ge | Flag bit for whether the GE module uses the CMOS default configuration. |
| bit1\_anti\_false\_color | Flag bit for whether the Anti-False-Color module uses the CMOS default configuration. |
| bit1\_bayer\_nr | Flag bit for whether the Bayer NR module uses the CMOS default configuration. |
| bit1\_ca | Flag bit for whether the CA module uses the CMOS default configuration. |
| bit1\_expander | Flag bit for whether the Expander module uses the CMOS default configuration. Valid only in sensor built-in mode. |
| bit1\_clut | Flag bit for whether the CLUT module uses the CMOS default configuration. |
| bit1\_wdr | Flag bit for whether the WDR module uses the CMOS default configuration. |
| bit1\_dehaze | Flag bit for whether the Dehaze module uses the CMOS default configuration. |
| bit1\_lcac | Flag bit for whether the Local CAC module uses the CMOS default configuration. |
| bit1\_acs | Flag bit for whether the ACS module uses the CMOS default configuration. |
| bit1\_rgbir | Flag bit for whether the RGBIR module uses the CMOS default configuration. Valid only in linear mode. |
| bit1\_bshp | Flag bit for whether the Bayer Sharpen module uses the CMOS default configuration. |
| bit1\_acac | Flag bit for whether the ACAC module uses the CMOS default configuration. |
| bit1\_crb | Flag bit for whether the CRB module uses the CMOS default configuration. Valid only in WDR mode. |

**Precautions** To use the CMOS configuration for an ISP algorithm module, set the corresponding flag bit to 1; otherwise, the algorithm's internal default configuration is used. **Related Data Types and Interfaces** [ot\_isp\_cmos\_default](#ot_isp_cmos_default) ### ot\_isp\_cmos\_default **Description** Defines the initialization parameter struct for the ISP base algorithm library. **Definition** Definition for Hi3403V100: `typedef struct { ot_isp_cmos_alg_key key; const ot_isp_drc_attr *drc; const ot_isp_demosaic_attr *demosaic; const ot_isp_pregamma_attr *pregamma; const ot_isp_gamma_attr *gamma; const ot_isp_sharpen_attr *sharpen; const ot_isp_ldci_attr *ldci; const ot_isp_dp_dynamic_auto_attr *dpc; const ot_isp_cmos_lsc *lsc; const ot_isp_cr_attr *ge; const ot_isp_anti_false_color_attr *anti_false_color; const ot_isp_nr_attr *bayer_nr; const ot_isp_ca_attr *ca; const ot_isp_expander_attr *expander; const ot_isp_cmos_clut *clut; const ot_isp_wdr_fs_attr *wdr; const ot_isp_dehaze_attr *dehaze; const ot_isp_local_cac_attr *lcac; const ot_isp_acac_attr *acac; const ot_isp_bayershp_attr *bshp; const ot_isp_cmos_acs *acs; const ot_isp_rgbir_attr *rgbir; const ot_isp_crb_attr *crb; ot_isp_noise_calibration noise_calibration; ot_isp_cmos_sensor_max_resolution sensor_max_resolution; ot_isp_cmos_sensor_mode sensor_mode; ot_isp_cmos_dng_color_param dng_color_param; ot_isp_cmos_wdr_switch_attr wdr_switch_attr;
} ot_isp_cmos_default;` **Members**

| Member Name | Description |
| --- | --- |
| key | Key identifying whether each algorithm uses the CMOS default configuration. |
| \*drc | DR Cstructure pointer. |
| \*demosaic | Demosaicstructure pointer. |
| \*pregamma | Pre Gammastructure pointer. |
| \*gamma | Gammastructure pointer. |
| \*sharpen | Sharpenstructure pointer. |
| \*ldci | LDC Istructure pointer. |
| \*dpc | DP Cstructure pointer. |
| \*lsc | LS Cstructure pointer. |
| \*ge | GE module structure pointer. |
| \*anti\_false\_color | Anti Falsestructure pointer. |
| \*bayer\_nr | BayerN Rstructure pointer. |
| \*ca | CA module structure pointer. |
| \*expander | Expanderstructure pointer. Valid only in sensor built-in mode. |
| \*clut | Clutstructure pointer. |
| \*wdr | WDR mode structure pointer. |
| \*dehaze | Dehazestructure pointer. |
| \*lcac | Local cacstructure pointer. |
| \*acac | acacstructure pointer. |
| \*bshp | Bayer sharpenstructure pointer. |
| \*acs | AC Sstructure pointer. |
| \*rgbir | RGBIR mode structure pointer. Valid only in linear mode. |
| \*crb | CR Bstructure pointer. Valid only in WDR mode. |
| noise\_calibration | Noise calibration struct. |
| sensor\_max\_resolution | Sensor maximum width/height struct. |
| sensor\_mode | Sensor mode struct. |
| dng\_color\_param | DNG struct. |
| wdr\_switch\_attr | WDR switching attributes. |

**Precautions** - The default values for sensor\_max\_resolution, sensor\_mode, and dng\_color\_param are defined in cmos.c; the default values for all other ISP base algorithms are in cmos\_ex.h. To modify default values, update the corresponding parameters. To bring up a new sensor, refer to the default values provided for other sensors.
- For each ISP algorithm module that is to use the CMOS default configuration, set the corresponding flag bit to 1 in cmos\_get\_isp\_default and assign the CMOS struct pointer for that module. If the CMOS default values are invalid, the algorithm initialization will fail and the algorithm will not operate correctly at runtime (the algorithm MPI interface will return error code 0xa01c8047 and the logmpp will show an algorithm initialization failure message). **Related Data Types and Interfaces** [ot\_isp\_sensor\_exp\_func](#ot_isp_sensor_exp_func) ### ot\_isp\_black\_level\_auto\_attr **Description** Defines the black level auto mode struct. **Definition** `typedef struct { td_bool update; td_u16 black_level[OT_ISP_WDR_MAX_FRAME_NUM][OT_ISP_BAYER_CHN_NUM];
} ot_isp_black_level_auto_attr;` **Members**

| Member Name | Description |
| --- | --- |
| update | Indicates whether the sensor black level changes dynamically with gain. Valid range: [0, 1]. If set to TD\_TRUE, the ISP always uses the dynamic black level configured in cmos.c; to manually change the ISP black level, set ss\_mpi\_isp\_set\_black\_level\_attr to manual mode. |
| black\_level | Sensor black level array. Valid range: [0, 0x3FFF] black\_level is the black level for 14-bit raw data. |

**Precautions** If the sensor black level does not change dynamically with gain, set update to TD\_FALSE. **Related Data Types and Interfaces** [ot\_isp\_sensor\_exp\_func](#ot_isp_sensor_exp_func) ### ot\_isp\_sensor\_total\_size\_attr **Description** Defines the actual width and height of the data written out by the sensor. **Definition** `typedef struct { ot_size ob_sensor_size;
} ot_isp_sensor_total_size_attr;` **Members**

| Member Name | Description |
| --- | --- |
| ob\_sensor\_size | Actual width and height of the data written out by the sensor. If the data written by the sensor includes the OB region,ob\_sensor\_size should be the width and height including the OB region. |

**Precautions** If the sensor output data includes an OB region, the MIPI output width and height must match ob\_sensor\_size to ensure correct dynamic BLC operation. **Related Data Types and Interfaces** [ot\_isp\_cmos\_black\_level](#ot_isp_cmos_black_level) ### ot\_isp\_cmos\_black\_level **Description** Defines the sensor black level struct. **Definition** `typedef struct { td_bool user_black_level_en; td_u16 user_black_level[OT_ISP_WDR_MAX_FRAME_NUM][OT_ISP_BAYER_CHN_NUM]; ot_isp_black_level_mode black_level_mode; ot_isp_black_level_manual_attr manual_attr; ot_isp_black_level_dynamic_attr dynamic_attr; ot_isp_black_level_auto_attr auto_attr; ot_isp_sensor_total_size_attr sensor_with_ob_attr;
} ot_isp_cmos_black_level;` **Members**

| Member Name | Description |
| --- | --- |
| user\_black\_level\_en | Enable for user-defined black level. |
| user\_black\_level | User-defined black level value. |
| black\_level\_mode | Black level mode selection. |
| manual\_attr | Black level configuration attributes in manual mode. |
| dynamic\_attr | Black level configuration attributes in dynamic mode. |
| auto\_attr | Black level configuration attributes in auto mode. |
| sensor\_with\_ob\_attr | Sensor output width/height including the OB region; used to guide Dynamic BLC in adjusting the OB statistics range. |

<a name="ZH-CN_TOPIC_0000002504084889"></a>**Precautions** - If black\_level\_mode is set to OT\_ISP\_BLACK\_LEVEL\_MODE\_AUTO: if the update member of [ot\_isp\_black\_level\_auto\_attr](#ZH-CN_TOPIC_0000002504084889) in cmos.c is TD\_TRUE, the ISP always uses the dynamic black level configuration from cmos.c; if TD\_FALSE, the non-dynamic configuration from cmos.c is used.
- If black\_level\_mode is set to OT\_ISP\_BLACK\_LEVEL\_MODE\_MANUAL: the manual black level configuration in cmos\_ex.h takes effect.
- If black\_level\_mode is set to OT\_ISP\_BLACK\_LEVEL\_MODE\_DYNAMIC, the dynamic BLC algorithm is used to measure the OB region and derive the black level value.
- When using a virtual pipe (vi\_pipe >= 4), OT\_ISP\_BLACK\_LEVEL\_MODE\_DYNAMIC is not supported. OT\_ISP\_BLACK\_LEVEL\_MODE\_DYNAMIC is also not supported in sensor built-in mode.
- If user\_black\_level\_en is enabled, all ISP modules use user\_black\_level as the black level.
- When using a virtual pipe (vi\_pipe >= 4), enabling user\_black\_level\_en is not supported. Enabling user\_black\_level\_en is also not supported in sensor built-in mode. **Related Data Types and Interfaces** [ot\_isp\_sensor\_exp\_func](#ot_isp_sensor_exp_func) ### ot\_isp\_sns\_regs\_info **Description** Defines the sensor register information. **Definition** `typedef struct { ot_isp_sns_type sns_type; td_u32 reg_num; td_u8 cfg2_valid_delay_max; td_u32 exp_distance[OT_ISP_WDR_MAX_FRAME_NUM - 1]; ot_isp_sns_commbus com_bus; union { ot_isp_i2c_data i2c_data[OT_ISP_MAX_SNS_REGS]; ot_isp_ssp_data ssp_data[OT_ISP_MAX_SNS_REGS]; }; struct { td_bool update; td_u8 delay_frame_num; td_u32 slave_vs_time; td_u32 slave_bind_dev; } slv_sync; td_bool config;
} ot_isp_sns_regs_info;` **Members**

| Member Name | Sub-member Name | Description | |
| --- | --- | --- | --- |
| sns\_type | OT\_ISP\_SNS\_I2C\_TYPE | Sensor communicates with ISP via I2C. | |
| OT\_ISP\_SNS\_SSP\_TYPE | Sensor communicates with ISP via SSP. | |
| reg\_num | - | Number of registers to configure when writing exposure results to the sensor. Dynamic modification is not supported. | |
| cfg2\_valid\_delay\_max | - | Maximum number of frames from register configuration to take effect, in frames; used to synchronize sensor and ISP registers. Under normal circumstances the exposure time register has the longest delay (1–2 frames), so the typical value is 1 or 2. | |
| exp\_distance | - | In WDR mode: line difference between the long and medium frames, the medium and short frames, and the short and ultra-short frames. | |
| com\_bus | i2c\_dev | I2C device number bound to the sensor. | |
| ssp\_dev | SPI device number struct bound to the sensor. | |
| bit4\_ssp\_dev | SPI device number bound to the sensor. |
| bit4\_ssp\_cs | SPI chip-select signal bound to the sensor. |
| i2c\_data | update | TD\_TRUE: data will be written to the sensor registers; TD\_FALSE: data will not be written to the sensor registers. | |
| delay\_frame\_num | Number of frames the sensor register configuration is delayed. This variable ensures that exposure time and gain take effect simultaneously. | |
| interrupt\_pos | Position at which the sensor register configuration takes effect. - 0x0: at the ultra-short frame start interrupt; 0x1: at the ultra-short frame end interrupt. - 0x10: at the short frame start interrupt; 0x11: at the short frame end interrupt. - 0x20: at the medium frame start interrupt; 0x21: at the medium frame end interrupt. - 0x30: at the long frame start interrupt; 0x31: at the long frame end interrupt. | |
| dev\_addr | Sensor device address. | |
| reg\_addr | Sensor register address. | |
| addr\_byte\_num | Sensor register address bit width. | |
| data | Sensor register data. | |
| data\_byte\_num | Sensor register data bit width. | |
| ssp\_data | update | TD\_TRUE: data will be written to the sensor registers; TD\_FALSE: data will not be written to the sensor registers. | |
| delay\_frame\_num | Number of frames the sensor register configuration is delayed. This variable ensures that exposure time and gain take effect simultaneously. | |
| interrupt\_pos | Position at which the sensor register configuration takes effect. - 0x0: at the frame start interrupt; 0x1: at the AF interrupt. - 0x10: at the short frame start interrupt; 0x11: at the short frame end interrupt. - 0x20: at the medium frame start interrupt; 0x21: at the medium frame end interrupt. - 0x30: at the long frame start interrupt; 0x31: at the long frame end interrupt. | |
| dev\_addr | Sensor device address. | |
| dev\_addr\_byte\_num | Sensor device address bit width. | |
| reg\_addr | Sensor register address. | |
| reg\_addr\_byte\_num | Sensor register address bit width. | |
| data | Sensor register data. | |
| data\_byte\_num | Sensor register data bit width. | |
| slv\_sync | update | TD\_TRUE: data will be written to the sensor registers; TD\_FALSE: data will not be written to the sensor registers. | |
| delay\_frame\_num | Number of frames the sensor register configuration is delayed. This variable ensures that exposure time and gain take effect simultaneously. | |
| slave\_vs\_time | XVS signal period, unit: sensor input clock cycles. | |
| slave\_bind\_dev | Binding relationship between the slave device number and vi\_pipe. | |
| config | -- | Sensor register data configuration completion flag. - TD\_TRUE: configuration complete. - TD\_FALSE: not yet configured. | |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_sensor\_exp\_func](#ot_isp_sensor_exp_func) ### ot\_isp\_3a\_alg\_lib **Description** Defines the AE/AWB algorithm library struct. **Definition** `typedef struct { td_s32 id; ot_char lib_name[ALG_LIB_NAME_SIZE_MAX];
} ot_isp_3a_alg_lib;` **Members**

| Member Name | Description |
| --- | --- |
| id | ID of the algorithm library instance. |
| lib\_name | Character array identifying the algorithm library name. |

**Precautions** The library name lib\_name distinguishes different algorithm libraries; the library id supports running multiple instances of the same algorithm library. **Related Data Types and Interfaces** None ### ot\_isp\_bind\_attr **Description** Defines the struct for the binding relationship between the ISP library, sensor, and 3A libraries. **Definition** `typedef struct { ot_sensor_id sensor_id; ot_isp_3a_alg_lib ae_lib; ot_isp_3a_alg_lib af_lib; ot_isp_3a_alg_lib awb_lib;
} ot_isp_bind_attr;` **Members**

| Member Name | Description |
| --- | --- |
| sensor\_id | Sensor ID. |
| ae\_lib | AE library struct. |
| af\_lib | AF library struct. |
| awb\_lib | AWB library struct. |

**Precautions** None **Related Data Types and Interfaces** None ### ot\_isp\_ctrl\_proc\_write **Description** Defines the ISP PROC information. **Definition** `typedef struct { ot_char *proc_buff; td_u32 buff_len; td_u32 write_len;
} ot_isp_ctrl_proc_write;` **Members**

| Member Name | Description |
| --- | --- |
| proc\_buff | Pointer to the PROC information buffer passed from ISP to the current algorithm. |
| buff\_len | Remaining bytes in the PROC information buffer passed from ISP to the current algorithm. Total buffer size is 8 KB. |
| write\_len | Number of bytes of PROC information passed from the current algorithm to the ISP. |

**Precautions** This interface is only relevant when the user is using a custom 3A algorithm and needs to support the proc information feature for that algorithm. **Related Data Types and Interfaces** None ### ot\_isp\_ctrl\_cmd **Description** Defines the ISP control commands for 3A algorithms. **Definition** `typedef enum { OT_ISP_WDR_MODE_SET = 8000, OT_ISP_PROC_WRITE, OT_ISP_AE_FPS_BASE_SET, OT_ISP_AE_BLC_SET, OT_ISP_AE_RC_SET, OT_ISP_AE_BAYER_FORMAT_SET, OT_ISP_AE_INIT_INFO_GET, OT_ISP_AWB_ISO_SET, OT_ISP_CHANGE_IMAGE_MODE_SET, OT_ISP_UPDATE_INFO_GET, OT_ISP_FRAMEINFO_GET, OT_ISP_ATTACHINFO_GET, OT_ISP_COLORGAMUTINFO_GET, OT_ISP_AWB_INTTIME_SET, OT_ISP_BAS_MODE_SET, OT_ISP_PROTRIGGER_SET, OT_ISP_AWB_PIRIS_SET, OT_ISP_AWB_SNAP_MODE_SET, OT_ISP_AWB_ZONE_ROW_SET, OT_ISP_AWB_ZONE_COL_SET, OT_ISP_AWB_ZONE_BIN_SET, OT_ISP_AWB_ERR_GET, OT_ISP_CTRL_CMD_BUTT,
} ot_isp_ctrl_cmd;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_WDR\_MODE\_SET | Set the WDR mode; configures the ISP control unit WDR mode into the algorithm module. The corresponding parameter type for this command is ot\_wdr\_mode. |
| OT\_ISP\_PROC\_WRITE | Set PROC write; configures the algorithm module PROC information into the ISP control unit. The corresponding parameter type is ot\_isp\_ctrl\_proc\_write. |
| OT\_ISP\_AE\_FPS\_BASE\_SET | Set the frame rate; configures the ISP control unit frame rate into the AE algorithm module. The corresponding parameter matches frame\_rate in ot\_isp\_pub\_attr. |
| OT\_ISP\_AE\_BLC\_SET | Set the black level; configures the black level information into the AE algorithm module. |
| OT\_ISP\_AE\_RC\_SET | Set RC module enable; passes the Radial Crop module enable status into the AE algorithm module. |
| OT\_ISP\_AE\_BAYER\_FORMAT\_SET | Set the Bayer image data format; passes the Bayer image data format into the AE algorithm module. |
| OT\_ISP\_AWB\_ISO\_SET | Set the ISO value; configures the current AE ISO value into the AWB module for automatic saturation adjustment. The corresponding parameter matches iso in ot\_isp\_ae\_result. |
| OT\_ISP\_CHANGE\_IMAGE\_MODE\_SET | Set the image resolution switch flag; configures the ISP resolution switch indicator into the algorithm module. Parameter type is td\_u8; 0 means resolution has not changed, any other value means it has changed. |
| OT\_ISP\_UPDATE\_INFO\_GET | Update AE and AWB status information; retrieves runtime status including AE and AWB state. |
| OT\_ISP\_FRAMEINFO\_GET | Get ISP frame information including ISO and noise reduction strength; used in conjunction with the encoding module. |
| OT\_ISP\_ATTACOTNFO\_GET | Get ISP frame extra information including ISO and per-module algorithm parameters. |
| OT\_ISP\_COLORGAMUTINFO\_GET | Get the channel color gamut attributes. |
| OT\_ISP\_AWB\_INTTIME\_SET | Set the exposure value; configures the current AE exposure value into the AWB module for indoor/outdoor detection. The corresponding parameter matches int\_time in ot\_isp\_ae\_result. |
| OT\_ISP\_BAS\_MODE\_SET | Set the BAS mode. |
| OT\_ISP\_PROTRIGGER\_SET | Professional capture trigger signal setting. When the user triggers a professional capture, ISP sends this signal to AE and AE starts professional exposure control. Note: not supported in this version. |
| OT\_ISP\_AWB\_PIRIS\_SET | Set the gain information for P-iris operation; used to get the current P-iris actual status. |
| OT\_ISP\_AWB\_SNAP\_MODE\_SET | Set whether the current mode is snapshot mode; configures the snapshot mode status into the AWB module. |
| OT\_ISP\_AWB\_ZONE\_ROW\_SET | Set the number of rows for AWB zone statistics. Stitching, cropping, and similar operations may cause the row count to vary; the row count must be configured into the AWB module. |
| OT\_ISP\_AWB\_ZONE\_COL\_SET | Set the number of columns for AWB zone statistics. Stitching, cropping, and similar operations may cause the column count to vary; the column count must be configured into the AWB module. |
| OT\_ISP\_AWB\_ZONE\_BIN\_SET | Set the number of luminance bins for AWB zone statistics. |

**Precautions** None **Related Data Types and Interfaces** None ### ot\_isp\_stitch\_attr **Description** Defines the ISP stitching struct. **Definition** `typedef struct { td_bool stitch_enable; td_bool main_pipe; td_u8 stitch_pipe_num; td_s8 stitch_bind_id[OT_VI_MAX_PIPE_NUM];
} ot_isp_stitch_attr;` **Members**

| Member Name | Description |
| --- | --- |
| stitch\_enable | Stitch enable. |
| main\_pipe | Whether this is the main pipe. |
| stitch\_pipe\_num | Total number of stitched pipes. |
| stitch\_bind\_id | Pipe numbers bound for stitching. For OT\_VI\_MAX\_PIPE\_NUM details, see the “Video Input” chapter of the MPP Media Processing Software V5.0 Development Reference. |

**Precautions** None. **Related Data Types and Interfaces** None. ### ot\_isp\_ae\_register **Description** Defines the AE registration struct. **Definition** `typedef struct { ot_isp_ae_exp_func ae_exp_func;
} ot_isp_ae_register;` **Members**

| Member Name | Description |
| --- | --- |
| ae\_exp\_func | Callback function struct for AE registration. |

**Precautions** This wrapper exists for extensibility. **Related Data Types and Interfaces** None ### ot\_isp\_ae\_exp\_func **Description** Defines the AE callback function struct. **Definition** `typedef struct { td_s32 (*pfn_ae_init)(td_s32 handle, const ot_isp_ae_param *ae_param); td_s32 (*pfn_ae_run)(td_s32 handle, const ot_isp_ae_info *ae_info, ot_isp_ae_result *ae_result, td_s32 reserved); td_s32 (*pfn_ae_ctrl)(td_s32 handle, td_u32 cmd, ot_void *value); td_s32 (*pfn_ae_exit)(td_s32 handle);
} ot_isp_ae_exp_func;` **Members**

| Member Name | Description |
| --- | --- |
| pfn\_ae\_init | Callback function pointer for AE initialization. |
| pfn\_ae\_run | Callback function pointer for AE execution. |
| pfn\_ae\_ctrl | Callback function pointer for controlling AE internal state. |
| pfn\_ae\_exit | Callback function pointer for AE destruction. |

**Precautions** - When calling [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), the pfn\_ae\_init callback is invoked to initialize the AE algorithm library.
- When calling [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164), the pfn\_ae\_run callback is invoked to run the AE algorithm library and compute the sensor exposure time, gain, and ISP digital gain.
- In the design approach, the algorithm library implements a ctrl interface to change internal operating state. The ctrl interface provides a command for parameter transfer and a VOID-type pointer for data transfer. On one hand, the ctrl interface is registered with the ISP library as a callback function pointer, allowing the ISP control unit to implicitly call commands to control the algorithm library's internal state. On the other hand, it also serves as a user-facing interface, enabling users to change the algorithm library's internal operating state. Example: `td_s32 ae_ctrl_cmd(td_s32 handle, td_u32 cmd, ot_void *value) { ae_check_pointer_return(value); switch (cmd) { case OT_ISP_WDR_MODE_SET: …… break; …… } return TD_SUCCESS; }` At runtime, the ISP control unit implicitly calls the pfn\_ae\_ctrl callback to notify the AE algorithm library to switch between WDR and linear modes, set the FPS, and notify sensor configuration. For details on the ctrl commands defined by the current firmware, see [ot\_isp\_ctrl\_cmd](#ZH-CN_TOPIC_0000002470924852). - When calling [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923), the pfn\_ae\_exit callback is invoked to destroy the AE algorithm library.
- An algorithm library supports initializing and running multiple instances; the handle parameter distinguishes different library instances. To support multiple instances, register the library multiple times with different alg\_lib.id values. Example: `ot_isp_3a_alg_lib ae_lib; ae_lib.id = 0; ot_vi_pipe vi_pipe = 0; strncpy(ae_lib.lib_name, OT_AE_LIB_NAME, sizeof(OT_AE_LIB_NAME)); ss_mpi_ae_register(vi_pipe,&ae_lib); ae_lib.id = 1; ss_mpi_ae_register(vi_pipe,&ae_lib);` **Related Data Types and Interfaces** [ot\_isp\_ae\_register](#ot_isp_ae_register) ### ot\_isp\_ae\_param **Description** Defines the initialization parameter struct that ISP provides to AE. **Definition** `typedef struct { ot_sensor_id sensor_id; td_u8 wdr_mode; td_u8 hdr_mode; td_u16 black_level; ot_float fps; ot_isp_bayer_format bayer; ot_isp_stitch_attr stitch_attr; td_s32 reserved;
} ot_isp_ae_param;` **Members**

| Member Name | Description |
| --- | --- |
| sensor\_id | ID of the sensor registered with ISP; used to verify that the sensor registered with ISP and the sensor registered with AE are consistent. |
| wdr\_mode | WDR mode; ISP provides WDR mode information to AE. |
| hdr\_mode | HDR mode; ISP provides HDR mode information to AE. Not supported. |
| black\_level | Black level value with 12-bit precision; ISP provides black level information to AE. |
| fps | Frame rate; ISP provides frame rate information to AE. |
| bayer | Sensor Bayer pattern; includes RGGB, GRBG, GBRG, and BGGR formats. |
| stitch\_attr | Stitch mode; ISP provides stitch mode information to AE. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_ae\_exp\_func](#ot_isp_ae_exp_func) ### ot\_isp\_people\_roi **Description** Defines the human/face statistics struct that ISP provides to AE. **Definition** `typedef struct { td_bool enable; td_bool available; td_u8 luma ;
} ot_isp_people_roi;` **Members**

| Member Name | Description |
| --- | --- |
| enable | Whether the model is enabled. |
| available | Whether the model has available detection results. |
| luma | Overall luminance of the model detection result. Valid range: [0x0, 0x FF] |

**Precautions** - When only the human silhouette model is available, a face luminance is estimated from the silhouette detection result; this estimate is less reliable than a direct face detection result.
- luma is the average Y-component luminance within the detected face or human silhouette bounding box in the YUV image. When using custom intelligence data with multiple face or silhouette detections, it is recommended to average the overall luminance across all detections. **Related Data Types and Interfaces** [ot\_isp\_ae\_info](#ot_isp_ae_info) ### ot\_isp\_tunnel\_roi **Description** Defines the tunnel statistics struct that ISP provides to AE. **Definition** `typedef struct { td_bool enable; td_bool available; td_u32 tunnel_area_ratio; td_u32 tunnel_exp_perf;
} ot_isp_tunnel_roi;` **Members**

| Member Name | Description |
| --- | --- |
| enable | Whether the model is enabled. |
| available | Whether the model has available detection results. |
| tunnel\_area\_ratio | Area ratio of the model detection result relative to the frame. Valid range: [0, 10000] |
| tunnel\_exp\_perf | Exposure performance of the model detection result. Valid range: [0, 10000] |

**Precautions** - tunnel\_exp\_perf is currently used only for the tunnel exit; it represents the ratio of overexposed area within the detected tunnel exit bounding box to the entire bounding box, measured in the YUV image.
- Passing tunnel detection results to AE enables maximum light control when entering or exiting tunnels in driving scenarios. This feature is only supported in WDR mode, and the exposure ratio must be set to auto mode. Use in linear mode is not recommended; results are not guaranteed. **Related Data Types and Interfaces** [ot\_isp\_ae\_info](#ot_isp_ae_info) ### ot\_isp\_face\_roi **Description** Defines the face fast-convergence algorithm struct that ISP provides to AE. **Definition** `typedef struct { td_bool enable; td_bool available; td_u64 frame_pts; ot_rect face_rect[OT_ISP_FACE_NUM];
} ot_isp_face_roi;` **Members**

| Member Name | Description |
| --- | --- |
| enable | Whether the face fast-convergence algorithm is enabled. |
| available | Whether a face has been detected. |
| frame\_pts | Timestamp of the frame in which the face was detected. |
| face\_rect | Array of face coordinate information. A maximum of 5 face coordinates are supported. For coordinate details, see [ot\_rect](#ot_rect). |

**Precautions** - ot\_isp\_face\_roi supports input of face model detection coordinates; width and height in face\_rect do not need to be 4-aligned. The AE algorithm uses the face coordinates and the corresponding frame PTS for fast convergence. Both enable here and enable in ot\_isp\_fast\_face\_ae\_attr must be set for the algorithm to take effect.
- A maximum of 5 faces are supported. When fewer than 5 faces are detected, the remaining entries in the face\_rect array must be set to 0. - The face fast-convergence algorithm is only supported for close-range use, where the face occupies a large portion of the image. If the face occupies a small area, image flickering may occur. It is recommended that the input face coordinates cover a reasonably large portion of the frame. **Related Data Types and Interfaces** [ot\_isp\_ae\_info](#ot_isp_ae_info) ### ot\_isp\_people\_type **Description** Defines the human/face statistics enum type that ISP provides to AE. **Definition** `typedef enum { OT_ISP_FACE_INDEX = 0, OT_ISP_PEOPLE_INDEX = 1, OT_ISP_PEOPLE_BUTT
} ot_isp_people_type;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_FACE\_INDEX | Face type. |
| OT\_ISP\_PEOPLE\_INDEX | Human silhouette type. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_ae\_info](#ot_isp_ae_info) ### ot\_isp\_tunnel\_type **Description** Defines the tunnel statistics enum type that ISP provides to AE. **Definition** `typedef enum { OT_ISP_TUNNEL_IN_INDEX = 0, OT_ISP_TUNNEL_OUT_INDEX = 1, OT_ISP_TUNNEL_BUTT
} ot_isp_tunnel_type;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_TUNNEL\_IN\_INDEX | Tunnel entrance type. |
| OT\_ISP\_TUNNEL\_OUT\_INDEX | Tunnel exit type. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_ae\_info](#ot_isp_ae_info) ### ot\_isp\_smart\_info **Description** Defines the smart information struct that ISP provides to AE. **Definition** `typedef struct { ot_isp_people_roi people_roi[OT_ISP_PEOPLE_CLASS_MAX]; ot_isp_tunnel_roi tunnel_roi[OT_ISP_TUNNEL_CLASS_MAX]; ot_isp_face_roi face_roi;
} ot_isp_smart_info;` **Members**

| Member Name | Description |
| --- | --- |
| people\_roi | Model detection results for human silhouettes and faces. |
| tunnel\_roi | Model detection results for tunnel entrances and exits. |
| face\_roi | Face coordinate information and corresponding PTS. |

**Precautions** - people\_roi supports only face model and human silhouette model detection results. people\_roi index 0 is the face detection result; index 1 is the human silhouette detection result.
- tunnel\_roi currently supports tunnel entrance and exit model detection results. tunnel\_roi index 0 is the tunnel entrance detection result; index 1 is the tunnel exit detection result. **Related Data Types and Interfaces** [ot\_isp\_ae\_info](#ot_isp_ae_info) ### ot\_isp\_fe\_ae\_stat\_1 **Description** Defines AE statistics attributes in the ISP FE. **Definition** `typedef struct { td_u32 pixel_count[OT_ISP_WDR_MAX_FRAME_NUM]; td_u32 pixel_weight[OT_ISP_WDR_MAX_FRAME_NUM]; td_u32 histogram_mem_array[OT_ISP_WDR_MAX_FRAME_NUM][OT_ISP_HIST_NUM]; td_u32 histogram_mem_array_ir[OT_ISP_HIST_NUM]; /* only support fe0 */ }ot_isp_fe_ae_stat_1;` **Members** None **Precautions** See [ot\_isp\_ae\_info](#ZH-CN_TOPIC_0000002470925126) for details. **Related Data Types and Interfaces** None ### ot\_isp\_be\_ae\_stat\_1 **Description** Defines AE statistics attributes in the ISP BE. **Definition** `typedef struct { td_u32 pixel_count; td_u32 pixel_weight; td_u32 histogram_mem_array[OT_ISP_HIST_NUM]; td_u32 estimate_histogram_mem_array[OT_ISP_HIST_NUM];
} ot_isp_be_ae_stat_1;` **Members** None **Precautions** See [ot\_isp\_ae\_info](#ZH-CN_TOPIC_0000002470925126) for details. **Related Data Types and Interfaces** None ### ot\_isp\_ae\_info **Description** Defines the statistics struct that ISP provides to AE. **Definition** `typedef struct { td_u32 frame_cnt; /* the counting of frame */ td_u64 frame_pts; td_u16 frame_width; td_u16 frame_height; ot_isp_smart_info smart_info; /* not support */ ot_isp_fe_ae_stat_1 *fe_ae_stat1; ot_isp_fe_ae_stat_2 *fe_ae_stat2; ot_isp_fe_ae_stat_3 *fe_ae_stat3; ot_isp_fe_ae_stitch_stat_3 *fe_ae_sti_stat; ot_isp_be_ae_stat_1 *be_ae_stat1; ot_isp_be_ae_stat_2 *be_ae_stat2; ot_isp_be_ae_stat_3 *be_ae_stat3; ot_isp_be_ae_stitch_stat_3 *be_ae_sti_stat;
} ot_isp_ae_info;` **Members**

| Member Name | Sub-member Name | Description |
| --- | --- | --- |
| frame\_cnt | - | Cumulative frame count. Valid range: [0, 0x FFFFFFFF] |
| frame\_pts | - | Timestamp of the current raw frame. |
| frame\_width | - | Frame width. |
| frame\_height | - | Frame height. |
| smart\_info | - | See the ot\_isp\_smart\_info interface description. |
| fe\_ae\_stat1 | pixel\_count | Total number of counted pixels. |
| pixel\_weight | Total number of weighted counted pixels. |
| histogram\_mem\_array | 1024-bin histogram statistics array. Valid range: [0, 0x FFFFFFFF] |
| histogram\_mem\_array\_ir | Supported on FE0 only. |
| fe\_ae\_stat2 | global\_avg\_r | Global R channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_gr | Global Gr channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_gb | Global Gb channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_b | Global B channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_ir | Supported on FE0 only. |
| fe\_ae\_stat3 | zone\_avg | Per-zone R/Gr/Gb/B channel averages. Valid range: [0, 0x FFFF] |
| zone\_avg\_ir | Supported on FE0 only. |
| fe\_ae\_sti\_stat | zone\_avg | Post-stitch Per-zone R/Gr/Gb/B channel averages. Valid range: [0, 0x FFFF] Only per-zone averages for pipes participating in stitching are valid; averages for other pipes are invalid. |
| be\_ae\_stat1 | pixel\_count | Total number of counted pixels. |
| pixel\_weight | Total number of weighted counted pixels. |
| histogram\_mem\_array | 1024-bin histogram statistics array. Valid range: [0, 0x FFFFFFFF] |
| estimate\_histogram\_mem\_array | Estimated BE statistics derived from FE statistics; used in scenarios where BE statistics have large latency and BE statistics are required. |
| be\_ae\_stat2 | global\_avg\_r | Global R channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_gr | Global Gr channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_gb | Global Gb channel average. Valid range: [0, 0x FFFF] |
| global\_avg\_b | Global B channel average. Valid range: [0, 0x FFFF] |
| be\_ae\_stat3 | zone\_avg | Per-zone R/Gr/Gb/B channel averages. Valid range: [0, 0x FFFF] |
| be\_ae\_sti\_stat | zone\_avg | Post-stitch Per-zone R/Gr/Gb/B channel averages. Valid range: [0, 0x FFFF] Only per-zone averages for the corresponding stitched pipe are valid; averages for other pipes are invalid. |

**Precautions** - The AE library can control its computation frequency based on frame\_cnt, e.g., running once every two frames.
- fe\_ae\_stat1 and be\_ae\_stat1 are the global 1024-bin histogram statistics at the FE and BE, respectively. These statisticsis obtained by taking the upper 10 bits of the input data stream; each bin value represents the pixel count for that grayscale level. The global 1024-bin histogram is affected by per-zone weights; the sum of all 1024 bins equals the weighted number of pixels participating in the statistics. Currently, the AE algorithm defaults to using only the Gr channel statistics. When a large red area is present, R and Gb channel statistics are used; when a large blue area is present, B and Gr channel statistics are used.
- When the MIPI or VI DEV data\_rate is set to DATA\_RATE\_X2, the pixel\_count and pixel\_weight values in fe\_ae\_stat1 are halved.
- fe\_ae\_stat2 and be\_ae\_stat2 are the global R/Gr/Gb/B four-channel averages at the FE and BE, respectively, computed using the upper 16 bits. Valid range: [0, 0x FFFF]. The global four-channel averages are affected by per-zone weights.
- fe\_ae\_stat3 and be\_ae\_stat3 are the per-zone R/Gr/Gb/B four-channel averages for each of the 15×17 zones at the FE and BE, respectively, using the upper 16 bits. Valid range: [0, 0x FFFF].
- The AE statistics module can apply square-root processing to the input data before statistics are computed. Square-root processing means normalizing the input data to 1 and then taking the square root. For example, with a 1024-bin histogram: if the input data is 12-bit and a pixel value is 2048, with square-root disabled, the upper 10 bits are used for statistics, incrementing the count for the bin corresponding to grayscale 512. With square-root enabled, 2048 normalized to 1 is 0.5; the square root of 0.5 is 0.707, which is 724 in 10-bit representation — the count for the bin corresponding to grayscale 724 is incremented。As a result, after square-root processing, smaller pixel values are noticeably increased, essentially compressing the precision in bright areas to improve precision in dark areas. It is recommended to enable square-root mode in WDR mode and disable it in linear mode. In square-root mode, the statistical precision is 11 bits and the lower 5 bits are 0, so the 16-bit maximum is 0x FFE0. Additionally, the position of the AE statistics module in the ISP pipeline can be changed; refer to the relevant “Statistics” section for details. **Table 1** Default configuration description of ot\_isp\_ae\_info statistics member variables

| Member Name | Primary Statistics | Default Position | Black Level | Weight Table Effect |
| --- | --- | --- | --- | --- |
| fe\_ae\_stat1 | 1024-bin histogram before WDR synthesis | After FE-WB | Not subtracted | Yes |
| fe\_ae\_stat2 | Global average before WDR synthesis | After FE-WB | Not subtracted | Yes |
| fe\_ae\_stat3 | Per-zone average before WDR synthesis | After FE-WB | Not subtracted | No |
| be\_ae\_stat1 | 1024-bin histogram after WDR synthesis | After BE-WB | Subtracted | Yes |
| be\_ae\_stat2 | Global average after WDR synthesis | After BE-WB | Subtracted | Yes |
| be\_ae\_stat3 | Per-zone average after WDR synthesis | After BE-WB | Subtracted | No |

> **Note:** >- The descriptions in the table are valid only under the ISP default configuration; actual behavior is affected by the black level configuration and the AE statistics position.
> - The pre-WDR (FE) statistics are fixed after the WB module, not configurable. When using FE statistics, the black level must be subtracted: subtract the 10-bit black level for histograms and the 16-bit black level for averages.The pre-WDR (FE) statistics are affected by the gain of processing modules preceding the FE AE (in Hi3403V100, these are DG/WB). The FE gain values for these modules are guaranteed by the algorithm internals to be consistent with BE; no separate configuration is needed.
> - In Hi3403V100, the channel-0 FE statistics pass through horizontal downsampling, so the number of points is halved.
> - In linear mode, the pre-WDR (FE) 1024-bin histogram is recommended. In WDR mode, either the pre-WDR (FE) 1024-bin histogram or the post-WDR (BE) 1024-bin histogram with square-root mode is recommended. In offline mode under heavy workloads, the pre-WDR (FE) statistics have better real-time performance, so FE statistics are recommended. The SDK-provided AE algorithm defaults to using BE statistics without square-root mode in linear mode, and BE statistics with square-root mode in WDR mode. Using BE statistics with square-root mode in linear mode, or BE statistics without square-root mode in WDR mode, will cause anomalies in the SDK-provided AE algorithm. **Related Data Types and Interfaces** [ot\_isp\_ae\_exp\_func](#ot_isp_ae_exp_func) ### ot\_isp\_ae\_stat\_attr **Description** Defines the register configuration struct returned by the AE library to the ISP. **Definition** `typedef struct { td_bool change; td_bool hist_adjust; td_u8 ae_be_sel; td_u8 four_plane_mode; td_u8 hist_offset_x; td_u8 hist_offset_y; td_u8 hist_skip_x; td_u8 hist_skip_y; td_bool mode_update; td_u8 hist_mode; td_u8 aver_mode; td_u8 max_gain_mode; td_bool wight_table_update; td_u8 weight_table[OT_ISP_MAX_PIPE_NUM][OT_ISP_AE_ZONE_ROW][OT_ISP_AE_ZONE_COLUMN];
> } ot_isp_ae_stat_attr;` **Members**

| Sub-member Name | Description |
| --- | --- |
| change | Whether the values in this structwhether the register needs to be configured. |
| hist\_adjust | AE histogram adjustment enable; controls the configuration of the six parameters: ae\_be\_sel, four\_plane\_mode, hist\_offset\_x, hist\_offset\_y, hist\_skip\_x, hist\_skip\_y. When hist\_adjust is enabled, the above six parameters take the values from ot\_isp\_ae\_result to configure the chip registers; When hist\_adjust is disabled, the above six parameters take the values from external registers (MPI configuration) to configure the chip registers. |
| ae\_be\_sel | Position of the AE statistics module in the ISP pipeline at the BE; default is 1. The AE statistics module at the FE is fixed after WB and its position cannot be moved. 0：After ISP digital gain； 1：After static WB； 2：After DRC。 |
| four\_plane\_mode | Four-plane mode enable; default is 0. When enabled, the 1024-bin histogram becomes a four-channel 256-bin histogram per BGGR channel. 0: Disabled; 1: Enabled. |
| hist\_skip\_x | Horizontal sampling point setting for histogram statistics. 0 = every pixel; 1 = every 2nd pixel; 2 = every 3rd pixel; 3 = every 4th pixel; 4 = every 5th pixel; 5 = every 8th pixel; 6+ = every 9th pixel. A value of 0 means sample every pixel for statistics; A value of 1 means sample every 2nd pixel, and so on. 0 is only supported when Four Plane Mode is enabled. |
| hist\_skip\_y | Vertical sampling point setting for histogram statistics. 0 = every pixel; 1 = every 2nd pixel; 2 = every 3rd pixel; 3 = every 4th pixel; 4 = every 5th pixel; 5 = every 8th pixel; 6+ = every 9th pixel. |
| hist\_offset\_x | Horizontal starting point setting for histogram statistics. 0: start from the first column; 1: start from the second column. |
| hist\_offset\_y | Vertical starting point setting for histogram statistics. 0: start from the first row; 1: start from the second row. |
| mode\_update | AE square-root mode configuration enable; controls the configuration of the three parameters hist\_mode, aver\_mode, and max\_gain\_mode. When mode\_update is non-zero, the above three parameters take the values from ot\_isp\_ae\_result to configure the logic registers; When mode\_update is 0, the above three parameters take the values from external registers (MPI configuration) to configure the logic registers. |
| hist\_mode | Square-root mode for the global 1024-bin histogram. 0: disabled (no square-root); 1: enabled (square-root). Affects only BE histogram statistics. |
| aver\_mode | Square-root mode for averages. 0: disabled (no square-root); 1: enabled (square-root). Affects only BE average statistics. |
| max\_gain\_mode | Square-root mode for the MG module. 0: disabled (no square-root); 1: enabled (square-root). Affects only MG module statistics. For comparison with AE per-zone statistics, it is recommended to configure the same mode as aver\_mode. |
| wight\_table\_update | AE weight table configuration enable; controls the weight\_table configuration. - When wight\_table\_update is non-zero, the weight table takes values from ot\_isp\_ae\_result to configure the chip registers; - When wight\_table\_update is 0, the weight table takes values from external registers (MPI configuration) to configure the chip registers. |
| weight\_table | AE weight table for the 15×17 zones. Valid range: [0, 15] |

**Precautions** - weight\_table supports configuring multi-channel weights on the main pipe in stitch mode: on the main pipe, assign values to the weight tables corresponding to each branch pipe index. In non-stitch mode, only the weight table for the corresponding pipe index takes effect.
- The SDK-provided AE algorithm only supports the 1024-bin histogram. Enabling four\_plane\_mode while using the AE algorithm will cause the AE algorithm to malfunction. **Related Data Types and Interfaces** [ot\_isp\_ae\_result](#ot_isp_ae_result) ### ot\_isp\_ae\_result **Description** Defines the register configuration struct returned by the AE library to the ISP. **Definition** `typedef struct { td_u32 int_time[4]; td_u32 isp_dgain; td_u32 again; td_u32 dgain; td_u32 iso; td_u32 isp_dgain_sf; td_u32 again_sf; td_u32 dgain_sf; td_u32 iso_sf; td_u8 ae_run_interval; td_bool piris_valid; td_s32 piris_pos; td_u32 piris_gain; td_u32 sns_lhcg_exp_ratio; ot_isp_fswdr_mode fswdr_mode; td_u32 wdr_gain[OT_ISP_WDR_MAX_FRAME_NUM]; td_u32 hmax_times; td_u32 vmax; ot_isp_ae_stat_attr stat_attr; ot_isp_dcf_update_info update_info;
} ot_isp_ae_result;` **Members**

| Member Name | Description |
| --- | --- |
| int\_time | AE-computed exposure time in 1/16 µs units; When converting exposure time from line count to µs, the offset in cmos.c must be taken into account. In linear mode and sensor built-in WDR mode, only int\_time[0] is valid; int\_time[1:3] should be set equal to int\_time[0]. In N-frame synthesis WDR mode, int\_time[0:(N-1)] are valid, with values in ascending order representing the shortest to the longest exposure time and used to calculate the long/short frame exposure ratio; int\_time[(N-1):3] should be set equal to int\_time[(N-1)]. int\_time[0] is also passed to other modules for exposure-time-related inter-module control and affects the AWB result provided by the SDK. This struct must be configured when using the AWB algorithm and multi-frame WDR mode. |
| isp\_dgain | ISP digital gain with 8-bit precision. Must be configured when ISP digital gain is used; set to 0x100 when not used. |
| again | Sensor analog gain with 10-bit precision. Must be configured when the multi-frame WDR algorithm is used; set to 0x400 when not used. |
| dgain | Sensor digital gain with 10-bit precision. Must be configured when the multi-frame WDR algorithm is used; set to 0x400 when not used. |
| iso | AE-computed total gain value. ISO represents the system gain, expressed as a constant 100 multiplied by the gain factor. For example, if the sensor gain is 2× and the ISP gain is 1×, the system ISO is calculated as: 2\*1\*100=200, i.e., the system ISO is 200. All ISO references in this document use this calculation method. This variable affects adaptive ISP effects such as denoising and sharpening;it must be configured. In 2-frame WDR mode, the ISO calculation includes WDR\_GAIN. |
| isp\_dgain\_sf | ISP digital gain for the short frame with 8-bit precision. Must be configured when the WDR algorithm is used; set to 0x400 when not used. |
| again\_sf | Sensor analog gain for the short frame with 10-bit precision. Must be configured when the WDR algorithm is used; set to 0x400 when not used. |
| dgain\_sf | Sensor digital gain for the short frame with 10-bit precision. Must be configured when the WDR algorithm is used; set to 0x400 when not used. |
| iso\_sf | AE-computed total gain for the short frame. In 2-frame WDR mode, the ISO calculation includes WDR\_GAIN. |
| ae\_run\_interval | AE algorithm execution interval. Valid range: [1, 255] 1: AE runs every frame; 2: AE runs once every 2 frames; and so on. It is recommended not to set this value greater than 2, otherwise the AE adjustment speed is affected. In WDR mode, setting this value to 1 is recommended for smoother AE convergence. This variable determines the frame interval for configuring the AE result into the sensor and ISP registers; it must be configured. |
| piris\_valid | Flag indicating whether P-iris is valid. - When TD\_TRUE: the P-iris driver is called back in kernel mode to configure the stepper motor position. - When TD\_FALSE: no callback. - When using the AE algorithm with a P-iris driver and P-iris lens, this must be set to TD\_TRUE. When connecting a non-P-iris lens, set to TD\_FALSE. |
| piris\_pos | P-iris stepper motor position. Valid range depends on the specific P-iris lens. This value must be configured when using a P-iris driver with a P-iris lens. |
| piris\_gain | P-iris aperture equivalent gain. Valid range depends on the specific P-iris lens. Can be used to calculate the equivalent exposure when the P-iris is active, for reference by other modules. When using a non-P-iris lens, it is recommended to set this value to 512. Valid range: [0, 1024] |
| sns\_lhcg\_exp\_ratio | Baseline exposure ratio for LCG+HCG mode. Only effective when the sensor supports LCG+HCG mode. Set to 64 when not used. |
| fswdr\_mode | WDR synthesis mode. 0: normal multi-frame WDR synthesis mode; 1: long-frame mode; 2: automatic long-frame mode. |
| wdr\_gain | Multi-channel digital gain before WDR synthesis with 8-bit precision. Must be configured when using multi-channel ISP digital gain before WDR synthesis; set to 0x100 when not used. |
| hmax\_times | Time for the sensor to read out one line, in ns. |
| vmax | Total number of lines actually active per sensor frame, in lines. |
| stat\_attr | Register configuration struct returned by the AE library to the ISP. |
| update\_info | Used to pass AE-related DCF information; only exposure-related parameters take effect. |

**Precautions** - The ISP base algorithm modules adjust their configuration parameters based on the total gain computed by AE, e.g., sharpening and denoising.
- weight\_table supports configuring multi-channel weights on the main pipe in stitch mode: on the main pipe, assign values to the weight tables corresponding to each branch pipe index. In non-stitch mode, only the weight table for the corresponding pipe index takes effect.
- When converting the exposure time int\_time from line count to µs, use lines\_per500ms in cmos.c. The conversion relationship is as follows: int\_time[0] =(((td\_u64)int\_time\_rst[0] \* 1024 - offset) \* 500000 / ae\_sns\_dft->lines\_per500ms) >> 10 In the formula above, int\_time\_rst[0] is the exposure time in lines, offset = offset \* 1024, where offset is the exposure time offset; see the description of ot\_isp\_ae\_accuracy. - To ensure exposure ratio accuracy, the exposure time precision in int\_time is 1/16 µs. When computing the exposure time, left-shift by 4 bits after converting to µs; otherwise, the exposure ratio calculation may have errors and the exposure time obtained by other modules will be too small.
- When using a non-AE algorithm, the parameters int\_time, isp\_dgain, again, dgain, iso, hmax\_times, and vmax must be configured; otherwise, the inter-module control will be affected. Other parameters may be configured as needed. **Related Data Types and Interfaces** [ot\_isp\_ae\_exp\_func](#ot_isp_ae_exp_func) ### ot\_isp\_awb\_register **Description** Defines the AWB registration struct. **Definition** `typedef struct { ot_isp_awb_exp_func awb_exp_func;
} ot_isp_awb_register;` **Members**

| Member Name | Description |
| --- | --- |
| awb\_exp\_func | Callback function struct for AWB registration. |

**Precautions** This wrapper exists for extensibility. **Related Data Types and Interfaces** [ot\_isp\_awb\_exp\_func](#ot_isp_awb_exp_func) ### ot\_isp\_awb\_exp\_func **Description** Defines the AWB callback function struct. **Definition** `typedef struct { td_s32 (*pfn_awb_init)(td_s32 handle, const ot_isp_awb_param *awb_param, ot_isp_awb_result *awb_result); td_s32 (*pfn_awb_run)(td_s32 handle, const ot_isp_awb_info *awb_info, ot_isp_awb_result *awb_result, td_s32 reserved); td_s32 (*pfn_awb_ctrl)(td_s32 handle, td_u32 cmd, ot_void *value); td_s32 (*pfn_awb_exit)(td_s32 handle);
} ot_isp_awb_exp_func;` **Members**

| Member Name | Description |
| --- | --- |
| pfn\_awb\_init | Callback function pointer for AWB initialization. |
| pfn\_awb\_run | Callback function pointer for AWB execution. |
| pfn\_awb\_ctrl | Callback function pointer for controlling AWB internal state. |
| pfn\_awb\_exit | Callback function pointer for AWB destruction. |

**Precautions** - When calling [ss\_mpi\_isp\_init](#ZH-CN_TOPIC_0000002471085190), the pfn\_awb\_init callback is invoked to initialize the AWB algorithm library.
- The [ot\_isp\_awb\_result](#ZH-CN_TOPIC_0000002503964823) parameter of the pfn\_awb\_init callback returns the initial AWB gains and initial color correction matrix at ISP startup.
- When calling [ss\_mpi\_isp\_run](#ZH-CN_TOPIC_0000002470925164), the pfn\_awb\_run callback is invoked to run the AWB algorithm library and compute the white balance gains and color correction matrix.
- At runtime, the ISP control unit implicitly calls the pfn\_awb\_ctrl callback to notify the AWB algorithm library to switch between WDR and linear modes, set ISO, and set the exposure time (unit: µs). The purpose of setting ISO is to achieve ISO-saturation linkage since higher gain results in greater chroma noise requiring saturation adjustment. The purpose of setting exposure time is to assist with indoor/outdoor detection. For detailed descriptions of the ctrl commands defined by the current firmware, see [ot\_isp\_ctrl\_cmd](#ZH-CN_TOPIC_0000002470924852). - When calling [ss\_mpi\_isp\_exit](#ZH-CN_TOPIC_0000002503964923), the pfn\_awb\_exit callback is invoked to destroy the AWB algorithm library. **Related Data Types and Interfaces** [ot\_isp\_awb\_register](#ot_isp_awb_register) ### ot\_isp\_awb\_param **Description** Defines the initialization parameter struct that ISP provides to AWB. **Definition** `typedef struct { ot_sensor_id sensor_id; td_u8 wdr_mode; td_u8 awb_zone_row; td_u8 awb_zone_col; td_u8 awb_zone_bin; ot_isp_stitch_attr stitch_attr; td_u16 awb_width; td_u16 awb_height; td_u32 init_iso; td_s8 reserved;
} ot_isp_awb_param;` **Members**

| Member Name | Description |
| --- | --- |
| sensor\_id | ID of the sensor registered with ISP; used to verify that the sensor registered with ISP and the sensor registered with AWB are consistent. |
| wdr\_mode | WDR mode; ISP provides WDR mode information to AWB. |
| awb\_zone\_row | Number of rows in the AWB statistics result. |
| awb\_zone\_col | Number of columns in the AWB statistics result. |
| awb\_zone\_bin | Number of luminance bins in the AWB statistics result. |
| stitch\_attr | Stitching information struct. |
| awb\_width | Image width passed by firmware to the AWB algorithm library. |
| awb\_height | Image height passed by firmware to the AWB algorithm library. |
| init\_iso | AE exposure ISO value passed by firmware to the AWB algorithm library. |
| reserved | Reserved parameter. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_awb\_exp\_func](#ot_isp_awb_exp_func) ### ot\_isp\_awb\_stat\_1 **Description** Defines the AWB statistics struct. **Definition** `typedef struct { td_u16 metering_awb_avg_r; td_u16 metering_awb_avg_g; td_u16 metering_awb_avg_b; td_u16 metering_awb_count_all;
} ot_isp_awb_stat_1;` **Members**

| Member Name | Description |
| --- | --- |
| metering\_awb\_avg\_r | R-channel average of white points in Bayer-domain global statistics. R channel average. Valid range: [0, 0x FFFF]. |
| metering\_awb\_avg\_g | G-channel average of white points in Bayer-domain global statistics. G channel average. Valid range: [0, 0x FFFF]. |
| metering\_awb\_avg\_b | B-channel average of white points in Bayer-domain global statistics. B channel average. Valid range: [0, 0x FFFF]. |
| metering\_awb\_count\_all | Number of white points in Bayer-domain global statistics. Normalized. White point count. Valid range: [0, 0x FFFF]. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_awb\_info](#ot_isp_awb_info) ### ot\_isp\_awb\_stat\_result **Description** Defines the AWB statistics struct. **Definition** `typedef struct { td_u16 *zone_avg_r; td_u16 *zone_avg_g; td_u16 *zone_avg_b; td_u16 *zone_count;
} ot_isp_awb_stat_result;` **Members**

| Member Name | Description |
| --- | --- |
| \*zone\_avg\_r | Start address of the R-channel average array for white points in Bayer-domain per-zone statistics. R channel average. Valid range: [0, 0x FFFF]. |
| \*zone\_avg\_g | Start address of the G-channel average array for white points in Bayer-domain per-zone statistics. G channel average. Valid range: [0, 0x FFFF]. |
| \*zone\_avg\_b | Start address of the B-channel average array for white points in Bayer-domain per-zone statistics. B channel average. Valid range: [0, 0x FFFF]. |
| \*zone\_count | Start address of the white point count array in Bayer-domain per-zone statistics. Normalized. White point count. Valid range: [0, 0x FFFF]. |

**Precautions** None **Related Data Types and Interfaces** [ot\_isp\_awb\_info](#ot_isp_awb_info) ### ot\_isp\_awb\_info **Description** Defines the statistics struct that ISP provides to AWB. **Definition** `typedef struct { td_u32 frame_cnt; ot_isp_awb_stat_1 *awb_stat1; ot_isp_awb_stat_result awb_stat2; td_u8 awb_gain_switch; td_u8 awb_stat_switch; td_bool wb_gain_in_sensor; td_u32 wdr_wb_gain[OT_ISP_BAYER_CHN_NUM];
} ot_isp_awb_info;` **Members**

| Member Name | Description |
| --- | --- |
| frame\_cnt | Cumulative frame count. Valid range: [0, 0x FFFFFFFF] |
| \*awb\_stat1 | Awbstatistics1 |
| awb\_stat2 | Awbstatistics2 |
| awb\_gain\_switch | Position of white balance gain in the ISP. Valid range: [0, 1]. 0: WB gain configured at DG1 before WDR synthesis. 1: WB gain configured at WB. Hi3403V100 does not support configuring WB gain at DG1 for now. |
| awb\_stat\_switch | Position of the white balance statistics module in the ISP. Valid range: [0, 1, 2]. 0: WB statistics module after DG. 1: WB statistics module after EXPANDER. 2: WB statistics module after DRC. Hi3403V100 does not support configuring the WB statistics module after EXPANDER for now. |
| wb\_gain\_in\_sensor | Whether the white balance gain is configured in the sensor. Valid range: [0, 1]. 0: WB gain configured in ISP. 1: WB gain configured in sensor. Hi3403V100 does not support configuring WB gain in sensor for now. |
| wdr\_wb\_gain[-] | White balance gain value configured at DG1 before WDR synthesis. |

**Precautions** - The AWB library can control its computation frequency based on frame\_cnt, e.g., running once every two frames.
<a name="ZH-CN_TOPIC_0000001175137694"></a>- [ot\_isp\_awb\_info](#ZH-CN_TOPIC_0000001175137694)provides both global and per-zone statistics. The number of horizontal and vertical zones varies by mode; they can be obtained from the awb\_zone\_row and awb\_zone\_col parameters in [ot\_isp\_awb\_param](#ZH-CN_TOPIC_0000002503965117). The number of AWB zones = awb\_zone\_row \* awb\_zone\_col.
- Switching the WB statistics module position causes 2 frames of incorrect statistics. It is recommended to configure a reasonable value at startup to avoid switching. If switching is unavoidable, freeze the AWB algorithm for at least 2 frames after switching, then recompute once the statistics are correct.
- In non-stitch mode, configuring the WB statistics module after DRC via ss\_mpi\_isp\_set\_stats\_cfg and disabling the luminance effect on WB weights via ss\_mpi\_isp\_set\_wb\_attr can improve the reddish dark area issue in WDR mode. In stitch mode, adjusting the statistics module position is not supported; it is recommended to fix the statistics module after DG. **Related Data Types and Interfaces** [ot\_isp\_awb\_exp\_func](#ot_isp_awb_exp_func) ### ot\_isp\_awb\_raw\_stat\_attr **Description** Defines the AWB Bayer-domain statistics struct. **Definition** `typedef struct { td_bool stat_cfg_update; td_u16 metering_white_level_awb; td_u16 metering_black_level_awb; td_u16 metering_cr_ref_max_awb; td_u16 metering_cb_ref_max_awb; td_u16 metering_cr_ref_min_awb; td_u16 metering_cb_ref_min_awb;
} ot_isp_awb_raw_stat_attr;` **Members**

| Member Name | Description |
| --- | --- |
| stat\_cfg\_update | Whether the values in this structwhether the register needs to be configured. |
| metering\_white\_level\_awb | Upper luminance limit for finding white points in Bayer-domain statistics. Valid range: [0x0, 0x FFFF]，Default value0x FFFF。 |
| metering\_black\_level\_awb | Lower luminance limit for finding white points in Bayer-domain statistics. Valid range: [0x0, metering\_white\_level\_awb]，Default value0x0。 |
| metering\_cr\_ref\_max\_awb | Maximum R/G chromaticity for finding white points in Bayer-domain statistics, 8-bit precision, valid range: [0x0, 0x FFF]，Default value512。 |
| metering\_cb\_ref\_max\_awb | Maximum B/G chromaticity for finding white points in Bayer-domain statistics, 8-bit precision, valid range: [0x0, 0x FFF]，Default value512。 |
| metering\_cr\_ref\_min\_awb | Minimum R/G chromaticity for finding white points in Bayer-domain statistics, 8-bit precision, valid range: [0x0, metering\_cr\_ref\_max\_awb]，Default value128。 |
| metering\_cb\_ref\_min\_awb | Minimum B/G chromaticity for finding white points in Bayer-domain statistics, 8-bit precision, valid range: [0x0, metering\_cb\_ref\_max\_awb]，Default value128。 |

<a name="ZH-CN_TOPIC_0000001174819192"></a>**Figure 1** White region selection parameters **Precautions** - The information in [ot\_isp\_awb\_raw\_stat\_attr](#ZH-CN_TOPIC_0000001174819192) determines which pixels are considered white points and thus participate in statistics. When developing a new AWB algorithm, the default values can be used, or custom configurations can be set. The stat\_cfg\_update flag indicates whether the current frame needs the stat\_attr struct values to be written to the registers at runtime.
- Only Bayer-domain statistics are supported. **Related Data Types and Interfaces** None ### ot\_isp\_awb\_result **Description** Defines the register configuration struct returned by the AWB library to the ISP. **Definition** `typedef struct { td_u32 white_balance_gain[OT_ISP_BAYER_CHN_NUM]; td_u16 color_matrix[OT_ISP_CCM_MATRIX_SIZE]; td_u32 color_temp; td_u8 saturation; ot_isp_awb_raw_stat_attr raw_stat_attr;
} ot_isp_awb_result;` **Members**

| Member Name | Description |
| --- | --- |
| white\_balance\_gain[[OT\_ISP\_BAYER\_CHN\_NUM](#OT_ISP_BAYER_CHN_NUM)] | R, Gr, Gb, B color channel gains computed by the white balance algorithm; represented with 16-bit precision. Valid range: [0x10000, 0x FFF00] |
| color\_matrix[[OT\_ISP\_CCM\_MATRIX\_SIZE](#OT_ISP_CCM_MATRIX_SIZE)] | Color restoration matrix; represented with 8-bit precision. |
| color\_temp | Current AWB color temperature. |
| saturation | Current saturation. |
| raw\_stat\_attr | Defines the AWB Bayer-domain statistics struct. |

**Precautions** - The AWB algorithm first computes the R, Gr, Gb, and B color channel gains to correct for white. 16-bit precision means the lower 16 bits are fractional.
- In WDR mode, AWB statistics and gains do not require special handling and are the same as in linear mode.
- The AWB algorithm then computes a 3×3 color correction matrix to restore true colors. 8-bit precision means the lower 8 bits are fractional. **Related Data Types and Interfaces** [ot\_isp\_awb\_exp\_func](#ot_isp_awb_exp_func) ### ot\_isp\_awb\_calibration\_gain **Description** Defines the gain struct output by AWB online calibration. **Definition** `typedef struct { td_u16 avg_r_gain; td_u16 avg_b_gain;
} ot_isp_awb_calibration_gain;` **Members**

| Member Name | Description |
| --- | --- |
| avg\_r\_gain | Rgain value output by AWB online calibration. |
| avg\_b\_gain | Bgain value output by AWB online calibration. |

**Precautions** The Rgain and Bgain values are the averages of Rgain and Bgain from several blocks at the center of the image. **Related Data Types and Interfaces** None ### ot\_isp\_dcf\_const\_info **Description** Defines user-configurable DCF info parameters. **Definition** `typedef struct { td_u8 image_description[OT_DCF_DRSCRIPTION_LENGTH]; td_u8 make[OT_DCF_DRSCRIPTION_LENGTH]; td_u8 model[OT_DCF_DRSCRIPTION_LENGTH]; td_u8 software[OT_DCF_DRSCRIPTION_LENGTH]; td_u8 light_source; td_u32 focal_length; td_u8 scene_type; td_u8 custom_rendered; td_u8 focal_length_in35mm_film; td_u8 scene_capture_type; td_u8 gain_control; td_u8 contrast; td_u8 saturation; td_u8 sharpness; td_u8 metering_mode;
} ot_isp_dcf_const_info;` **Members**

| Member Name | Description |
| --- | --- |
| image\_description | Image description and source; the tool that generated the image. Data format: ASCII string, max 32 characters. |
| make | Manufacturer; the product manufacturer. Data format: ASCII string, max 32 characters. |
| model | Model; the device model. Data format: ASCII string, max 32 characters. |
| software | Software; displays the firmware version. Data format: ASCII string, max 32 characters. |
| light\_source | Light source; indicates the white balance setting. 0: Unknown. 1: Daylight; 2: Fluorescent; 3: Incandescent (tungsten); 4: Flash; 10: Cloudy; 17: Standard Light A; 18: Standard Light B; 19: Standard Light C; 20：D55； 21：D65； 22：D75； 255: Other. |
| focal\_length | Focal length of the lens when the photo was taken, in mm. Upper 16 bits: numerator; lower 16 bits: denominator. |
| scene\_type | Indicates the type of capture scene. Value '0x01' means the image was captured directly by the camera. Not supported for now. |
| custom\_rendered | Custom image processing. 0: Standard; 1: Custom. |
| focal\_length\_in35mm\_film | 35 mm equivalent focal length. 0: this focal length does not exist. |
| scene\_capture\_type | Scene capture type. 0: Standard; 1: Landscape mode; 2: Portrait mode; 3: Night mode. |
| gain\_control | Gain control. 0：None； 1：Low gain up； 2 ：High gain up； 3：Low gain down； 4：High gain down。 |
| contrast | Contrast。 |
| saturation | Saturation。 0: None; 1: Low; 2: High. |
| sharpness | Sharpness. |
| metering\_mode | Metering mode; user-configurable. |

**Precautions** None **Related Data Types and Interfaces** - [ss\_mpi\_isp\_set\_dcf\_info](#ss_mpi_isp_set_dcf_info)
- [ss\_mpi\_isp\_get\_dcf\_info](#ss_mpi_isp_get_dcf_info) ### ot\_isp\_dcf\_update\_info **Description** Defines ISP real-time updated DCF info parameters. **Definition** `typedef struct { td_u32 iso_speed_ratings; td_u32 exposure_time; td_u32 exposure_bias_value; td_u8 exposure_program; td_u32 f_number; td_u32 max_aperture_value; td_u8 exposure_mode; td_u8 white_balance;
} ot_isp_dcf_update_info;` **Members**

| Member Name | Description |
| --- | --- |
| iso\_speed\_ratings | ISO speed. Read-only. |
| exposure\_time | Exposure time (reciprocal of shutter speed), in seconds. Upper 16 bits: numerator; lower 16 bits: denominator. Read-only. |
| exposure\_bias\_value | Exposure compensation at the time of capture, in APEX (EV). Upper 16 bits: numerator; lower 16 bits: denominator. Read-only. |
| exposure\_program | Exposure program used by the camera when capturing. 1: Manual exposure; 2: Normal program AE; 3: Aperture priority AE; 4: Shutter priority AE; 5: Creative program (slow); 6: Action program (high-speed); 7: Portrait mode; 8: Landscape mode. Read-only. |
| f\_number | Aperture value. Upper 16 bits: numerator; lower 16 bits: denominator. Read-only. |
| max\_aperture\_value | Maximum aperture of the lens. Upper 16 bits: numerator; lower 16 bits: denominator. Read-only. |
| exposure\_mode | Exposure mode. 0: Auto exposure; 1: Manual exposure; 2: Auto bracket exposure. Read-only. |
| white\_balance | White balance. 0: Auto white balance; 1: Manual white balance. Read-only. |

**Precautions** None **Related Data Types and Interfaces** - [ss\_mpi\_isp\_set\_dcf\_info](#ss_mpi_isp_set_dcf_info)
- [ss\_mpi\_isp\_get\_dcf\_info](#ss_mpi_isp_get_dcf_info) ### ot\_isp\_dcf\_info **Description** Defines the DCF info parameter struct. **Definition** `typedef struct { ot_isp_dcf_const_info isp_dcf_const_info; ot_isp_dcf_update_info isp_dcf_update_info;
} ot_isp_dcf_info;` **Members**

| Member Name | Description |
| --- | --- |
| isp\_dcf\_const\_info | DCF user-configurable parameters. |
| isp\_dcf\_update\_info | DCF ISP real-time updated parameters. |

**Precautions** None **Related Data Types and Interfaces** - [ss\_mpi\_isp\_set\_dcf\_info](#ss_mpi_isp_set_dcf_info)
- [ss\_mpi\_isp\_get\_dcf\_info](#ss_mpi_isp_get_dcf_info) ### ot\_isp\_pipe\_diff\_mode **Description** Defines the pipe difference mode. **Definition** `typedef enum { OT_ISP_PIPE_DIFF_CALIBRATION_MODE = 0, OT_ISP_PIPE_DIFF_USER_MODE = 1, OT_ISP_PIPE_DIFF_MODE_BUTT
} ot_isp_pipe_diff_mode;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_PIPE\_DIFF\_CALIBRATION\_MODE | Calibration mode. When set to calibration mode, use the calibration results obtained from PQ\_Stitching\_Tool to configure pipe\_diff\_param. In this mode, the configured gain value will affect BE statistics. |
| OT\_ISP\_PIPE\_DIFF\_USER\_MODE | User mode. In user mode, the parameters in pipe\_diff\_param are independent of each other. The configured gain value will not affect AE/AWB/AF statistics after the ISP Dgain module. |

**Precautions** If pipe\_diff\_param has not been calibrated, it is recommended to set it to OT\_ISP\_PIPE\_DIFF\_USER\_MODE and manually adjust offset, gain, and color\_matrix values based on the actual scene to achieve color consistency across stitched channels. **Related Data Types and Interfaces** [ot\_isp\_pipe\_diff\_attr](#ot_isp_pipe_diff_attr) ### ot\_isp\_pipe\_diff\_param **Description** Defines the two-channel ISP difference parameter struct. **Definition** `typedef struct { td_s32 offset[OT_ISP_BAYER_CHN_NUM] td_u32 gain[OT_ISP_BAYER_CHN_NUM]; td_u16 color_matrix[OT_ISP_CCM_MATRIX_SIZE];
} ot_isp_pipe_diff_param;` **Members**

| Member Name | Description |
| --- | --- |
| offset[[OT\_ISP\_BAYER\_CHN\_NUM](#OT_ISP_BAYER_CHN_NUM)] | Multi-channel black level difference offset. Valid range: [-0x3FFF, 0x3FFF] The four values in this array correspond to the R, Gr, Gb, and B channels, respectively. Configuration is based on 14-bit raw data. |
| gain[[OT\_ISP\_BAYER\_CHN\_NUM](#OT_ISP_BAYER_CHN_NUM)] | Multi-channel gain difference ratio with 8-bit fractional precision. Valid range: [0x80, 0x400] The four values in this array correspond to the R, Gr, Gb, and B channels, respectively. |
| color\_matrix[[OT\_ISP\_CCM\_MATRIX\_SIZE](#OT_ISP_CCM_MATRIX_SIZE)] | Multi-channel color correction matrix difference ratio with 8-bit fractional precision. bit 15is the sign bit，0: positive; 1: negative, e.g., 0x8010 represents -16. Valid range: [0x0, 0x FFFF] |

**Precautions** Offset is only valid when ot\_isp\_black\_level\_mode is set to OT\_ISP\_BLACK\_LEVEL\_MODE\_AUTO. **Related Data Types and Interfaces** [ot\_isp\_pipe\_diff\_attr](#ot_isp_pipe_diff_attr) ### ot\_isp\_pipe\_diff\_attr **Description** Defines the two-channel ISP difference attribute struct. **Definition** `typedef struct { ot_isp_pipe_diff_mode mode; ot_isp_pipe_diff_param param;
} ot_isp_pipe_diff_attr;` **Members**

| Member Name | Description |
| --- | --- |
| mode | Pipe difference mode. |
| param | Two-channel ISP difference parameters. |

<a name="ZH-CN_TOPIC_0000001174819194"></a>**Precautions** [ot\_isp\_pipe\_diff\_attr](#ZH-CN_TOPIC_0000001174819194)Primarily used in stitch mode to configure the brightness and color differences of multi-channel images, correcting the differences so that the stitched image has smooth transitions in the blending region. **Related Data Types and Interfaces** None ### ot\_isp\_ob\_stats\_update\_pos **Description** Defines the position for reading OB region statistics. **Definition** `typedef enum { OT_ISP_UPDATE_OB_STATS_FE_FRAME_END = 0, OT_ISP_UPDATE_OB_STATS_FE_FRAME_START = 1, OT_ISP_UPDATE_OB_STATS_BUTT,
} ot_isp_ob_stats_update_pos;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_UPDATE\_OB\_STATS\_FE\_FRAME\_END | Read the current frame OB region statistics at the FE frame end. |
| OT\_ISP\_UPDATE\_OB\_STATS\_FE\_FRAME\_START | Read the previous frame OB region statistics at the FE frame start. |

**Precautions** - OT\_ISP\_UPDATE\_OB\_STATS\_FE\_FRAME\_END reads the current frame dynamic BLC statistics at frame end and configures the black level for each ISP module. The configuration takes effect in the next frame, meaning the dynamic BLC result takes effect one frame later than the AE adjustment.
- OT\_ISP\_UPDATE\_OB\_STATS\_FE\_FRAME\_START reads the previous frame dynamic BLC statistics at frame start and configures the black level for each ISP module. The configuration takes effect in the next frame, meaning the dynamic BLC result takes effect two frames later than the AE adjustment.
- The time interval between a frame end and the next frame start is uncontrollable. Therefore, when reading dynamic BLC at frame end and configuring ISP black level registers, synchronization issues may arise if the computation and configuration cannot be completed in time. **Related Data Types and Interfaces** [ot\_isp\_ctrl\_param](#ot_isp_ctrl_param) ### ot\_isp\_alg\_run\_select **Description** Defines whether to bypass algorithm modules in the ISP BE. **Definition** `typedef enum { OT_ISP_ALG_RUN_NORM = 0, OT_ISP_ALG_RUN_FE_ONLY = 1, OT_ISP_ALG_RUN_BUTT,
}ot_isp_alg_run_select;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_ALG\_RUN\_NORM | Run all ISP algorithm modules. |
| OT\_ISP\_ALG\_RUN\_FE\_ONLY | Run only FE algorithm modules. |

**Precautions** 1. Modification is only supported before calling isp\_mem\_init; dynamic modification after isp\_mem\_init is not supported.
2. Only supported on a physical pipe configured as OT\_ISP\_ALG\_RUN\_FE\_ONLY. **Related Data Types and Interfaces** None ### ot\_isp\_run\_wakeup\_select **Description** Defines the interrupt type for waking up the ISP in run mode. **Definition** `typedef enum { OT_ISP_RUN_WAKEUP_FE_START = 0, OT_ISP_RUN_WAKEUP_BE_END = 1, OT_ISP_RUN_WAKEUP_BUTT,
}ot_isp_run_wakeup_select;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_RUN\_WAKEUP\_FE\_START | ISP woken up by the FE frame start interrupt. |
| OT\_ISP\_RUN\_WAKEUP\_BE\_END | ISP woken up by the BE frame end interrupt. |

**Precautions** 1. Modification is only supported before calling [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920); dynamic modification after [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920) is not supported.
2. ot\_isp\_run\_wakeup\_select defaults to OT\_ISP\_RUN\_WAKEUP\_FE\_START and can be used with the ss\_mpi\_isp\_run interface. The recommended calling flow is shown in [Figure 1](#fig86541627175814). **Figure 1** Interface call flow (1) [ "API Call Flow (1)")](figures/API Call Flow(1)) 1. If frames need to be retrieved from VI and then raw data sent for processing, ot\_isp\_run\_wakeup\_select can be set to OT\_ISP\_RUN\_WAKEUP\_BE\_END and used with the ss\_mpi\_isp\_run interface. The recommended calling flow is shown in [Figure 2](#fig1140172181212). This configuration uses the run\_be software path. When calling ss\_mpi\_vi\_send\_pipe\_raw to send raw frames, ensure even frame intervals. Uneven raw frame delivery may affect image quality during exposure ratio switching, mode switching, and similar scenarios. Differences and trade-offs of run\_be compared with run and runonce: - Compared with run, run\_be supports manual frame submission, but synchronization anomalies may occur if the frame submission delay is too long. - Both run\_be and runonce support manual frame submission. run\_be supports multi-channel stitch mode frame submission; runonce does not support multi-channel stitching. runonce uses serial processing between software and hardware; run\_be uses parallel processing, which optimizes logical performance. Therefore, run\_be is recommended for video processing scenarios where performance is critical; runonce is recommended for snapshot scenarios. **Figure 2** Interface call flow (2) [ "API Call Flow (2)")](figures/API Call Flow(2)) **Related Data Types and Interfaces** None ### ot\_isp\_ctrl\_param **Description** Defines the ISP control parameters struct. **Definition** `typedef struct { td_u8 be_buf_num; td_u32 proc_param; td_u32 stat_interval; td_u32 update_pos; td_u32 interrupt_time_out; td_u32 pwm_num; td_u32 port_interrupt_delay; td_bool ldci_tpr_flt_en; ot_isp_ob_stats_update_pos ob_stats_update_pos; ot_isp_alg_run_select alg_run_select; ot_isp_run_wakeup_select isp_run_wakeup_select;
} ot_isp_ctrl_param;` **Members**

| Member Name | Description |
| --- | --- |
| be\_buf\_num | Number of ISP BE config buffers in offline mode. Only effective in offline mode. Valid range: [2, 20]; Hi3403V100 default: 8. |
| proc\_param | ISP PROC information update frequency. Default: 30. Minimum is 1, no upper limit.When proc\_param is n, the ISP PROC information is updated once every n frames. |
| stat\_interval | ISP statistics update frequency. Note: for high frame rate scenarios (120 fps and above), reduce the ISP statistics update frequency via stat\_interval to lower ISP CPU utilization and reduce performance consumption. Valid range: (0,0xffffffff]。Default: 1. |
| update\_pos | Default value is 0。 0: Based on the configured value of the u8IntPos member in ot\_isp\_sns\_regs\_info, sensor registers are configured at the frame start or frame end interrupt; Any other value: sensor registers are configured at the frame end interrupt. Valid range: [0,1] |
| interrupt\_time\_out | Interrupt timeout in ms. Default: 200. |
| pwm\_num | PWM number. Default: 3. |
| port\_interrupt\_delay | Port interrupt delay time. Default: 0. Resolves flicker that occurs in some sensors in half WDR mode when configuring sensor registers in the first few lines; a delay is needed. port\_interrupt\_delay is calculated based on the VI operating clock frequency, in clock cycles. For example, if the VI clock is 300 M Hz and the delay is 1 ms, the calculation of port\_interrupt\_delay is as follows: port\_interrupt\_delay（1ms）= 300M/1000ms = 300000 Note: port\_interrupt\_delay is effective only in half WDR mode, since configuring the sensor in other modes does not use Port interrupts. |
| ldci\_tpr\_flt\_en | Indicates whether LDCI temporal filtering is enabled. Default: 0. |
| ob\_stats\_update\_pos | Indicates Location for reading OB region statistics. Default value is 0. |
| alg\_run\_select | ISP algorithm execution selection. 0: Run all ISP algorithms; 1: Run only ISP FE algorithms. Default value is 0。 |
| isp\_run\_wakeup\_select | Wakeup interrupt source selection for ISP. 0：ISP woken up by the FE frame start interrupt. 1：ISP woken up by the BE frame end interrupt. Default value is 0。 |

**Precautions** - The default value of proc\_param is 30, meaning the ISP Proc information is updated once every 30 frames. To disable ISP Proc information, set proc\_param to 0 via [ss\_mpi\_isp\_set\_ctrl\_param](#ZH-CN_TOPIC_0000002504084839) before [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920); no memory is allocated for ISP Proc information, and proc\_param cannot later be set to a non-zero value.
- When setting proc\_param to a non-zero value for the first time via [ss\_mpi\_isp\_set\_ctrl\_param](#ZH-CN_TOPIC_0000002504084839), it must be done before [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920) because memory for Proc information storage must be allocated. Subsequent changes can only switch between non-zero values.
- Frequent ISP Proc info updates consume CPU resources. It is recommended to update once every 30 frames, or enable only for debugging.
- update\_pos, pwm\_num, port\_interrupt\_delay, ldci\_tpr\_flt\_en, be\_buf\_num, ob\_stats\_update\_pos, and alg\_run\_select can only be set via [ss\_mpi\_isp\_set\_ctrl\_param](#ZH-CN_TOPIC_0000002504084839) before [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920). After [ss\_mpi\_isp\_mem\_init](#ZH-CN_TOPIC_0000002471084920), these 7 parameters cannot be changed. There is no restriction on the calling order of [ss\_mpi\_isp\_get\_ctrl\_param](#ZH-CN_TOPIC_0000002471085186).
- proc\_param, stat\_interval, and interrupt\_time\_out can be dynamically changed via [ss\_mpi\_isp\_set\_ctrl\_param](#ZH-CN_TOPIC_0000002504084839).
- Setting ISP control parameters when loading the kernel module is not supported.
- In Offline mode with heavy workloads, using the default be\_buf\_num may cause ISP to report “get Free Be Buf is fail” errors even without frame drops. In this case, increase be\_buf\_num to mitigate the issue. For lighter workloads with tight memory constraints, reduce be\_buf\_num appropriately.
- alg\_run\_select can only be set to OT\_ISP\_ALG\_RUN\_FE\_ONLY on a physical pipe.
- OT\_ISP\_ALG\_RUN\_FE\_ONLY is generally used in scenarios where only FE AE/AF statistics are needed without running BE. When configured as OT\_ISP\_ALG\_RUN\_FE\_ONLY, ISP only registers and runs FE algorithm modules (blc, FE AE, FE AF, HRS, FE isp\_dgain), and no longer runs BE algorithms, configures BE registers, or reads BE statistics, saving CPU time. This differs from bypassing BE logic. It is recommended to use together with ss\_mpi\_vi\_set\_pipe\_frame\_source(vi\_pipe, OT\_VI\_PIPE\_FRAME\_SOURCE\_USER) to bypass viproc processing. For details on the ss\_mpi\_vi\_set\_pipe\_frame\_source interface, see the VI chapter of the MPP Media Processing Software V5.0 Development Reference.
- When BE input is YUV data, the OT\_ISP\_ALG\_RUN\_FE\_ONLY configuration is invalid.
- Only in scenarios where frames are retrieved from VI and raw data is sent for processing does the ISP need to set the interrupt source (isp\_run\_wakeup\_select) to BE frame end interrupt. In other scenarios, only the frame start interrupt is supported.
- When the interrupt source is set to BE frame end interrupt via isp\_run\_wakeup\_select, the following restrictions apply: 1）Frame-mode WDR is not supported. 2）When performing static defective pixel calibration, if the raw frame submission delay is large and uneven in time, static defective pixel calibration may fail. 3) Using superimposed interrupt bottom-half configuration is not supported. 4）Processing of input YUV format is not supported. **Related Data Types and Interfaces** - [ss\_mpi\_isp\_set\_ctrl\_param](#ss_mpi_isp_set_ctrl_param)
- [ss\_mpi\_isp\_get\_ctrl\_param](#ss_mpi_isp_get_ctrl_param) ### ot\_isp\_mod\_param **Description** Defines the ISP module parameters struct. **Definition** `typedef struct { td_u32 interrupt_bottom_half; td_u32 quick_start; td_bool long_frame_interrupt_en;
} ot_isp_mod_param;` **Members**

| Member Name | Description |
| --- | --- |
| interrupt\_bottom\_half | Indicates whether ISP interrupt processing uses the bottom-half mechanism. Default: 0. - interrupt\_bottom\_half =0：ISP kernel-mode processing (reading statistics and configuring sensor and ISP synchronization registers) is completed in the interrupt service routine; - interrupt\_bottom\_half = 1: ISP kernel-mode processing (reading statistics and configuring sensor and ISP synchronization registers) is completed in the interrupt bottom half. |
| quick\_start | Indicates whether ISP uses fast startup. Default: 0. - quick\_start=0：ISP initialization configures the sensor sequence. - quick\_start=1: ISP initialization does not configure the sensor sequence. Not supported on Hi3403V100. |
| long\_frame\_interrupt\_en | Indicates whether ISP responds to the long-frame interrupt in WDR mode. Default: 0. 0: Disabled; 1: Enabled. |

**Precautions** - Setting the interrupt bottom half is not supported. The [ss\_mpi\_isp\_get\_mod\_param](#ZH-CN_TOPIC_0000002503964891) interface has no call-order restrictions and can be used to query the current state.
- When setting quick\_start fast startup via [ss\_mpi\_isp\_set\_mod\_param](#ZH-CN_TOPIC_0000002503965069), the interface call must precede the main ISP service (e.g., for multi-pipe scenarios, the call order must come before starting the main multi-pipe service), and the ISP kernel module must already be loaded. The [ss\_mpi\_isp\_get\_mod\_param](#ZH-CN_TOPIC_0000002503964891) interface has no call-order restrictions and can be used to query the current state.
- Setting ISP module parameters when loading the kernel module is not supported.
- When long\_frame\_interrupt\_en is set to 1, in WDR mode the ISP interrupt response count increases, affecting the ISP interrupt response time and increasing CPU load.
- When the interrupt bottom half is enabled, synchronization anomalies may occur in four-channel stitch mode, linear mode (1080p, 120 fps), and sensors with registers configured in the blanking region. **Related Data Types and Interfaces** - [ss\_mpi\_isp\_set\_mod\_param](#ss_mpi_isp_set_mod_param)
- [ss\_mpi\_isp\_get\_mod\_param](#ss_mpi_isp_get_mod_param) ### ot\_isp\_quick\_start\_param **Description** Defines the fast AE startup parameter struct (without light sensor). **Definition** `typedef struct { td_bool quick_start_enable; td_u8 black_frame_num; td_bool ir_mode_en; td_u32 init_exposure_ir; td_u32 iso_thr_ir; td_u16 ir_cut_delay_time;
} ot_isp_quick_start_param;` **Members**

| Member Name | Description |
| --- | --- |
| quick\_start\_enable | Whether to enable AE fast convergence mode at startup. When TD\_TRUE, AE fast convergence mode is turned on and AE converges at the fastest speed at startup (for most scenes, convergence can be completed within 10 frames). This mode can meet the requirement for fast AE convergence at startup without a light sensor. |
| black\_frame\_num | Number of bad frames initially output by the sensor. This parameter is effective when quick\_start\_enable is TD\_TRUE. |
| ir\_mode\_en | IR mode switch supported in AE fast convergence mode. When TD\_TRUE, AE fast convergence supports IR mode. This parameter is effective when quick\_start\_enable is TD\_TRUE. |
| init\_exposure\_ir | Initial exposure under IR mode, equal to exposure time multiplied by exposure gain, where the exposure time unit is µs. This parameter takes effect when both quick\_start\_enable and ir\_mode\_en are TD\_TRUE. |
| iso\_thr\_ir | In AE fast convergence mode, sets the ISO threshold for switching to IR mode (IR CUT on, IR LED on). This parameter is effective when quick\_start\_enable is TD\_TRUE. |
| ir\_cut\_delay\_time | Sets the physical time required to open the IR CUT, in ms. This parameter is effective when quick\_start\_enable is TD\_TRUE. |

**Precautions** - black\_frame\_num should be set to the number of bad frames initially output by the sensor. Some sensors output several bad frames at startup; for sensors without bad frames at startup, set to 0.
- When AE fast convergence mode is enabled, if no IR CUT or IR LED hardware is present, it is recommended to set ir\_mode\_en to TD\_FALSE. In this case, AE starts in fast convergence mode without the corresponding IR fast convergence mode.
- During IR CUT activation, a large brightness change occurs for the sensor. The AE algorithm internally waits for the IR CUT switch to complete. To ensure AE convergence speed and accelerate fast convergence, ir\_cut\_delay\_time should be set appropriately and should not be significantly larger than the actual IR CUT switching time. **Related Data Types and Interfaces** None. ### ot\_isp\_init\_attr **Description** Defines the AE/AWB initialization parameter struct for ISP first startup. **Definition** `typedef struct { td_bool is_ir_mode; td_u32 ae_comp; td_u32 exp_time; td_float int_time_accu; td_u32 a_gain; td_float again_accu; td_u32 d_gain; td_float dgain_accu; td_u32 ispd_gain; td_u32 exposure; td_u32 init_iso; td_u32 lines_per500ms; td_u32 piris_fno; td_u16 wb_r_gain; td_u16 wb_g_gain; td_u16 wb_b_gain; td_u16 sample_r_gain; td_u16 sample_b_gain; td_u16 init_ccm[OT_ISP_CCM_MATRIX_SIZE]; td_bool ae_route_ex_valid; td_bool quick_start_en; ot_isp_ae_route ae_route; ot_isp_ae_route_ex ae_route_ex; ot_isp_ae_route ae_route_sf; ot_isp_ae_route_ex ae_route_sf_ex;
} ot_isp_init_attr;` **Members**

| Member Name | Description |
| --- | --- |
| is\_ir\_mode | Sets whether the ISP startup state is IR mode. |
| ae\_comp | Sets the AE target brightness after ISP startup. |
| exp\_time | Sets the AE initial exposure time at ISP first startup, in µs. In FSWDR mode, represents the current shortest-frame (VS) exposure time. Not supported. |
| int\_time\_accu | Sets the precision of the exposure time after ISP startup. |
| a\_gain | Sets the AE initial sensor analog gain at ISP first startup, with 10-bit precision. Not supported. |
| again\_accu | Sets the precision of the sensor analog gain after ISP startup. |
| d\_gain | Sets the AE initial sensor digital gain at ISP first startup, with 10-bit precision. Not supported. |
| dgain\_accu | Sets the precision of the sensor digital gain after ISP startup. |
| ispd\_gain | Sets the AE initial ISP digital gain at ISP first startup, with 10-bit precision. Not supported. |
| exposure | Sets the AE initial exposure at ISP first startup, equal to exposure time multiplied by exposure gain, where the exposure time unit is µs. |
| init\_iso | Sets the AE initial ISO value at ISP first startup. |
| lines\_per500ms | Sets the exposure line count per 500 ms, used to calculate the AE initial exposure. |
| piris\_fno | Equivalent gain corresponding to the P-Iris aperture F-number. Not supported. |
| wb\_r\_gain | Sets the AWB R-channel gain at ISP first startup. |
| wb\_g\_gain | Sets the AWB G-channel gain at ISP first startup. |
| wb\_b\_gain | Sets the AWB B-channel gain at ISP first startup. |
| sample\_r\_gain | Sets the G/R value for AWB online calibration of the current device. |
| sample\_b\_gain | Sets the G/B value for AWB online calibration of the current device. |
| init\_ccm | Sets the CCM value at ISP first startup. |
| ae\_route\_ex\_valid | Sets the AE extended route enable switch at ISP first startup. When TD\_TRUE, the extended route is used; otherwise, the normal route is used. |
| quick\_start\_en | Sets fast startup parameters without a light sensor. |
| ae\_route | Sets the AE exposure route at ISP first startup. |
| ae\_route\_ex | Sets the AE extended exposure route at ISP first startup. |
| ae\_route\_sf | Sets the AE short-frame exposure route at ISP first startup; used only in WDR mode. |
| ae\_route\_sf\_ex | Sets the AE short-frame extended exposure route at ISP first startup; used only in WDR mode. |

**Precautions** - Setting the initial AWB gains and CCM coefficients before ISP startup can improve color consistency between consecutive frames.
- Setting the initial AE exposure route before ISP startup allows the AE algorithm to retain and automatically apply the initially set AE route after a frame rate change. **Related Data Types and Interfaces** - [ot\_isp\_sns\_obj](#ot_isp_sns_obj)
- [ot\_isp\_quick\_start\_param](#ot_isp_quick_start_param) ### ot\_isp\_sns\_mirrorflip\_type **Description** Defines the sensor mirror-flip enum. **Definition** `typedef enum { ISP_SNS_NORMAL = 0, ISP_SNS_MIRROR = 1, ISP_SNS_FLIP = 2, ISP_SNS_MIRROR_FLIP = 3, ISP_SNS_BUTT
} ot_isp_sns_mirrorflip_type;` **Members**

| Member Name | Description |
| --- | --- |
| ISP\_SNS\_NORMAL | Sensor normal output. |
| ISP\_SNS\_MIRROR | sensor mirror Output |
| ISP\_SNS\_FLIP | sensor flip Output |
| ISP\_SNS\_MIRROR\_FLIP | Sensor mirror-flip Output |

**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_sns\_obj](#ot_isp_sns_obj) ### ot\_isp\_sns\_blc\_clamp **Description** Defines the sensor black level correction switch. **Definition** `typedef struct { td_bool blc_clamp_en;
} ot_isp_sns_blc_clamp;` **Members**

| Member Name | Description |
| --- | --- |
| blc\_clamp\_en | Sensor black level correction switch. When TD\_TRUE, the sensor internal black level correction is enabled; when TD\_FALSE, it is disabled. |

**Precautions** Some sensors output different numbers of OB rows when the internal black level correction is enabled vs. disabled. When using this interface, check the OB row count change. If the OB row count change affects other algorithm functions, adjust the configurations of the affected algorithms accordingly. **Related Data Types and Interfaces** [ot\_isp\_sns\_obj](#ot_isp_sns_obj) ### ot\_isp\_sns\_bus\_ex **Description** Defines the extended sensor communication protocol struct. **Definition** `typedef struct { char bus_addr;
} ot_isp_sns_bus_ex;` **Members**

| Member Name | Description |
| --- | --- |
| bus\_addr | Specifies the serdes device address corresponding to the sensor bound to this pipe. |

**Precautions** None. **Related Data Types and Interfaces** [ot\_isp\_sns\_obj](#ot_isp_sns_obj) ### ot\_isp\_sns\_obj **Description** Defines the object pointer to the sensor. **Definition** `typedef struct { td_s32 (*pfn_register_callback)(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *ae_lib, ot_isp_3a_alg_lib *awb_lib); td_s32 (*pfn_un_register_callback)(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *ae_lib, ot_isp_3a_alg_lib *awb_lib); td_s32 (*pfn_set_bus_info)(ot_vi_pipe vi_pipe, ot_isp_sns_commbus sns_bus_info); td_s32 (*pfn_set_bus_ex_info)(ot_vi_pipe vi_pipe, ot_isp_sns_bus_ex *serdes_info); ot_void (*pfn_standby)(ot_vi_pipe vi_pipe); ot_void (*pfn_restart)(ot_vi_pipe vi_pipe); ot_void (*pfn_mirror_flip)(ot_vi_pipe vi_pipe, ot_isp_sns_mirrorflip_type sns_mirror_flip); ot_void (*pfn_set_blc_clamp)(ot_vi_pipe vi_pipe, ot_isp_sns_blc_clamp sns_blc_clamp); td_s32 (*pfn_write_reg)(ot_vi_pipe vi_pipe, td_u32 addr, td_u32 data); td_s32 (*pfn_read_reg)(ot_vi_pipe vi_pipe, td_u32 addr); td_s32 (*pfn_set_init)(ot_vi_pipe vi_pipe, ot_isp_init_attr *init_attr);
} ot_isp_sns_obj;` **Members**

| Member Name | Description |
| --- | --- |
| pfn\_register\_callback | Pointer to the sensor registration function. |
| pfn\_un\_register\_callback | Pointer to the sensor deregistration function. |
| pfn\_set\_bus\_info | Pointer to the sensor I2C/SPI binding function. |
| pfn\_set\_bus\_ex\_info | Pointer to the sensor extended communication function. |
| pfn\_standby | Pointer to the sensor standby function. |
| pfn\_restart | Pointer to the sensor restart function. |
| pfn\_mirror\_flip | Pointer to the sensor mirror-flip function. |
| pfn\_set\_blc\_clamp | Pointer to the sensor black level correction function. |
| pfn\_write\_reg | Pointer to the sensor write-register function. |
| pfn\_read\_reg | Pointer to the sensor read-register function. |
| pfn\_set\_init | Pointer to the sensor AE/AWB initialization parameter function. |

**Precautions** ot\_isp\_sns\_obj was introduced to distinguish between different sensor libraries. Usage: `ot_isp_sns_obj g_sns_xxx_obj = { .pfn_register_callback = sensor_register_callback, .pfn_un_register_callback = sensor_unregister_callback, .pfn_standby = xxx_standby, .pfn_restart = xxx_restart, .pfn_mirror_flip = xxx_mirror_flip, .pfn_set_blc_clamp = xxx_blc_clamp, .pfn_read_reg = xxx_read_register, .pfn_set_bus_info = xxx_set_bus_info, .pfn_set_init = sensor_set_init
};` **Related Data Types and Interfaces** None ### ot\_isp\_sns\_state **Description** Defines the sensor global variable parameter struct. **Definition** `typedef struct { td_bool init; td_bool sync_init; td_u8 img_mode; td_u8 hdr; ot_wdr_mode wdr_mode; ot_isp_sns_regs_info regs_info[ISP_SNS_SAVE_INFO_MAX]; td_u32 fl[ISP_SNS_SAVE_INFO_MAX]; td_u32 fl_std; td_u32 wdr_int_time[OT_ISP_WDR_MAX_FRAME_NUM]; td_u32 sensor_wb_gain[OT_ISP_BAYER_CHN_NUM];
} ot_isp_sns_state;` **Members**

| Member Name | Description |
| --- | --- |
| init | Sensor initialization state flag. |
| sync\_init | Sensor register synchronization initialization state flag. |
| img\_mode | Sensor resolution mode setting. |
| hdr | Records whether in HDR mode. Not supported. |
| wdr\_mode | Sensor WDR mode setting. |
| regs\_info[[ISP\_SNS\_SAVE\_INFO\_MAX](#ISP_SNS_SAVE_INFO_MAX)] | Sensor register state. regs\_info[0] represents the current frame sensor register state; regs\_info[1] represents the previous frame sensor register state. |
| fl[[ISP\_SNS\_SAVE\_INFO\_MAX](#ISP_SNS_SAVE_INFO_MAX)] | Records the total number of lines actually active for a frame. fl[0] is the current frame line count; fl[1] is the previous frame line count. |
| fl\_std | Total number of lines for one frame at the reference frame rate. |
| wdr\_int\_time[[OT\_ISP\_WDR\_MAX\_FRAME\_NUM](#OT_ISP_WDR_MAX_FRAME_NUM)] | Exposure time in WDR mode. wdr\_int\_time[0] is the VS frame exposure time; wdr\_int\_time[1] is the S frame; wdr\_int\_time[2] is the M frame; wdr\_int\_time[3] is the L frame. |
| sensor\_wb\_gain | AWB gain to be configured on the sensor. 8-bit fractional precision. Valid range: [0x0, 0x FFF]; gains are ordered as RGGB. |

**Precautions** - ot\_isp\_sns\_state is a struct introduced to preserve global variables in cmos.c. When multiple ISP channels load the sensor library simultaneously, sensor-state-related global variables are distinguished by vi\_pipe.
- By default, AWB gains are configured in the ISP; the user does not need to be concerned with the sensor\_wb\_gain parameter.
- To configure AWB gains in the sensor, assign the callback function pfn\_cmos\_get\_awb\_gains and write the AWB gain values from sensor\_wb\_gain to the corresponding sensor registers. **Related Data Types and Interfaces** None ### ot\_isp\_awb\_alg **Description** Defines the AWB algorithm type. **Definition** `typedef enum { OT_ISP_ALG_AWB_GW = 0, OT_ISP_ALG_AWB_SPEC = 1, OT_ISP_ALG_BUTT
} ot_isp_awb_alg;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_ALG\_AWB\_GW | Gray world AWB algorithm. |
| OT\_ISP\_ALG\_AWB\_SPEC | Machine-learning AWB algorithm. |

**Precautions** Hi3403V100 does not support machine-learning AWB. **Related Data Types and Interfaces** ot\_isp\_wb\_attr ### ot\_isp\_ir\_status **Description** Defines the current IR state of the device. **Definition** `typedef enum { OT_ISP_IR_STATUS_NORMAL = 0, OT_ISP_IR_STATUS_IR = 1, OT_ISP_IR_BUTT
} ot_isp_ir_status;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_IR\_STATUS\_NORMAL | Device is currently in normal state (non-IR). |
| OT\_ISP\_IR\_STATUS\_IR | Device is currently in IR state. |

**Precautions** None **Related Data Types and Interfaces** None ### ot\_isp\_ir\_switch\_status **Description** Defines the IR switching state of the device. **Definition** `typedef enum { OT_ISP_IR_SWITCH_NONE = 0, OT_ISP_IR_SWITCH_TO_NORMAL = 1, OT_ISP_IR_SWITCH_TO_IR = 2, OT_ISP_IR_SWITCH_BUTT
} ot_isp_ir_switch_status;` **Members**

| Member Name | Description |
| --- | --- |
| OT\_ISP\_IR\_SWITCH\_NONE | Device does not switch IR state. |
| OT\_ISP\_IR\_SWITCH\_TO\_NORMAL | Device switches to normal state (non-IR). |
| OT\_ISP\_IR\_SWITCH\_TO\_IR | Device switches to IR state. |

**Precautions** None **Related Data Types and Interfaces** None ### ot\_isp\_ir\_auto\_attr **Description** Defines the automatic IR switching attributes. **Definition** `typedef struct { td_bool en; td_u32 normal_to_ir_iso_threshold; td_u32 ir_to_normal_iso_threshold; td_u32 rg_max; td_u32 rg_min; td_u32 bg_max; td_u32 bg_min; ot_isp_ir_status ir_status; ot_isp_ir_switch_status ir_switch;
} ot_isp_ir_auto_attr;` **Members**

| Member Name | Description |
| --- | --- |
| en | IR auto-switch enabled. TD\_FALSE: Disable; TD\_TRUE: Enable. |
| normal\_to\_ir\_iso\_threshold | ISO threshold for switching from normal state to IR state. When the actual effective ISO is greater than this threshold, the system needs to switch to IR state. Valid range: [0, 0x FFFFFFFF] |
| ir\_to\_normal\_iso\_threshold | ISO threshold for switching from IR state to normal state. When the actual effective ISO is less than this threshold, the system needs to switch to normal state. Valid range: [0, 0x FFFFFFFF] |
| rg\_max | Maximum R/G value in IR state. When the actual image R/G exceeds this parameter, the system needs to switch to normal state. 4.8 format. Valid range: [0, 0x FFF] |
| rg\_min | Minimum R/G value in IR state. When the actual image R/G is less than this parameter, the system needs to switch to normal state. 4.8 format. Valid range: [0, rg\_max] |
| bg\_max | Maximum B/G value in IR state. When the actual image B/G exceeds this parameter, the system needs to switch to normal state. 4.8 format.Valid range: [0, 0x FFF] |
| bg\_min | Minimum B/G value in IR state. When the actual image B/G is less than this parameter, the system needs to switch to normal state. 4.8 format. Valid range: [0, bg\_max] |
| ir\_status | The current IR state of the device. Should be configured to the actual IR state of the device. The user must ensure the correctness of the state. |
| ir\_switch | The IR switching state of the device, read-only. |

**Precautions** - The configuration values of normal\_to\_ir\_iso\_threshold/ir\_to\_normal\_iso\_threshold/rg\_max/rg\_min/bg\_max/bg\_min are related to the sensor/lens/filter/IR light.
- The configuration values of rg\_max/rg\_min/bg\_max/bg\_min can be generated by referring to the calibration process in mpp/sample/ir\_auto/sample\_ir\_auto.c. **Related Data Types and Interfaces** None

