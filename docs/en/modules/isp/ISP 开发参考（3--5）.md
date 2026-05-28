---
title: Chapter 3–5
---

title: "AE"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ISP Dev Reference/ISP Dev Reference (3-5).md
--- # AE

## Overview The ISP AE module implements the following functionality: based on the automatic metering system, it obtains the current image exposure and automatically configures the lens aperture, sensor shutter, and gain to achieve optimal image quality. The auto exposure algorithm is mainly divided into aperture priority, shutter priority, and gain priority. In aperture priority mode, the algorithm prioritizes adjusting the aperture to a suitable position before allocating exposure time and gain. This is only suitable for P-Iris lenses, and it balances noise and depth of field. In shutter priority mode, the algorithm prioritizes allocating exposure time before allocating sensor gain and ISP gain, resulting in less noise in the captured image. In gain priority mode, the algorithm prioritizes allocating sensor gain and ISP gain before allocating exposure time, suitable for scenes with moving objects. The current AE algorithm also supports customers setting more flexible exposure allocation strategies. The workflow of the AE module is shown in [Figure 1](#fig78111144161318). **Figure 1** AE Module Workflow Diagram [¶](#overview-the-isp-ae-module-implements-the-following-functionality-based-on-the-automatic-metering-system-it-obtains-the-current-image-exposure-and-automatically-configures-the-lens-aperture-sensor-shutter-and-gain-to-achieve-optimal-image-quality-the-auto-exposure-algorithm-is-mainly-divided-into-aperture-priority-shutter-priority-and-gain-priority-in-aperture-priority-mode-the-algorithm-prioritizes-adjusting-the-aperture-to-a-suitable-position-before-allocating-exposure-time-and-gain-this-is-only-suitable-for-p-iris-lenses-and-it-balances-noise-and-depth-of-field-in-shutter-priority-mode-the-algorithm-prioritizes-allocating-exposure-time-before-allocating-sensor-gain-and-isp-gain-resulting-in-less-noise-in-the-captured-image-in-gain-priority-mode-the-algorithm-prioritizes-allocating-sensor-gain-and-isp-gain-before-allocating-exposure-time-suitable-for-scenes-with-moving-objects-the-current-ae-algorithm-also-supports-customers-setting-more-flexible-exposure-allocation-strategies-the-workflow-of-the-ae-module-is-shown-in-figure-1-figure-1-ae-module-workflow-diagram "锚链接")

## Important Concepts - Exposure Time: The time during which the sensor accumulates charge, from the start of exposure of the sensor pixel to the readout of the charge.[¶](#important-concepts-exposure-time-the-time-during-which-the-sensor-accumulates-charge-from-the-start-of-exposure-of-the-sensor-pixel-to-the-readout-of-the-charge "锚链接")

- Exposure Gain: The total amplification factor for the sensor's output charge, generally including digital gain and analog gain. Analog gain introduces slightly less noise, so analog gain is typically preferred.
- Aperture: The aperture is a mechanical device in the lens that can change the size of the aperture opening.
- Anti-flicker: Image flicker caused by the mismatch between the power frequency of electric lights and the sensor's frame rate. Anti-flicker is generally achieved by limiting the exposure time and modifying the sensor's frame rate. ## Function Description The AE module consists of two parts: the ISP AE statistics information module and the AE algorithm Firmware for AE control strategy. The ISP AE statistics information module mainly provides brightness information statistics of the sensor input data. The statistics information provided includes histograms and average values, which can simultaneously provide 1024-bin histograms of the entire image and R/Gr/Gb/B four-component average statistics, as well as R/Gr/Gb/B four-component average statistics for each block when the entire image is divided into MxN blocks, as shown in [Figure 1](#fig1568813224314). **Figure 1** AE 1024-bin Statistics Histogram [](figures/AE 1024-bin Statistics Histogram) The main working principle of the AE algorithm is to obtain the statistical information of the input image in real time, compare it with the set target brightness, and dynamically adjust the sensor's exposure time, gain, and lens aperture size so that the actual brightness approaches the set target brightness. Its working principle is shown in [Figure 2](#fig85992506321). **Figure 2** AE Working Principle Diagram [](figures/AE Working Principle Diagram)

## API Reference ### AE Library Interfaces All AE library interfaces are only for the AE library provided by the SDK. If the customer implements their own AE library, they do not need to pay attention to these interfaces and cannot use them. - [ss\_mpi\_ae\_register](#ZH-CN_TOPIC_0000002470925134): Register the AE library with ISP.[¶](#api-reference-ae-library-interfaces-all-ae-library-interfaces-are-only-for-the-ae-library-provided-by-the-sdk-if-the-customer-implements-their-own-ae-library-they-do-not-need-to-pay-attention-to-these-interfaces-and-cannot-use-them-ss_mpi_ae_register-register-the-ae-library-with-isp "锚链接")

