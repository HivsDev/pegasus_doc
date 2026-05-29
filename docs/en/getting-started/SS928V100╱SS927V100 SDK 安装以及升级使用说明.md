---
title: Install the SDK
---

# Install the SDK

title: "Hi3403V100 SDK Installation and Upgrade Guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/Hi3403V100╱ SDK 安装以及升级使用说明/Hi3403V100╱ SDK 安装以及升级使用说明.md
--- # Preface
**Overview** This document describes the installation and upgrade procedures for the Hi3403V100 SDK, enabling users to quickly set up the SDK runtime environment on the corresponding chip's DEMB board. > **Note:** >This document uses Hi3403V100 as the reference. Unless otherwise specified, the content applies equally to . **Product Versions** The product versions corresponding to this document are listed below.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Intended Audience** This document is primarily intended for the following engineers: - Technical support engineers
- Software development engineers **Symbol Conventions** The following symbols may appear in this document with the meanings described below.

| **Symbol** | **Description** |
| --- | --- |
| | Indicates a high-risk hazard that, if not avoided, will result in death or serious injury. |

**Revision History**

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First preliminary release. |

# First-Time SDK Installation
<a name="ZH-CN_TOPIC_0000002457836393"></a>If you have already installed the SDK, refer directly to [Installing and Upgrading the Hi3403V100 DEMO Board Development Environment](#ZH-CN_TOPIC_0000002457836393). ## Hi3403V100 SDK Package Location Under the `Hi3403V100R001***/01.software/board` directory, you will find a file named `Hi3403V100_SDK_Vx.x.x.x.tgz`. This is the software development kit for Hi3403V100. ## Extracting the SDK Package On a Linux server (or a PC running Linux — any mainstream distribution is supported), run `tar -zxf Hi3403V100_SDK_Vx.x.x.x.tgz` to extract the archive. This produces a directory named `Hi3403V100_SDK_Vx.x.x.x`. ## Unpacking the SDK Contents Navigate into the `Hi3403V100_SDK_Vx.x.x.x` directory and run `./sdk.unpack` (as root or with sudo) to expand the compressed contents of the SDK package. Follow the on-screen prompts to complete the operation. If you need to copy the SDK package via a Windows system, first run `./sdk.cleanup` to repack the contents, copy to the new location, then expand again. ## Setting Up the Development Environment on a Linux Server Refer to the *Open Harmony Small Version User Guide*. ## Building osdrv Refer to the readme file in the osdrv directory. ## SDK Directory Structure The `Hi3403V100_SDK_Vx.x.x.x` directory structure is as follows: ├── smp #smp directory │ ├── a55\_linux │ ├── interdrv #mipitx and other driver source code │ ├── vendor #peripheral driver source code │ ├── mpp │ │ ├── component │ │ │ ├── gfbg #gfbg source code │ │ │ ├── security\_subsys #security subsystem source code │ │ │ └── pciv #pciv source code │ │ ├── cbb │ │ │ └── isp #isp source code │ │ ├── out #mpp build output directory │ │ ├── ko #kernel ko modules │ │ ├── lib #user-space lib libraries │ │ ├── include #header files │ │ ├── init #kernel module initialization source code │ │ └── obj #kernel module obj files │ └── osal #OS abstraction layer source code │ ├── include #OS abstraction layer header files │ └── linux #Linux OS adaptation layer source files │ ├── dsp\_liteos #DSP driver ├── open\_source #open-source third-party source code │ ├── u-boot #U-Boot source code │ ├── linux #kernel source code │ ├── eigen #eigen source code │ ... ├── platform #platform code │ ├── liteos #Lite OS code package ├── osdrv #OS-related directory │ ├── components #proprietary component source code │ ├── pub #pre-built images and binaries │ ├── rootfs\_scripts #filesystem initialization directories and scripts │ ├── tools #system tool source code ├── package #SDK compressed packages │ ├── smp.tgz #media processing platform software package │ ├── osdrv.tgz #OS-related package │ ├── platform.tgz #platform code package │ └── open\_source.tgz #third-party open-source software package ├── scripts #shell scripts directory ├── sdk.cleanup #SDK cleanup script └── sdk.unpack #SDK unpack script # Installing and Upgrading the Hi3403V100 DEMO Board Development Environment
If you are using an Hi3403V100 DEMO board, you can flash U-Boot, the kernel, and the filesystem using the following procedures. All operations below use the network for updates: - If the board does not have U-Boot, use the tool at `01.software/pc/Tool Platform` to flash it. For detailed flashing instructions, refer to the *Burn Tool User Guide* located in the `01.software/pc/Tool Platform` directory.
- If the board already has U-Boot, follow the steps below to flash U-Boot, kernel, and rootfs to Flash via the network interface. The DEMO board boots from SPI Flash by default. ## Configuring the TFTP Server You can use any TFTP server. First build U-Boot, kernel, and rootfs, then copy the resulting files to the TFTP server's root directory. ## Parameter Configuration After powering on the board, press any key to enter U-Boot. Set serverip (the TFTP server IP), ipaddr (the board IP), and ethaddr (the board's MAC address). `setenv serverip xx.xx.xx.xx
setenv ipaddr xx.xx.xx.xx
setenv ethaddr xx:xx:xx:xx:xx:xx
setenv netmask xx.xx.xx.xx
setenv gatewayip xx.xx.xx.xx
ping serverip (verify network connectivity)` > **Notice:** >- Hi3403V100 supports two boot modes: fast boot (using `u-boot-Hi3403V100.bin`) and non-fast boot (non-secure/secure boot, using `boot_image.bin`). See Chapter 2 "Boot Modes" in the *Hi3403V100 Secure Boot User Guide*.

> - The boot mode can be confirmed by reading register `0x10122090`. A value of `0x5` indicates fast boot; any other value indicates non-fast boot.
> - Boards ship with "non-secure boot" as the default. The following instructions use this mode as the example. ## Flashing Image Files to SPI Nor Flash Using a 32 MB SPI Nor Flash as an example. Address space layout:

| | | | |
| --- | --- | --- | --- |
| 1MB | 11MB | 19MB | 1MB |
| boot\_image.bin | kernel | rootfs | sample.bin |

The following operations are based on the address space layout shown above. Adjust as needed for your actual configuration. 1. Flash U-Boot `sf probe 0 mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 boot_image.bin sf probe 0 sf erase 0 0x100000 sf write 0x42000000 0 0x100000 reset` 2. Flash kernel `mw.b 0x42000000 0xff 0xb00000 tftp 0x42000000 uImage_Hi3403V100 sf probe 0 sf erase 0x100000 0xb00000 sf write 0x42000000 0x100000 0xb00000` 3. Flash filesystem `mw.b 0x42000000 0xff 0x1300000 tftp 0x42000000 rootfs_Hi3403V100_64k.jffs2 sf probe 0 sf erase 0xc00000 0x1300000 sf write 0x42000000 0xc00000 0x1300000` 4. Flash Lite OS image (optional) `mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 sample.bin sf probe 0 sf erase 0x1f00000 0x100000 sf write 0x42000000 0x1f00000 0x100000` 5. Set boot parameters `setenv bootargs 'mem=512M console=tty AMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),11M(kernel),19M(rootfs),1M(sample.bin)';sa setenv bootcmd 'sf probe 0;sf read 0x44000000 0x1f00000 0x100000;go_riscv 0x44000000; sf read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa Without Lite OS: setenv bootargs 'mem=512M console=tty AMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),11M(kernel),19M(rootfs) ';sa setenv bootcmd 'sf probe 0; sf read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa` ## Flashing Image Files to NAND Flash Using a 64 MB NAND Flash as an example. Address space layout:

| | | | |
| --- | --- | --- | --- |
| 1MB | 11MB | 32MB | 1MB |
| boot\_image.bin | kernel | rootfs | sample.bin |

The following operations are based on the address space layout shown above. Adjust as needed for your actual configuration. 1. Flash U-Boot `mw.b 0x42000000 0xff 0x100000 tftp 42000000 boot_image.bin nand erase 0 0x100000 nand write 0x42000000 0 0x100000 reset` 1. Flash kernel `mw.b 0x42000000 0xff 0xb00000 tftp 0x42000000 uImage_Hi3403V100 nand erase 0x100000 0xb00000 nand write 0x42000000 0x100000 0xb00000` 2. Flash filesystem `mw.b 0x42000000 0xff 0x2000000 tftp 0x42000000 rootfs_Hi3403V100_2k_128k_32M.ubifs nand erase 0xc00000 0x2000000 nand write 0x42000000 0xc00000 0x2000000` 3. Flash Lite OS image (optional) `mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 sample.bin nand erase 0x2c00000 0x100000 nand write 0x42000000 0x2c00000 0x100000` 4. Set boot parameters `setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),11M(kernel),32M(rootfs.ubifs),1M(sample)';sa setenv bootcmd 'nand read 0x44000000 0x2c00000 0x100000;go_riscv 0x44000000;nand read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa Without Lite OS: setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),11M(kernel),32M(rootfs.ubifs) ';sa setenv bootcmd 'nand read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa` ## Flashing Image Files to EMMC Address space layout:

| | | | |
| --- | --- | --- | --- |
| 1MB | 11MB | 96MB | 1MB |
| boot\_image.bin | kernel | rootfs | sample.bin |

<a name="ZH-CN_TOPIC_0000002457876529"></a><a name="ZH-CN_TOPIC_0000002424357662"></a>The following operations are based on the address space layout shown above. Adjust as needed for your actual configuration. 1. Flash U-Boot `mw.b 0x42000000 0xff 0x100000 tftp 42000000 boot_image.bin mmc write 0 0x42000000 0 0x800 reset` 2. Flash kernel `mw.b 0x42000000 0xff 0xb00000 tftp 0x42000000 uImage_Hi3403V100 mmc write 0 0x42000000 0x800 0x5800` 3. Flash filesystem `mw.b 0x42000000 0xff 0x6000000 tftp 0x42000000 rootfs_Hi3403V100_96M.ext4 mmc write 0 0x42000000 0x6000 0x30000` 4. Flash Lite OS image (optional) `mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 sample.bin mmc write 0 0x42000000 0x36000 0x800` 5. Set boot parameters `setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(uboot.bin),11M(kernel),96M(rootfs.ext4),1M(sample)';sa setenv bootcmd ' mmc read 0 0x44000000 0x36000 0x800;go_riscv 0x44000000;mmc read 0 0x50000000 0x800 0x5800; bootm 50000000';sa Without Lite OS: setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(uboot.bin),11M(kernel),96M(rootfs.ext4)';sa setenv bootcmd 'mmc read 0 0x50000000 0x800 0x5800; bootm 50000000';sa` > **Notice:** >Adjust the image sizes in the commands for [Flashing Image Files to SPI Nor Flash](#ZH-CN_TOPIC_0000002424357662) through [Flashing Image Files to EMMC](#ZH-CN_TOPIC_0000002457876529) to match the actual image sizes. The default Lite OS boot address is `0x44000000`. If the customer's memory layout differs, adjust the Lite OS boot address accordingly. If Lite OS is not used, customers can adjust the Linux boot address instead. ## Booting the New System reset # Reboot to enter the new system. # Pre-Development Environment Setup

## Pin Multiplexing Pin multiplexing related to media services, DDR priority configuration, and similar settings are configured in the `interdrv/sys_config` open-source driver (managed via Linux DTS). If the configuration does not match your hardware, you can modify it directly. The `sys_config.ko` driver is called by `load_Hi3403V100` and is executed before MPP kernel modules are loaded. Pin multiplexing for non-MPP peripherals is configured uniformly in U-Boot. For details, refer to the *Hi3403V100 U-Boot Porting and Application Development Guide*. # Development Using the SDK and DEMO Board[¶](#pin-multiplexing-pin-multiplexing-related-to-media-services-ddr-priority-configuration-and-similar-settings-are-configured-in-the-interdrvsys_config-open-source-driver-managed-via-linux-dts-if-the-configuration-does-not-match-your-hardware-you-can-modify-it-directly-the-sys_configko-driver-is-called-by-load_hi3403v100-and-is-executed-before-mpp-kernel-modules-are-loaded-pin-multiplexing-for-non-mpp-peripherals-is-configured-uniformly-in-u-boot-for-details-refer-to-the-hi3403v100-u-boot-porting-and-application-development-guide-development-using-the-sdk-and-demo-board "锚链接")

## Enabling Linux Networking 1. Configure the network `ifconfig eth0 hw ether xx:xx:xx:xx:xx:xx; ifconfig eth0 xx.xx.xx.xx netmask xx.xx.xx.xx; route add default gw xx.xx.xx.xx` 2. Ping another machine to verify network connectivity. ## Using NFS for Development 1. During development, NFS is the recommended file system, as it eliminates the need to rebuild and reflash the root filesystem.[¶](#enabling-linux-networking-1-configure-the-network-ifconfig-eth0-hw-ether-xxxxxxxxxxxx-ifconfig-eth0-xxxxxxxx-netmask-xxxxxxxx-route-add-default-gw-xxxxxxxx-2-ping-another-machine-to-verify-network-connectivity-using-nfs-for-development-1-during-development-nfs-is-the-recommended-file-system-as-it-eliminates-the-need-to-rebuild-and-reflash-the-root-filesystem "锚链接")

1. Mount the NFS filesystem with: `mount -t nfs -o nolock -o tcp -o rsize=32768,wsize=32768 xx.xx.xx.xx:/your-nfs-path /mnt` 3. Files on the server are then accessible under `/mnt` for development. ## Enabling the Telnet Service # Once the network is working, run `telnetd &` to start the board's telnet service. You can then log in to the board via telnet. ## Running MPP Services On the board's Linux system, navigate to the `mpp/out/ko` directory and load the kernel modules: `cd mpp/ko
 ./load_Hi3403V100 -a` ## Switching Between Linux and LiteOS Copy the compiled `sample.bin` and the `load_riscv` tool to the Linux system, then run the following commands: `cp load_riscv /bin
 chmod +x /bin/load_riscv
 load_riscv 0x44000000 sample.bin` Note: The `load_riscv` tool is located at `osdrv/tools/board/load_riscv/bin`. Log in to the board via telnet under Linux and navigate to the komod directory, then load the kernel modules: `cd /komod
 insmod ipcm.ko
 insmod virt-tty.ko` Run the following command to enter Lite OS: `virt-tty riscv` To switch back to Linux from Lite OS, press `Ctrl + C`. # Address Space Allocation and Usage

## DDR Memory Management - All DDR memory is divided into two pools: OS memory, managed by the operating system; and MMZ memory, reserved exclusively for media services and managed by the MMZ module.[¶](#ddr-memory-management-all-ddr-memory-is-divided-into-two-pools-os-memory-managed-by-the-operating-system-and-mmz-memory-reserved-exclusively-for-media-services-and-managed-by-the-mmz-module "锚链接")

- OS memory starts at `0x50000000`. The size is configurable via bootargs (e.g., `setenv bootargs 'mem=512M ...'` allocates 512 MB to the OS). Adjust as needed.
- MMZ memory is managed by the `ot_osal.ko` kernel module (in `mpp/out/ko`). The MMZ start address and size are specified as module parameters when loading the osal module, via `mmz_start` and `mmz_size` in the load script.
- Ensure the MMZ memory address range does not overlap with OS memory. ## DEMO Board DDR Memory Layout Using a 4 GB DDR configuration as an example, the memory layout based on this document and the SDK default configuration is: DDR: `|-------------|--------------------| 0x40000000 # Memory managed by IPCM.
 | 2MB | IPCM |
 |-------------|--------------------| 0x40200000 # Memory managed by DSP Lite OS.
 | 62MB | DSP |
 |-------------|--------------------| 0x44000000 # Memory managed by RISC-V Lite OS.
 | 192MB | RISV-V |
 |-------------|--------------------| 0x50000000 # Memory managed by Linux OS.
 | 512MB | Linux OS |
 |-------------|--------------------| 0x70000000 # Memory managed by MMZ block anonymous.
 | 3328MB | MMZ |
 |-------------|--------------------| 0x FFFFFFFF # End of memory managed by MMZ.` Notes: 1. When configuring boot parameters, set the OS managed memory to 512 MB: `setenv bootargs 'mem=512M...'`.
- For special use cases, the `load_Hi3403V100` script can be modified to customize MMZ partitioning, for example: `insmod ot_osal.ko anony=1 mmz_allocator=ot mmz=anonymous,0,0x70000000,1786M:jpeg,0,0x DFA00000,6M`.

