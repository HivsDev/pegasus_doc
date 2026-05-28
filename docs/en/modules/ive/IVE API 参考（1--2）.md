---
title: IVE API 1–2
---

# IVE API 1–2

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/IVE API Reference/IVE API Reference (1-2).md
--- # Preface
**Overview** This document is written for programmers developing recognition and analysis solutions using the IVE co-processor of the media processing chip. It is intended to provide various reference information supported by the IVE co-processor during development, including APIs, header files, error codes, Proc information, etc. > **Note:** > Unless otherwise specified in this document, the content for and Hi3403V100 is identical. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Target Audience** This document (guide) is primarily intended for the following engineers: - Technical support engineers
- Software development engineers **Symbol Conventions** The following symbols may appear in this document, with their meanings described below.

| **Symbol** | **Description** |
| --- | --- |
| | Indicates a high-risk hazard which, if not avoided, will result in death or serious injury. |

**Change History**

| Document Version | Date | Description |
| --- | --- | --- |
| 00B01 | 2024-12-27 | First release. |

# Overview

## Overview IVE (Identification Video Engine) is a hardware acceleration module in the media processing chip recognition and analysis system. Users developing recognition and analysis solutions based on IVE can accelerate recognition and analysis while reducing CPU usage. The operators currently provided by IVE can support the development of video diagnosis, perimeter prevention, and other recognition and analysis solutions. ## Function Description ### Important Concepts - Handle: When a user calls an operator to create a task, the system assigns a handle to each task to identify different tasks. - Immediate return flag is\_instant: After creating a task, if the user wants to be notified promptly when the task is completed, set is\_instant to TD\_TRUE when creating the task. Otherwise, if the user does not care whether the task is completed, it is recommended to set is\_instant to TD\_FALSE, allowing chained execution with subsequent tasks, reducing interrupt count and improving performance. - Query: The user calls ss\_mpi\_ive\_query with the handle returned by the system to check whether the corresponding operator task is completed. - Timely cache flush: The IVE hardware can only obtain data from DDR. If the access space is cacheable and the CPU has previously accessed it when calling an IVE task, to prevent IVE input/output data from being interfered with by the CPU cache, the user needs to call the ss\_mpi\_sys\_mmz\_flush\_cache interface to flush the cache (see the MPP Media Processing Software Vx.y Development Reference for details), flushing data from cache to DDR for IVE use. - Stride: A measure consistent with the width of an image or two-dimensional data, as shown in [Figure 1](#fig1615616519207). - ot\_svp\_img image data stride: represents the number of units calculated as "pixels" per row of the image. The pixel bit width can be 8bit, 16bit, etc. - ot\_svp\_data two-dimensional data stride: represents the number of bytes per row of two-dimensional data. ot\_svp\_img can be viewed as an image where one "pixel" is represented by 8bit, so stride is uniformly expressed as the number of units calculated as "pixels" per row of the image or two-dimensional data. **Figure 1** Stride Diagram - Alignment: To quickly access memory start addresses or cross-row data, the hardware requires that memory addresses or memory strides must be multiples of the alignment coefficient. - Data memory start address alignment: Current IVE operators have requirements for 1-byte alignment, 2-byte alignment, and 16-byte alignment for their inputs and outputs. Refer to the parameter requirements in each operator's API reference. - Stride alignment: For two-dimensional generalized images, two-dimensional single-component data, and one-dimensional array data, the stride must satisfy 16 "pixel" alignment. > **Note:** > When using DDR4, to improve memory access efficiency, it is recommended to use 256-byte alignment for the start address and odd multiples of 256 "pixels" for stride alignment. If using a 64-bit operating system, the MMZ address used must be within a 4GB space, otherwise an exception will occur. - Input/Output Data Types: - Two-dimensional generalized image data: ot\_svp\_img, ot\_svp\_src\_img, ot\_svp\_dst\_img. Image types refer to ot\_svp\_img\_type. - Two-dimensional single-component data: ot\_svp\_data, two-dimensional data in bytes, mainly used for DMA, etc. - One-dimensional data: ot\_svp\_mem\_info, ot\_svp\_src\_mem\_info, ot\_svp\_dst\_mem\_info. # API ReferenceThe IVE module provides basic interfaces for creating tasks and querying tasks. This functional module provides the following MPIs: - [ss\_mpi\_ive\_dma](#ZH-CN_TOPIC_0000002504091099): Create a direct memory access task.[¶](#overview-ive-identification-video-engine-is-a-hardware-acceleration-module-in-the-media-processing-chip-recognition-and-analysis-system-users-developing-recognition-and-analysis-solutions-based-on-ive-can-accelerate-recognition-and-analysis-while-reducing-cpu-usage-the-operators-currently-provided-by-ive-can-support-the-development-of-video-diagnosis-perimeter-prevention-and-other-recognition-and-analysis-solutions-function-description-important-concepts-handle-when-a-user-calls-an-operator-to-create-a-task-the-system-assigns-a-handle-to-each-task-to-identify-different-tasks-immediate-return-flag-is_instant-after-creating-a-task-if-the-user-wants-to-be-notified-promptly-when-the-task-is-completed-set-is_instant-to-td_true-when-creating-the-task-otherwise-if-the-user-does-not-care-whether-the-task-is-completed-it-is-recommended-to-set-is_instant-to-td_false-allowing-chained-execution-with-subsequent-tasks-reducing-interrupt-count-and-improving-performance-query-the-user-calls-ss_mpi_ive_query-with-the-handle-returned-by-the-system-to-check-whether-the-corresponding-operator-task-is-completed-timely-cache-flush-the-ive-hardware-can-only-obtain-data-from-ddr-if-the-access-space-is-cacheable-and-the-cpu-has-previously-accessed-it-when-calling-an-ive-task-to-prevent-ive-inputoutput-data-from-being-interfered-with-by-the-cpu-cache-the-user-needs-to-call-the-ss_mpi_sys_mmz_flush_cache-interface-to-flush-the-cache-see-the-mpp-media-processing-software-vxy-development-reference-for-details-flushing-data-from-cache-to-ddr-for-ive-use-stride-a-measure-consistent-with-the-width-of-an-image-or-two-dimensional-data-as-shown-in-figure-1-ot_svp_img-image-data-stride-represents-the-number-of-units-calculated-as-pixels-per-row-of-the-image-the-pixel-bit-width-can-be-8bit-16bit-etc-ot_svp_data-two-dimensional-data-stride-represents-the-number-of-bytes-per-row-of-two-dimensional-data-ot_svp_img-can-be-viewed-as-an-image-where-one-pixel-is-represented-by-8bit-so-stride-is-uniformly-expressed-as-the-number-of-units-calculated-as-pixels-per-row-of-the-image-or-two-dimensional-data-figure-1-stride-diagram-alignment-to-quickly-access-memory-start-addresses-or-cross-row-data-the-hardware-requires-that-memory-addresses-or-memory-strides-must-be-multiples-of-the-alignment-coefficient-data-memory-start-address-alignment-current-ive-operators-have-requirements-for-1-byte-alignment-2-byte-alignment-and-16-byte-alignment-for-their-inputs-and-outputs-refer-to-the-parameter-requirements-in-each-operators-api-reference-stride-alignment-for-two-dimensional-generalized-images-two-dimensional-single-component-data-and-one-dimensional-array-data-the-stride-must-satisfy-16-pixel-alignment-note-when-using-ddr4-to-improve-memory-access-efficiency-it-is-recommended-to-use-256-byte-alignment-for-the-start-address-and-odd-multiples-of-256-pixels-for-stride-alignment-if-using-a-64-bit-operating-system-the-mmz-address-used-must-be-within-a-4gb-space-otherwise-an-exception-will-occur-inputoutput-data-types-two-dimensional-generalized-image-data-ot_svp_img-ot_svp_src_img-ot_svp_dst_img-image-types-refer-to-ot_svp_img_type-two-dimensional-single-component-data-ot_svp_data-two-dimensional-data-in-bytes-mainly-used-for-dma-etc-one-dimensional-data-ot_svp_mem_info-ot_svp_src_mem_info-ot_svp_dst_mem_info-api-referencethe-ive-module-provides-basic-interfaces-for-creating-tasks-and-querying-tasks-this-functional-module-provides-the-following-mpis-ss_mpi_ive_dma-create-a-direct-memory-access-task "锚链接")