- [ss\_mpi\_ae\_unregister](#ZH-CN_TOPIC_0000002471084866): Unregister the AE library from ISP.
- [ss\_mpi\_ae\_sensor\_reg\_callback](#ZH-CN_TOPIC_0000002470924952): The sensor registration callback interface provided by the AE library.
- [ss\_mpi\_ae\_sensor\_unreg\_callback](#ZH-CN_TOPIC_0000002471084858): The sensor unregistration callback interface provided by the AE library. #### ss\_mpi\_ae\_register 【Description】 Register the AE library with ISP. 【Syntax】 `td_s32 ss_mpi_ae_register(ot_vi_pipe vi_pipe, const ot_isp_3a_alg_lib *ae_lib);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_lib | Pointer to the AE algorithm library structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 - This interface calls the AE registration callback interface ss\_mpi\_isp\_ae\_lib\_reg\_callback provided by the ISP library to implement the registration of the AE library provided by the SDK with the ISP library.
- Multiple instances of the AE library can be registered.
- This interface does not support multi-process operations. 【Example】 `ot_vi_pipe vi_pipe = 0;
ae_lib.id = 0;
strcpy(ae_lib.lib_name, OT_AE_LIB_NAME); ss_mpi_ae_register(vi_pipe, &ae_lib);
ae_lib.id = 1; ss_mpi_ae_register(vi_pipe, &ae_lib);` 【Related Topics】 None #### ss\_mpi\_ae\_unregister 【Description】 Unregister the AE library from ISP. 【Syntax】 `td_s32 ss_mpi_ae_unregister(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *ae_lib);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_lib | Pointer to the AE algorithm library structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 - This interface calls the AE unregistration callback interface ss\_mpi\_isp\_ae\_lib\_unreg\_callback provided by the ISP library to implement the unregistration of the AE library from the ISP library.
- This interface does not support multi-process operations. 【Example】 `ot_vi_pipe vi_pipe = 0;
ae_lib.id = 0;strcpy(ae_lib.lib_name, OT_AE_LIB_NAME); ss_mpi_ae_unregister(vi_pipe, & ae_lib);
ae_lib.id = 1; ss_mpi_ae_unregister(vi_pipe, & ae_lib);` 【Related Topics】 None #### ss\_mpi\_ae\_sensor\_reg\_callback 【Description】 The sensor registration callback interface provided by the AE library. 【Syntax】 `td_s32 ss_mpi_ae_sensor_reg_callback(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *ae_lib, ot_isp_sns_attr_info *sns_attr_info, ot_isp_ae_sensor_register *pregister);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_lib | Pointer to the AE algorithm library structure. | Input |
| sns\_attr\_info | Attributes of the sensor registered with AE. | Input |
| pregister | Pointer to the sensor registration structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 - SensorId is a custom value defined in the sensor library, mainly used to verify whether the sensor registered with ISP and the sensor registered with 3A are the same sensor.
- AE obtains differentiated initialization parameters and controls the sensor through a series of callback interfaces registered by the sensor.
- This interface does not support multi-process operations. **Figure 1** Interface between the AE library and the sensor library [](figures/Interface between the AE library and the sensor library) 【Example】 `ot_isp_3a_alg_lib ae_lib;
ot_isp_ae_sensor_register ae_register;
ot_isp_sns_attr_info sns_attr_info;
ot_isp_ae_sensor_exp_func *exp_func = &ae_register.sns_exp;
(ot_void)memset_s(exp_func, sizeof(ot_isp_ae_sensor_exp_func), 0, sizeof(ot_isp_ae_sensor_exp_func));
exp_func->pfn_cmos_get_ae_default = cmos_get_ae_default;
exp_func->pfn_cmos_fps_set = cmos_fps_set;
exp_func->pfn_cmos_slow_framerate_set= cmos_slow_framerate_set; exp_func->pfn_cmos_inttime_update = cmos_inttime_update;
exp_func->pfn_cmos_gains_update = cmos_gains_update;
exp_func->pfn_cmos_again_calc_table = cmos_again_calc_table;
exp_func->pfn_cmos_dgain_calc_table = cmos_dgain_calc_table;
exp_func->pfn_cmos_get_inttime_max = cmos_get_inttime_max;
exp_func->pfn_cmos_ae_fswdr_attr_set = cmos_ae_fswdr_attr_set;
exp_func->pfn_cmos_ae_quick_start_status_set = cmos_ae_quick_start_status_set; ot_vi_pipe vi_pipe = 0;
ae_lib.id = 0;
sns_attr_info.sensor_id = SENSOR_NAME_ID;
strncpy(ae_lib.lib_name, OT_AE_LIB_NAME, sizeof(OT_AE_LIB_NAME));
ret = ss_mpi_ae_sensor_reg_callback(vi_pipe, &ae_lib, &sns_attr_info, &ae_register);
if (ret != TD_SUCCESS) { printf("sensor register callback function to ae lib failed!\n"); return ret;
}` 【Related Topics】 None #### ss\_mpi\_ae\_sensor\_unreg\_callback 【Description】 The sensor unregistration callback interface provided by the AE library. 【Syntax】 `td_s32 ss_mpi_ae_sensor_unreg_callback(ot_vi_pipe vi_pipe, ot_isp_3a_alg_lib *ae_lib, ot_sensor_id sensor_id);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_lib | Pointer to the AE algorithm library structure. | Input |
| sensor\_id | ID of the sensor to be unregistered from AE. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 - SensorId is a custom value defined in the sensor library, mainly used to verify whether the sensor unregistered from ISP and the sensor unregistered from 3A are the same sensor.
- This interface does not support multi-process operations. 【Example】 `ot_isp_3a_alg_lib ae_lib;
ot_vi_pipe vi_pipe = 0;
ae_lib.id = 0;
strncpy(ae_lib.lib_name, OT_AE_LIB_NAME, sizeof(OT_AE_LIB_NAME));
ret = ss_mpi_ae_sensor_unreg_callback(vi_pipe, &ae_lib, SENSOR_NAME_ID);
if (ret != TD_SUCCESS) { printf("sensor register callback function to ae lib failed!\n"); return ret;
}` 【Related Topics】 None ### AE Control Module Exposure control interfaces: - [ss\_mpi\_isp\_set\_exposure\_attr](#ZH-CN_TOPIC_0000002503964781): Set AE exposure attributes.
- [ss\_mpi\_isp\_get\_exposure\_attr](#ZH-CN_TOPIC_0000002504084835): Get AE exposure attributes.
- [ss\_mpi\_isp\_set\_wdr\_exposure\_attr](#ZH-CN_TOPIC_0000002504084905): Set AE exposure attributes in WDR mode.
- [ss\_mpi\_isp\_get\_wdr\_exposure\_attr](#ZH-CN_TOPIC_0000002470924854): Get AE exposure attributes in WDR mode.
- [ss\_mpi\_isp\_set\_hdr\_exposure\_attr](#ZH-CN_TOPIC_0000002504084737): Set AE exposure attributes in HDR mode.
- [ss\_mpi\_isp\_get\_hdr\_exposure\_attr](#ZH-CN_TOPIC_0000002504084897): Get AE exposure attributes in HDR mode.
- [ss\_mpi\_isp\_set\_smart\_exposure\_attr](#ZH-CN_TOPIC_0000002471084856): Set AE exposure attributes in smart mode.
- [ss\_mpi\_isp\_get\_smart\_exposure\_attr](#ZH-CN_TOPIC_0000002504084961): Get AE exposure attributes in smart mode.
- [ss\_mpi\_isp\_set\_fast\_face\_ae\_attr](#ZH-CN_TOPIC_0000002503964919): Set AE exposure attributes in face fast convergence mode.
- [ss\_mpi\_isp\_get\_fast\_face\_ae\_attr](#ZH-CN_TOPIC_0000002504084751): Get AE exposure attributes in face fast convergence mode.
- [ss\_mpi\_isp\_set\_ae\_route\_attr](#ZH-CN_TOPIC_0000002504084821): Set AE exposure allocation strategy attributes.
- [ss\_mpi\_isp\_get\_ae\_route\_attr](#ZH-CN_TOPIC_0000002471084932): Get AE exposure allocation strategy attributes.
- [ss\_mpi\_isp\_set\_ae\_route\_attr\_ex](#ZH-CN_TOPIC_0000002503965045): Set AE exposure allocation extension attributes, supporting separate configuration of sensor analog gain, sensor digital gain, and ISP digital gain in the AE allocation strategy.
- [ss\_mpi\_isp\_get\_ae\_route\_attr\_ex](#ZH-CN_TOPIC_0000002471084852): Get AE exposure allocation strategy extension attributes.
- [ss\_mpi\_isp\_set\_ae\_route\_sf\_attr](#ZH-CN_TOPIC_0000002503964803): In WDR mode, set the AE short frame exposure allocation strategy attributes.
- [ss\_mpi\_isp\_get\_ae\_route\_sf\_attr](#ZH-CN_TOPIC_0000002471085052): Get AE short frame exposure allocation strategy attributes.
- [ss\_mpi\_isp\_set\_ae\_route\_sf\_attr\_ex](#ZH-CN_TOPIC_0000002503964835): In WDR mode, set the AE short frame exposure allocation strategy extension attributes.
- [ss\_mpi\_isp\_get\_ae\_route\_sf\_attr\_ex](#ZH-CN_TOPIC_0000002470925156): Get AE short frame exposure allocation strategy extension attributes.
- [ss\_mpi\_isp\_query\_exposure\_info](#ZH-CN_TOPIC_0000002503964993): Get AE internal status information.
- [ss\_mpi\_isp\_set\_exp\_convert](#ZH-CN_TOPIC_0000002470925022): Set attributes related to equal exposure conversion at different frame rates.
- [ss\_mpi\_isp\_get\_exp\_convert](#ZH-CN_TOPIC_0000002504084753): Get exposure parameter attributes related to equal exposure conversion results at different frame rates. #### ss\_mpi\_isp\_set\_exposure\_attr 【Description】 Set AE exposure attributes. 【Syntax】 `td_s32 ss_mpi_isp_set_exposure_attr (ot_vi_pipe vi_pipe, const ot_isp_exposure_attr *exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| exp\_attr | Pointer to the AE exposure attribute structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 - When the AE exposure control type is Auto, the exposure time and exposure gain are automatically controlled by the AE algorithm. Different exposure effects can be achieved by configuring parameters in the auto exposure attribute structure [ot\_isp\_ae\_attr](#ZH-CN_TOPIC_0000002470924872).
- When the AE exposure control type is Manual, you can control the enable types (exposure time enable, sensor analog gain enable, sensor digital gain enable, ISP digital gain enable) and the corresponding exposure parameters (exposure time, sensor analog gain, sensor digital gain, ISP digital gain) through the manual exposure attribute structure manual\_attr.
- When the AE exposure control type is Auto, the parameters configured for manual exposure attributes are invalid. Similarly, when the AE exposure control type is Manual, the parameters configured for auto exposure attributes are invalid.
- When the AE exposure control type is Manual, if the exposure parameter settings exceed the maximum (minimum) value, the sensor's supported maximum (minimum) value will be used instead.
- Whether in auto exposure or manual exposure, the unit of exposure time is microseconds (us), and the unit of exposure gain is a multiple of 10-bit precision, i.e., 1024 represents 1x, 2048 represents 2x, etc.
- In WDR mode, when the priority frame is set to long frame, exposure is prioritized according to the long frame exposure route. In 2-in-1 WDR mode when gain is configured separately, the short frame exposure route is adjusted based on the long frame exposure parameters. When the priority frame is set to short frame, exposure is prioritized according to the short frame exposure route. In 2-in-1 WDR mode when gain is configured separately, the long frame exposure route is adjusted based on the short frame exposure parameters.
- In 2-in-1 WDR mode with separate gain configuration, if the sensor supports different gains for long and short frames, different sensor analog gains, sensor digital gains, and WDR gains can be achieved for long and short frames. If the sensor does not support different gains for long and short frames, different WDR gains can still be achieved for long and short frames. 【Example】 Auto exposure attribute setting: `ot_vi_pipe vi_pipe = 0;
ot_isp_exposure_attr exp_attr; ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);
exp_attr. bypass = TD_FALSE; exp_attr. prior_frame= OT_ISP_LONG_FRAME;
exp_attr. ae_gain_sep_cfg= TD_FALSE; exp_attr. op_type= OT_OP_MODE_AUTO; exp_attr. auto_attr. exp_time_range.max = 40000;
exp_attr. auto_attr. exp_time_range.min = 10; ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);
exp_attr. auto_attr.speed = 0x80; ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);
exp_attr. auto_attr. exp_attr =OT_ISP_AE_EXP_HIGHLIGHT_PRIOR; exp_attr. auto_attr. hist_ratio_slope= 0x100;
exp_attr. auto_attr. max_hist_offset= 0x40;
ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);
exp_attr. auto_attr. antiflicker. enable= TD_TRUE;
exp_attr. auto_attr. antiflicker. frequency= 50;
exp_attr. auto_attr. antiflicker. mode= OT_ISP_ANTIFLICKER_NORMAL_MODE;
ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);
exp_attr. auto_attr. ae_delay_attr. black_delay_frame = 10;
exp_attr. auto_attr. ae_delay_attr. white_delay_frame = 0;
ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);` Manual exposure attribute setting: `ot_vi_pipe vi_pipe = 0;
ot_isp_exposure_attr exp_attr; ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);exp_attr. bypass= TD_FALSE; exp_attr. op_type= OT_OP_MODE_MANUAL; exp_attr. manual_attr. a_gain_op_type = OT_OP_MODE_MANUAL;
exp_attr. manual_attr. d_gain_op_type = OT_OP_MODE_MANUAL
exp_attr. manual_attr. ispd_gain_op_type = OT_OP_MODE_MANUAL;
exp_attr. manual_attr. exp_time_op_type = OT_OP_MODE_MANUAL;
exp_attr. manual_attr. a_gain = 0x400;
exp_attr. manual_attr. d_gain = 0x400;
exp_attr. manual_attr. isp_d_gain = 0x400;
exp_attr. manual_attr. exp_time = 0x40000; ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr);` 【Related Topics】 [ss\_mpi\_isp\_get\_exposure\_attr](#ss_mpi_isp_get_exposure_attr) #### ss\_mpi\_isp\_get\_exposure\_attr 【Description】 Get AE exposure attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_exposure_attr(ot_vi_pipe vi_pipe, ot_isp_exposure_attr *exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| exp\_attr | Pointer to the AE exposure attribute structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_set\_exposure\_attr](#ss_mpi_isp_set_exposure_attr) #### ss\_mpi\_isp\_set\_wdr\_exposure\_attr 【Description】 Set AE exposure attributes in WDR mode. 【Syntax】 `td_s32 ss_mpi_isp_set_wdr_exposure_attr(ot_vi_pipe vi_pipe, const ot_isp_wdr_exposure_attr *wdr_exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| wdr\_exp\_attr | Pointer to the AE exposure attribute structure in WDR mode. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_get\_wdr\_exposure\_attr](#ss_mpi_isp_get_wdr_exposure_attr) #### ss\_mpi\_isp\_get\_wdr\_exposure\_attr 【Description】 Get AE exposure attributes in WDR mode. 【Syntax】 `td_s32 ss_mpi_isp_get_wdr_exposure_attr(ot_vi_pipe vi_pipe, ot_isp_wdr_exposure_attr *wdr_exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| wdr\_exp\_attr | Pointer to the AE exposure attribute structure in WDR mode. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libss\_isp.a, libot\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_set\_wdr\_exposure\_attr](#ss_mpi_isp_set_wdr_exposure_attr) #### ss\_mpi\_isp\_set\_hdr\_exposure\_attr 【Description】 Set AE exposure attributes in HDR mode. 【Syntax】 `td_s32 ss_mpi_isp_set_hdr_exposure_attr(ot_vi_pipe vi_pipe, const ot_isp_hdr_exposure_attr *hdr_exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| hdr\_exp\_attr | Pointer to the AE exposure attribute structure in HDR mode. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 Hi3403V100 does not support HDR mode. 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_get\_hdr\_exposure\_attr](#ss_mpi_isp_get_hdr_exposure_attr) #### ss\_mpi\_isp\_get\_hdr\_exposure\_attr 【Description】 Get AE exposure attributes in HDR mode. 【Syntax】 `td_s32 ss_mpi_isp_get_hdr_exposure_attr(ot_vi_pipe vi_pipe, ot_isp_hdr_exposure_attr *hdr_exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| hdr\_exp\_attr | Pointer to the AE exposure attribute structure in HDR mode. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 Hi3403V100 does not support HDR mode. 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_set\_hdr\_exposure\_attr](#ss_mpi_isp_set_hdr_exposure_attr) #### ss\_mpi\_isp\_set\_smart\_exposure\_attr 【Description】 Set AE exposure attributes in smart mode. Only takes effect when smart information is available. 【Syntax】 `td_s32 ss_mpi_isp_set_smart_exposure_attr(ot_vi_pipe vi_pipe, const ot_isp_smart_exposure_attr *smart_exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| smart\_exp\_attr | Pointer to the AE exposure attribute structure in smart mode. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - When customers use this function, they can obtain corresponding smart information through their own smart module and pass it to ISP. For the transfer method, refer to the ss\_mpi\_isp\_set\_smart\_info interface. After ISP obtains the brightness information of faces or human figures, it will adjust the exposure accordingly so that the brightness of faces or human figures reaches the set target value.
- For detailed usage of the interface, refer to the [ot\_isp\_smart\_exposure\_attr](#ZH-CN_TOPIC_0000002503964907) description. 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_get\_smart\_exposure\_attr](#ss_mpi_isp_get_smart_exposure_attr) #### ss\_mpi\_isp\_get\_smart\_exposure\_attr 【Description】 Get AE exposure attributes in smart mode. Only takes effect when smart information is available. 【Syntax】 `td_s32 ss_mpi_isp_get_smart_exposure_attr(ot_vi_pipe vi_pipe, ot_isp_smart_exposure_attr *smart_exp_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| smart\_exp\_attr | Pointer to the AE exposure attribute structure in smart mode. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_set\_smart\_exposure\_attr](#ss_mpi_isp_set_smart_exposure_attr) #### ss\_mpi\_isp\_set\_fast\_face\_ae\_attr 【Description】 Set AE exposure attributes in face fast convergence mode. Only takes effect when face coordinate information is available. 【Syntax】 `td_s32 ot_mpi_isp_set_fast_face_ae_attr(ot_vi_pipe vi_pipe, const ot_isp_fast_face_ae_attr *fast_face_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| fast\_face\_attr | Pointer to the AE exposure attribute structure in face fast convergence mode. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_fast_face_ae_attr fast_face_attr;
ss_mpi_isp_get_fast_face_ae_attr (vi_pipe, &fast_face_attr);
fast_face_attr. enable = TD_TRUE;
ss_mpi_isp_set_fast_face_ae_attr (vi_pipe, &fast_face_attr);` 【Related Topics】 - [ss\_mpi\_isp\_get\_fast\_face\_ae\_attr](#ss_mpi_isp_set_fast_face_ae_attr)
- [ot\_isp\_fast\_face\_ae\_attr](#ot_isp_fast_face_ae_attr) #### ss\_mpi\_isp\_get\_fast\_face\_ae\_attr 【Description】 Get AE exposure attributes in face fast convergence mode. Only takes effect when face coordinate information is available. 【Syntax】 `td_s32 ss_mpi_isp_get_fast_face_ae_attr(ot_vi_pipe vi_pipe, ot_isp_fast_face_ae_attr *fast_face_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| fast\_face\_attr | Pointer to the AE exposure attribute structure in face fast convergence mode. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_fast_face_ae_attr fast_face_attr;
ss_mpi_isp_get_fast_face_ae_attr (vi_pipe, &fast_face_attr);
fast_face_attr. enable = TD_TRUE;
ss_mpi_isp_set_fast_face_ae_attr (vi_pipe, &fast_face_attr);` 【Related Topics】 - [ss\_mpi\_isp\_set\_fast\_face\_ae\_attr](#ss_mpi_isp_get_fast_face_ae_attr)
- [ot\_isp\_fast\_face\_ae\_attr](#ot_isp_fast_face_ae_attr) #### ss\_mpi\_isp\_set\_ae\_route\_attr 【Description】 Set AE exposure allocation strategy attributes. 【Syntax】 `td_s32 ss_mpi_isp_set_ae_route_attr(ot_vi_pipe vi_pipe, const ot_isp_ae_route *ae_route_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_attr | Pointer to the AE exposure allocation strategy structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - This interface is used to set the AE exposure allocation route. The exposure calculated by AE will be allocated according to the set route. Users can set exposure priority, gain priority, or aperture priority according to their needs.
- The AE allocation route diagram is shown in [Figure 1](#_Ref376180242). The AE allocation route follows these constraints: - Supports up to 16 nodes, each node has three components: exposure time, gain, and aperture. Gain includes analog gain, digital gain, and ISP digital gain. - The unit of exposure time in a node is us. It cannot be set to 0, nor too small such that the actual corresponding exposure line count is 0, otherwise an exception may occur. - The aperture component only supports P-Iris, not DC-Iris. Since DC-Iris cannot be precisely controlled, the aperture component is invalid for DC-Iris and manual aperture lenses. - The exposure amount of a node is the product of exposure time, gain, and aperture. The node exposure amounts increase monotonically. - If the exposure amount increases between adjacent nodes, one component should increase while others remain fixed. The increasing component determines the allocation strategy for that segment. - Equal exposure amount nodes are not supported. - Users can set different routes for different scenarios, and the allocation route supports dynamic switching. - The AE allocation route cannot be used to limit the maximum and minimum values of exposure parameters. - For DC-Iris and manual aperture lenses, the default AE allocation strategy is to allocate exposure time first, then gain. For P-Iris lenses, the default strategy is to adjust the aperture first, then exposure time, and finally gain. - When switching between DC-Iris and P-Iris online, the AE route will be reset to the default allocation strategy. - In 2-in-1 WDR mode, when the priority frame is short frame and gain separate configuration is not enabled, the AE route does not take effect. - During auto frame dropping, if the AE route is set in cmos.c, the AE route from cmos.c will be used after switching. - When switching between linear mode and WDR mode, if the AE route is set in cmos.c, the route from cmos.c will be used after switching. - When switching frame rate or resolution, if the user-set maximum exposure target time is greater than the maximum exposure time allowed after switching, the maximum exposure time of the route will be updated. - In cases where the actually effective AE route may differ from the MPI setting, use [ss\_mpi\_isp\_query\_exposure\_info](#ZH-CN_TOPIC_0000002503964993) to get the actually effective AE route. **Figure 1** AE Allocation Route Diagram [](figures/AE Allocation Route Diagram) 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_ae_route ae_route;
td_u32 route_node[3][3] = {{100,1024,1},{40000,1024,1},{40000,16384,1}}; ss_mpi_isp_get_ae_route_attr(vi_pipe, &ae_route);ae_route.total_num = 3;
memcpy(ae_route. route_node, route_node, sizeof(route_node));
ss_mpi_isp_set_ae_route_attr(vi_pipe, &ae_route);` 【Related Topics】 - [ss\_mpi\_isp\_get\_ae\_route\_attr](#ss_mpi_isp_get_ae_route_attr)
- [ot\_isp\_ae\_route](#ot_isp_ae_route) #### ss\_mpi\_isp\_get\_ae\_route\_attr 【Description】 Get AE exposure allocation strategy attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_ae_route_attr(ot_vi_pipe vi_pipe, ot_isp_ae_route *ae_route_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_attr | Pointer to the AE exposure allocation strategy structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_set\_ae\_route\_attr](#ss_mpi_isp_set_ae_route_attr) #### ss\_mpi\_isp\_set\_ae\_route\_attr\_ex 【Description】 Set AE exposure allocation extension attributes, supporting separate configuration of sensor analog gain, sensor digital gain, and ISP digital gain in the AE allocation strategy. 【Syntax】 `td_s32 ss_mpi_isp_set_ae_route_attr_ex(ot_vi_pipe vi_pipe, const ot_isp_ae_route_ex *ae_route_attr_ex);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_attr\_ex | Pointer to the AE exposure allocation strategy extension attribute structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - This interface is used to set AE exposure allocation extension attributes. The exposure calculated by AE will be allocated according to the set route. Users can set exposure time priority, sensor analog gain priority, sensor digital gain priority, ISP digital gain priority, and aperture priority according to their needs. This interface can be used to set the exposure allocation route in WDR mode, reducing the power frequency flicker phenomenon caused by multi-frame WDR synthesis under normal indoor illumination.
- Whether the AE exposure allocation extension attributes take effect can be configured through the ae\_route\_ex\_valid parameter in the [ss\_mpi\_isp\_set\_exposure\_attr](#ZH-CN_TOPIC_0000002503964781) interface. When ae\_route\_ex\_valid is TD\_TRUE, the extended AE route is used; otherwise, the normal AE route is used.
- The AE extended allocation route follows these constraints: - Supports up to 16 nodes, each node has five components: exposure time, sensor analog gain, sensor digital gain, ISP digital gain, and aperture. - The unit of exposure time in a node is us. - The aperture component only supports P-Iris. - Node exposure amounts increase monotonically. - Equal exposure amount nodes are not supported. - Users can switch routes dynamically for different scenarios. - The default extended allocation strategy differs for DC-Iris/manual aperture vs P-Iris lenses. - For complete details, refer to the original Chinese documentation. 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_exposure_attr exp_attr;
ot_isp_ae_route_ex ae_route_attr_ex;
td_u32 route_ex_node [6][5] = {{ 30, 1024, 1024, 1024, 0}, { 30, 1024, 1024, 1024, 10}, { 30, 16384, 1024, 1024, 10}, {1000000, 16384, 1024, 1024, 10}, {1000000, 16384, 16384, 1024, 10}, {1000000, 16384, 16384, 4096, 10}};
ss_mpi_isp_get_ae_route_attr_ex(vi_pipe, &ae_route_attr_ex);
ss_mpi_isp_get_exposure_attr(vi_pipe, &exp_attr); exp_attr. ae_route_ex_valid = TD_TRUE;
ae_route_attr_ex. total_num = 6;
memcpy(ae_route_attr_ex. route_ex_node, route_ex_node, sizeof(route_ex_node));
ss_mpi_isp_set_ae_route_attr_ex (vi_pipe, & ae_route_attr_ex);
ss_mpi_isp_set_exposure_attr (vi_pipe, &exp_attr);` 【Related Topics】 - [ss\_mpi\_isp\_get\_ae\_route\_attr\_ex](#ss_mpi_isp_get_ae_route_attr_ex)
- [ss\_mpi\_isp\_set\_exposure\_attr](#ss_mpi_isp_set_exposure_attr)
- [ot\_isp\_ae\_route\_ex](#ot_isp_ae_route_ex) #### ss\_mpi\_isp\_get\_ae\_route\_attr\_ex 【Description】 Get AE exposure allocation strategy extension attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_ae_route_attr_ex(ot_vi_pipe vi_pipe, ot_isp_ae_route_ex *ae_route_attr_ex);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_attr\_ex | Pointer to the AE exposure allocation strategy extension attribute structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None. 【Example】 None. 【Related Topics】 [ss\_mpi\_isp\_set\_ae\_route\_attr\_ex](#ss_mpi_isp_set_ae_route_attr_ex) #### ss\_mpi\_isp\_set\_ae\_route\_sf\_attr 【Description】 In WDR mode, set the AE short frame exposure allocation strategy attributes. 【Syntax】 `td_s32 ss_mpi_isp_set_ae_route_sf_attr(ot_vi_pipe vi_pipe, const ot_isp_ae_route *ae_route_sf_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_sf\_attr | Pointer to the AE short frame exposure allocation strategy structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - This interface is used to set the AE short frame exposure allocation route in WDR mode. The short frame exposure calculated by AE will be allocated according to the set route. Users can set exposure priority, gain priority, or aperture priority according to their needs.
- The AE allocation route follows these constraints: - Supports up to 16 nodes, each node has three components: exposure time, gain, and aperture. - The unit of exposure time in a node is us. - The aperture component only supports P-Iris. - Node exposure amounts increase monotonically. - Equal exposure amount nodes are not supported. - Users can switch routes dynamically for different scenarios. - Online DC-Iris and P-Iris switching will reset the short frame AE route. - Short frame AE route does not take effect when the priority frame is long frame and gain separate configuration is not enabled, or in linear mode. - For complete details, refer to the original Chinese documentation. 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_ae_route ae_route_sf_attr;
td_u32 route_node [3][3] = {{100,1024,1},{20000,1024,1},{20000,16384,1}}; ss_mpi_isp_get_ae_route_sf_attr (vi_pipe, &ae_route_sf_attr);
ae_route_sf_attr.total_num = 3;
memcpy(ae_route_sf_attr.route_node, route_node, sizeof(route_node));
ss_mpi_isp_set_ae_route_sf_attr (vi_pipe, &ae_route_sf_attr);` 【Related Topics】 - [ss\_mpi\_isp\_get\_ae\_route\_sf\_attr](#ss_mpi_isp_get_ae_route_sf_attr)
- [ot\_isp\_ae\_route](#ot_isp_ae_route) #### ss\_mpi\_isp\_get\_ae\_route\_sf\_attr 【Description】 Get AE short frame exposure allocation strategy attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_ae_route_sf_attr(ot_vi_pipe vi_pipe, ot_isp_ae_route *ae_route_sf_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_sf\_attr | Pointer to the AE short frame exposure allocation strategy structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 [ss\_mpi\_isp\_set\_ae\_route\_sf\_attr](#ss_mpi_isp_set_ae_route_sf_attr) #### ss\_mpi\_isp\_set\_ae\_route\_sf\_attr\_ex 【Description】 In WDR mode, set the AE short frame exposure allocation strategy extension attributes. 【Syntax】 `td_s32 ss_mpi_isp_set_ae_route_sf_attr_ex(ot_vi_pipe vi_pipe, const ot_isp_ae_route_ex *ae_route_sf_attr_ex);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_sf\_attr\_ex | Pointer to the AE short frame exposure allocation strategy extension attribute structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - This interface is used to set the AE short frame exposure allocation extension attributes in WDR mode. The short frame exposure calculated by AE will be allocated according to the set route. Users can set exposure time priority, sensor analog gain priority, sensor digital gain priority, ISP digital gain priority, and aperture priority according to their needs.
- Whether the AE exposure allocation extension attributes take effect can be configured through the ae\_route\_ex\_valid parameter in the [ss\_mpi\_isp\_set\_exposure\_attr](#ZH-CN_TOPIC_0000002503964781) interface.
- The AE extended allocation route follows constraints similar to the standard extended route but for short frames. 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_exposure_attr exp_attr;
ot_isp_ae_route_ex ae_route_sf_attr_ex;
td_u32 route_ex_node [6][5] = {{ 30, 1024, 1024, 1024, 0}, { 30, 1024, 1024, 1024, 10}, { 30, 16384, 1024, 1024, 10}, {20000, 16384, 1024, 1024, 10}, {20000, 16384, 16384, 1024, 10}, {20000, 16384, 16384, 4096, 10}};
ss_mpi_isp_get_ae_route_sf_attr_ex (vi_pipe, & ae_route_sf_attr_ex);
ss_mpi_isp_get_exposure_attr (vi_pipe, &exp_attr); exp_attr. ae_route_ex_valid= TD_TRUE;
ae_route_sf_attr_ex. total_num= 6;
memcpy(ae_route_sf_attr_ex. route_ex_node, route_ex_node, sizeof(route_ex_node));
ss_mpi_isp_get_ae_route_sf_attr_ex (vi_pipe, & ae_route_sf_attr_ex);
ss_mpi_isp_set_exposure_attr (vi_pipe, &exp_attr);` 【Related Topics】 - [ss\_mpi\_isp\_get\_ae\_route\_sf\_attr\_ex](#ss_mpi_isp_get_ae_route_sf_attr_ex)
- [ss\_mpi\_isp\_set\_exposure\_attr](#ss_mpi_isp_set_exposure_attr)
- [ot\_isp\_ae\_route\_ex](#ot_isp_ae_route_ex) #### ss\_mpi\_isp\_get\_ae\_route\_sf\_attr\_ex 【Description】 Get AE short frame exposure allocation strategy extension attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_ae_route_sf_attr_ex(ot_vi_pipe vi_pipe, ot_isp_ae_route_ex *ae_route_sf_attr_ex);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| ae\_route\_sf\_attr\_ex | Pointer to the AE exposure allocation strategy extension attribute structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None. 【Example】 None. 【Related Topics】 [ss\_mpi\_isp\_set\_ae\_route\_sf\_attr\_ex](#ss_mpi_isp_set_ae_route_sf_attr_ex) #### ss\_mpi\_isp\_query\_exposure\_info 【Description】 Get AE internal status information, including global 5-bin histogram, 1024-bin histogram, and average brightness statistics, as well as exposure time, gain, exposure amount, and the actually effective AE route during AE operation. 【Syntax】 `td_s32 ss_mpi_isp_query_exposure_info(ot_vi_pipe vi_pipe, ot_isp_exp_info *exp_info);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| exp\_info | Pointer to the exposure internal status information structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - The obtained exposure time is in microseconds (us), and the obtained sensor analog gain, sensor digital gain, and ISP digital gain are in multiples with 10-bit precision.
- The obtained exposure amount = (exposure time \* exposure gain), not considering the aperture state. The exposure time is in units of lines, and the exposure gain includes sensor analog gain, sensor digital gain, and ISP digital gain.
- The stability of AE can be determined by querying hist\_error. If the absolute value of hist\_error is less than the exposure tolerance deviation value, it means AE will not take action currently.
- The AE route obtained through this interface and the AE route in Proc information are both actually effective values. However, the node exposure time in this interface is in us, while the exposure time in Proc information is in units of lines.
- If the user uses a non-SDK provided AE algorithm, this interface needs to be implemented by the user, and the PQTOOLS xml file needs to be modified accordingly.
- Calling this interface requires ensuring that the system is already running and statistics have been generated. 【Example】 `ot_vi_pipe vi_pipe = 0;
ot_isp_exp_info exp_info;
ss_mpi_isp_query_exposure_info (vi_pipe, &exp_info); printf("Sensor exposure time: %d\n",exp_info.exp_time);
printf("Analog Gain: %d\n",exp_info. a_gain);
printf("Digital Gain: %d\n",exp_info. d_gain);
printf("ISP Gain: %d\n",exp_info. isp_d_gain);
printf("Exposure: %d\n",exp_info. exposure);
printf("Average Luminance: %d\n",exp_info. ave_lum);
printf("Hist error: %d\n",exp_info. hist_error);
exp_info. exposure_is_max? printf("Exposure is MAX!\n") : printf("Exposure is NOT MAX!\n");
for(i = 0; i < 1024; i++)
{ printf("Hist1024Value[%d]: %d\n",i, exp_info. ae_hist1024_value [i]);
}` 【Related Topics】 None #### ss\_mpi\_isp\_set\_exp\_convert 【Description】 Set the exposure parameter attributes related to equal exposure conversion. 【Syntax】 `td_s32 ss_mpi_isp_set_exp_convert(ot_vi_pipe vi_pipe, ot_isp_exp_conv_param *conv_param);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| conv\_param | Pointer to the equal exposure conversion related exposure attribute. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 As input, besides setting the input vi\_pipe number, only the tar\_fps member variable in conv\_param needs to be set to the target frame rate. 【Example】 `ot_vi_pipe vi_pipe = 0; td_s32 i; ot_isp_exp_conv_param conv_param; conv_param. tar_fps= 3000; ss_mpi_isp_set_exp_convert (vi_pipe, &conv_param); ss_mpi_isp_get_vd_time_out(vi_pipe, OT_ISP_VD_FE_START, 50); ss_mpi_isp_get_exp_convert (vi_pipe, &conv_param); for (i = 0; i < 4; i++) { printf("time_reg. reg_addr [%d]: 0x%x, time_reg. reg_value [%d]: 0x%x\n", i, conv_param. time_reg [i]. reg_addr, i, conv_param. time_reg [i]. reg_value); printf("again_reg. reg_addr [%d]: 0x%x, again_reg. reg_value [%d]: 0x%x\n", i, conv_param. again_reg [i]. reg_addr, i, conv_param. again_reg [i]. reg_value); printf("dgain_reg. reg_addr [%d]: 0x%x, dgain_reg. reg_value [%d]: 0x%x\n", i, conv_param. dgain_reg [i]. reg_addr, i, conv_param. dgain_reg [i]. reg_value); }` 【Related Topics】 None #### ss\_mpi\_isp\_get\_exp\_convert 【Description】 Get the exposure parameter attributes related to equal exposure conversion. 【Syntax】 `td_s32 ss_mpi_isp_get_exp_convert(ot_vi_pipe vi_pipe, ot_isp_exp_conv_param *conv_param);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| conv\_param | Pointer to the equal exposure conversion related exposure attribute. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - The converted Sensor exposure time, analog gain, and digital gain are all Sensor register values with corresponding register addresses, which can be directly written to the Sensor registers. The converted ISP digital gain is in multiples with 10-bit precision.
- The converted Sensor exposure time, analog gain, and digital gain each have up to 10 register values and 10 register addresses. 【Example】 None 【Related Topics】 None ### AI Control Module Iris control interfaces: - [ss\_mpi\_isp\_set\_iris\_attr](#ZH-CN_TOPIC_0000002503964851): Set iris control attributes.
- [ss\_mpi\_isp\_get\_iris\_attr](#ZH-CN_TOPIC_0000002503964783): Get iris control attributes.
- [ss\_mpi\_isp\_set\_dciris\_attr](#ZH-CN_TOPIC_0000002470924940): Set DC-Iris auto iris control attributes.
- [ss\_mpi\_isp\_get\_dciris\_attr](#ZH-CN_TOPIC_0000002504084869): Get DC-Iris auto iris control attributes.
- [ss\_mpi\_isp\_set\_piris\_attr](#ZH-CN_TOPIC_0000002503964847): Set P-Iris auto iris control attributes.
- [ss\_mpi\_isp\_get\_piris\_attr](#ZH-CN_TOPIC_0000002471084962): Get P-Iris auto iris control attributes. #### ss\_mpi\_isp\_set\_iris\_attr 【Description】 Set iris control attributes. This function can realize settings for manual iris attributes and iris type parameters. 【Syntax】 `td_s32 ss_mpi_isp_set_iris_attr(ot_vi_pipe vi_pipe, const ot_isp_iris_attr *iris_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| iris\_attr | Pointer to the iris control attribute structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - Before conducting AI algorithm testing, it is recommended to confirm whether the AI circuit characteristics meet the recorder requirements.
- Set the correct iris type attribute based on the actual lens iris type being connected, and then set the relevant DC-Iris/P-Iris control attributes. If connecting a manual aperture lens, set the iris type to OT\_ISP\_IRIS\_DC\_TYPE, and it is recommended to disable AI in this case.
- The manual iris attribute is mainly used for debugging and can be set through this MPI. For P-Iris lenses, the manual iris\_fno value is affected by the maximum and minimum aperture target values. For more auto iris attribute parameters, call [ss\_mpi\_isp\_set\_dciris\_attr](#ZH-CN_TOPIC_0000002470924940) and [ss\_mpi\_isp\_get\_piris\_attr](#ZH-CN_TOPIC_0000002471084962) to configure. 【Example】 None 【Related Topics】 - [ot\_isp\_iris\_attr](#ot_isp_iris_attr)
- [ss\_mpi\_isp\_set\_dciris\_attr](#ss_mpi_isp_set_dciris_attr)
- [ss\_mpi\_isp\_set\_piris\_attr](#ss_mpi_isp_set_piris_attr) #### ss\_mpi\_isp\_get\_iris\_attr 【Description】 Get iris control attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_iris_attr(ot_vi_pipe vi_pipe, ot_isp_iris_attr *iris_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| iris\_attr | Pointer to the iris control attribute structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 None #### ss\_mpi\_isp\_set\_dciris\_attr 【Description】 Set the DC-Iris AI algorithm control attributes. This function can realize parameter settings for the DC-Iris auto iris. 【Syntax】 `td_s32 ss_mpi_isp_set_dciris_attr(ot_vi_pipe vi_pipe, const ot_isp_dciris_attr *dciris_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| dciris\_attr | Pointer to the DC-Iris auto iris control attribute structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - DC-Iris iris control uses a PID algorithm. The algorithm adjusts the PWM duty cycle to control the iris size based on the image brightness. When the exposure time and gain reach the minimum target values, it enters the iris control zone. When the iris control can meet the target brightness requirements, AE returns directly, keeping the exposure time and gain unchanged. When the image brightness stabilizes and the PWM duty cycle remains at the open value for a period, the AI algorithm considers the iris fully open, exits the iris control zone, and returns control to AE.
- When AI function is disabled, for DC-Iris lenses, the iris opens to maximum. 【Example】 None 【Related Topics】 - [ot\_isp\_iris\_attr](#ot_isp_iris_attr)
- [ot\_isp\_dciris\_attr](#ot_isp_dciris_attr) #### ss\_mpi\_isp\_get\_dciris\_attr 【Description】 Get the DC-Iris auto iris control attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_dciris_attr(ot_vi_pipe vi_pipe, ot_isp_dciris_attr *dciris_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| dciris\_attr | Pointer to the DC-Iris auto iris control attribute structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 None #### ss\_mpi\_isp\_set\_piris\_attr 【Description】 Set the P-Iris auto iris control attributes. 【Syntax】 `td_s32 ss_mpi_isp_set_piris_attr(ot_vi_pipe vi_pipe, const ot_isp_piris_attr *piris_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| piris\_attr | Pointer to the P-Iris auto iris control attribute structure. | Input |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 - The P-Iris auto iris control attribute contains a write-only parameter step\_fno\_table\_change. It is recommended to assign the structure first, call the set MPI once, then call the get MPI.
- P-Iris lens iris control is performed through the AE allocation route.
- When AI function is disabled, for P-Iris lenses, the iris opens to the maximum aperture target value corresponding to the stepper motor position.
- When using a single iris with multiple pipes, only one pipe can control the iris. 【Example】 `ot_vi_pipe vi_pipe = 0; ot_isp_piris_attr piris_attr, piris_attr_def; td_u16 total_step_def = 93; td_u16 step_count_def = 62; td_u16 step_fno_table_def[1024] = {30,35,40,45,50,56,61,67,73,79,85,92,98,105,112,120,127,135,143,150,158,166,174,183,191,200,208,217,225,234,243,252,261,270,279,289,298,307,316,325,335,344,353,362,372,381,390,399,408,417,426,435,444,453,462,470,478,486,493,500,506,512}; ot_isp_iris_f_no max_iris_fno_target_def = 9; ot_isp_iris_f_no min_iris_fno_target_def = 5; piris_attr_def. step_fno_table_change= TD_TRUE; piris_attr_def. zero_is_max= TD_TRUE; piris_attr_def. step_count= step_count_def; piris_attr_def. total_step= total_step_def; piris_attr_def. max_iris_fno_target = max_iris_fno_target_def; piris_attr_def. min_iris_fno_target = min_iris_fno_target_def; memcpy(piris_attr_def. step_fno_table, step_fno_table_def, sizeof(piris_attr_def. step_fno_table)); ss_mpi_isp_set_piris_attr (vi_pipe, &piris_attr_def); ss_mpi_isp_get_piris_attr (vi_pipe, &piris_attr);` 【Related Topics】 - [ot\_isp\_iris\_attr](#ot_isp_iris_attr)
- [ot\_isp\_piris\_attr](#ot_isp_piris_attr) #### ss\_mpi\_isp\_get\_piris\_attr 【Description】 Get the P-Iris auto iris control attributes. 【Syntax】 `td_s32 ss_mpi_isp_get_piris_attr(ot_vi_pipe vi_pipe, ot_isp_piris_attr *piris_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| vi\_pipe | vi\_pipe number. | Input |
| piris\_attr | Pointer to the P-Iris auto iris control attribute structure. | Output |

【Return Value】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure, the value is the error code. |

【Requirements】 - Header files: ot\_common\_isp.h, ss\_mpi\_isp.h, ss\_mpi\_ae.h
- Library files: libot\_isp.a, libss\_isp.a, libot\_ae.a 【Notes】 None 【Example】 None 【Related Topics】 None ## Data Types ### Register - [OT\_ISP\_HIST\_NUM](#ZH-CN_TOPIC_0000002470924896): Defines the number of histogram bins.
- [OT\_ISP\_AI\_MAX\_STEP\_FNO\_NUM](#ZH-CN_TOPIC_0000002470924950): Defines the maximum number of aperture steps.
- [ot\_isp\_ae\_sensor\_register](#ZH-CN_TOPIC_0000002504084731): Defines the sensor registration structure.
- [ot\_isp\_ae\_sensor\_exp\_func](#ZH-CN_TOPIC_0000002504084949): Defines the sensor callback function structure.
- [ot\_isp\_ae\_sensor\_default](#ZH-CN_TOPIC_0000002470924862): Defines the initialization parameter structure for the AE algorithm library.
- [ot\_isp\_ae\_accuracy\_type](#ZH-CN_TOPIC_0000002470924972): Defines the enumeration for precision types of exposure time and gain.
- [ot\_isp\_ae\_accuracy](#ZH-CN_TOPIC_0000002503964839): Defines the structure for precision of exposure time and gain. #### OT\_ISP\_HIST\_NUM 【Description】 Defines the number of histogram bins. 【Definition】 ```

# define OT\_ISP\_HIST\_NUM 1024[¶](#define-ot_isp_hist_num-1024 "锚链接")

`【Notes】 None. 【Related Data Types and Interfaces】 - ot_isp_fe_ae_stat_1
- ot_isp_be_ae_stat_1
- ot_isp_ae_stats
- ot_isp_ae_stitch_stats
- [ot_isp_exp_info](#ot_isp_exp_info) #### OT_ISP_AI_MAX_STEP_FNO_NUM<a name="ZH-CN_TOPIC_0000002470924950"></a> 【Description】 Defines the maximum number of aperture steps. 【Definition】`

# define OT\_ISP\_AI\_MAX\_STEP\_FNO\_NUM 1024[¶](#define-ot_isp_ai_max_step_fno_num-1024 "锚链接")

`【Notes】 None. 【Related Data Types and Interfaces】 [ot_isp_piris_attr](#ot_isp_piris_attr) #### ot_isp_ae_sensor_register<a name="ZH-CN_TOPIC_0000002504084731"></a> 【Description】 Defines the sensor registration structure. 【Definition】`
typedef struct { ot\_isp\_ae\_sensor\_exp\_func sns\_exp;
} ot\_isp\_ae\_sensor\_register;
``` 【Members】

| Member Name | Description |
| --- | --- |
| sns\_exp | Sensor registration callback function structure. |

【Notes】 Encapsulated for extensibility. 【Related Data Types and Interfaces】 [ot\_isp\_ae\_sensor\_exp\_func](#ot_isp_ae_sensor_exp_func) #### ot\_isp\_ae\_sensor\_exp\_func 【Description】 Defines the sensor callback function structure. 【Definition】 `typedef struct { td_s32 (*pfn_cmos_get_ae_default)(ot_vi_pipe vi_pipe, ot_isp_ae_sensor_default *ae_sns_dft); ot_void (*pfn_cmos_fps_set)(ot_vi_pipe vi_pipe, ot_float f32_fps, ot_isp_ae_sensor_default *ae_sns_dft); ot_void (*pfn_cmos_slow_framerate_set)(ot_vi_pipe vi_pipe, td_u32 full_lines, ot_isp_ae_sensor_default *ae_sns_dft); ot_void (*pfn_cmos_inttime_update)(ot_vi_pipe vi_pipe, td_u32 int_time); ot_void (*pfn_cmos_gains_update)(ot_vi_pipe vi_pipe, td_u32 again, td_u32 dgain); ot_void (*pfn_cmos_again_calc_table)(ot_vi_pipe vi_pipe, td_u32 *again_lin, td_u32 *again_db); ot_void (*pfn_cmos_dgain_calc_table)(ot_vi_pipe vi_pipe, td_u32 *dgain_lin, td_u32 *dgain_db); ot_void (*pfn_cmos_get_inttime_max)(ot_vi_pipe vi_pipe, td_u16 man_ratio_enable, td_u32 *ratio, ot_isp_ae_int_time_range *int_time, td_u32 *lf_max_int_time); ot_void (*pfn_cmos_ae_fswdr_attr_set)(ot_vi_pipe vi_pipe, ot_isp_ae_fswdr_attr *ae_fswdr_attr); ot_void (*pfn_cmos_ae_quick_start_status_set)(ot_vi_pipe vi_pipe, td_bool quick_start_status); ot_void (*pfn_cmos_exp_param_convert)(ot_vi_pipe vi_pipe, ot_isp_ae_convert_param *exp_param);
} ot_isp_ae_sensor_exp_func;` 【Members】

| Member Name | Description |
| --- | --- |
| pfn\_cmos\_get\_ae\_default | Callback function pointer to get the initial values of the AE algorithm library. |
| pfn\_cmos\_fps\_set | Sets the sensor frame rate. |
| pfn\_cmos\_slow\_framerate\_set | Sets the sensor frame dropping. |
| pfn\_cmos\_inttime\_update | Sets the sensor exposure time. |
| pfn\_cmos\_gains\_update | Sets the sensor analog gain and digital gain. |
| pfn\_cmos\_again\_calc\_table | Calculates TABLE type sensor analog gain. |
| pfn\_cmos\_dgain\_calc\_table | Calculates TABLE type sensor digital gain. |
| pfn\_cmos\_get\_inttime\_max | In WDR mode, callback function pointer to calculate the maximum short frame exposure time. |
| pfn\_cmos\_ae\_fswdr\_attr\_set | In LineWDR mode, sets the long frame mode. |
| pfn\_cmos\_ae\_quick\_start\_status\_set | Sets the AE no-photosensor quick start convergence status. |

【Notes】 - If a callback function pointer does not need to be assigned, it must be set to NULL.
- In [ot\_isp\_ae\_sensor\_default](#ZH-CN_TOPIC_0000002470924862), the precision of exposure time and gain is defined.
- When not using the no-photosensor quick start function, pfn\_cmos\_ae\_quick\_start\_status\_set must be set to NULL.
- quick\_start\_status is the flag for AE no-photosensor quick start convergence status. 【Related Data Types and Interfaces】 ot\_isp\_sensor\_register #### ot\_isp\_ae\_sensor\_default 【Description】 Defines the initialization parameter structure for the AE algorithm library. 【Definition】 `typedef struct { td_u8 ae_compensation; td_u32 lines_per500ms; td_u32 flicker_freq; ot_float fps; td_u32 hmax_times; td_u32 init_exposure; td_u32 init_int_time; td_u32 init_again; td_u32 init_dgain; td_u32 init_isp_dgain; td_u32 init_ae_speed; td_u32 init_ae_tolerance; td_u32 full_lines_std; td_u32 full_lines_max; td_u32 full_lines; td_u32 binning_full_lines; td_u32 max_int_time; td_u32 min_int_time; td_u32 max_int_time_target; td_u32 min_int_time_target; ot_isp_ae_accuracy int_time_accu; td_u32 max_again; td_u32 min_again; td_u32 max_again_target; td_u32 min_again_target; ot_isp_ae_accuracy again_accu; td_u32 max_dgain; td_u32 min_dgain; td_u32 max_dgain_target; td_u32 min_dgain_target; ot_isp_ae_accuracy dgain_accu; td_u32 max_isp_dgain_target; td_u32 min_isp_dgain_target; td_u32 isp_dgain_shift; td_u32 max_int_time_step; td_bool max_time_step_enable; td_u32 max_inc_time_step[OT_ISP_WDR_MAX_FRAME_NUM]; td_u32 max_dec_time_step[OT_ISP_WDR_MAX_FRAME_NUM]; td_u32 lf_max_short_time; td_u32 lf_min_exposure; ot_isp_ae_route ae_route_attr; td_bool ae_route_ex_valid; ot_isp_ae_route_ex ae_route_attr_ex; ot_isp_ae_route ae_route_sf_attr; ot_isp_ae_route_ex ae_route_sf_attr_ex; td_u16 man_ratio_enable; td_u32 arr_ratio[OT_ISP_EXP_RATIO_NUM]; ot_isp_iris_type iris_type; ot_isp_piris_attr piris_attr; ot_isp_iris_f_no max_iris_fno; ot_isp_iris_f_no min_iris_fno; ot_isp_ae_strategy ae_exp_mode; td_u16 iso_cal_coef; td_u8 ae_run_interval; td_u32 exp_ratio_max; td_u32 exp_ratio_min; td_bool diff_gain_support; ot_isp_quick_start_param quick_start; ot_isp_prior_frame prior_frame; td_bool ae_gain_sep_cfg; td_bool lhcg_support; td_u32 sns_lhcg_exp_ratio;
} ot_isp_ae_sensor_default;` 【Members】

| Member Name | Description |
| --- | --- |
| ae\_compensation | AE brightness target value, range [0,255], recommended 0x38~0x40. |
| lines\_per500ms | Total number of lines per 500ms. |
| flicker\_freq | Anti-flicker frequency, 256x power frequency. |
| fps | Base frame rate. |