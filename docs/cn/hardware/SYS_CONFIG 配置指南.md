# 前言<a name="ZH-CN_TOPIC_0000002441661589"></a>

**概述<a name="section142mcpsimp"></a>**

本文为使用MPP媒体处理芯片进行开发的工程师而写，目的是供您在开发过程中查阅媒体处理软件SYS\_CONFIG子模块的各种参考信息，包括系统控制、时钟配置、管脚复用等。本文档描述SYS\_CONFIG中的各个关键函数的使用方法，以及相关的配置原理。

> **说明：** 
>本文以Hi3403V100描述为例，未有特殊说明，SS927V100与Hi3403V100内容一致。

**产品版本<a name="section145mcpsimp"></a>**

与本文档相对应的产品版本如下。

<a name="table148mcpsimp"></a>
<table><thead align="left"><tr id="row153mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row159mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>V100</p>
</td>
</tr>

</tbody>
</table>

**读者对象<a name="section164mcpsimp"></a>**

本文档（本指南）主要适用于以下工程师：

-   技术支持工程师
-   软件开发工程师

**符号约定<a name="section170mcpsimp"></a>**

在本文中可能出现下列标志，它们所代表的含义如下。

<a name="table173mcpsimp"></a>
<table><thead align="left"><tr id="row178mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.3.1.1"><p id="p180mcpsimp"><a name="p180mcpsimp"></a><a name="p180mcpsimp"></a><strong id="b181mcpsimp"><a name="b181mcpsimp"></a><a name="b181mcpsimp"></a>符号</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79%" id="mcps1.1.3.1.2"><p id="p183mcpsimp"><a name="p183mcpsimp"></a><a name="p183mcpsimp"></a><strong id="b184mcpsimp"><a name="b184mcpsimp"></a><a name="b184mcpsimp"></a>说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row186mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p188mcpsimp"><a name="p188mcpsimp"></a><a name="p188mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img src="figures/zh-cn_image_0000002408102390.png" alt="" /></span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p190mcpsimp"><a name="p190mcpsimp"></a><a name="p190mcpsimp"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>

</tbody>
</table>

**表 2**  时钟复位寄存器地址

<a name="_table61494432"></a>
<table><thead align="left"><tr id="row355mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.5.1.1"><p id="p357mcpsimp"><a name="p357mcpsimp"></a><a name="p357mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.5.1.2"><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>基址变量</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.3"><p id="p361mcpsimp"><a name="p361mcpsimp"></a><a name="p361mcpsimp"></a>基地址</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.4"><p id="p363mcpsimp"><a name="p363mcpsimp"></a><a name="p363mcpsimp"></a>长度</p>
</th>
</tr>
</thead>
<tbody><tr id="row365mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.5.1.1 "><p id="p367mcpsimp"><a name="p367mcpsimp"></a><a name="p367mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.2 "><p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>g_reg_crg_base</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.3 "><p id="p371mcpsimp"><a name="p371mcpsimp"></a><a name="p371mcpsimp"></a>0x11010000</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.4 "><p id="p373mcpsimp"><a name="p373mcpsimp"></a><a name="p373mcpsimp"></a>0x10000</p>
</td>
</tr>
</tbody>
</table>

**表 3**  管脚复用寄存器地址

<a name="_table16578980"></a>
<table><thead align="left"><tr id="row381mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.5.1.1"><p id="p383mcpsimp"><a name="p383mcpsimp"></a><a name="p383mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.5.1.2"><p id="p385mcpsimp"><a name="p385mcpsimp"></a><a name="p385mcpsimp"></a>基址变量</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.3"><p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>基地址</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.4"><p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>长度</p>
</th>
</tr>
</thead>
<tbody><tr id="row391mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="27%" headers="mcps1.2.5.1.1 "><p id="p393mcpsimp"><a name="p393mcpsimp"></a><a name="p393mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.2 "><p id="p395mcpsimp"><a name="p395mcpsimp"></a><a name="p395mcpsimp"></a>g_reg_iocfg_base</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.3 "><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>0x10230000</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.4 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>0x10000</p>
</td>
</tr>

</tbody>
</table>

**表 6**  DDR寄存器地址

