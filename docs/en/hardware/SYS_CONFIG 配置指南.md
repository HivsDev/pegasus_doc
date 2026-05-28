---
title: SYS_CONFIG
---

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/SYS\_CONFIG配置指南/SYS\_CONFIG 配置指南.md
--- # Preface
**Overview** This document is written for engineers developing with the MPP media processing chip. Its purpose is to provide various reference information about the SYS\_CONFIG sub-module of the media processing software during development, including system control, clock configuration, and pin multiplexing. This document describes the usage of each key function in SYS\_CONFIG and the related configuration principles. >[](../../../reference/sys-config/public_sys-resources/icon-note.gif) **Note:**

> This document uses the Hi3403V100 description as an example. Unless otherwise specified, the content for is the same as for Hi3403V100. **Product Version** The product version corresponding to this document is as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |
| V100 |

**Target Audience** This document (guide) is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document. Their meanings are as follows.

| **Symbol** | **Description** |
| --- | --- |
|  | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History**

| **Document Version** | **Release Date** | **Revision Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim release. |

# Overview

## SYS\_CONFIG Introduction SYS\_CONFIG is a module for system-level and board-level configuration. Its main function is to configure the initialization environment that does not require dynamic modification when the sys\_config.ko module is loaded. It includes the following parts: - Initialization[¶](#sys_config-introduction-sys_config-is-a-module-for-system-level-and-board-level-configuration-its-main-function-is-to-configure-the-initialization-environment-that-does-not-require-dynamic-modification-when-the-sys_configko-module-is-loaded-it-includes-the-following-parts-initialization "锚链接")

