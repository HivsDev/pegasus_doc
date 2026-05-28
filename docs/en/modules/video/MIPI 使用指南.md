---
title: MIPI
---

# MIPI

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/MIPI User Guide/MIPI User Guide.md
--- # Preface
**Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

> **Note:** >This document uses the Hi3403V100 description as an example. Unless otherwise specified, the content for is consistent with Hi3403V100. **Target Audience** This document (guide) is primarily applicable to the following engineers: - Technical Support Engineer
> - Software Development Engineer **Symbol Conventions** The following symbols may appear in this document, and their meanings are as follows.

| Symbol | Description |
| --- | --- |
| | Indicates a high-level risk hazard that, if not avoided, will result in death or serious injury. |

**Revision History** The revision history accumulates descriptions of each document update. The latest version of the document includes updates from all previous document versions.

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# MIPI User Guide

## Overview MIPI Rx receives raw video data through low-voltage differential signals, converts the received serial differential signal into DC (Digital Camera) timing, and then passes it to the next-level module VICAP (Video Capture). MIPI Rx supports serial video signal inputs such as MIPI D-PHY, LVDS (Low-Voltage Differential Signal), HiSPi (High-Speed Serial Pixel Interface), and is also compatible with the DC video interface. ## Important Concepts - MIPI MIPI stands for Mobile Industry Processor Interface. The MIPI interface described in this document specifically refers to a communication interface that uses D-PHY transmission specification at the physical layer and CSI-2 at the protocol layer. - LVDS LVDS stands for Low-Voltage Differential Signaling. It uses synchronization codes to distinguish between blanking intervals and valid data. - Lane A pair of high-speed differential lines used to connect the transmitter and receiver. It can be either a clock Lane or a data Lane. - Synchronization Code The MIPI interface uses short packets within CSI-2 for synchronization. LVDS uses synchronization codes to distinguish valid data from blanking intervals. LVDS has two synchronization methods: - Using SOF/EOF to indicate frame start and end, and SOL/EOL to indicate line start and end. The synchronization method is shown in [Figure 1](#fig9405124663417). **Figure 1** SOF/EOF/SOL/EOL Synchronization Method - Using SAV(invalid) EAV(invalid) to indicate the start and end of invalid data in the blanking interval, and SAV(valid) EAV(valid) to indicate the start and end of valid pixel data. Each synchronization code consists of 4 fields, each with a bit width consistent with the pixel data bit width. The first 3 fields are fixed reference code words, and the 4th field is determined by the sensor manufacturer. Since different sensors may have different synchronization codes, the synchronization code must be configured according to the sensor. The synchronization method is shown in [Figure 2](#fig1737184853619). **Figure 2** SAV/EAV Synchronization Method ## Functional Description MIPI Rx is a capture unit that supports multiple differential video input interfaces. It receives data from MIPI/LVDS/sub-LVDS/HiSPi/DC interfaces through combo-PHY. By configuring different functional modes, MIPI Rx can support data transmission at various speeds and resolutions, and support multiple external input devices. The maximum number of supported Lanes is shown in [Table 1](#_Ref484179711). **Table 1** Maximum Number of Supported Lanes [¶](#overview-mipi-rx-receives-raw-video-data-through-low-voltage-differential-signals-converts-the-received-serial-differential-signal-into-dc-digital-camera-timing-and-then-passes-it-to-the-next-level-module-vicap-video-capture-mipi-rx-supports-serial-video-signal-inputs-such-as-mipi-d-phy-lvds-low-voltage-differential-signal-hispi-high-speed-serial-pixel-interface-and-is-also-compatible-with-the-dc-video-interface-important-concepts-mipi-mipi-stands-for-mobile-industry-processor-interface-the-mipi-interface-described-in-this-document-specifically-refers-to-a-communication-interface-that-uses-d-phy-transmission-specification-at-the-physical-layer-and-csi-2-at-the-protocol-layer-lvds-lvds-stands-for-low-voltage-differential-signaling-it-uses-synchronization-codes-to-distinguish-between-blanking-intervals-and-valid-data-lane-a-pair-of-high-speed-differential-lines-used-to-connect-the-transmitter-and-receiver-it-can-be-either-a-clock-lane-or-a-data-lane-synchronization-code-the-mipi-interface-uses-short-packets-within-csi-2-for-synchronization-lvds-uses-synchronization-codes-to-distinguish-valid-data-from-blanking-intervals-lvds-has-two-synchronization-methods-using-sofeof-to-indicate-frame-start-and-end-and-soleol-to-indicate-line-start-and-end-the-synchronization-method-is-shown-in-figure-1-figure-1-sofeofsoleol-synchronization-method-using-savinvalid-eavinvalid-to-indicate-the-start-and-end-of-invalid-data-in-the-blanking-interval-and-savvalid-eavvalid-to-indicate-the-start-and-end-of-valid-pixel-data-each-synchronization-code-consists-of-4-fields-each-with-a-bit-width-consistent-with-the-pixel-data-bit-width-the-first-3-fields-are-fixed-reference-code-words-and-the-4th-field-is-determined-by-the-sensor-manufacturer-since-different-sensors-may-have-different-synchronization-codes-the-synchronization-code-must-be-configured-according-to-the-sensor-the-synchronization-method-is-shown-in-figure-2-figure-2-saveav-synchronization-method-functional-description-mipi-rx-is-a-capture-unit-that-supports-multiple-differential-video-input-interfaces-it-receives-data-from-mipilvdssub-lvdshispidc-interfaces-through-combo-phy-by-configuring-different-functional-modes-mipi-rx-can-support-data-transmission-at-various-speeds-and-resolutions-and-support-multiple-external-input-devices-the-maximum-number-of-supported-lanes-is-shown-in-table-1-table-1-maximum-number-of-supported-lanes "锚链接")

| Solution | Maximum Number of Lanes |
| --- | --- |
| Hi3403V100 | MIPI Rx supports up to 8-Lane MIPI input or 8-Lane LVDS input. |

MIPI Rx can interface with multiple sensors simultaneously. The maximum number of sensors is shown in [Table 2](#_Ref502909111). **Table 2** Maximum Number of Connected Sensors

| Solution | Number of Sensors |
| --- | --- |
| Hi3403V100 | 4 |

MIPI Rx can interface with different numbers of sensors simultaneously, and each sensor may require a different number of Lanes. Therefore, users need to determine the LANE distribution mode of MIPI Rx. For specific Lane distribution modes, please refer to [Table 3](#_Toc468799631). **Table 3** MIPI Rx Lane Distribution Mode

| Solution | Mode | DEV0 | DEV1 | DEV2 | DEV3 |
| --- | --- | --- | --- | --- | --- |
| Hi3403V100 | 0 | L0~L7 | N | N | N |

For detailed MIPI Rx Lane pin connections, please refer to [Table 4](#_Ref484014656). **Table 4** MIPI Rx Lane Pin Relationship

| Solution | LANE | MIPI0 | MIPI1 | MIPI2 | MIPI3 |
| --- | --- | --- | --- | --- | --- |
| Hi3403V100 | Lane0 | Yes | - | - | - |
| Lane1 | Yes | Yes | - | - |