<a name="table461mcpsimp"></a>
<table><thead align="left"><tr id="row469mcpsimp"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.5.1.1"><p id="p471mcpsimp"><a name="p471mcpsimp"></a><a name="p471mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.5.1.2"><p id="p473mcpsimp"><a name="p473mcpsimp"></a><a name="p473mcpsimp"></a>基址变量</p>
</th>
<th class="cellrowborder" valign="top" width="28.28282828282828%" id="mcps1.2.5.1.3"><p id="p475mcpsimp"><a name="p475mcpsimp"></a><a name="p475mcpsimp"></a>基地址</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.4"><p id="p477mcpsimp"><a name="p477mcpsimp"></a><a name="p477mcpsimp"></a>长度</p>
</th>
</tr>
</thead>
<tbody><tr id="row479mcpsimp"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p481mcpsimp"><a name="p481mcpsimp"></a><a name="p481mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.5.1.2 "><p id="p483mcpsimp"><a name="p483mcpsimp"></a><a name="p483mcpsimp"></a>g_reg_ddr_base</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.3 "><p id="p485mcpsimp"><a name="p485mcpsimp"></a><a name="p485mcpsimp"></a>0x11140000</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.4 "><p id="p487mcpsimp"><a name="p487mcpsimp"></a><a name="p487mcpsimp"></a>0x10000</p>
</td>
</tr>
</tbody>
</table>

**表 7**  MIPI\_TX寄存器地址

<a name="_table071427174311"></a>
<table><thead align="left"><tr id="row495mcpsimp"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.5.1.1"><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.5.1.2"><p id="p499mcpsimp"><a name="p499mcpsimp"></a><a name="p499mcpsimp"></a>基址变量</p>
</th>
<th class="cellrowborder" valign="top" width="28.28282828282828%" id="mcps1.2.5.1.3"><p id="p501mcpsimp"><a name="p501mcpsimp"></a><a name="p501mcpsimp"></a>基地址</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.4"><p id="p503mcpsimp"><a name="p503mcpsimp"></a><a name="p503mcpsimp"></a>长度</p>
</th>
</tr>
</thead>
<tbody><tr id="row505mcpsimp"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p507mcpsimp"><a name="p507mcpsimp"></a><a name="p507mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.5.1.2 "><p id="p509mcpsimp"><a name="p509mcpsimp"></a><a name="p509mcpsimp"></a>g_reg_mipi_tx_base</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.3 "><p id="p511mcpsimp"><a name="p511mcpsimp"></a><a name="p511mcpsimp"></a>0x17A80000</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.4 "><p id="p513mcpsimp"><a name="p513mcpsimp"></a><a name="p513mcpsimp"></a>0x10000</p>
</td>
</tr>
</tbody>
</table>

本章节对寄存器地址的映射是其他章节的寄存器配置的基础，在完成本章节寄存器物理地址（即寄存器地址）映射后得到寄存器虚拟地址，通过寄存器虚拟地址可完成对相应寄存器的读写。

操作函数如下：

```
#define sys_writel(addr, value) ((*((volatile unsigned int *)(addr))) = (value))
#define sys_read(addr) (*((volatile int *)(addr)))
```

-   sys\_writel是写函数，addr表示寄存器虚拟地址，value表示写入寄存器的值。
-   sys\_read是读函数，addr表示寄存器虚拟地址。操作的结果即为读取到的寄存器的值。

# 系统控制<a name="ZH-CN_TOPIC_0000002408262198"></a>


## VI VPSS在线离线模式<a name="ZH-CN_TOPIC_0000002441701441"></a>

根据VI VPSS在线离线模式情况，需要选择VI VPSS在线离线模式。

以下以Hi3403V100为例说明。


### VI VPSS在线离线模式配置<a name="ZH-CN_TOPIC_0000002408102290"></a>

【配置】

g\_reg\_misc\_base 见表1.

```
static void set_vi_online_video_norm_vpss_online_qos(void) 
{ 
    void *misc_base = sys_config_get_reg_misc(); 
  
    sys_writel(misc_base + 0x1000, 0x44777755); 
    sys_writel(misc_base + 0x1004, 0x45455066); 
    sys_writel(misc_base + 0x1008, 0x60050055); 
    sys_writel(misc_base + 0x100c, 0x45433306); 
    sys_writel(misc_base + 0x1010, 0x33333366); 
    sys_writel(misc_base + 0x1014, 0x33503333); 
    sys_writel(misc_base + 0x1018, 0x00044466); 
  
    sys_writel(misc_base + 0x101c, 0x44777765); 
    sys_writel(misc_base + 0x1020, 0x55556066); 
    sys_writel(misc_base + 0x1024, 0x60050056); 
    sys_writel(misc_base + 0x1028, 0x46433306); 
    sys_writel(misc_base + 0x102c, 0x66555377); 
    sys_writel(misc_base + 0x1030, 0x33503663); 
    sys_writel(misc_base + 0x1034, 0x00055577); 
}
```