- System Control
- Clock Reset Configuration
- Pin Multiplexing SYS\_CONFIG is released both as a binary .ko file and as source code. The source code is located in the interdrv/sysconfig directory. To modify the SYS\_CONFIG code, refer to the following documents and steps (using Hi3403V100 as an example): - To modify clock configuration and system control, first refer to the chip manual, then modify the sysconfig code.
- To modify pin multiplexing configuration, first refer to the chip manual, then modify the sysconfig code. Depending on the video input sensor connected, the system control and chip pin multiplexing configuration may differ. This can be distinguished by the module parameter g\_sensor\_list. For example: insmod sys\_config.ko sensors="sns0=sensor0\_xxx,sns1=sensor1\_xxx,sns2=sensor2\_xxx,sns3=sensor3\_xxx" vo\_intf="bt1120" Or: insmod sys\_config.ko sensors=sns0=sensor0\_xxx,sns1=sensor1\_xxx,sns2=sensor2\_xxx,sns3=sensor3\_xxx vo\_intf=bt1120 The meaning of each module parameter is shown in [Table 1](#_table34233312). **Table 1** Module Parameter Meanings

| Parameter | Meaning |
| --- | --- |
| sensors | sensors list, passed as a string.  For example:  sensors="sns0=sensor0\_xxx,sns1=sensor1\_xxx,sns2=sensor2\_xxx,sns3=sensor3\_xxx"  Or  sensors=sns0=sensor0\_xxx,sns1=sensor1\_xxx,sns2=sensor2\_xxx,sns3=sensor3\_xxx  sensors=none means no sensor pins are configured. |
| vo\_intf | VO interface type selection. Default is "mipi\_tx".  MIPI\_TX: vo\_intf="mipitx" or "mipi\_tx";  BT.1120: vo\_intf ="bt.1120" or "bt1120";  BT.656: vo\_intf ="bt.656" or "bt656";  RGB\_6BIT: vo\_intf ="rgb\_6bit" or "rgb6bit";  RGB\_8BIT: vo\_intf ="rgb\_8bit" or "rgb8bit";  RGB\_16BIT: vo\_intf ="rgb\_16bit" or "rgb16bit";  RGB\_18BIT: vo\_intf ="rgb\_18bit" or "rgb18bit";  RGB\_24BIT: vo\_intf ="rgb\_24bit" or "rgb24bit";  No VO pins configured: vo\_intf = "none".  Any string with the above prefixes will be considered valid input. If the string length exceeds 15 characters, the driver will fail to load. |
| g\_hdmi\_en | Whether to configure HDMI pins. g\_hdmi\_en=1 means configure, g\_hdmi\_en=0 means do not configure. Default is 1. |
| g\_i2c\_en | Whether to configure I2C pins. g\_i2c\_en=1 means configure, g\_i2c\_en=0 means do not configure. Default is 1. |
| g\_audio\_en | Whether to configure audio pins. g\_audio\_en=1 means configure, g\_audio\_en=0 means do not configure. Default is 1. |

Users can modify the relevant content in the SYS\_CONFIG module source code file based on the actual physical environment: - Modify the corresponding system configuration according to the actual system configuration;
- Modify the corresponding clock according to the actual system operating clock requirements;
- Modify the pin multiplexing related content according to the actual physical circuit pin usage layout. After modification, compile and load the module .ko to complete the configuration of the desired new user environment. The SYS\_CONFIG configuration flow is shown in [Figure 1](#_fig9145151194318). **Figure 1** SYS\_CONFIG Overall Flow Chart [](figures/SYS_CONFIGOverallstreamgraph.png) Includes the following 4 flows: - Initialization (sysconfig\_init) Maps the addresses of the configuration registers. The main register addresses include CRG, system control, MISC, IO pin multiplexing, GPIO control, MIPI, etc. - System Control (sys\_ctl) Configures the system control section, such as QoS settings for online/offline modes of VI and VPSS. - Clock Reset Configuration (clk\_cfg) Configures clocks for modules such as VI, VO, SPI, I2C, etc. - Pin Multiplexing Configuration (pin\_mux) Configures pin multiplexing for different functions based on different application scenarios. # Initialization
SYS\_CONFIG initialization performs ioremap mappings for the register addresses that need to be configured, obtaining virtual addresses that the software can operate on. The following are the register addresses mapped during SYS\_CONFIG initialization. **Table 1** MISC Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_misc\_base | 0x11024000 | 0x5000 |

**Table 2** Clock Reset Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_crg\_base | 0x11010000 | 0x10000 |

**Table 3** Pin Multiplexing Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_iocfg\_base | 0x10230000 | 0x10000 |
| g\_reg\_iocfg2\_base | 0x102f0000 | 0x10000 |

**Table 4** GPIO Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_gpio\_base | 0x11090000 | 0x12000 |

**Table 5** SYS Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_sys\_base | 0x11020000 | 0x4000 |

**Table 6** DDR Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_ddr\_base | 0x11140000 | 0x10000 |

**Table 7** MIPI\_TX Register Addresses

| Solution | Base Address Variable | Base Address | Length |
| --- | --- | --- | --- |
| Hi3403V100 | g\_reg\_mipi\_tx\_base | 0x17A80000 | 0x10000 |

The register address mapping described in this chapter is the foundation for register configuration in other chapters. After completing the mapping of the register physical addresses (i.e., register addresses) in this chapter, the register virtual addresses are obtained. Through the register virtual addresses, the corresponding registers can be read and written. The operation functions are as follows: ```

# define sys\_writel(addr, value) ((*((volatile unsigned int* )(addr))) = (value))[¶](#define-sys_writeladdr-value-volatile-unsigned-int-addr-value "锚链接")

# define sys\_read(addr) (*((volatile int* )(addr)))[¶](#define-sys_readaddr-volatile-int-addr "锚链接")

``` - sys\_writel is the write function. addr is the register virtual address, and value is the value to be written to the register.
- sys\_read is the read function. addr is the register virtual address. The result of the operation is the value read from the register. # System Control

## VI VPSS Online/Offline Mode Based on the VI VPSS online/offline mode situation, the VI VPSS online/offline mode needs to be selected. The following uses Hi3403V100 as an example. ### VI VPSS Online/Offline Mode Configuration [Configuration] g\_reg\_misc\_base is described in [Table 1](#_table44115416). ```[¶](#vi-vpss-onlineoffline-mode-based-on-the-vi-vpss-onlineoffline-mode-situation-the-vi-vpss-onlineoffline-mode-needs-to-be-selected-the-following-uses-hi3403v100-as-an-example-vi-vpss-onlineoffline-mode-configuration-configuration-g_reg_misc_base-is-described-in-table-1 "锚链接")

static void set\_vi\_online\_video\_norm\_vpss\_online\_qos(void) { void \*misc\_base = sys\_config\_get\_reg\_misc; sys\_writel(misc\_base + 0x1000, 0x44777755); sys\_writel(misc\_base + 0x1004, 0x45455066); sys\_writel(misc\_base + 0x1008, 0x60050055); sys\_writel(misc\_base + 0x100c, 0x45433306); sys\_writel(misc\_base + 0x1010, 0x33333366); sys\_writel(misc\_base + 0x1014, 0x33503333); sys\_writel(misc\_base + 0x1018, 0x00044466); sys\_writel(misc\_base + 0x101c, 0x44777765); sys\_writel(misc\_base + 0x1020, 0x55556066); sys\_writel(misc\_base + 0x1024, 0x60050056); sys\_writel(misc\_base + 0x1028, 0x46433306); sys\_writel(misc\_base + 0x102c, 0x66555377); sys\_writel(misc\_base + 0x1030, 0x33503663); sys\_writel(misc\_base + 0x1034, 0x00055577); }
``` [Description] MDDRC\_QOS\_CTRL0 is the QoS register. Offset Address: 0x5000 Total Reset Value: 0x0000\_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [30:28] | RW | dpu\_w\_qos | DPU write channel QoS configuration. | 0x0 |
| [26:24] | RW | ive\_w\_qos | IVE write channel QoS configuration. | 0x0 |
| [22:20] | RW | vpss\_w\_qos | VPSS write channel QoS configuration. | 0x0 |
| [18:16] | RW | viproc\_2nd\_w\_qos | VIPROC\_2ND write channel QoS configuration. | 0x0 |
| [14:12] | RW | viproc\_1st\_w\_qos | VIPROC\_1ST write channel QoS configuration. | 0x0 |
| [10:8] | RW | vicap\_w\_qos | VICAP write channel QoS configuration. | 0x0 |
| [6:4] | RW | vdh\_w\_qos | VDH write channel QoS configuration. | 0x0 |
| [2:0] | RW | vedu\_w\_qos | VEDU write channel QoS configuration. | 0x0 |

Configuration value 0x44777755: - Bits[30:28]=0x4, indicates DPU write channel QoS configured to 4.
- Bits[26:24]=0x4, indicates IVE write channel QoS configured to 4.
- Bits[22:20]=0x7, indicates VPSS write channel QoS configured to 7.
- Bits[18:16]=0x7, indicates VIPROC\_2ND write channel QoS configured to 7.
- Bits[14:12]=0x7, indicates VIPROC\_1ST write channel QoS configured to 7.
- Bits[10:8]=0x7, indicates VICAP write channel QoS configured to 7.
- Bits[6:4]=0x5, indicates VDH write channel QoS configured to 5.
- Bits[2:0]=0x5, indicates VEDU write channel QoS configured to 5. [Precautions] None. # Clock Reset Configuration
Clocks are the foundation for normal operation of each module. The following uses Hi3403V100 as an example to describe clock-related configurations. The clock reset configuration function is as follows (the actual function implementation depends on the application scenario): `void clk_cfg(void)
{ i2c_spi_clk_cfg; ……
}` ## VI Clock Reset Configuration ### VICAP Clock [Configuration] g\_reg\_crg\_base is described in [Table 2](#_table61494432). `/* vicap ppc&bus reset&cken, ppc 600M */
sys_writel(g_reg_crg_base + 0x9140, 0x6030);` [Description] PERI\_CRG9296 is the VICAP clock and reset control register. Refer to the chip manual. Offset Address: 0x9140 Total Reset Value: 0x0000\_0003

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [14:12] | RW | vi\_ppc\_cksel | VICAP operating clock selection.  000: 150M Hz;  001: 300M Hz;  010: 396M Hz;  011: 475M Hz;  Others: 600M Hz. | 0x0 |
| [5] | RW | vi\_bus\_cken | VICAP BUS clock gating.  0: Clock off;  1: Clock on. | 0x0 |
| [4] | RW | vi\_ppc\_cken | VICAP PPC clock gating.  0: Clock off;  1: Clock on. | 0x0 |
| [1] | RW | vi\_bus\_srst\_req | VICAP BUS soft reset request.  0: No reset;  1: Reset. | 0x1 |
| [0] | RW | vi\_ppc\_srst\_req | VICAP PPC soft reset request.  0: No reset;  1: Reset. | 0x1 |

Configuration value 0x6030: - Bits[14:12]=0x6, indicates clock configured to 600M Hz;
- Bits[5:4]=0x3, indicates VICAP clock gating enabled. [Precautions] The operating clock must be greater than the SENSOR clock. ### PORT Clock [Configuration] (Using PORT0 configuration as an example) g\_reg\_crg\_base is described in [Table 2](#_table61494432). `/* vi port */
sys_writel(g_reg_crg_base + 0x9148, 0xff0);
sys_writel(g_reg_crg_base + 0x9164, 0x7010);
sys_writel(g_reg_crg_base + 0x9184, 0x7010);
sys_writel(g_reg_crg_base + 0x91a4, 0x7010);
sys_writel(g_reg_crg_base + 0x91c4, 0x7010);` [Description] PERI\_CRG9305 is the VICAP PORT0 clock and reset control register. Offset Address: 0x9164 Total Reset Value: 0x0000\_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [14:12] | RW | vi\_p0\_cksel | VICAP PORT0 clock selection:  000: 100M Hz;  001: 150M Hz;  010: 200M Hz;  011: 250M Hz;  100: 300M Hz;  101: 396M Hz;  110: 475M Hz;  111: 600M Hz. | 0x0 |
| [4] | RW | vi\_p0\_cken | VICAP PORT0 clock gating.  0: Clock off;  1: Clock on. | 0x0 |
| [0] | RW | vi\_p0\_srst\_req | VICAP PORT0 soft reset request.  0: No reset;  1: Reset. | 0x0 |

Configuration value 0x7010: Bits[14:12]=0x7, indicates PORT clock configured to 600M Hz. [Precautions] None. ### CMOS Clock [Configuration] g\_reg\_crg\_base is described in [Table 2](#_table61494432). `/* vi cmos0 */
sys_writel(g_reg_crg_base + 0x9160, 0x0);` [Description] PERI\_CRG9304 is the VI CMOS0 clock reset configuration register. Offset Address: 0x9160 Total Reset Value: 0x0000\_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [31:21] | - | reserved | Reserved. | 0x000 |
| [20] | RW | vi\_cmos0\_pctrl | VI CMOS clock phase control.  0: Clock not inverted;  1: Clock inverted. | 0x0 |
| [19:0] | - | reserved | Reserved. | 0x00000 |

Configuration value 0x0: Bits[20]=0x0, indicates VI CMOS clock phase not inverted. [Precautions] None. ### SENSOR Clock [Configuration] (Using SENSOR0 configuration as an example) g\_reg\_crg\_base is described in [Table 2](#_table61494432). `static void sensor_clock_config(int index, unsigned int clock)
{ int offset = 0x8440; offset += index * (0x20); /* sensor0 - 3 */ sys_writel(g_reg_crg_base + offset, clock); /* im327 clock: 0x8010 */
}` [Description] sysconfig parses the sensor number and sensor name passed through module parameters to resolve the corresponding register address and configuration value. For example, when the module parameter is sensors=sns0=sensor0\_xxx, it resolves index=0, clock=0x8010, and the calculated offset for sensor0 is 0x8440. The SENSOR0 clock reset configuration register is used as an example for detailed description. PERI\_CRG8464 is the SENSOR0 clock reset configuration register. Offset Address: 0x8440 Total Reset Value: 0x0000\_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [15:12] | RW | sensor0\_cksel | SENSOR0 clock (reference clock output from the chip to the sensor) selection.  0x0: 74.25M Hz;  0x1: 72M Hz;  0x2: 54M Hz;  0x3: 50M Hz;  0x4: 24M Hz;  0x8: 37M Hz;  0x9: 36M Hz;  0xA: 27M Hz;  0xB: 25M Hz;  0xC: 12M Hz;  Others: Reserved. | 0x0 |
| [4] | RW | sensor0\_cken | SENSOR0 clock (reference clock output from the chip to the sensor) gating.  0: Clock off;  1: Clock on. | 0x0 |
| [1] | RW | sensor0\_ctrl\_srst\_req | SENSOR0 slave mode control module soft reset request.  0: No reset;  1: Reset. | 0x0 |
| [0] | RW | sensor0\_srst\_req | SENSOR0 soft reset request.  0: No reset;  1: Reset. | 0x0 |

Configuration value 0x8010: Bits[15:12]=0x8, indicates SENSOR0 clock configured to 37M Hz. [Precautions] None. ### VIPROC Clock [Configuration] g\_reg\_crg\_base is described in [Table 2](#_table61494432). `/* viproc_pre ppc&bus reset&cken, ppc 600M */
sys_writel(g_reg_crg_base + 0x9740, 0x4010);` [Description] PERI\_CRG9680 is the VIPROC clock and reset control register. Offset Address: 0x9740 Total Reset Value: 0x0000\_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [14:12] | RW | viproc\_cksel | VIPROC offline mode clock selection.  000: 150M Hz;  001: 300M Hz;  010: 396M Hz;  011: 475M Hz;  100: 600M Hz;  Others: Reserved. | 0x0 |
| [4] | RW | viproc\_cken | VIPROC clock gating.  0: Clock off;  1: Clock on. | 0x0 |
| [0] | RW | viproc\_srst\_req | VIPROC soft reset request.  0: No reset;  1: Reset. | 0x0 |

Configuration value 0x4010: - Bits[14:12]=0x4, indicates clock configured to 600M Hz;
- Bits[4]=0x1, indicates VIPROC clock gating enabled. [Precautions] None. ## SPI Clock VO RGB interface output and external LCD display screens use the SPI bus. The SPI clock needs to be enabled. [Configuration] g\_reg\_crg\_base is described in [Table 2](#_table61494432). `static void i2c_spi_clk_cfg(void)
{
void *g_reg_crg_base = sys_config_get_reg_crg; /* SPI */ sys_writel(g_reg_crg_base + 0x4480, 0x10); /* ssp0 reset&cken */ sys_writel(g_reg_crg_base + 0x4488, 0x10); /* ssp1 reset&cken */ sys_writel(g_reg_crg_base + 0x4490, 0x10); /* ssp2 reset&cken */ sys_writel(g_reg_crg_base + 0x4498, 0x10); /* ssp3 reset&cken */ sys_writel(g_reg_crg_base + 0x44a0, 0x10); /* 3wire spi reset&cken */
}` [Description] PERI\_CRG4384 is the SPI0 clock gating and reset register. Offset Address: 0x4480 Total Reset Value: 0x0000\_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [31:5] | - | reserved | Reserved. | 0x00000 |
| [4] | RW | spi0\_cken | SPI0 clock gating configuration register.  0: Clock off.  1: Clock on. | 0x0 |
| [3:1] | - | reserved | Reserved. | 0x00 |
| [0] | RW | spi0\_srst\_req | SPI0 soft reset request.  0: De-assert reset;  1: Reset. | 0x0 |

Configuration value 0x10: - Bits[0]=0, indicates SPI0 reset de-asserted;
- Bits[4]=1, indicates SPI0 clock enabled. [Precautions] None. # Pin Multiplexing
Pin multiplexing allows the chip to flexibly use pin resources among its limited output pins to meet different scenario requirements, with pins serving different functions in different scenarios. ## I2C Bus Pin Multiplexing I2C buses are generally used to configure peripheral chips. In peripheral drivers, the I2C interface is typically used to configure peripheral chips. Therefore, the corresponding pins need to be configured as I2C pins in SYS\_CONFIG. ### I2C Pin Multiplexing [Configuration] g\_reg\_iocfg2\_base is described in [Table 3](#_table16578980). I2C0: `static void i2c0_pin_mux(void) { void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x013C, 0x2031); sys_writel(iocfg2_base + 0x0140, 0x2031); }` I2C1: `static void i2c1_pin_mux(void) { void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x00E8, 0x0072); sys_writel(iocfg2_base + 0x00EC, 0x0072); }` [Description] Taking I2C0 as an example, the I2C schematic is shown in [Figure 1](#fig13182150165411). Refer to the hardware schematic. **Figure 1** I2C Schematic [](figures/I2Coriginarrangegraph.jpg) I2C0 requires 2 pins: I2C0\_SCL (clock) and I2C0\_SDA (data). The pin multiplexing for these 2 pins is described below. #### Clock Pin Configuration (AM19) AM19 (Register: 0x0102F0140). **Table 1** AM19 AM20 Pin Control Register

| Register Name | Pin Number | Function | Address | Default Value | Field Bits | Field Description |
| --- | --- | --- | --- | --- | --- | --- |
| iocfg\_reg101 | AM20 | Pin I2C0\_SDA IO Config Register. | 0x0102F013C | 0x1100 | 31:15 | Reserved. |
| 7:4 | Pin drive capability selection: 0x0: IO6\_2 level 1;  0x1: IO6\_2 level 2;  0x2: IO6\_2 level 3;  0x3: IO6\_2 level 4;  Others: Reserved. |
| 3:0 | Function selection:  0x0: GPIO11\_4;  0x1: I2C0\_SDA;  Others: Reserved. |
| iocfg\_reg102 | AM19 | Pin I2C0\_SCL IO Config Register. | 0x0102F0140 | 0x1100 | 31:15 | Reserved. |
| 7:4 | Pin drive capability selection:  0x0: IO6\_2 level 1;  0x1: IO6\_2 level 2;  0x2: IO6\_2 level 3;  0x3: IO6\_2 level 4;  Others: Reserved. |
| 3:0 | Function selection:  0x1: I2C0\_SCL;  Others: Reserved. |

The pin has 1 multiplexing scenario: I2C0\_SCL. AM19 configuration value 0x2001: - Bits[3:0]=0x1, pin multiplexed to 1, configured as I2C0\_SCL;
- Bits[7:4]=0x0, pin drive capability configured to level 4 (maximum), higher level value means higher drive capability;
- Bits[13]=0x1, input level threshold select 3.3V/5V PAD. #### DATA Pin Configuration (AM20) AM20 (Register: 0x0102F013C). AM20 pin control register is shown in [Table 1](#_table796515471314). The pin has 2 multiplexing scenarios: GPIO11\_4/I2C0\_SDA. AM20 configuration value 0x2001: - Bits[3:0]=0x1, pin multiplexed to 1, configured as I2C0\_SDA;
- Bits[7:4]=0x0, pin drive capability configured to level 4 (maximum), higher level value means higher drive capability;
- Bits[13]=0x1, input level threshold select 3.3V/5V PAD. [Precautions] None. ## SPI Bus Pin Multiplexing The LCD display screen IC chip connects to the main chip via the SPI bus. In the LCD screen driver, the SPI interface is typically used to configure the LCD IC chip. Therefore, the corresponding pins need to be configured as SPI pins. ### SPI Pin Multiplexing [Configuration] (Using Hi3403V100 as an example) g\_reg\_iocfg2\_base1 is described in [Table 3](#_table16578980) `static void spi0_pin_mux(void) { void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x01D8, 0x02b1); sys_writel(iocfg2_base + 0x01DC, 0x0251); sys_writel(iocfg2_base + 0x01E0, 0x0201); sys_writel(iocfg2_base + 0x01E4, 0x0201); }` [Description] SPI0\_SDI (AL33), SPI0\_SDO (AL34), SPI0\_CSN (AM34), SPI0\_SCLK (AK33) pins are shown in [Figure 1](#_fig1987716341641). **Figure 1** SPI0 Schematic [](figures/SPI0originarrangegraph.jpg) The multiplexing configuration of the AK33 pin is used as an example. The SPI0\_SCLK (AK33) pin control register is shown in [Table 1](#_table3777103411415). **Table 1** AK33 Pin Control Register

| Register Name | Pin Number | Function | Address | Default Value | Field Bits | Field Description |
| --- | --- | --- | --- | --- | --- | --- |
| iocfg\_reg140 | AK33 | Pin SPI0\_SCLK IO Config Register. | 0x0102F01D8 | 0x1200 | 31:15 | Reserved. |
| 7:4 | Pin drive capability selection:  0x0: IO2 level 1;  0x1: IO2 level 2;  0x2: IO2 level 3;  0x3: IO2 level 4;  0x4: IO2 level 5;  0x5: IO2 level 6;  0x6: IO2 level 7;  0x7: IO2 level 8;  0x8: IO2 level 9;  0x9: IO2 level 10;  0xA: IO2 level 11;  0xB: IO2 level 12;  0xC: IO2 level 13;  0xD: IO2 level 14;  0xE: IO2 level 15;  0xF: IO2 level 16;  Others: Reserved. |
| 3:0 | Function selection:  0x0: GPIO16\_3;  0x1: SPI0\_SCLK;  0x2: I2C2\_SCL;  0x3: SPI\_3WIRE\_CLK;  Others: Reserved. |

AK33 pin has 4 function multiplexing options: GPIO16\_3/SPI0\_SCLK/I2C2\_SCL/SPI\_3WIRE\_CLK Current AK33 pin configuration value: 0x02b1 - Bits [3:0]=1, indicates AK33 multiplexed as SPI0\_SCLK
- Bits[7:4]=0xb, indicates drive capability select level 12
- Bits[9]=0x1, indicates pin pull-down: On [Precautions] None. ## VI Pin Multiplexing Video input receives video data through BT.656/BT.1120/MIPI interfaces, captures video data according to certain video reception protocols, and stores the data into specified memory areas. The following describes pin multiplexing in VICAP. ### PORT Pin Multiplexing #### MIPI\_RX Pin Multiplexing [Configuration] g\_reg\_iocfg2\_base is described in [Table 3](#_table16578980). Taking the MIPI\_RX PHY0 interface of Hi3403V100 as an example: `static void mipi0_rx_pin_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x01B0, 0x0000); sys_writel(iocfg2_base + 0x01B4, 0x0000); sys_writel(iocfg2_base + 0x01C0, 0x0000); sys_writel(iocfg2_base + 0x01C4, 0x0000); sys_writel(iocfg2_base + 0x01B8, 0x0000); sys_writel(iocfg2_base + 0x01BC, 0x0000); sys_writel(iocfg2_base + 0x01A8, 0x0000); sys_writel(iocfg2_base + 0x01AC, 0x0000); sys_writel(iocfg2_base + 0x0198, 0x0000); sys_writel(iocfg2_base + 0x019C, 0x0000); sys_writel(iocfg2_base + 0x01A0, 0x0000); sys_writel(iocfg2_base + 0x01A4, 0x0000);
}` [Description] The schematic is shown in [Figure 1](#_toc51764061). **Figure 1** MIPI\_RX0 Schematic [](figures/MIPI_RX0originarrangegraph.png) When the VI video capture interface is MIPI\_RX, the 10 pins shown in [Figure 1](#_toc51764061) need to be configured for MIPI\_RX related functions. The 10 pins of the MIPI interface consist of 1 pair of clock lines and 4 pairs of DATA lines, with 1 pair of pins being 1 pair of differential signals. - Clock pin configuration (using AP30 multiplexed as MIPI\_RX0\_CK0P as an example). **Table 1** AP30 Pin Control Register

| Register Name | Pin Number | Function | Address | Default Value | Field Bits | Field Description |
| --- | --- | --- | --- | --- | --- | --- |
| iocfg\_reg129 | AP30 | Pin MIPI\_RX0\_CK0P IO Config Register. | 0x0102F01AC | 0x1200 | 31:15 | Reserved. |
| 7:4 | Reserved. |
| 3:0 | Function selection:  0x0: MIPI\_RX0\_CK0P;  0x1: GPIO15\_0;  Others: Reserved. |

The pin has 2 multiplexing scenarios: MIPI\_RX0\_CK0P/GPIO15\_0. Configuration value 0x0000: Bits[3:0]=0, pin multiplexed to 0, configured as MIPI\_RX0\_CK0P. - DATA pin configuration (using AN31 multiplexed as MIPI\_RX0\_D0N as an example). **Table 2** AN31 Pin Control Register

| Register Name | Pin Number | Function | Address | Default Value | Field Bits | Field Description |
| --- | --- | --- | --- | --- | --- | --- |
| iocfg\_reg124 | AN31 | Pin MIPI\_RX0\_D0N IO Config Register. | 0x0102F0198 | 0x1200 | 31:15 | Reserved. |
| 7:4 | Reserved. |
| 3:0 | Function selection:  0x0: MIPI\_RX0\_D0N;  0x1: GPIO14\_3;  Others: Reserved. |

The pin has 2 multiplexing scenarios: MIPI\_RX0\_D0N /GPIO14\_3. Configuration value 0x0000: Bits[3:0]=0, pin multiplexed to 0, configured as MIPI\_RX0\_D0P. The multiplexing configuration of other pins is similar to the above example and will not be described in detail. [Precautions] None. #### BT.656 Pin Multiplexing (VI) [Configuration] Taking the BT.656 interface of device 1 as an example. g\_reg\_iocfg\_base is described in [Table 3](#_table16578980). `static void vi_bt656_mode_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x0158, 0x0206); sys_writel(iocfg2_base + 0x016C, 0x0006); sys_writel(iocfg2_base + 0x0178, 0x0006); sys_writel(iocfg2_base + 0x017C, 0x0006); sys_writel(iocfg2_base + 0x0174, 0x0006); sys_writel(iocfg2_base + 0x0160, 0x0206); sys_writel(iocfg2_base + 0x015C, 0x0206); sys_writel(iocfg2_base + 0x0164, 0x0206); sys_writel(iocfg2_base + 0x0154, 0x0206);
}` [Description] The schematic is shown in [Figure 1](#_toc51764062). **Figure 1** VI BT.656 Schematic [](figures/VI-BT-656originarrangegraph.png) When the VI video capture interface is BT.656, the 10 pins shown in the figure above need to be configured for BT.656 related functions. The 10 pins of the BT.656 interface include a clock pin and 8 DATA pins (VI\_DATA0~VI\_DATA7). - Clock pin configuration (using AK22 multiplexed as VI\_CLK as an example): **Table 1** AK22 Pin Control Register

| Register Name | Pin Number | Function | Address | Default Value | Field Bits | Field Description |
| --- | --- | --- | --- | --- | --- | --- |
| iocfg\_reg108 | AK22 | Pin SPI1\_CSN0 IO Config Register. | 0x0102F0158 | 0x1200 | 31:15 | Reserved. |
| 7:4 | Pin drive capability selection:  0x0: IO2 level 1; 0x1: IO2 level 2; 0x2: IO2 level 3; 0x3: IO2 level 4; 0x4: IO2 level 5; 0x5: IO2 level 6; 0x6: IO2 level 7; 0x7: IO2 level 8; 0x8: IO2 level 9; 0x9: IO2 level 10; 0xA: IO2 level 11; 0xB: IO2 level 12; 0xC: IO2 level 13; 0xD: IO2 level 14; 0xE: IO2 level 15; 0xF: IO2 level 16; Others: Reserved. |
| 3:0 | Function selection:  0x0: GPIO12\_3; 0x1: SPI1\_CSN0; 0x2: I2C4\_SDA; 0x3: SENSOR1\_HS; 0x4: SENSOR0\_HS; 0x5: SENSOR2\_HS; 0x6: VI\_CLK; 0x7: HT\_SD2; Others: Reserved. |

The pin has 8 multiplexing scenarios: HT\_SD2/VI\_CLK/SENSOR2\_HS/SENSOR1\_HS/SENSOR0\_HS/I2C4\_SDA/SPI1\_CSN0/GPIO12\_3. Configuration value 0x0206: Bits[3:0]=0x6, pin multiplexed to 6, configured as VI\_CLK. - DATA pin configuration: VI\_DATA0~VI\_DATA7 are the corresponding BT.656 interface related functions. Using AN24 multiplexed as VI\_DATA0 as an example, the pin has 4 multiplexing scenarios: HT\_DO6/VI\_DATA0/GPIO13\_0/MIPI\_RX1\_D0P. Configuration value 0x0006: Bits[3:0]=0x6, pin multiplexed to 6, configured as VI\_DATA0. Other pin multiplexing relationships are similar to the above examples and will not be described in detail. [Precautions] None. #### BT.1120 Pin Multiplexing (VI) The BT.1120 interface consists of a clock pin (VI\_CLK) and 16 data pins (VI\_DATA0~VI\_DATA15). [Configuration] g\_reg\_iocfg\_base is described in [Table 3](#_table16578980). `static void vi_bt1120_mode_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x0158, 0x0206); sys_writel(iocfg2_base + 0x016C, 0x0006); sys_writel(iocfg2_base + 0x0178, 0x0006); sys_writel(iocfg2_base + 0x017C, 0x0006); sys_writel(iocfg2_base + 0x0174, 0x0006); sys_writel(iocfg2_base + 0x0160, 0x0206); sys_writel(iocfg2_base + 0x015C, 0x0206); sys_writel(iocfg2_base + 0x0164, 0x0206); sys_writel(iocfg2_base + 0x0154, 0x0206); sys_writel(iocfg2_base + 0x0194, 0x0006); sys_writel(iocfg2_base + 0x0190, 0x0006); sys_writel(iocfg2_base + 0x0184, 0x0006); sys_writel(iocfg2_base + 0x0180, 0x0006); sys_writel(iocfg2_base + 0x0188, 0x0006); sys_writel(iocfg2_base + 0x018C, 0x0006); sys_writel(iocfg2_base + 0x0170, 0x0006); sys_writel(iocfg2_base + 0x0168, 0x0006);
}` [Description] The schematic is shown in [Figure 1](#_toc51764063). **Figure 1** VI BT.1120 Schematic [](figures/VI-BT-1120originarrangegraph.png) When the VI video capture interface is BT.1120, the corresponding pins in the figure above need to be configured for BT.1120 related functions. The BT.1120 interface pins consist of a clock pin and 16 DATA pins (VI\_DATA0~VI\_DATA15). The clock pin configuration is the same as described in the BT.656 section (AK22 multiplexed as VI\_CLK). VI\_DATA0~VI\_DATA7 configuration refers to the BT.656 DATA pin description. VI\_DATA8~VI\_DATA15 are additional pins configured similarly. For example, AK26 multiplexed as VI\_DATA8 has 4 multiplexing scenarios: HT\_CLK\_OUT/VI\_DATA8/GPIO14\_2/MIPI\_RX1\_D3P, configured with value 0x0006, Bits[3:0]=0x6. [Precautions] Hi3403V100 has only 1 BT.656 interface. When configuring the BT.1120 interface, in addition to configuring BT.656 pins for VI\_DATA0~DATA7, 8 additional pins need to be configured as VI\_DATA8~DATA15. #### SENSOR Reference Clock Pin SENSOR pins are used to connect external sensors. The main chip provides a reference clock to the sensor. [Configuration] g\_reg\_iocfg\_base is described in [Table 3](#_table16578980). SENSOR0-3: `static void sensor0_pin_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x01C8, 0x02d1); sys_writel(iocfg2_base + 0x01CC, 0x0101);
}
static void sensor1_pin_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x0150, 0x02d1); sys_writel(iocfg2_base + 0x014C, 0x0201);
}
static void sensor2_pin_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x01E8, 0x02d4); sys_writel(iocfg2_base + 0x0160, 0x0205);
}
static void sensor3_pin_mux(void)
{ void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x0154, 0x02d2);
}` [Description] SENSOR0\_CLK (AL32), SENSOR0\_RSTN (AM32) schematic is shown in [Figure 1](#_toc51764064). **Figure 1** SENSOR0 Schematic [](figures/SENSOR0originarrangegraph.png) The AL32 pin (iocfg\_reg136, 0x0102F01C8) controls SENSOR0\_CLK. AL32 has 4 function multiplexing options: GPIO15\_7/SENSOR0\_CLK/SENSOR1\_CLK/SENSOR2\_CLK. Configuration value 0x02d1: Bits[3:0]=1 (SENSOR0\_CLK), Bits[7:4]=d (drive level 14), Bits[9]=1 (pull-down on). [Precautions] None. ## VO Pin Multiplexing ### HDMI Pin Multiplexing [Configuration] (Using Hi3403V100 as an example) g\_reg\_iocfg2\_base is described in [Table 3](#_table16578980). `static void hdmi_pin_mux(void) { void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x00E4, 0x2801); sys_writel(iocfg2_base + 0x00E8, 0x6801); sys_writel(iocfg2_base + 0x00EC, 0x6801); }` [Description] HDMI\_HOTPLUG (AK11, register iocfg\_reg79, 0x0102F00E4), HDMI\_SDA (AL11), HDMI\_SCL (AL12). **Figure 1** HDMI Schematic [](figures/HDM Ioriginarrangegraph.jpg) AK11 has 2 function multiplexing options: GPIO9\_2/HDMI\_HOTPLUG. Configuration value 0x2801: Bits[3:0]=1 (HDMI\_HOTPLUG), Bits[7:4]=0 (drive level 1), Bits[11]=1 (Schmitt input on), Bits[13]=1 (3.3V/5V PAD). [Precautions] None. ### MIPI\_TX Pin Multiplexing [Configuration] (Using Hi3403V100 as an example) g\_reg\_iocfg2\_base is described in [Table 3](#_table16578980). `static void vo_mipi_tx_pin_mux(void) { void *iocfg2_base = sys_config_get_reg_iocfg2; sys_writel(iocfg2_base + 0x00D8, 0x0201); sys_writel(iocfg2_base + 0x00A0, 0x0000); sys_writel(iocfg2_base + 0x00A4, 0x0000); sys_writel(iocfg2_base + 0x00A8, 0x0000); sys_writel(iocfg2_base + 0x00AC, 0x0000); sys_writel(iocfg2_base + 0x00B0, 0x0000); sys_writel(iocfg2_base + 0x00B4, 0x0000); sys_writel(iocfg2_base + 0x00B8, 0x0000); sys_writel(iocfg2_base + 0x00BC, 0x0000); sys_writel(iocfg2_base + 0x00C0, 0x0000); sys_writel(iocfg2_base + 0x00C4, 0x0000);
}` [Description] VSYNC\_TE\_MIPITX (AL4, register iocfg\_reg76, 0x0102F00D8) controls the MIPI\_TX VSYNC/TE signal. AL4 has 5 function options: GPIO0\_2/VSYNC\_TE\_MIPITX/VO\_BT1120\_DATA13/RGB\_DATA17/PWM0\_OUT15\_0\_N. Configuration value 0x0201: Bits[3:0]=1 (VSYNC\_TE\_MIPITX), Bits[7:4]=0 (level 1), Bits[9]=0 (pull-down on). **Figure 1** MIPI\_TX Schematic [](figures/MIPI_TXoriginarrangegraph.jpg) [Precautions] Except for VSYNC\_TE\_MIPITX, the drive capability of other MIPI\_TX pins is configured by the MIPI\_TX PHY register 0x68. Default value is 0x05. ### VO BT.1120 Pin Multiplexing [Configuration] (Using Hi3403V100 as an example) g\_reg\_iocfg2\_base is described in [Table 3](#_table16578980), g\_reg\_mipi\_tx\_base is described in [Table 7](#_table071427174311). `static void vo_bt_pin_mux(int vo_bt_mode) { void *iocfg2_base = sys_config_get_reg_iocfg2; vo_cmos_set_pin_drive_cap(MIPI_TX_DRIVE_CAP_LEVEL3); sys_writel(iocfg2_base + 0x00C8, 0x0682); sys_writel(iocfg2_base + 0x00A8, 0x2); sys_writel(iocfg2_base + 0x00AC, 0x2); sys_writel(iocfg2_base + 0x00B0, 0x2); sys_writel(iocfg2_base + 0x00B4, 0x2); sys_writel(iocfg2_base + 0x00B8, 0x2); sys_writel(iocfg2_base + 0x00C0, 0x2); sys_writel(iocfg2_base + 0x00C4, 0x2); sys_writel(iocfg2_base + 0x00BC, 0x2); if (vo_bt_mode == VO_BT656_MODE) return; sys_writel(iocfg2_base + 0x00D4, 0x0242); sys_writel(iocfg2_base + 0x00A0, 0x2); sys_writel(iocfg2_base + 0x00A4, 0x2); sys_writel(iocfg2_base + 0x00D0, 0x0242); sys_writel(iocfg2_base + 0x00CC, 0x0242); sys_writel(iocfg2_base + 0x00D8, 0x0242); sys_writel(iocfg2_base + 0x00E0, 0x0242); sys_writel(iocfg2_base + 0x00DC, 0x0242);
}` [Description] VO\_BT1120\_CLK (AH4, iocfg\_reg72, 0x0102F00C8) has 4 function options: GPIO8\_6/SPI2\_SCLK/VO\_BT1120\_CLK/RGB\_DATA10. Configuration 0x06f2: Bits[3:0]=2 (VO\_BT1120\_CLK), Bits[7:4]=0xf (level 16), Bits[9]=1 (pull-down on), Bits[10]=1 (slow edge). **Figure 1** VO BT.1120 Schematic [](figures/VO-BT-1120originarrangegraph.jpg)
[](../../../reference/sys-config/figures/zh-cn_image_0000002441661705.jpg) The drive capability of DATA0~DATA7, DATA9, DATA10 pins is configured by the MIPI\_TX controller (levels 0~3, default level 3). The PHY register write/read sequences are provided in the original document. Write example:

```
PHY_REG_CFG1 = 0x100XX (XX = PHY register address)
PHY_REG_CFG0 = 0x2
PHY_REG_CFG0 = 0x0
PHY_REG_CFG1 = 0xYY (YY = configuration value)
PHY_REG_CFG0 = 0x2
PHY_REG_CFG0 = 0x0
``` Read example:
```

