---
title: MotionFusion
---

# MotionFusion

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/en/MotionFusion Development Reference/MotionFusion Development Reference.md
--- # Preface
**Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Revision History** The revision history cumulates documentation changes for each document update. The latest version of the document contains all updates from previous versions.

| Document Version | Release Date | Change Description |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First temporary version release. |

# Overview

## Overview MotionFusion refers to motion sensor fusion and compensation. It preprocesses data from motion measurement devices such as gyroscopes and accelerometers, and provides calibrated gyroscope data for image stabilization through calibration and compensation. ## Basic Concepts - **Zero Bias** In a stationary state, the expected values of Gyro angular velocity and ACC acceleration should be 0. However, due to device manufacturing process issues or system errors, there may still be non-zero values in a stationary state. This value is called zero bias. - **Temperature Drift** The zero bias value of a device may vary at different temperatures. The zero bias values corresponding to different temperatures are called temperature drift. - **Calibration** The process of calibrating the accuracy or precision of a gyroscope or accelerometer using standard measurement methods. Calibration can eliminate systematic errors caused by manufacturing processes, improve device accuracy or precision, and determine the static characteristic indicators of the device or measurement system. - **Six-Side Calibration** Calibrating Sensitivity Scale Factor Error and Crosstalk (axis crosstalk) issues of a gyroscope or accelerometer device caused by its own characteristics or installation. - **Online Calibration** The process of a device self-calibrating. During normal operation, the device automatically calibrates or compensates for its own measurement errors. # API Reference[¶](#overview-motionfusion-refers-to-motion-sensor-fusion-and-compensation-it-preprocesses-data-from-motion-measurement-devices-such-as-gyroscopes-and-accelerometers-and-provides-calibrated-gyroscope-data-for-image-stabilization-through-calibration-and-compensation-basic-concepts-zero-bias-in-a-stationary-state-the-expected-values-of-gyro-angular-velocity-and-acc-acceleration-should-be-0-however-due-to-device-manufacturing-process-issues-or-system-errors-there-may-still-be-non-zero-values-in-a-stationary-state-this-value-is-called-zero-bias-temperature-drift-the-zero-bias-value-of-a-device-may-vary-at-different-temperatures-the-zero-bias-values-corresponding-to-different-temperatures-are-called-temperature-drift-calibration-the-process-of-calibrating-the-accuracy-or-precision-of-a-gyroscope-or-accelerometer-using-standard-measurement-methods-calibration-can-eliminate-systematic-errors-caused-by-manufacturing-processes-improve-device-accuracy-or-precision-and-determine-the-static-characteristic-indicators-of-the-device-or-measurement-system-six-side-calibration-calibrating-sensitivity-scale-factor-error-and-crosstalk-axis-crosstalk-issues-of-a-gyroscope-or-accelerometer-device-caused-by-its-own-characteristics-or-installation-online-calibration-the-process-of-a-device-self-calibrating-during-normal-operation-the-device-automatically-calibrates-or-compensates-for-its-own-measurement-errors-api-reference "锚链接")