【描述说明】

MDDRC\_QOS\_CTRL0为QOS寄存器。

Offset Address: 0x5000   Total Reset Value: 0x0000\_0000

<a name="table535mcpsimp"></a>
<table><thead align="left"><tr id="row543mcpsimp"><th class="cellrowborder" valign="top" width="12.000000000000002%" id="mcps1.1.6.1.1"><p id="p545mcpsimp"><a name="p545mcpsimp"></a><a name="p545mcpsimp"></a>Bits</p>
</th>
<th class="cellrowborder" valign="top" width="12.000000000000002%" id="mcps1.1.6.1.2"><p id="p547mcpsimp"><a name="p547mcpsimp"></a><a name="p547mcpsimp"></a>Access</p>
</th>
<th class="cellrowborder" valign="top" width="23.000000000000004%" id="mcps1.1.6.1.3"><p id="p549mcpsimp"><a name="p549mcpsimp"></a><a name="p549mcpsimp"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="42.00000000000001%" id="mcps1.1.6.1.4"><p id="p551mcpsimp"><a name="p551mcpsimp"></a><a name="p551mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11.000000000000002%" id="mcps1.1.6.1.5"><p id="p553mcpsimp"><a name="p553mcpsimp"></a><a name="p553mcpsimp"></a>Reset</p>
</th>
</tr>
</thead>
<tbody><tr id="row555mcpsimp"><td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.1.6.1.1 "><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>[30:28]</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p559mcpsimp"><a name="p559mcpsimp"></a><a name="p559mcpsimp"></a>RW</p>
</td>
<td class="cellrowborder" valign="top" width="23.000000000000004%" headers="mcps1.1.6.1.3 "><p id="p561mcpsimp"><a name="p561mcpsimp"></a><a name="p561mcpsimp"></a>dpu_w_qos</p>
</td>
<td class="cellrowborder" valign="top" width="42.00000000000001%" headers="mcps1.1.6.1.4 "><p id="p563mcpsimp"><a name="p563mcpsimp"></a><a name="p563mcpsimp"></a>dpu写通道QOS配置</p>
</td>
<td class="cellrowborder" valign="top" width="11.000000000000002%" headers="mcps1.1.6.1.5 "><p id="p565mcpsimp"><a name="p565mcpsimp"></a><a name="p565mcpsimp"></a>0x0</p>
</td>
</tr>





