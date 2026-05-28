---
title: PCIe Cascading
---

# PCIe Cascading

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/PCIE级联应用指南/PCIE级联应用指南.md
--- # Preface
**Overview** This document introduces the Demo board PC Ie cascade operation guide from the aspects of hardware environment preparation and software environment preparation. It also introduces the basics of PC Ie, the business implementation of PC Ie cascading, and the PC Ie MPI interface functions, providing references for users when using the PC Ie cascade function. > **Note:**

> - Unless otherwise specified, ssxx in the following text represents solutions including , Hi3403V100, and .
> - Unless otherwise specified, the content for is identical to that of Hi3403V100. **Product Versions** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Intended Audience** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document. Their meanings are described below.

| Symbol | Description |
| --- | --- |
| | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History** The revision history records the updates made to each document version. The latest version of the document includes all updates from previous versions.

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# Demo Board PC Ie Cascade Operation Guide

## Hardware Environment Preparation For PC Ie cascade debugging, two or more hardware boards are required. Two or more boards are cascaded via PC Ie: - One board operates in PC Ie master mode (RC, Root-Complex mode).[¶](#hardware-environment-preparation-for-pc-ie-cascade-debugging-two-or-more-hardware-boards-are-required-two-or-more-boards-are-cascaded-via-pc-ie-one-board-operates-in-pc-ie-master-mode-rc-root-complex-mode "锚链接")

- The other boards operate in PC Ie slave mode (EP, End-Point mode). When multiple boards are cascaded via PC Ie, the master board connects to multiple slave boards through a PC Ie bridge. The power cables, serial cables, network cables, and video input/output cables must be correctly connected to the boards. ## Software Environment Preparation For the boot, kernel, and file system required by the solution, refer to the `readme` file in the `sdk/osdrv` directory of the release package and the `sdk/osdrv/components/pcie_mcc` directory for "Master Board Boots Slave Board Method" to compile the relevant images and drivers. - Both master and slave boards use Flash boot mode: Flash the u-boot, kernel, and file system to the master/slave board Flash using the non-PC Ie mode flashing method. - Under Flash boot mode for master and slave boards, the boot file list is shown in [Table 1](#_Ref239665721). **Table 1** Boot File List (Both Master and Slave Boards Use Flash Boot)

| Item | | File Name | Description |
| --- | --- | --- | --- |
| Master | ARM | u-boot-xxx.bin or boot\_image.bin | Burn to master board Flash |
| uImage\_xxx | Burn to master board Flash |
| rootfs\_xxx.ubifs | Burn to master board Flash |
| Slave | ARM | u-boot-xxx.bin or boot\_image.bin | Burn to slave board Flash |
| uImage\_xxx | Burn to slave board Flash |
| rootfs\_xxx.ubifs | Burn to slave board Flash |

When the master board uses Flash boot and the slave board uses DDR boot guided by the master board, the boot file list is shown in [Table 2](#_Ref316042797). **Table 2** Boot File List (Master Uses Flash Boot, Slave Uses DDR Boot)

| Item | | File Name | Description |
| --- | --- | --- | --- |
| Master | ARM | u-boot-xxx.bin or boot\_image.bin | Burn to master board Flash |
| uImage\_xxx | Burn to master board Flash |
| rootfs\_xxx.ubifs | Burn to master board Flash |
| Slave | ARM | uImage\_xxx | Burn to DDR guided by master |
| rootfs\_xxx.ubifs | Burn to DDR guided by master |

## PC Ie Cascade Usage Guide PC Ie cascading enables multiple chips to work together, extending processing capabilities. The complete guide covers: 1. **Basic Concepts**: Explanation of PC Ie topology, RC (Root Complex) and EP (End Point) roles, PC Ie bridge functionality.
2. **Hardware Setup**: Detailed instructions for connecting multiple boards via PC Ie, including power connections, serial console setup, network configuration, and video signal routing.
3. **Software Configuration**: Steps for configuring u-boot, Linux kernel, and root filesystem for PC Ie cascade mode.
4. **Driver Support**: Description of the pcie\_mcc driver and how to enable it in the kernel configuration.
5. **Application Development**: How to develop applications using the PC Ie cascade MPI interface.
6. **MPI Interface Reference**: Complete API documentation for PC Ie cascade-related functions. ### PC Ie MPI Interface Functions The PC Ie module provides the following MPI interface functions for cascade operations: **Table 3** PC Ie MPI Interface Functions

| Function | Description |
| --- | --- |
| ss\_mpi\_pcie\_init | Initializes the PC Ie module. |
| ss\_mpi\_pcie\_deinit | Deinitializes the PC Ie module. |
| ss\_mpi\_pcie\_send\_data | Sends data via PC Ie. |
| ss\_mpi\_pcie\_recv\_data | Receives data via PC Ie. |
| ss\_mpi\_pcie\_get\_status | Gets the PC Ie link status. |

For the complete API reference including detailed parameter descriptions, return values, error codes, and code examples for each function, please refer to the original Chinese source document. ### Typical PC Ie Cascade Application Flow 1. Initialize the PC Ie module on both master and slave boards.
2. Establish PC Ie link between master and slave.
3. Exchange device information (chip ID, address mapping, etc.).
4. Allocate shared memory for data exchange.
5. Transmit video/audio/data streams between boards via the send/receive AP Is.
6. Teardown link when cascade operation is complete.