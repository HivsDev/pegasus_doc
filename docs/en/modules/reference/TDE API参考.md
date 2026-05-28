---
title: TDE
---

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/TDE API参考/TDE API参考.md
--- # Preface
**Overview** This document mainly introduces the TDE API, data types, and Proc debug information. > **Note:**

> - Unless otherwise specified, is consistent with Hi3403V100. **Product Version** The product version corresponding to this document is as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Target Audience** This document is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions (see original document for icon images)** **Revision History** | Document Version | Release Date | Revision Description |
|---|---|---|
| 00B01 | 2025-09-15 | First interim release. | # Overview

## Overview Two Dimensional Engine (TDE) is a hardware acceleration module for 2D graphics operations. It provides functions such as bit block transfer, color fill, rectangle drawing, line drawing, rotation, scaling, de-flicker filtering, alpha blending, and colorkey operations. ## Module Loading ### Load Command ```[¶](#overview-two-dimensional-engine-tde-is-a-hardware-acceleration-module-for-2d-graphics-operations-it-provides-functions-such-as-bit-block-transfer-color-fill-rectangle-drawing-line-drawing-rotation-scaling-de-flicker-filtering-alpha-blending-and-colorkey-operations-module-loading-load-command "锚链接")

insmod tde.ko [parameters]
``` ### Parameters #### Parameter g\_is\_resize\_filter Controls whether to enable the resize filter. 0 = disable, 1 = enable (default). #### Parameter g\_max\_node\_num Sets the maximum number of job nodes. Default is 60. Range: [1, 64]. #### Parameter g\_tde\_tmp\_buf TDE temporary buffer address. Must be configured for certain operations. #### Parameter g\_rgb\_truncation\_mode Sets the RGB truncation mode. 0 = truncate low bits (default), 1 = truncate high bits. ## Reference Domain Description ### API Reference Domain The API descriptions use the following reference domains: Purpose, Syntax, Parameters, Description, Return Value, Note, Reference, Related Data Types, Error Code. ### Data Type Reference Domain Data type descriptions use: Definition, Description, Members, Note, Reference, Related Data Types. # API Reference

## API Overview The TDE module provides hardware-accelerated 2D graphics operations. All operations are submitted as jobs that can be processed synchronously or asynchronously. **Figure 1** TDE Software Flow **Function List:** | Category | Function | Description |[¶](#api-overview-the-tde-module-provides-hardware-accelerated-2d-graphics-operations-all-operations-are-submitted-as-jobs-that-can-be-processed-synchronously-or-asynchronously-figure-1-tde-software-flow-function-list-category-function-description "锚链接")

|---|---|---|
| Job Control | ss\_tde\_open | Open TDE device |
| | ss\_tde\_close | Close TDE device |
| | ss\_tde\_begin\_job | Begin a TDE job |
| | ss\_tde\_end\_job | End and submit a TDE job |
| | ss\_tde\_cancel\_job | Cancel a TDE job |
| | ss\_tde\_wait\_for\_done | Wait for a specific job to complete |
| | ss\_tde\_wait\_all\_done | Wait for all jobs to complete |
| | ss\_tde\_reset | Reset TDE hardware |
| Draw Operations | ss\_tde\_quick\_fill | Quick fill a rectangular area with color |
| | ss\_tde\_quick\_draw\_rect | Draw a rectangle outline |
| | ss\_tde\_draw\_multi\_rect | Draw multiple rectangles |
| | ss\_tde\_draw\_line | Draw lines |
| BitBLT Operations | ss\_tde\_quick\_copy | Quick copy image data |
| | ss\_tde\_quick\_resize | Resize image data |
| | ss\_tde\_bit\_blit | Bit block transfer with ROP |
| | ss\_tde\_mb\_blit | Multi-bit block transfer |
| | ss\_tde\_bitmap\_mask\_rop | Bitmap mask ROP operation |
| | ss\_tde\_bitmap\_mask\_blend | Bitmap mask blend operation |
| Special Operations | ss\_tde\_quick\_deflicker | De-flicker filter |
| | ss\_tde\_solid\_draw | Solid drawing with pattern |
| | ss\_tde\_rotate | Image rotation |
| | ss\_tde\_pattern\_fill | Pattern fill |
| Configuration | ss\_tde\_get\_deflicker\_level | Get de-flicker level |
| | ss\_tde\_set\_deflicker\_level | Set de-flicker level |
| | ss\_tde\_get\_alpha\_threshold\_value | Get alpha threshold value |
| | ss\_tde\_set\_alpha\_threshold\_value | Set alpha threshold value |
| | ss\_tde\_get\_alpha\_threshold\_state | Get alpha threshold state |
| | ss\_tde\_set\_alpha\_threshold\_state | Set alpha threshold state |
| | ss\_tde\_enable\_rgn\_deflicker | Enable regional de-flicker | ## Function Reference ### ss\_tde\_open [Purpose]
Open the TDE device and obtain a device handle. [Syntax]
```c