<tr id="row3286mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p3288mcpsimp"><a name="p3288mcpsimp"></a><a name="p3288mcpsimp"></a>10</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3290mcpsimp"><a name="p3290mcpsimp"></a><a name="p3290mcpsimp"></a>管脚电平转换速率控制：</p>
<p id="p3291mcpsimp"><a name="p3291mcpsimp"></a><a name="p3291mcpsimp"></a>0x0：快沿输出；</p>
<p id="p3292mcpsimp"><a name="p3292mcpsimp"></a><a name="p3292mcpsimp"></a>0x1：慢沿输出。</p>
</td>
</tr>
<tr id="row3293mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p3295mcpsimp"><a name="p3295mcpsimp"></a><a name="p3295mcpsimp"></a>9</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3297mcpsimp"><a name="p3297mcpsimp"></a><a name="p3297mcpsimp"></a>管脚下拉控制：</p>
<p id="p3298mcpsimp"><a name="p3298mcpsimp"></a><a name="p3298mcpsimp"></a>0x0：关闭；</p>
<p id="p3299mcpsimp"><a name="p3299mcpsimp"></a><a name="p3299mcpsimp"></a>0x1：打开。</p>
</td>
</tr>
<tr id="row3300mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p3302mcpsimp"><a name="p3302mcpsimp"></a><a name="p3302mcpsimp"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3304mcpsimp"><a name="p3304mcpsimp"></a><a name="p3304mcpsimp"></a>管脚上拉控制：</p>
<p id="p3305mcpsimp"><a name="p3305mcpsimp"></a><a name="p3305mcpsimp"></a>0x0：关闭；</p>
<p id="p3306mcpsimp"><a name="p3306mcpsimp"></a><a name="p3306mcpsimp"></a>0x1：打开。</p>
</td>
</tr>
<tr id="row3307mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p3309mcpsimp"><a name="p3309mcpsimp"></a><a name="p3309mcpsimp"></a>7:4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3311mcpsimp"><a name="p3311mcpsimp"></a><a name="p3311mcpsimp"></a>管脚驱动能力选择：</p>
<p id="p3312mcpsimp"><a name="p3312mcpsimp"></a><a name="p3312mcpsimp"></a>0x0：IO2档位1；</p>
<p id="p3313mcpsimp"><a name="p3313mcpsimp"></a><a name="p3313mcpsimp"></a>0x1：IO2档位2；</p>
<p id="p3314mcpsimp"><a name="p3314mcpsimp"></a><a name="p3314mcpsimp"></a>0x2：IO2档位3；</p>
<p id="p3315mcpsimp"><a name="p3315mcpsimp"></a><a name="p3315mcpsimp"></a>0x3：IO2档位4；</p>
<p id="p3316mcpsimp"><a name="p3316mcpsimp"></a><a name="p3316mcpsimp"></a>0x4：IO2档位5；</p>
<p id="p3317mcpsimp"><a name="p3317mcpsimp"></a><a name="p3317mcpsimp"></a>0x5：IO2档位6；</p>
<p id="p3318mcpsimp"><a name="p3318mcpsimp"></a><a name="p3318mcpsimp"></a>0x6：IO2档位7；</p>
<p id="p3319mcpsimp"><a name="p3319mcpsimp"></a><a name="p3319mcpsimp"></a>0x7：IO2档位8；</p>
<p id="p3320mcpsimp"><a name="p3320mcpsimp"></a><a name="p3320mcpsimp"></a>0x8：IO2档位9；</p>
<p id="p3321mcpsimp"><a name="p3321mcpsimp"></a><a name="p3321mcpsimp"></a>0x9：IO2档位10；</p>
<p id="p3322mcpsimp"><a name="p3322mcpsimp"></a><a name="p3322mcpsimp"></a>0xA：IO2档位11；</p>
<p id="p3323mcpsimp"><a name="p3323mcpsimp"></a><a name="p3323mcpsimp"></a>0xB：IO2档位12；</p>
<p id="p3324mcpsimp"><a name="p3324mcpsimp"></a><a name="p3324mcpsimp"></a>0xC：IO2档位13；</p>
<p id="p3325mcpsimp"><a name="p3325mcpsimp"></a><a name="p3325mcpsimp"></a>0xD：IO2档位14；</p>
<p id="p3326mcpsimp"><a name="p3326mcpsimp"></a><a name="p3326mcpsimp"></a>0xE：IO2档位15；</p>
<p id="p3327mcpsimp"><a name="p3327mcpsimp"></a><a name="p3327mcpsimp"></a>0xF：IO2档位16；</p>
<p id="p3328mcpsimp"><a name="p3328mcpsimp"></a><a name="p3328mcpsimp"></a>其它：保留。</p>
</td>
</tr>
<tr id="row3329mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p3331mcpsimp"><a name="p3331mcpsimp"></a><a name="p3331mcpsimp"></a>3:0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3333mcpsimp"><a name="p3333mcpsimp"></a><a name="p3333mcpsimp"></a>功能选择：</p>
<p id="p3334mcpsimp"><a name="p3334mcpsimp"></a><a name="p3334mcpsimp"></a>0x0：LSADC_CH3；</p>
<p id="p3335mcpsimp"><a name="p3335mcpsimp"></a><a name="p3335mcpsimp"></a>0x1：GPIO10_0；</p>
<p id="p3336mcpsimp"><a name="p3336mcpsimp"></a><a name="p3336mcpsimp"></a>0x2：PCIE_RST_N；</p>
<p id="p3337mcpsimp"><a name="p3337mcpsimp"></a><a name="p3337mcpsimp"></a>其它：保留。</p>
</td>
</tr>
</tbody>
</table>

管脚存在3种复用情形：LSADC\_CH3 / GPIO10\_0 / PCIE\_RST\_N。

AP17配置值为0x00000201：

-   Bits\[3:0\]=0x1表示管脚功能选择为GPIO10\_0；
-   Bits\[7:4\]=0x0表示管脚驱动能力配置为档位1，档位值越大，对应的驱动能力越大；
-   Bits\[9:8\]=0x2表示管脚上拉控制关闭, 下拉控制打开，结合实际电路配置；
-   Bits\[10\]=0x0表示电平转换速率为快沿输出。

GPIO\_DIR为GPIO方向控制寄存器，配置寄存器0x1109A400的Bits \[7:0\]为0x01，表示配置GPIO10\_0为输出方向。