- [ss\_mpi\_ive\_filter](#ZH-CN_TOPIC_0000002470931284): Create a 5x5 template filter task.
- [ss\_mpi\_ive\_csc](#ZH-CN_TOPIC_0000002470931294): Create a color space conversion task.
- [ss\_mpi\_ive\_filter\_and\_csc](#ZH-CN_TOPIC_0000002470931218): Create a composite filter and color space conversion task.
- [ss\_mpi\_ive\_sobel](#ZH-CN_TOPIC_0000002471091284): Create a 5x5 template sobel-like gradient computation task.
- [ss\_mpi\_ive\_mag\_and\_ang](#ZH-CN_TOPIC_0000002470931308): Create a 5x5 template gradient magnitude and angle computation task.
- [ss\_mpi\_ive\_dilate](#ZH-CN_TOPIC_0000002503971205): Create a dilation task.
- [ss\_mpi\_ive\_erode](#ZH-CN_TOPIC_0000002503971269): Create an erosion task.
- [ss\_mpi\_ive\_threshold](#ZH-CN_TOPIC_0000002471091326): Create an image binarization task.
- [ss\_mpi\_ive\_and](#ZH-CN_TOPIC_0000002504091087): Create a binary image AND task.
- [ss\_mpi\_ive\_sub](#ZH-CN_TOPIC_0000002503971163): Create a grayscale image subtraction task.
- [ss\_mpi\_ive\_or](#ZH-CN_TOPIC_0000002471091296): Create a binary image OR task.
- [ss\_mpi\_ive\_integ](#ZH-CN_TOPIC_0000002470931322): Create an integral image statistics task.
- [ss\_mpi\_ive\_hist](#ZH-CN_TOPIC_0000002504091123): Create a histogram statistics task.
- [ss\_mpi\_ive\_threshold\_s16](#ZH-CN_TOPIC_0000002470931220): Create an s16 to 8-bit data thresholding task.
- [ss\_mpi\_ive\_threshold\_u16](#ZH-CN_TOPIC_0000002470931242): Create a u16 to u8 data thresholding task.
- [ss\_mpi\_ive\_16bit\_to\_8bit](#ZH-CN_TOPIC_0000002471091216): Create a 16-bit to 8-bit linear conversion task.
- [ss\_mpi\_ive\_order\_stats\_filter](#ZH-CN_TOPIC_0000002504091093): Create a 3x3 template order statistics filter task.
- [ss\_mpi\_ive\_map](#ZH-CN_TOPIC_0000002470931234): Create a Map (mapping u8->u8 / u8->u16 / u8->s16 assignment) task.
- [ss\_mpi\_ive\_equalize\_hist](#ZH-CN_TOPIC_0000002471091322): Create a grayscale image histogram equalization task.
- [ss\_mpi\_ive\_add](#ZH-CN_TOPIC_0000002504091171): Create a weighted addition of two grayscale images task.
- [ss\_mpi\_ive\_xor](#ZH-CN_TOPIC_0000002504091203): Create a binary image XOR task.
- [ss\_mpi\_ive\_ncc](#ZH-CN_TOPIC_0000002503971167): Create a normalized cross-correlation computation for two same-resolution images task.
- [ss\_mpi\_ive\_ccl](#ZH-CN_TOPIC_0000002504091151): Create a connected component labeling for binary images task.
- [ss\_mpi\_ive\_gmm](#ZH-CN_TOPIC_0000002503971147): Create a GMM background modeling task.
- [ss\_mpi\_ive\_gmm2](#ZH-CN_TOPIC_0000002504091155): Create a GMM2 background modeling task.
- [ss\_mpi\_ive\_canny\_hys\_edge](#ZH-CN_TOPIC_0000002503971215): Create a Canny strong/weak edge extraction for grayscale images task.
- [ss\_mpi\_ive\_canny\_edge](#ZH-CN_TOPIC_0000002470931286): Create the second half of Canny edge extraction: connect edge points to form a Canny edge map.
- [ss\_mpi\_ive\_lbp](#ZH-CN_TOPIC_0000002503971201): Create an LBP computation task.
- [ss\_mpi\_ive\_norm\_grad](#ZH-CN_TOPIC_0000002503971195): Create a normalized gradient computation task, with all gradient components normalized to s8.
- [ss\_mpi\_ive\_lk\_optical\_flow\_pyr](#ZH-CN_TOPIC_0000002504091135): Create a multi-layer pyramid Lucas-Kanade optical flow computation task.
- [ss\_mpi\_ive\_st\_cand\_corner](#ZH-CN_TOPIC_0000002471091320): Create the first half of Shi-Tomasi-like corner detection: compute candidate corners.
- [ss\_mpi\_ive\_st\_corner](#ZH-CN_TOPIC_0000002470931280): Create the second half of Shi-Tomasi-like corner detection: select corners according to rules.
- [ss\_mpi\_ive\_sad](#ZH-CN_TOPIC_0000002471091328): Compute 4x4/8x8/16x16 block-based 16-bit/8-bit SAD images and threshold the SAD output.
- [ss\_mpi\_ive\_resize](#ZH-CN_TOPIC_0000002503971235): Create an image resize task.