# include "ss\_tde.h"[¶](#include-ss_tdeh "锚链接")

td\_s32 ss\_tde\_open(void);
`[Parameters]
None. [Description]
Opens the TDE device. Must be called before any other TDE operations. Returns a handle that is used in subsequent TDE operations. [Return Value]
Returns a non-negative handle on success. Returns a negative value on failure. ### ss\_tde\_close<a name="ZH-CN_TOPIC_0000002441718445"></a> [Purpose]
Close the TDE device. [Syntax]`c
td\_s32 ss\_tde\_close(td\_s32 hTde);
`[Parameters]
- h Tde: TDE device handle obtained from ss\_tde\_open. [Description]
Closes the TDE device and releases related resources. ### ss\_tde\_begin\_job<a name="ZH-CN_TOPIC_0000002408279190"></a> [Purpose]
Begin a new TDE job. [Syntax]`c
td\_s32 ss\_tde\_begin\_job(td\_s32 hTde, ot\_tde\_handle *phJob);
`[Description]
Creates a new job handle for subsequent TDE operations. Multiple operations can be added to a single job. ### ss\_tde\_end\_job<a name="ZH-CN_TOPIC_0000002408279158"></a> [Purpose]
End and submit a TDE job for execution. [Syntax]`c
td\_s32 ss\_tde\_end\_job(td\_s32 hTde, ot\_tde\_handle hJob, td\_bool bSync, td\_bool bBlock, td\_u32 u32TimeOut);
`[Parameters]
- h Tde: TDE device handle.
- h Job: Job handle to submit.
- bSync: Synchronous (TD_TRUE) or asynchronous (TD_FALSE) execution.
- b Block: Blocking mode.
- u32Time Out: Timeout in milliseconds for blocking mode. ### ss\_tde\_cancel\_job<a name="ZH-CN_TOPIC_0000002408119222"></a> [Purpose]
Cancel a previously submitted TDE job. ### ss\_tde\_wait\_for\_done<a name="ZH-CN_TOPIC_0000002408279142"></a> [Purpose]
Wait for a specific TDE job to complete. ### ss\_tde\_wait\_all\_done<a name="ZH-CN_TOPIC_0000002408279162"></a> [Purpose]
Wait for all submitted TDE jobs to complete. ### ss\_tde\_reset<a name="ZH-CN_TOPIC_0000002441678533"></a> [Purpose]
Reset the TDE hardware. ### ss\_tde\_quick\_fill<a name="ZH-CN_TOPIC_0000002408279206"></a> [Purpose]
Quickly fill a rectangular area with a solid color. [Syntax]`c
td\_s32 ss\_tde\_quick\_fill(td\_s32 hTde, ot\_tde\_handle hJob, const ot\_tde\_surface* pstDst, const ot\_tde\_fill\_rect \*pstFillRect, td\_u32 u32Color);
``` [Description]
Fills the destination rectangle with the specified color. Supports RGB and ARGB color formats. ### ss\_tde\_quick\_draw\_rect [Purpose]
Draw a rectangle outline (border only). ### ss\_tde\_draw\_multi\_rect [Purpose]
Draw multiple rectangles in a single operation. ### ss\_tde\_draw\_line [Purpose]
Draw one or more lines between specified coordinates. ### ss\_tde\_quick\_copy [Purpose]
Quickly copy image data from source to destination surface. ### ss\_tde\_quick\_resize [Purpose]
Resize (scale) an image from source to destination rectangle. [Description]
Supports both upscaling and downscaling with configurable filter options. ### ss\_tde\_quick\_deflicker [Purpose]
Apply de-flicker filter to reduce flickering in interlaced displays. ### ss\_tde\_solid\_draw [Purpose]
Solid drawing operation with configurable pattern and alpha. ### ss\_tde\_rotate [Purpose]
Rotate an image by 0, 90, 180, or 270 degrees. ### ss\_tde\_bit\_blit [Purpose]
Bit block transfer with raster operation (ROP) codes. [Description]
Transfers source image data to destination with programmable ROP codes for combining source and destination pixel data. ### ss\_tde\_pattern\_fill [Purpose]
Fill a rectangle using a pattern image source. ### ss\_tde\_mb\_blit [Purpose]
Multi-block bit block transfer. ### ss\_tde\_bitmap\_mask\_rop [Purpose]
Bit block transfer with bitmap mask and ROP. ### ss\_tde\_bitmap\_mask\_blend [Purpose]
Bit block transfer with bitmap mask and alpha blending. ### ss\_tde\_get\_deflicker\_level / ss\_tde\_set\_deflicker\_level [Purpose]
Get/set the de-flicker filter level. ### ss\_tde\_get\_alpha\_threshold\_value / ss\_tde\_set\_alpha\_threshold\_value [Purpose]
Get/set the alpha threshold value for alpha comparison operations. ### ss\_tde\_get\_alpha\_threshold\_state / ss\_tde\_set\_alpha\_threshold\_state [Purpose]
Get/set the alpha threshold state (enabled/disabled). ### ss\_tde\_enable\_rgn\_deflicker [Purpose]
Enable or disable regional de-flicker for specific regions. # Data Type

## Data Structure Index The TDE module defines the following data types: - **ot\_tde\_handle**: TDE job handle type.[¶](#data-structure-index-the-tde-module-defines-the-following-data-types-ot_tde_handle-tde-job-handle-type "锚链接")

- **ot\_tde\_surface**: Defines a TDE surface, including physical address, virtual address, width, height, stride, and color format.
- **ot\_tde\_color\_format**: Enumeration of supported color formats (RGB565, RGB888, ARGB8888, etc.).
- **ot\_tde\_mb\_color\_format**: Color format for multi-block operations.
- **ot\_tde\_fill\_rect**: Rectangle definition for fill operations.
- **ot\_tde\_rect**: Generic rectangle structure with x, y, w, h.
- **ot\_tde\_point**: Point coordinate structure.
- **ot\_tde\_deflicker\_level**: De-flicker level enumeration.
- **ot\_tde\_alpha\_threshold**: Alpha threshold configuration structure.
- **ot\_tde\_rop\_code**: Raster operation code type. ## Color Format Mapping **Table 1** Color Format Mapping | ot\_tde\_color\_format | Description | Byte Order (in memory) |
 |---|---|---|
 | OT\_TDE\_COLOR\_FMT\_ARGB1555 | ARGB 1:5:5:5 | A1R5G5B5 |
 | OT\_TDE\_COLOR\_FMT\_ARGB4444 | ARGB 4:4:4:4 | A4R4G4B4 |
 | OT\_TDE\_COLOR\_FMT\_ARGB8888 | ARGB 8:8:8:8 | B0G0R0A0 |
 | OT\_TDE\_COLOR\_FMT\_RGB565 | RGB 5:6:5 | B5G6R5 | (For the complete color format list, refer to the header file ss\_tde.h.) ## Detailed Data Type Descriptions ### ot\_tde\_surface [Definition]
 `c
 typedef struct { td_u32 phys_addr; td_u32 virt_addr; td_u32 width; td_u32 height; td_u32 stride; ot_tde_color_format color_format; td_bool alpha_enable; td_u8 alpha0; td_u8 alpha1;
 } ot_tde_surface;` [Description]
 Defines a surface (image buffer) for TDE operations. [Members]
- phys\_addr: Physical address of the surface buffer.
- virt\_addr: Virtual address of the surface buffer.
- width: Width in pixels.
- height: Height in pixels.
- stride: Stride (bytes per line).
- color\_format: Color format of the surface.
- alpha\_enable: Whether global alpha is enabled.
- alpha0/alpha1: Global alpha values for the surface. ### ot\_tde\_color\_format [Definition]
 `c
 typedef enum { OT_TDE_COLOR_FMT_RGB565 = 0x0, OT_TDE_COLOR_FMT_ARGB1555, OT_TDE_COLOR_FMT_ARGB4444, OT_TDE_COLOR_FMT_ARGB8888, OT_TDE_COLOR_FMT_ARGB8888, /* ... additional formats */
 } ot_tde_color_format;` [Description]
 Enumeration of supported color formats for TDE surfaces. ### Additional Data Types Refer to the header files for complete definitions of ot\_tde\_fill\_rect, ot\_tde\_rect, ot\_tde\_point, ot\_tde\_deflicker\_level, and other related types. # Proc Debug Information TDE module debug information is available through: - `/proc/umap/tde`: Displays TDE job status, hardware utilization, error counts, and current configuration parameters. The proc output includes:
- TDE version information.
- Job queue status (queued, running, completed).
- Module parameters (resize filter, max node num, tmp buf, truncation mode).
- Per-operation statistics.