bspmm g\_reg\_mipi\_tx\_base+0x00b8 0x10066
bspmm g\_reg\_mipi\_tx\_base+0x00b4 0x2
bspmm g\_reg\_mipi\_tx\_base+0x00b4 0x0
bspmd.l g\_reg\_mipi\_tx\_base+0x00b8
`### VO BT.656 Pin Multiplexing<a name="ZH-CN_TOPIC_0000002408102278"></a> [Configuration Example]`
static void vo\_bt\_pin\_mux(int vo\_bt\_mode) { void *iocfg2\_base = sys\_config\_get\_reg\_iocfg2; vo\_cmos\_set\_pin\_drive\_cap(MIPI\_TX\_DRIVE\_CAP\_LEVEL3); sys\_writel(iocfg2\_base + 0x00C8, 0x0682); sys\_writel(iocfg2\_base + 0x00A8, 0x2); sys\_writel(iocfg2\_base + 0x00AC, 0x2); sys\_writel(iocfg2\_base + 0x00B0, 0x2); sys\_writel(iocfg2\_base + 0x00B4, 0x2); sys\_writel(iocfg2\_base + 0x00B8, 0x2); sys\_writel(iocfg2\_base + 0x00C0, 0x2); sys\_writel(iocfg2\_base + 0x00C4, 0x2); sys\_writel(iocfg2\_base + 0x00BC, 0x2); if (vo\_bt\_mode == VO\_BT656\_MODE) return; }
`[Description] VO BT.656 uses DATA0~DATA7 of the VO BT.1120 interface. Refer to the VO BT.1120 section for drive capability configuration. **Figure 1** VO BT.656 Schematic<a name="_fig355162313143"></a>  ### RGB Pin Multiplexing<a name="ZH-CN_TOPIC_0000002408102134"></a> [Configuration Example]`
static void vo\_rgb\_pin\_mux(int vo\_rgb\_mode) { void* iocfg2\_base = sys\_config\_get\_reg\_iocfg2; vo\_cmos\_set\_pin\_drive\_cap(MIPI\_TX\_DRIVE\_CAP\_LEVEL2); sys\_writel(iocfg2\_base + 0x0098, 0x0223); sys\_writel(iocfg2\_base + 0x0080, 0x0213); sys\_writel(iocfg2\_base + 0x008C, 0x0213); sys\_writel(iocfg2\_base + 0x0090, 0x0213); sys\_writel(iocfg2\_base + 0x00C0, 0x3); sys\_writel(iocfg2\_base + 0x00B8, 0x3); sys\_writel(iocfg2\_base + 0x00CC, 0x0233); sys\_writel(iocfg2\_base + 0x00D0, 0x0233); sys\_writel(iocfg2\_base + 0x00AC, 0x3); sys\_writel(iocfg2\_base + 0x00B4, 0x3); if (vo\_rgb\_mode == VO\_RGB\_6BIT\_MODE) return; sys\_writel(iocfg2\_base + 0x00B0, 0x3); sys\_writel(iocfg2\_base + 0x00A8, 0x3); if (vo\_rgb\_mode == VO\_RGB\_8BIT\_MODE) return; sys\_writel(iocfg2\_base + 0x00A0, 0x3); sys\_writel(iocfg2\_base + 0x00A4, 0x3); sys\_writel(iocfg2\_base + 0x00C8, 0x0233); sys\_writel(iocfg2\_base + 0x00D4, 0x0233); sys\_writel(iocfg2\_base + 0x0084, 0x0213); sys\_writel(iocfg2\_base + 0x0094, 0x0213); sys\_writel(iocfg2\_base + 0x0088, 0x0213); sys\_writel(iocfg2\_base + 0x009C, 0x0213); if (vo\_rgb\_mode == VO\_RGB\_16BIT\_MODE) return; sys\_writel(iocfg2\_base + 0x00E0, 0x0233); sys\_writel(iocfg2\_base + 0x00D8, 0x0233); if (vo\_rgb\_mode == VO\_RGB\_18BIT\_MODE) return; sys\_writel(iocfg2\_base + 0x00BC, 0x3); sys\_writel(iocfg2\_base + 0x00C4, 0x3); sys\_writel(iocfg2\_base + 0x0068, 0x0203); sys\_writel(iocfg2\_base + 0x006C, 0x0203); sys\_writel(iocfg2\_base + 0x0064, 0x0203); sys\_writel(iocfg2\_base + 0x0060, 0x0213); }
`[Description] RGB interface signals (RGB\_CLK, RGB\_DE, RGB\_HS, RGB\_VS, RGB\_DATA0~RGB\_DATA23) are output through various pins. Refer to schematic figures in the original document. Example: AF2 (iocfg\_reg60, 0x0102F0098) is RGB\_CLK with function options SDIO0\_CDATA3/GPIO1\_0/RGB\_CLK/VO\_BT1120\_DATA13/PWM1\_OUT10\_0\_P. Configuration 0x0223: Bits[3:0]=3 (VO\_BT1120\_DATA13 in BT mode, or RGB\_CLK in RGB mode). ### Audio Pin Multiplexing<a name="ZH-CN_TOPIC_0000002408262150"></a> [Configuration]`
static void audio\_pin\_mux(void) { void *iocfg2\_base = sys\_config\_get\_reg\_iocfg2; sys\_writel(iocfg2\_base + 0x00F4, 0x0041); sys\_writel(iocfg2\_base + 0x00F8, 0x0041); }
`[Description] Audio pins are configured for I2S interface functionality. Refer to the hardware schematic for specific pin connections. [Precautions] None. ### Amplifier GPIO Pin Multiplexing<a name="ZH-CN_TOPIC_0000002441661489"></a> [Configuration] (Using Hi3403V100 as an example)`
static void amp\_unmute\_pin\_mux(void) { void* iocfg2\_base = get\_reg\_iocfg2; void *gpio\_base = get\_reg\_gpio; /* GPIO10\_0 */ sys\_writel(iocfg2\_base + 0x00FC, 0x0201); /* output high */ sys\_writel(gpio\_base + 0xA400, 0x01); sys\_writel(gpio\_base + 0xA004, 0x01); }
``` [Description] The amplifier chip enable is controlled via GPIO10\_0 (AP17, iocfg\_reg85, 0x0102F00FC). AP17 has 3 function options: LSADC\_CH3/GPIO10\_0/PCIE\_RST\_N. Configuration 0x00000201: Bits[3:0]=1 (GPIO10\_0), Bits[7:4]=0 (drive level 1), Bits[9:8]=2 (pull-down on, pull-up off), Bits[10]=0 (fast edge). GPIO\_DIR register (0x1109A400) Bit[0]=1 sets GPIO10\_0 as output. GPIO\_DATA register (0x1109A004) Bit[0]=1 drives the pin high.* *Figure 1*\* GPIO10\_0 Schematic [](figures/GPIO10_0originarrangegraph.png) [Precautions] None. # Other
None.