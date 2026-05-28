---
title: GFBG
---

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/GFBG API 参考/GFBG API 参考.md
--- # Preface
**Overview** This document mainly introduces the GFBG API, data types, and Proc debug information. >[](../../../../reference/api/gfbg/public_sys-resources/icon-note.gif) **Note:**

> - Unless otherwise specified, is identical to Hi3403V100, and is identical to . **Product Version** The product version corresponding to this document is as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |
| V100 |
| V100 |
| V101 |
| V100 |
| V100 |

**Target Audience** This document is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document.

| Symbol | Description |
| --- | --- |
|  | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History**

| **Document Version** | **Release Date** | **Revision Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim release. |

# Overview

## Overview Graphic Framebuffer Group (GFBG) is a module of the digital media processing platform that manages image overlay layers. Based on Linux Framebuffer, it provides basic Linux Framebuffer functions and extends additional graphics layer control features such as inter-layer Alpha, origin setting, and FB extension modes. ## Reference Domain Description ### API Reference Domain This manual uses 9 reference domains to describe API information. Their functions are shown in [Table 1](#_Ref177443220). **Table 1** API Reference Domain Description [¶](#overview-graphic-framebuffer-group-gfbg-is-a-module-of-the-digital-media-processing-platform-that-manages-image-overlay-layers-based-on-linux-framebuffer-it-provides-basic-linux-framebuffer-functions-and-extends-additional-graphics-layer-control-features-such-as-inter-layer-alpha-origin-setting-and-fb-extension-modes-reference-domain-description-api-reference-domain-this-manual-uses-9-reference-domains-to-describe-api-information-their-functions-are-shown-in-table-1-table-1-api-reference-domain-description "锚链接")

| Reference Domain | Meaning |
| --- | --- |
| Purpose | Briefly describes the main function of the API. |
| Syntax | Lists the header files and API prototype declarations required to call the API. |
| Parameters | Lists API parameters, parameter descriptions, and parameter attributes. |
| Description | Briefly describes the working process of the API. |
| Return Value | Describes the return value of the API. |
| Note | Supplementary instructions and precautions. |
| Reference | Lists other API functions related to this API. |
| Related Data Types | Lists data types related to this API. |
| Error Code | Describes the error codes returned by the API. |

### Data Type Reference Domain **Table 1** Data Type Reference Domain Description

| Reference Domain | Meaning |
| --- | --- |
| Definition | Data structure or enumeration type definition. |
| Description | Describes the function of the data type. |
| Members | Describes the members of the data structure. |
| Note | Supplementary instructions and precautions. |
| Reference | Lists other API functions related to this data type. |
| Related Data Types | Lists data types related to this data type. |

# API Reference

## API Categories GFBG AP Is are mainly accessed through ioctl system calls on the Framebuffer device node (/dev/fbX). AP Is are divided into: - **Standard functions**: Linux standard Framebuffer ioctl operations.[¶](#api-categories-gfbg-ap-is-are-mainly-accessed-through-ioctl-system-calls-on-the-framebuffer-device-node-devfbx-ap-is-are-divided-into-standard-functions-linux-standard-framebuffer-ioctl-operations "锚链接")

- **Extended functions**: GFBG-specific extended ioctl operations, including general functions, layer control functions, and module parameter functions. ## ioctl Functions The GFBG module uses the Linux standard ioctl system call. The ioctl command format is as follows: ```

# include int ioctl(int fd, unsigned long request, ...);[¶](#include-int-ioctlint-fd-unsigned-long-request "锚链接")

`- **fd**: File descriptor of the Framebuffer device.
- **request**: The ioctl command code.
- **...**: Optional parameter (usually a pointer to a data structure). ## Standard Functions<a name="ZH-CN_TOPIC_0000002408095170"></a> ### FBIOGET\_VSCREENINFO<a name="ZH-CN_TOPIC_0000002408255078"></a> [Purpose]
Get the current framebuffer variable screen information. [Syntax]`

```
#include <linux/fb.h>
int ioctl(int fd, FBIOGET_VSCREENINFO, struct fb_var_screeninfo *var);
``` [Parameters]
- fd: Framebuffer device file descriptor.
- var: Pointer to the output struct fb_var_screeninfo. [Description]
This ioctl retrieves the current variable parameters of the framebuffer, including resolution, color depth, timing parameters, etc. [Return Value]
Returns 0 on success, -1 on error with errno set. ### FBIOPUT\_VSCREENINFO<a name="ZH-CN_TOPIC_0000002408255102"></a> [Purpose]
Set the framebuffer variable screen information. [Syntax]
```

`int ioctl(int fd, FBIOPUT_VSCREENINFO, struct fb_var_screeninfo *var);` [Description]
Sets the framebuffer's variable parameters. After changing parameters, the hardware may need to be reconfigured. ### FBIOGET\_FSCREENINFO [Purpose]
Get the framebuffer fixed screen information. ### FBIOPAN\_DISPLAY [Purpose]
Pan the display to a different position in the virtual screen buffer. [Description]
Used for double-buffering and smooth scrolling by changing the visible area's start offset. ## Extended Functions ### General Functions #### FBIOGET\_CAPABILITY\_GFBG [Purpose]
Get the capability information of the GFBG device. [Syntax]

```
#include <ss_ot_common.h>
int ioctl(int fd, FBIOGET_CAPABILITY_GFBG, ot_gfbg_capability *cap);
``` [Parameters]
- cap: Pointer to the output ot_gfbg_capability structure. [Description]
Returns the capabilities supported by the GFBG module, such as maximum layer count, supported mirror modes, alpha support, etc. #### FBIOGET\_SCREEN\_ORIGIN\_GFBG<a name="ZH-CN_TOPIC_0000002441694257"></a> [Purpose]
Get the current display origin (start position) of the graphics layer. [Syntax]
```