Offset Address: 400   Total Reset Value: 0x00

<a name="table3348mcpsimp"></a>
<table><thead align="left"><tr id="row3356mcpsimp"><th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.1.6.1.1"><p id="p3358mcpsimp"><a name="p3358mcpsimp"></a><a name="p3358mcpsimp"></a>Bits</p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.6.1.2"><p id="p3360mcpsimp"><a name="p3360mcpsimp"></a><a name="p3360mcpsimp"></a>Access</p>
</th>
<th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.1.6.1.3"><p id="p3362mcpsimp"><a name="p3362mcpsimp"></a><a name="p3362mcpsimp"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.1.6.1.4"><p id="p3364mcpsimp"><a name="p3364mcpsimp"></a><a name="p3364mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.6.1.5"><p id="p3366mcpsimp"><a name="p3366mcpsimp"></a><a name="p3366mcpsimp"></a>Reset</p>
</th>
</tr>
</thead>
<tbody><tr id="row3368mcpsimp"><td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.1.6.1.1 "><p id="p3370mcpsimp"><a name="p3370mcpsimp"></a><a name="p3370mcpsimp"></a>[7:0]</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.6.1.2 "><p id="p3372mcpsimp"><a name="p3372mcpsimp"></a><a name="p3372mcpsimp"></a>RW</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.6.1.3 "><p id="p3374mcpsimp"><a name="p3374mcpsimp"></a><a name="p3374mcpsimp"></a>gpio_dir</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.1.6.1.4 "><p id="p3376mcpsimp"><a name="p3376mcpsimp"></a><a name="p3376mcpsimp"></a>GPIO方向控制寄存器。Bits [7:0]分别对应GPIO_DATA[7:0]，各Bit可独立控制。</p>
<p id="p3377mcpsimp"><a name="p3377mcpsimp"></a><a name="p3377mcpsimp"></a>0：输入；</p>
<p id="p3378mcpsimp"><a name="p3378mcpsimp"></a><a name="p3378mcpsimp"></a>1：输出。</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.6.1.5 "><p id="p3380mcpsimp"><a name="p3380mcpsimp"></a><a name="p3380mcpsimp"></a>0x00</p>
</td>
</tr>
</tbody>
</table>

GPIO\_DATA为GPIO数据寄存器，配置寄存器0x1109A004的Bits \[7:0\]为0x01，表示配置GPIO10\_0为输出高电平。

Offset Address: 0x000～0x3FC   Total Reset Value: 0x00

<a name="table3384mcpsimp"></a>
<table><thead align="left"><tr id="row3392mcpsimp"><th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.1.6.1.1"><p id="p3394mcpsimp"><a name="p3394mcpsimp"></a><a name="p3394mcpsimp"></a>Bits</p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.6.1.2"><p id="p3396mcpsimp"><a name="p3396mcpsimp"></a><a name="p3396mcpsimp"></a>Access</p>
</th>
<th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.1.6.1.3"><p id="p3398mcpsimp"><a name="p3398mcpsimp"></a><a name="p3398mcpsimp"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.1.6.1.4"><p id="p3400mcpsimp"><a name="p3400mcpsimp"></a><a name="p3400mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.6.1.5"><p id="p3402mcpsimp"><a name="p3402mcpsimp"></a><a name="p3402mcpsimp"></a>Reset</p>
</th>
</tr>
</thead>
<tbody><tr id="row3404mcpsimp"><td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.1.6.1.1 "><p id="p3406mcpsimp"><a name="p3406mcpsimp"></a><a name="p3406mcpsimp"></a>[7:0]</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.6.1.2 "><p id="p3408mcpsimp"><a name="p3408mcpsimp"></a><a name="p3408mcpsimp"></a>RW</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.6.1.3 "><p id="p3410mcpsimp"><a name="p3410mcpsimp"></a><a name="p3410mcpsimp"></a>gpio_data</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.1.6.1.4 "><p id="p3412mcpsimp"><a name="p3412mcpsimp"></a><a name="p3412mcpsimp"></a>当GPIO配置为输入模式时，为GPIO输入数据；当GPIO配置为输出模式时，为输出数据。各比特均可独立控制。与GPIO_DIR配合使用。</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.6.1.5 "><p id="p3414mcpsimp"><a name="p3414mcpsimp"></a><a name="p3414mcpsimp"></a>0x00</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

# 其他<a name="ZH-CN_TOPIC_0000002441661557"></a>

无。

