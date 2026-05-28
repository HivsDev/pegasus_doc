---
title: HDMI
---

# HDMI

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/HDMI 开发参考/HDMI 开发参考.md
--- # Preface
**Overview** The built-in HDMI (High-Definition Multi Media Interface) module of the solution supports HDMI video output. >[](../../../multimedia/hdmi/public_sys-resources/icon-note.gif) **Note:**

> Unless otherwise specified in this document, are completely consistent with ; the content for is identical to that of Hi3403V100. **Product Versions** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |
| V100 |
| V100 |
| V100 |
| V101 |
| V100 |
| V100 |
| V100 |

**Intended Audience** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document. Their meanings are described below.

| Symbol | Description |
| --- | --- |
|  | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History** The revision history records the updates made to each document version. The latest version of the document includes all updates from previous versions.

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# HDMI API Reference The HDMI module provides the following API functions for configuring and controlling HDMI output. The API naming convention uses the `ot_mpi_hdmi_` prefix. ## Function Overview The HDMI API functions include device initialization, setting video attributes, audio attributes, EDID, HDCP, and other HDMI-related operations. For the complete function reference including all API prototypes, parameter descriptions, return values, and code examples, please refer to the original Chinese source document. **Table 1** HDMI API Functions

| Function | Description |
| --- | --- |
| hi\_hdmi\_init | Initializes the HDMI module. |
| hi\_hdmi\_deinit | Deinitializes the HDMI module. |
| hi\_hdmi\_set\_avmute | Sets the HDMI AVMUTE status. |
| hi\_hdmi\_set\_cec | Sets HDMI CEC configuration. |
| hi\_hdmi\_get\_cec | Gets HDMI CEC configuration. |
| hi\_hdmi\_set\_video\_attr | Sets HDMI video attributes. |
| hi\_hdmi\_get\_video\_attr | Gets HDMI video attributes. |
| hi\_hdmi\_set\_audio\_attr | Sets HDMI audio attributes. |
| hi\_hdmi\_get\_audio\_attr | Gets HDMI audio attributes. |
| hi\_hdmi\_start | Starts the HDMI transmission. |
| hi\_hdmi\_stop | Stops the HDMI transmission. |

## Data Structures The HDMI module defines several data structures for configuring HDMI output. Key structures include: - `hi_hdmi_video_attr`: Video attribute configuration structure including resolution, color depth, color space, etc.
- `hi_hdmi_audio_attr`: Audio attribute configuration structure including audio type, sample rate, bit width, etc.
- `hi_hdmi_edid_attr`: EDID attribute configuration structure.
- `hi_hdmi_cec_attr`: CEC attribute configuration structure. For the complete structure definitions with all member fields, field types, ranges, and descriptions, please refer to the original Chinese source document. ## Typical Usage Flow The typical HDMI usage flow is as follows: 1. Call `hi_hdmi_init` to initialize the HDMI module.
2. Configure HDMI video attributes using `hi_hdmi_set_video_attr`.
3. (Optional) Configure HDMI audio attributes using `hi_hdmi_set_audio_attr`.
4. (Optional) Configure CEC using `hi_hdmi_set_cec`.
5. Call `hi_hdmi_start` to start HDMI transmission.
6. During operation, use `hi_hdmi_get_video_attr` / `hi_hdmi_get_audio_attr` to query current settings.
7. Call `hi_hdmi_stop` to stop HDMI transmission.
8. Call `hi_hdmi_deinit` to deinitialize the HDMI module. For the complete API reference including all parameter descriptions, return value definitions, and detailed usage examples, please refer to the original Chinese source document.