int ioctl(int fd, FBIOGET\_SCREEN\_ORIGIN\_GFBG, ot\_gfbg\_origin *origin);
`[Description]
Returns the X and Y coordinate offset of the current graphics layer. #### FBIOPUT\_SCREEN\_ORIGIN\_GFBG<a name="ZH-CN_TOPIC_0000002441654497"></a> [Purpose]
Set the display origin of the graphics layer. [Syntax]`
int ioctl(int fd, FBIOPUT\_SCREEN\_ORIGIN\_GFBG, ot\_gfbg\_origin* origin);
``` [Description]
Allows repositioning the graphics layer origin to achieve split-screen or overlay effects. #### FBIOGET\_SHOW\_GFBG [Purpose]
Get the current show/hide status of the graphics layer. #### FBIOPUT\_SHOW\_GFBG [Purpose]
Set the show/hide status of the graphics layer. #### FBIOGET\_MIRROR\_MODE [Purpose]
Get the current mirror mode of the graphics layer. #### FBIOPUT\_MIRROR\_MODE [Purpose]
Set the mirror mode of the graphics layer. #### FBIOGET\_ALPHA\_GFBG [Purpose]
Get the alpha blending configuration of the graphics layer. #### FBIOPUT\_ALPHA\_GFBG [Purpose]
Set the alpha blending configuration of the graphics layer. #### FBIOGET\_COLORKEY\_GFBG [Purpose]
Get the colorkey configuration of the graphics layer. #### FBIOPUT\_COLORKEY\_GFBG [Purpose]
Set the colorkey configuration of the graphics layer. #### FBIOGET\_DEFLICKER\_GFBG [Purpose]
Get the de-flicker configuration of the graphics layer. #### FBIOPUT\_DEFLICKER\_GFBG [Purpose]
Set the de-flicker configuration of the graphics layer. #### FBIOGET\_VER\_BLANK\_GFBG [Purpose]
Get the vertical blanking status. [Description]
Used to synchronize frame buffer updates with the display vertical blanking interval to avoid tearing. #### FBIOGET\_COLKEY\_MULTI\_GFBG / FBIOPUT\_COLKEY\_MULTI\_GFBG [Purpose]
Get/set multi-window colorkey configuration. #### FBIOPUT\_CSC\_GFBG / FBIOGET\_CSC\_GFBG [Purpose]
Get/set the CSC (Color Space Conversion) matrix for the graphics layer. #### FBIOGET\_LAYOUT\_GFBG / FBIOPUT\_LAYOUT\_GFBG [Purpose]
Get/set the GFBG layer layout configuration. [Description]
Configures the layer binding relationship with the VO device. #### FBIORESET\<X>\_GFBG (FBIORESET\_ALPHA\_GFBG, FBIORESET\_COLORKEY\_GFBG, etc.) [Purpose]
Reset specific GFBG parameters to their default values. ### Layer Function #### FBIOGET\_LAYER\_ID / FBIOPUT\_LAYER\_ID [Purpose]
Get/set the current operation layer ID for multi-layer GFBG configurations. (Additional layer-specific ioctls follow the same pattern for alpha, colorkey, show, origin, etc., but with layer ID applied.) ### Module Parameter Function Module parameters can be configured when loading the gfbg.ko module, or through proc file system interfaces at runtime. # Data Type

## GFBG Capability ### ot\_gfbg\_capability [Definition][¶](#gfbg-capability-ot_gfbg_capability-definition "锚链接")

`c
typedef struct { ot_gfbg_layer layer_id; ot_gfbg_bool mirror; ot_gfbg_bool colorkey; ot_gfbg_bool alphablend; unsigned int max_layer_num;
} ot_gfbg_capability;` [Description]
Describes the capability information of the GFBG device. [Members]
- layer\_id: Supported graphics layer ID.
- mirror: Whether mirror mode is supported.
- colorkey: Whether colorkey is supported.
- alphablend: Whether alpha blending is supported.
- max\_layer\_num: Maximum number of graphics layers. ### ot\_gfbg\_alpha [Definition]
`c
typedef struct { ot_gfbg_alpha_flag alpha_flag; unsigned int alpha0; unsigned int alpha1;
} ot_gfbg_alpha;` [Description]
Alpha blending configuration structure for GFBG layers. ### ot\_gfbg\_colorkey [Definition]
`c
typedef struct { unsigned int key; unsigned char mask_r; unsigned char mask_g; unsigned char mask_b; unsigned char mask_alpha;
} ot_gfbg_colorkey;` [Description]
Colorkey configuration structure. Pixels matching the colorkey become transparent. ### Additional Data Types The GFBG API defines additional data types for mirror mode, origin, CSC matrix, layout configuration, and multi-window colorkey. Refer to the header files for complete definitions. # Proc Debug Information GFBG provides debug information through the proc file system: - `/proc/umap/gfbg`: Displays overall GFBG status, including layer configurations, alpha settings, colorkey settings, mirror modes, and current display status. Note: In heterogeneous systems, VO runs on the Lite OS side while GFBG runs on the Linux side. When a graphics layer is closed, the default CSC parameters are restored. The VO proc information may temporarily not reflect GFBG layer updates.