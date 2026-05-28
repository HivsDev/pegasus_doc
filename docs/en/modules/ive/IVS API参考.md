---
title: IVS
---

# IVS

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/IVS API参考/IVS API参考.md
--- # Preface
**Overview** This document is written for programmers developing recognition analysis solutions using IVS. It is intended to provide reference information supported by IVS during development, including AP Is, header files, error codes, etc. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |
| V100 |

**Intended Audience** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document, and their meanings are described below.

| **Symbol** | **Description** |
| --- | --- |
|  | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History**

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release |

# Overview

## Overview IVS (Intelligent Video Surveillance) is a higher-level recognition video capture application API compared to IVE (Intelligent Video Engine). Users can quickly develop related recognition applications based on IVS. The recognition applications currently supported by IVS include: MD (Motion Detection). # MD[¶](#overview-ivs-intelligent-video-surveillance-is-a-higher-level-recognition-video-capture-application-api-compared-to-ive-intelligent-video-engine-users-can-quickly-develop-related-recognition-applications-based-on-ivs-the-recognition-applications-currently-supported-by-ivs-include-md-motion-detection-md "锚链接")

## Functional Description ### Motion Detection Motion detection detects the motion state of a video by detecting changes in video brightness, producing video detection analysis results. #### Basic Concepts - MD Algorithm The MD algorithm includes two types: frame difference method (MD\_ALG\_MODE\_REF) and background method (MD\_ALG\_MODE\_BG). - Frame Difference Method (MD\_ALG\_MODE\_REF) An algorithm that directly uses the user-specified image as a reference frame to produce video detection analysis results is called the frame difference method. - Background Method (MD\_ALG\_MODE\_BG) During MD processing, a background image of the current video is generated. An algorithm that then uses the background image as a reference frame to produce video detection analysis results is called the background method. - Background Update Weight When the MD algorithm is set to the background method, each MD process generates a static partial image. This partial image and the background undergo a pixel value overlay. New background = (static partial image overlay weight x static partial image + dynamic partial image overlay weight y old background) >> 16. > **Caution:**[¶](#functional-description-motion-detection-motion-detection-detects-the-motion-state-of-a-video-by-detecting-changes-in-video-brightness-producing-video-detection-analysis-results-basic-concepts-md-algorithm-the-md-algorithm-includes-two-types-frame-difference-method-md_alg_mode_ref-and-background-method-md_alg_mode_bg-frame-difference-method-md_alg_mode_ref-an-algorithm-that-directly-uses-the-user-specified-image-as-a-reference-frame-to-produce-video-detection-analysis-results-is-called-the-frame-difference-method-background-method-md_alg_mode_bg-during-md-processing-a-background-image-of-the-current-video-is-generated-an-algorithm-that-then-uses-the-background-image-as-a-reference-frame-to-produce-video-detection-analysis-results-is-called-the-background-method-background-update-weight-when-the-md-algorithm-is-set-to-the-background-method-each-md-process-generates-a-static-partial-image-this-partial-image-and-the-background-undergo-a-pixel-value-overlay-new-background-static-partial-image-overlay-weight-x-static-partial-image-dynamic-partial-image-overlay-weight-y-old-background-16-caution "锚链接")