This functional module provides the following MPIs to the user: - [ss\_mpi\_mfusion\_set\_attr](#ZH-CN_TOPIC_0000002441701417): Sets the motionfusion attributes.
- [ss\_mpi\_mfusion\_get\_attr](#ZH-CN_TOPIC_0000002408102330): Gets the motionfusion attributes.
- [ss\_mpi\_mfusion\_set\_gyro\_drift](#ZH-CN_TOPIC_0000002408102362): Sets the Gyro zero bias.
- [ss\_mpi\_mfusion\_get\_gyro\_drift](#ZH-CN_TOPIC_0000002441701377): Gets the Gyro zero bias.
- [ss\_mpi\_mfusion\_set\_gyro\_six\_side\_calibration](#ZH-CN_TOPIC_0000002441701473): Sets the Gyro six-side calibration.
- [ss\_mpi\_mfusion\_get\_gyro\_six\_side\_calibration](#ZH-CN_TOPIC_0000002408262182): Gets the Gyro six-side calibration.
- [ss\_mpi\_mfusion\_set\_gyro\_temperature\_drift](#ZH-CN_TOPIC_0000002408262230): Sets the Gyro temperature drift parameters.
- [ss\_mpi\_mfusion\_get\_gyro\_temperature\_drift](#ZH-CN_TOPIC_0000002441701449): Gets the Gyro temperature drift parameters.
- [ss\_mpi\_mfusion\_set\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441661621): Sets the Gyro online temperature drift.
- [ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441701513): Gets the Gyro online temperature drift.
- [ss\_mpi\_mfusion\_set\_gyro\_online\_drift](#ZH-CN_TOPIC_0000002408102190): Sets the Gyro online zero bias.
- [ss\_mpi\_mfusion\_get\_gyro\_online\_drift](#ZH-CN_TOPIC_0000002408102286): Gets the Gyro online zero bias.
- [ss\_mpi\_mfusion\_bind\_vi](#ZH-CN_TOPIC_0000002408262258): Binds the fusion and pipe, chn.
- [ss\_mpi\_mfusion\_unbind\_vi](#ZH-CN_TOPIC_0000002408102254): Unbinds the fusion and pipe, chn. ## ss\_mpi\_mfusion\_set\_attr 【Description】 Sets the motionfusion attributes. 【Syntax】 `td_s32 ss_mpi_mfusion_set_attr(const td_u32 fusion_id, const ot_mfusion_attr *mfusion_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| fusion\_id | Fusion device ID number. Range: [0, 1]. | Input |
| mfusion\_attr | Pointer to motionfusion attributes. | Input |

【Return Values】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure. See [Error Codes](#ZH-CN_TOPIC_0000002441701493). |

【Requirements】 - Header files: ot\_common\_motionfusion.h, ss\_mpi\_motionfusion.h
- Library file: libss\_motionfusion.a 【Notes】 Magnetometer attribute settings are not currently supported. 【Example】 None. 【Related Topics】 None. ## ss\_mpi\_mfusion\_get\_attr 【Description】 Gets the motionfusion attributes. 【Syntax】 `td_s32 ss_mpi_mfusion_get_attr(const td_u32 fusion_id, ot_mfusion_attr *mfusion_attr);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| fusion\_id | Fusion device ID number. Range: [0, 1]. | Input |
| mfusion\_attr | Pointer to motionfusion attributes. | Output |

【Return Values】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure. See [Error Codes](#ZH-CN_TOPIC_0000002441701493). |

【Requirements】 - Header files: ot\_common\_motionfusion.h, ss\_mpi\_motionfusion.h
- Library file: libss\_motionfusion.a 【Notes】 None. 【Example】 None. 【Related Topics】 None. ## ss\_mpi\_mfusion\_set\_gyro\_drift 【Description】 Sets the Gyro zero bias. 【Syntax】 `td_s32 ss_mpi_mfusion_set_gyro_drift(const td_u32 fusion_id, const ot_mfusion_drift *gyro_drift);` 【Parameters】

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| fusion\_id | Fusion device ID number. Range: [0, 1]. | Input |
| gyro\_drift | Gyroscope zero bias enable switch; gyroscope zero bias parameter array including zero bias values for x, y, and z axes. | Input |

【Return Values】

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failure. See [Error Codes](#ZH-CN_TOPIC_0000002441701493). |

【Requirements】 - Header files: ot\_common\_motionfusion.h, ss\_mpi\_motionfusion.h
- Library file: libss\_motionfusion.a 【Notes】 - To maintain zero bias stability unaffected by any range, the configured zero bias parameter is the product of the gyroscope raw reading zero bias multiplied by the range.
- The zero bias calibration process is: at a typical operating temperature, the gyroscope is stationary. The readings for the x, y, and z axes are obtained and averaged. The average is then multiplied by the range to obtain the final zero bias.
- The Gyro zero bias function is mutually exclusive with the Gyro online zero bias, Gyro temperature drift parameters, and Gyro online temperature drift parameters. Once one function is enabled, the others cannot be enabled. 【Example】 None. 【Related Topics】 None. ## ss\_mpi\_mfusion\_get\_gyro\_drift 【Description】 Gets the Gyro zero bias. ... ## ss\_mpi\_mfusion\_set\_gyro\_six\_side\_calibration 【Description】 Sets the Gyro six-side calibration. ... ## ss\_mpi\_mfusion\_get\_gyro\_six\_side\_calibration 【Description】 Gets the Gyro six-side calibration. ... ## ss\_mpi\_mfusion\_set\_gyro\_temperature\_drift 【Description】 Sets the Gyro temperature drift parameters. ... ## ss\_mpi\_mfusion\_get\_gyro\_temperature\_drift 【Description】 Gets the Gyro temperature drift parameters. ... ## ss\_mpi\_mfusion\_set\_gyro\_online\_temperature\_drift 【Description】 Sets the Gyro online temperature drift parameters. ... ## ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift 【Description】 Gets the Gyro online temperature drift parameters. ... ## ss\_mpi\_mfusion\_set\_gyro\_online\_drift 【Description】 Sets the Gyro online zero bias. ... ## ss\_mpi\_mfusion\_get\_gyro\_online\_drift 【Description】 Gets the Gyro online zero bias. ... ## ss\_mpi\_mfusion\_bind\_vi 【Description】 Binds the fusion and pipe, chn. ... ## ss\_mpi\_mfusion\_unbind\_vi 【Description】 Unbinds the fusion and pipe, chn. ... ## Data Types ... ## Error Codes ...