> If using a 64-bit operating system, the MMZ address used must be within a 4 GB space, otherwise exceptions may occur. ## API Reference The MD API provides basic interfaces for initialization, exit, handle acquisition, handle release, background acquisition, and detection processing. This functional module provides the following AP Is: - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309): Initialization.
> - [ss\_ivs\_md\_exit](#ZH-CN_TOPIC_0000002408134148): Exit.
> - [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333): Creates an MD channel.
> - [ss\_ivs\_md\_destroy\_chn](#ZH-CN_TOPIC_0000002441853505): Destroys an MD channel.
> - [ss\_ivs\_md\_set\_chn\_attr](#ZH-CN_TOPIC_0000002408294068): Sets MD channel attributes.
> - [ss\_ivs\_md\_get\_chn\_attr](#ZH-CN_TOPIC_0000002408294052): Gets MD channel attributes.
> - [ss\_ivs\_md\_get\_bg](#ZH-CN_TOPIC_0000002408134192): Gets the background.
> - [ss\_ivs\_md\_proc](#ZH-CN_TOPIC_0000002441733297): Detection processing. ### ss\_ivs\_md\_init [Description] Initializes motion detection. [Syntax] `td_s32 ss_ivs_md_init(td_void)；` [Parameters] None. [Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - Before calling other MD interfaces, this interface must be called first for initialization, and it only needs to be called once. Otherwise, an error is returned.
- This interface must be used together with [ss\_ivs\_md\_exit](#ZH-CN_TOPIC_0000002408134148). [Example] None. [Related Topics] [ss\_ivs\_md\_exit](#ss_ivs_md_exit) ### ss\_ivs\_md\_exit [Description] Exits motion detection. [Syntax] `td_s32 ss_ivs_md_exit(td_void);` [Parameters] None. [Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization before calling this interface to exit. Otherwise, an error is returned. [Example] None. [Related Topics] [ss\_ivs\_md\_init](#ss_ivs_md_init) ### ss\_ivs\_md\_create\_chn [Description] Creates an MD channel. [Syntax] `td_s32 ss_ivs_md_create_chn(ot_md_chn md_chn, ot_md_attr *md_attr);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| md\_chn | Channel number. Valid range: [0, 63] | Input |
| md\_attr | Channel information pointer.  Must not be NULL. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_chn\_attr](#ss_ivs_md_get_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_destroy\_chn [Description] Destroys an MD channel. [Syntax] `td_s32 ss_ivs_md_destroy_chn(ot_md_chn md_chn);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| md\_chn | Channel number. Valid range: [0, 63] | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_chn\_attr](#ss_ivs_md_get_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_set\_chn\_attr [Description] Sets MD channel attributes. [Syntax] `td_s32 ss_ivs_md_set_chn_attr(ot_md_chn md_chn, ot_md_attr *md_attr);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| md\_chn | Channel number. Valid range: [0, 63] | Input |
| md\_attr | Channel information pointer.  Must not be NULL. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned.
- Static channel attributes (alg\_mode, sad\_mode, width, height) cannot be changed; they must match the values used when the channel was created. Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_get\_chn\_attr](#ss_ivs_md_get_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_get\_chn\_attr [Description] Gets MD channel attributes. [Syntax] `td_s32 ss_ivs_md_get_chn_attr(ot_md_chn md_chn, ot_md_attr *md_attr);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| md\_chn | Channel number. Valid range: [0, 63] | Input |
| md\_attr | Channel information pointer.  Must not be NULL. | Output |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_get\_bg [Description] Gets the motion detection background. [Syntax] `td_s32 ss_ivs_md_get_bg(ot_md_chn md_chn, ot_svp_dst_img *bg);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| md\_chn | Channel number. Valid range: [0, 63] | Input |

| Parameter Name | Supported Image Type | Address Alignment | Resolution |
| --- | --- | --- | --- |
| bg | OT\_SVP\_IMG\_TYPE\_U8C1 | 16 byte | 64x64 to 1920x1080 |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned.
- Background data can only be retrieved when using the background method. Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_proc [Description] Motion detection processing. [Syntax] `td_s32 ss_ivs_md_proc(ot_md_chn md_chn, ot_svp_src_img *cur, ot_svp_src_img *ref, ot_svp_dst_img *sad, ot_svp_dst_mem_info *blob)；` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| md\_chn | Channel number. Valid range: [0, 63] | Input |
| cur | Current frame image pointer; must not be NULL.  For detailed definitions, see Section 3.1 of the "IVE API Reference". | Input |
| ref | Reference frame image pointer; must not be NULL.  For detailed definitions, see Section 3.1 of the "IVE API Reference". | Input |
| sad | Sad pointer.  Based on md\_attr-> sad\_out\_ctrl, if output is required, must not be NULL.  For detailed definitions, see Section 3.1 of the "IVE API Reference". | Output |
| blob | Region information pointer.  Must not be NULL.  For detailed definitions, see Section 1.4 of the "SV Px.0 API Reference". | Output |

| Parameter Name | Supported Image Type | Address Alignment | Resolution |
| --- | --- | --- | --- |
| cur | OT\_SVP\_IMG\_TYPE\_U8C1 | 16 byte | 64x64 to 1920x1080 |
| ref | OT\_SVP\_IMG\_TYPE\_U8C1 | 16 byte | 64x64 to 1920x1080 |
| sad | OT\_SVP\_IMG\_TYPE\_U8C1/ OT\_SVP\_IMG\_TYPE\_U16C1 | 16 byte | Based on md\_attr->sad\_mode, corresponds to 4x4, 8x8, 16x16 block modes, with height and width being 1/4, 1/8, or 1/16 of cur respectively. |
| blob | -- | 16 byte | -- |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408294036). |

[Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned.
- The maximum number of output region information entries is 254. For region information, see the data type ot\_ive\_ccblob in Section 3 of the "IVE API Reference". The cur\_area\_threshold in the info member of ot\_ive\_ccblob is the area threshold information after block division. The connected region information output here is stored contiguously.
- In the same thread, after completing initialization and channel creation, call the ss\_ivs\_md\_proc interface only once for the same channel. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg) ## MD Data Types ### ot\_md\_alg\_mode [Description] Defines the MD algorithm mode. [Definition] `typedef enum { OT_MD_ALG_MODE_BG = 0x0,/*Base on background img*/ OT_MD_ALG_MODE_REF = 0x1,/*Base on reference img*/ OT_MD_ALG_MODE_BUTT
}ot_md_alg_mode;` [Members]

| Member Name | Description |
| --- | --- |
| OT\_MD\_ALG\_MODE\_BG | Background method. |
| OT\_MD\_ALG\_MODE\_REF | Frame difference method. |

[Notes] None. [Related Data Types and Interfaces] None. ### ot\_md\_attr [Description] Defines MD channel attributes. [Definition] `typedef struct { ot_md_alg_mode alg_mode; /*Md algorithm mode*/ ot_ive_sad_mode sad_mode; /*Sad mode*/ ot_ive_sad_out_ctrl sad_out_ctrl; /*Sad output ctrl*/ td_u32 width; /*Img width*/ td_u32 height; /*Img height*/ td_u16 sad_threshold; /*Sad thresh*/ ot_ive_ccl_ctrl ccl_ctrl; /*Ccl ctrl*/ ot_ive_add_ctrl add_ctrl; /*Add ctrl*/
}ot_md_attr` [Members]

| Member Name | Description |
| --- | --- |
| alg\_mode | Algorithm mode. |
| sad\_mode | Sad mode. For detailed definitions, see Section 3.3 of the "IVE API Reference". |
| sad\_out\_ctrl | Sad output control. For detailed definitions, see Section 3.3 of the "IVE API Reference".  Only supports OT\_IVE\_SAD\_OUT\_CTRL\_16BIT\_BOTH, OT\_IVE\_SAD\_OUT\_CTRL\_8BIT\_BOTH, and OT\_IVE\_SAD\_OUT\_CTRL\_THRESHOLD output controls. |
| width | Image width. Must be an even multiple of the macroblock width. Range: [64, 1920] |
| height | Image height. Must be an even multiple of the macroblock height. Range: [64, 1080] |
| sad\_threshold | Sad threshold.  Value depends on sad\_out\_ctrl:   1. OT\_IVE\_SAD\_OUT\_CTRL\_8BIT\_BOTH, range [0, 255] 2. OT\_IVE\_SAD\_OUT\_CTRL\_16BIT\_BOTH and OT\_IVE\_SAD\_OUT\_CTRL\_THRESHOLD, range [0, 65535] |
| ccl\_ctrl | CCL control parameters. For detailed definitions, see Section 3.3 of the "IVE API Reference". CCL control parameter member information applies to the image after block division. |
| add\_ctrl | Add control parameters. For detailed definitions, see Section 3.3 of the "IVE API Reference". |

[Notes] None. [Related Data Types and Interfaces] None. ## Error Codes IVS error codes mostly share the same definitions as IVE error codes. The first part of the IVS error code table is identical to that in the "IVE API Reference", with additional special codes listed at the end. **Table 1** IVS error codes

| Error Code | Macro Definition | Description |
| --- | --- | --- |
| 0xa01d8001 | OT\_ERR\_IVE\_INVALID\_DEV\_ID | Device ID is out of valid range |
| 0xa01d8003 | OT\_ERR\_IVE\_INVALID\_CHN\_ID | Channel group number error or invalid region handle |
| 0xa01d8007 | OT\_ERR\_IVE\_ILLEGAL\_PARAM | Parameter is out of valid range |
| 0xa01d8008 | OT\_ERR\_IVE\_EXIST | Attempting to create an already existing device, channel, or resource |
| 0xa01d8009 | OT\_ERR\_IVE\_UNEXIST | Attempting to use or destroy a non-existent device, channel, or resource |
| 0xa01d800a | OT\_ERR\_IVE\_NULL\_PTR | NULL pointer in function parameters |
| 0xa01d800b | OT\_ERR\_IVE\_NOT\_CFG | Module not configured |
| 0xa01d800c | OT\_ERR\_IVE\_NOT\_SUPPORT | Unsupported parameter or function |
| 0xa01d800d | OT\_ERR\_IVE\_NOT\_PERM | Operation not permitted, e.g., attempting to modify static configuration parameters |
| 0xa01d8014 | OT\_ERR\_IVE\_NO\_MEM | Memory allocation failed, e.g., insufficient system memory |
| 0xa01d8015 | OT\_ERR\_IVE\_NO\_BUF | Buffer allocation failed, e.g., requested image buffer too large |
| 0xa01d8016 | OT\_ERR\_IVE\_BUF\_EMPTY | No image in buffer |
| 0xa01d8017 | OT\_ERR\_IVE\_BUF\_FULL | Buffer is full of images |
| 0xa01d8018 | OT\_ERR\_IVE\_NOT\_READY | System not initialized or corresponding module not loaded |
| 0xa01d8021 | OT\_ERR\_IVE\_BAD\_ADDR | Illegal address |
| 0xa01d8022 | OT\_ERR\_IVE\_BUSY | System busy |
| 0xa01d8040 | OT\_ERR\_IVE\_SYS\_TIMEOUT | IVE system timeout |
| 0xa01d8041 | OT\_ERR\_IVE\_QUERY\_TIMEOUT | Query timeout |
| 0xa01d8042 | OT\_ERR\_IVE\_BUS\_ERR | Bus error |
| 0xa01d8043 | OT\_ERR\_IVE\_OPEN\_FILE | Failed to open file |
| 0xa01d8044 | OT\_ERR\_IVE\_READ\_FILE | Failed to read file |
| 0xa0308003 | OT\_ERR\_ODT\_INVALID\_CHN\_ID | ODT channel group number error or invalid region handle |
| 0xa0308008 | OT\_ERR\_ODT\_EXIST | Attempting to create an already existing device, channel, or resource |
| 0xa0308009 | OT\_ERR\_ODT\_UNEXIST | Attempting to use or destroy a non-existent device, channel, or resource |
| 0xa030800d | OT\_ERR\_ODT\_NOT\_PERM | Operation not permitted, e.g., attempting to modify static configuration parameters |
| 0xa0308018 | OT\_ERR\_ODT\_NOT\_READY | ODT not initialized |
| 0xa0308022 | OT\_ERR\_ODT\_BUSY | ODT system busy |

## Proc Debug Information ### Overview Debug information uses the proc file system under Linux, which can reflect the current operating status of the system in real time. The recorded information can be used for problembitbit and analysis. [File Directory] /proc/umap [Information Viewing Method] - On the console, you can use the cat command to view information. `cat /proc/umap/md` can view the MD proc information. Other commonly used file operation commands can also be used, for example, `cp /proc/umap/md ./` to copy the file to the current directory.
- In an application, the above files can be treated as ordinary read-only files for read operations, such as fopen, fread, etc. >[](../../../../reference/api/ivs/public_sys-resources/icon-note.gif) **Note:**

> The following 2 situations should be noted when describing parameters:
> - For parameters with values of {0, 1}, if the specific mapping between values and meanings is not listed, a value of 1 indicates affirmative, and 0 indicates negative.
> - For parameters with values of {aaa, bbb, ccc}, if the specific mapping between values and meanings is not listed, the parameter meaning can be directly determined based on the values aaa, bbb, or ccc. ### MD Proc Information Description [Debug Information] `~ # cat /proc/umap/md
> [MD] Version: [Vx.x.x.x B0xx Release], Build Time[Feb 20 2020, 16:42:49] ---------------------------md chn attr-----------------------------------
> no. w h alg sad_mode sad_out_ctrl sad_thr ccl_mode ccl_init_thr 0 720 576 0 0 0 200 1 16 ccl_step xwt ywt frm_rate cost_tm_per_frm
> 4 32768 32768 0 2625` [Debug Information Analysis] Records the working status information of MD. [Parameter Description]

| Parameter | | Description |
| --- | --- | --- |
| md chn attr  Channel attributes | no. | Channel number. |
| alg | Working algorithm.  0: Background method;  1: Frame difference method. |
| sad\_mode | Sad mode.  0: 4x4 macroblock;  1: 8x8 macroblock;  2: 16x16 macroblock. |
| sad\_out\_ctrl | Sad output control.  0: OT\_IVE\_SAD\_OUT\_CTRL\_16BIT\_BOTH;  1: OT\_IVE\_SAD\_OUT\_CTRL\_8BIT\_BOTH;  4: OT\_IVE\_SAD\_OUT\_CTRL\_THRESHOLD. |
| sad\_thr | Sad threshold. |
| ccl\_mode | CCL mode.  0: 4-connected;  1: 8-connected. |
| ccl\_init\_thr | CCL initial threshold. |
| ccl\_step | CCL step. |
| xwt | Background method update X weight. |
| ywt | Background method update Y weight. |
| frm\_rate | Frame rate. |
| cost\_tm\_per\_frm | Time per frame (unit: us).  **Note: Frame rate and time per frame are calculated every 10 seconds.** |