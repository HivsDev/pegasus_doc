# 前言<a name="ZH-CN_TOPIC_0000002424362222"></a>

**概述<a name="section3088mcpsimp"></a>**

本文为ISP图像质量调试而写，内部详细介绍了ISP各模块调试方法，目的是为您在开发过程中遇到的问题提供解决办法和帮助。

> **说明：** 
>本文以Hi3403V100描述为例，未有特殊说明，SS927V100与Hi3403V100内容一致。

**产品版本<a name="section3091mcpsimp"></a>**

与本文档相对应的产品版本如下。

<a name="table3094mcpsimp"></a>
<table><thead align="left"><tr id="row3099mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p3101mcpsimp"><a name="p3101mcpsimp"></a><a name="p3101mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p3103mcpsimp"><a name="p3103mcpsimp"></a><a name="p3103mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row3105mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p3107mcpsimp"><a name="p3107mcpsimp"></a><a name="p3107mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p3109mcpsimp"><a name="p3109mcpsimp"></a><a name="p3109mcpsimp"></a>V100</p>
</td>
</tr>

</tbody>
</table>

**读者对象<a name="section3110mcpsimp"></a>**

本文档（本指南）主要适用于以下工程师：

-   技术支持工程师
-   软件开发工程师

**符号约定<a name="section133020216410"></a>**

在本文中可能出现下列标志，它们所代表的含义如下。

<a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>符号</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img src="figures/zh-cn_image_0000002424362510.png" alt="" /></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>


<tr id="row607mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p609mcpsimp"><a name="p609mcpsimp"></a><a name="p609mcpsimp"></a>mesh_strength</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p611mcpsimp"><a name="p611mcpsimp"></a><a name="p611mcpsimp"></a>用来全局纠正LSC标定后的强度。当镜头shading很严重的时候，画面四个角补偿的增益很大，容易导致噪声很大，而且画面有格子现象。这个调整<span xml:lang="sv-SE" id="ph612mcpsimp"><a name="ph612mcpsimp"></a><a name="ph612mcpsimp"></a>mesh_strength小于一倍强度，可以减少LSC的补偿值，让四个角的补偿增益较小一些，达到优化噪声和画面格子问题。</span></p>
<p id="p613mcpsimp"><a name="p613mcpsimp"></a><a name="p613mcpsimp"></a>取值范围：[0, 65535]</p>
</td>
</tr>
<tr id="row614mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p616mcpsimp"><a name="p616mcpsimp"></a><a name="p616mcpsimp"></a>blend_ratio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p618mcpsimp"><a name="p618mcpsimp"></a><a name="p618mcpsimp"></a>两张增益表的融合比例</p>
<p xml:lang="sv-SE" id="p619mcpsimp"><a name="p619mcpsimp"></a><a name="p619mcpsimp"></a><span xml:lang="en-US" id="ph620mcpsimp"><a name="ph620mcpsimp"></a><a name="ph620mcpsimp"></a>取值范围：</span>[0, 256]</p>
</td>
</tr>
<tr id="row621mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p623mcpsimp"><a name="p623mcpsimp"></a><a name="p623mcpsimp"></a>bnr_lsc_auto_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p625mcpsimp"><a name="p625mcpsimp"></a><a name="p625mcpsimp"></a>BNR LSC的表参考Mesh LSC表的使能。默认关，使用用户配置的bnr_lsc_gain_lut表；开启后参考会lsc_gain_lut的表，自动刷新bnr_lsc_gain_lut。</p>
<p id="p626mcpsimp"><a name="p626mcpsimp"></a><a name="p626mcpsimp"></a>取值范围：[0,1]</p>
</td>
</tr>
<tr id="row627mcpsimp"><td class="cellrowborder" rowspan="5" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p629mcpsimp"><a name="p629mcpsimp"></a><a name="p629mcpsimp"></a>ot_isp_shading_lut_attr</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p631mcpsimp"><a name="p631mcpsimp"></a><a name="p631mcpsimp"></a>mesh_scale</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p633mcpsimp"><a name="p633mcpsimp"></a><a name="p633mcpsimp"></a>增益表精度控制参数</p>
<p id="p634mcpsimp"><a name="p634mcpsimp"></a><a name="p634mcpsimp"></a>取值范围：<span xml:lang="sv-SE" id="ph635mcpsimp"><a name="ph635mcpsimp"></a><a name="ph635mcpsimp"></a>[0, 7]</span></p>
</td>
</tr>
<tr id="row636mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>x_grid_width [(OT_ISP_LSC_GRID_COL - 1)/2]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>用来储存各GRID分区宽度大小信息。该接口各分量最小值为4，总和应为原画面宽度的四分之一。（例如原画面大小为1080p，则该接口各参数总和应为480）</p>
<p xml:lang="sv-SE" id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a><span xml:lang="en-US" id="ph642mcpsimp"><a name="ph642mcpsimp"></a><a name="ph642mcpsimp"></a>取值范围：</span>[4, width/4 - 60]，width为原画面的宽度</p>
</td>
</tr>
<tr id="row643mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>y_grid_width[(OT_ISP_LSC_GRID_ROW - 1)/2]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>用来储存各GRID分区高度大小信息。该接口各分量最小值为4，总和应为原画面高度的四分之一。（例如原画面大小为1080p，则该接口各参数总和应为270）</p>
<p xml:lang="sv-SE" id="p648mcpsimp"><a name="p648mcpsimp"></a><a name="p648mcpsimp"></a><span xml:lang="en-US" id="ph649mcpsimp"><a name="ph649mcpsimp"></a><a name="ph649mcpsimp"></a>取值范围：</span>[4,height/4 - 60]，height为原画面的高度</p>
</td>
</tr>
<tr id="row650mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p652mcpsimp"><a name="p652mcpsimp"></a><a name="p652mcpsimp"></a>lsc_gain_lut[2]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p654mcpsimp"><a name="p654mcpsimp"></a><a name="p654mcpsimp"></a>两组色温下的增益表配置。硬件基于这两组表以及blend_ratio进行当前色温下校正增益表的计算</p>
<p xml:lang="sv-SE" id="p655mcpsimp"><a name="p655mcpsimp"></a><a name="p655mcpsimp"></a><span xml:lang="en-US" id="ph656mcpsimp"><a name="ph656mcpsimp"></a><a name="ph656mcpsimp"></a>取值范围：</span>[0, 1023]</p>
</td>
</tr>
<tr id="row657mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>bnr_lsc_gain_lut</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p661mcpsimp"><a name="p661mcpsimp"></a><a name="p661mcpsimp"></a>用于BNR LSC参考所用的增益表。</p>
<p xml:lang="sv-SE" id="p662mcpsimp"><a name="p662mcpsimp"></a><a name="p662mcpsimp"></a><span xml:lang="en-US" id="ph663mcpsimp"><a name="ph663mcpsimp"></a><a name="ph663mcpsimp"></a>取值范围：</span>[0, 65535]</p>
</td>
</tr>
</tbody>
</table>

### 调试步骤<a name="ZH-CN_TOPIC_0000002457881153"></a>

Shading是与一种镜头有关的缺陷，对于每个镜头都需按照[《图像质量调试工具使用指南》](../ai/图像质量调试工具使用指南.md)LSC部分所描述的步骤进行数据的采集与标定，将获取的标定结果写入cmos\_ex.h文件中或直接导入到PQTools上。具体每个参数的作用和对图像的影响可参考上表中的描述。

> **须知：** 
>-   增益表的默认配置与ot\_isp\_cmos\_alg\_key中的bit1\_lsc 标志位有关，如果bit1\_lsc=1\)，则采用cmos\_ex.h中的配置值作为默认值；否则默认配置为1倍增益。具体请参考[《ISP开发参考》](ISP 开发参考（1--2）.md)。
>-   在标定时，如果看到“Please set Mesh scale to \*”说明所标定图像的增益超过了所设定的mesh\_scale的增益范围，应当把mesh\_scale设定为推荐的数值，重新进行Mesh Shading的标定。

## Gamma<a name="ZH-CN_TOPIC_0000002424202274"></a>





### 功能描述<a name="ZH-CN_TOPIC_0000002457881093"></a>

Gamma模块对图像进行亮度空间非线性转换以适配输出设备。Gamma模块校正R、G、B时调用同一组Gamma表，Gamma表各节点之间的间距相同，节点之间的图像像素值使用线性插值生成。

### 关键参数<a name="ZH-CN_TOPIC_0000002457840889"></a>

**表 1**  Gamma关键参数

<a name="table1389mcpsimp"></a>
<table><thead align="left"><tr id="row1395mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.2.3.1.1"><p id="p1397mcpsimp"><a name="p1397mcpsimp"></a><a name="p1397mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.2.3.1.2"><p id="p1399mcpsimp"><a name="p1399mcpsimp"></a><a name="p1399mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1401mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.3.1.1 "><p id="p1403mcpsimp"><a name="p1403mcpsimp"></a><a name="p1403mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.3.1.2 "><p id="p1405mcpsimp"><a name="p1405mcpsimp"></a><a name="p1405mcpsimp"></a><span xml:lang="sv-SE" id="ph1406mcpsimp"><a name="ph1406mcpsimp"></a><a name="ph1406mcpsimp"></a>Gamma</span>校正功能使能。</p>
<p xml:lang="sv-SE" id="p1407mcpsimp"><a name="p1407mcpsimp"></a><a name="p1407mcpsimp"></a>TD_FALSE：<span xml:lang="en-US" id="ph1408mcpsimp"><a name="ph1408mcpsimp"></a><a name="ph1408mcpsimp"></a>关闭</span>；</p>
<p xml:lang="sv-SE" id="p1409mcpsimp"><a name="p1409mcpsimp"></a><a name="p1409mcpsimp"></a>TD_TRUE：<span xml:lang="en-US" id="ph1410mcpsimp"><a name="ph1410mcpsimp"></a><a name="ph1410mcpsimp"></a>使能。</span></p>
<p xml:lang="sv-SE" id="p1411mcpsimp"><a name="p1411mcpsimp"></a><a name="p1411mcpsimp"></a><span xml:lang="en-US" id="ph1412mcpsimp"><a name="ph1412mcpsimp"></a><a name="ph1412mcpsimp"></a>默认值为</span>TD_TRUE。</p>
</td>
</tr>
<tr id="row1413mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.3.1.1 "><p id="p1415mcpsimp"><a name="p1415mcpsimp"></a><a name="p1415mcpsimp"></a>curve_type</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p1417mcpsimp"><a name="p1417mcpsimp"></a><a name="p1417mcpsimp"></a>Gamma曲线选择<span xml:lang="en-US" id="ph1418mcpsimp"><a name="ph1418mcpsimp"></a><a name="ph1418mcpsimp"></a>。</span></p>
<p xml:lang="sv-SE" id="p1419mcpsimp"><a name="p1419mcpsimp"></a><a name="p1419mcpsimp"></a><span xml:lang="en-US" id="ph1420mcpsimp"><a name="ph1420mcpsimp"></a><a name="ph1420mcpsimp"></a>默认值为</span>OT_ISP_GAMMA_CURVE_DEFAULT。</p>
<p xml:lang="sv-SE" id="p1421mcpsimp"><a name="p1421mcpsimp"></a><a name="p1421mcpsimp"></a>SDR模式为 OT_ISP_GAMMA_CURVE_SRGB</p>
<p xml:lang="sv-SE" id="p1422mcpsimp"><a name="p1422mcpsimp"></a><a name="p1422mcpsimp"></a>HDR模式为 OT_ISP_GAMMA_CURVE_HDR，不支持该选项</p>
<p xml:lang="sv-SE" id="p1423mcpsimp"><a name="p1423mcpsimp"></a><a name="p1423mcpsimp"></a>用户自定义模式为OT_ISP_GAMMA_CURVE_USER_DEFINE</p>
</td>
</tr>
<tr id="row1424mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.3.1.1 "><p id="p1426mcpsimp"><a name="p1426mcpsimp"></a><a name="p1426mcpsimp"></a>table[OT_ISP_GAMMA_NODE_NUM]</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p1428mcpsimp"><a name="p1428mcpsimp"></a><a name="p1428mcpsimp"></a>Gamma表。</p>
<p xml:lang="sv-SE" id="p1429mcpsimp"><a name="p1429mcpsimp"></a><a name="p1429mcpsimp"></a>取值范围：[0, 0xFFF]</p>
</td>
</tr>
</tbody>
</table>

### 调试步骤<a name="ZH-CN_TOPIC_0000002457840929"></a>

用户自定义Gamma曲线时，必须确保Gamma表配置正确。WDR模式下的Gamma曲线与线性模式不一样，WDR模式下Gamma应配置为线性模式（Y=X）。

HDR模式下应配置为OT\_ISP\_GAMMA\_CURVE\_HDR模式。

不同场景下Gamma曲线配置不同，按关注点进行相应的曲线调整。

### Gamma参数<a name="ZH-CN_TOPIC_0000002424202390"></a>

如果使用用户自定义Gamma曲线时，也可以通过PQ工具上，Curve区域的相关参数进行配置并生成Gamma曲线。

**图 1**  Gamma参数配置选项Curve区域<a name="fig673mcpsimp"></a>  
<img src="figures/Gamma参数配置选项Curve区域.png" alt="" />

Curve区域由两个参数组成，Gamma COEFFI和Slope at zero。其中Gamma COEFFI用来控制Gamma生成的形状，Slope at zero用来控制Gamma曲线的零点斜率大小。

两个参数对曲线形状的影响具体如下：

如果Slope at zero的值一致，则曲线起始阶段斜率一致，值也基本相同，曲线由于Gamma COEFFI参数的不同而形状不同，变化趋势如下。

**图 2**  Gamma COEFFI对Gamma曲线的影响<a name="fig678mcpsimp"></a>  
<img src="figures/Gamma-COEFFI对Gamma曲线的影响.png" alt="" />

-   如果是COEFFI不变，而只是Slope at zero有变化，则曲线整体形状不变，只是在0点斜率处发生变化（会导致整体曲线发生轻微位移）。

**图 3**  Gamma COEFFI对Gamma曲线的影响<a name="fig682mcpsimp"></a>  
<img src="figures/Gamma-COEFFI对Gamma曲线的影响-0.png" alt="" />

**图 4**  Gamma COEFFI对Gamma曲线的影响（零点斜率处放大）<a name="fig684mcpsimp"></a>  
<img src="figures/Gamma-COEFFI对Gamma曲线的影响（零点斜率处放大）.png" alt="" />

## White Balance<a name="ZH-CN_TOPIC_0000002424362106"></a>





### 功能描述<a name="ZH-CN_TOPIC_0000002457840965"></a>

同一物体在不同光源照射下呈现的颜色是不同的，受光源色温的影响。低色温光源下，白色物体偏红，高色温光源下，白色物体偏蓝。人眼可根据大脑的记忆判断，识别物体的真实颜色。AWB（Auto White Balance）算法的功能是降低外界光源对物体真实颜色的影响，使得我们采集的颜色信息转变为在理想日光光源下的无偏色信息。

AWB算法的基本原理是，根据场景内灰色物体的颜色信息，计算R, G, B颜色通道的增益，乘以增益后，RGB三个通道达到平衡。

AWB的增益是全局的，因此，在混合光源下，不能达到所有灰色区域的RGB三通道平衡。

目前我们提供两种AWB算法，分别为AWB与SPECAWB。SPECAWB应用了机器学习算法, 通过学习大量场景内的Wb Gain值获得不同亮度下的光源分布概率，结合实际场景内的白点来还原颜色。当场景内缺乏灰色参考,或者大面积肤色时SPECAWB算法可以获得更好的性能。相比AWB算法的主要效果提升如[图1](#fig13215624131819)所示。

**图 1**  AWB和SPECAWB算法<a name="fig13215624131819"></a>  
<img src="figures/AWB和SPECAWB算法.png" alt="" />

### 关键参数\(AWB\)<a name="ZH-CN_TOPIC_0000002424362038"></a>

**表 1**  AWB标定参数

<a name="table732mcpsimp"></a>
<table><thead align="left"><tr id="row738mcpsimp"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p740mcpsimp"><a name="p740mcpsimp"></a><a name="p740mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p742mcpsimp"><a name="p742mcpsimp"></a><a name="p742mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row744mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p746mcpsimp"><a name="p746mcpsimp"></a><a name="p746mcpsimp"></a>ref_color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>静态白平衡系数标定的环境色温，单位Kelvin。推荐在Macbeth D50标准光源环境或室外晴天环境捕获24色卡Raw数据进行标定。</p>
<p id="p749mcpsimp"><a name="p749mcpsimp"></a><a name="p749mcpsimp"></a>取值范围：[0x0, 0xFFFF]</p>
</td>
</tr>
<tr id="row750mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p752mcpsimp"><a name="p752mcpsimp"></a><a name="p752mcpsimp"></a>static_wb[4]</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p754mcpsimp"><a name="p754mcpsimp"></a><a name="p754mcpsimp"></a>静态白平衡系数，由AWB标定工具给出。</p>
<p id="p755mcpsimp"><a name="p755mcpsimp"></a><a name="p755mcpsimp"></a>取值范围：[0x0, 0xFFF]</p>
</td>
</tr>
<tr id="row756mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p758mcpsimp"><a name="p758mcpsimp"></a><a name="p758mcpsimp"></a>curve_para[0-2]</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p760mcpsimp"><a name="p760mcpsimp"></a><a name="p760mcpsimp"></a>普朗克曲线系数，<span xml:lang="en-US" id="ph761mcpsimp"><a name="ph761mcpsimp"></a><a name="ph761mcpsimp"></a>由AWB标定工具给出。</span>普朗克曲线描绘白色块在不同色温的标准光源下的颜色表现。</p>
</td>
</tr>
<tr id="row762mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p764mcpsimp"><a name="p764mcpsimp"></a><a name="p764mcpsimp"></a>curve_para[3-5]</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p766mcpsimp"><a name="p766mcpsimp"></a><a name="p766mcpsimp"></a>色温曲线系数，<span xml:lang="en-US" id="ph767mcpsimp"><a name="ph767mcpsimp"></a><a name="ph767mcpsimp"></a>由AWB标定工具给出。</span>色温曲线描绘白色块的颜色表现与色温的对应关系。</p>
</td>
</tr>
</tbody>
</table>

**表 2**  AWB参数

<a name="table768mcpsimp"></a>
<table><thead align="left"><tr id="row774mcpsimp"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p776mcpsimp"><a name="p776mcpsimp"></a><a name="p776mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p778mcpsimp"><a name="p778mcpsimp"></a><a name="p778mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row780mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p782mcpsimp"><a name="p782mcpsimp"></a><a name="p782mcpsimp"></a>alg_type</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p784mcpsimp"><a name="p784mcpsimp"></a><a name="p784mcpsimp"></a>白平衡的算法类型属性，支持OT_ISP_AWB_ALG_LOWCOST和OT_ISP_AWB_ALG_ADVANCE可选。OT_ISP_AWB_ALG_LOWCOST CPU占用较少，对光源的适应性较好。OT_ISP_AWB_ALG_ADVANCE提升了AWB精度。</p>
</td>
</tr>
<tr id="row785mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p787mcpsimp"><a name="p787mcpsimp"></a><a name="p787mcpsimp"></a>speed</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p789mcpsimp"><a name="p789mcpsimp"></a><a name="p789mcpsimp"></a>AWB收敛速度，值越大，AWB收敛越快。</p>
<p id="p790mcpsimp"><a name="p790mcpsimp"></a><a name="p790mcpsimp"></a>取值范围：[0x0, 0xFFF]</p>
</td>
</tr>
<tr id="row791mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p793mcpsimp"><a name="p793mcpsimp"></a><a name="p793mcpsimp"></a>high_color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p795mcpsimp"><a name="p795mcpsimp"></a><a name="p795mcpsimp"></a>AWB支持的色温上限，推荐取值在[10000, 15000]。</p>
<p xml:lang="sv-SE" id="p796mcpsimp"><a name="p796mcpsimp"></a><a name="p796mcpsimp"></a>色温上限越大，蓝色物体对AWB的干扰越大。</p>
</td>
</tr>
<tr id="row797mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p799mcpsimp"><a name="p799mcpsimp"></a><a name="p799mcpsimp"></a>low_color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p801mcpsimp"><a name="p801mcpsimp"></a><a name="p801mcpsimp"></a>AWB支持的色温下限，推荐取值在[1500, 2500]。</p>
<p xml:lang="sv-SE" id="p802mcpsimp"><a name="p802mcpsimp"></a><a name="p802mcpsimp"></a>色温下限越小，橙色、红色物体对AWB的干扰越大。</p>
</td>
</tr>
<tr id="row803mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p805mcpsimp"><a name="p805mcpsimp"></a><a name="p805mcpsimp"></a>ct_limit</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p807mcpsimp"><a name="p807mcpsimp"></a><a name="p807mcpsimp"></a>检测色温超出色温范围时，AWB算法的动作。检测色温在色温范围内时，该模块不生效。</p>
<p id="p808mcpsimp"><a name="p808mcpsimp"></a><a name="p808mcpsimp"></a>支持Manual和Auto两种方式，Manual模式下，由用户定义色温超限时AWB的增益；Auto模式下，根据AWB标定参数，确定色温超限时AWB的增益。</p>
</td>
</tr>
<tr id="row809mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p811mcpsimp"><a name="p811mcpsimp"></a><a name="p811mcpsimp"></a>shift_limit</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p813mcpsimp"><a name="p813mcpsimp"></a><a name="p813mcpsimp"></a>以普朗克曲线为中心点，shift_limit为半径确定AWB支持的光源范围。取值越大，对特殊光源的支持越广，影响特定场景下AWB精度。推荐取值0x30-0x50。</p>
</td>
</tr>
<tr id="row814mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p816mcpsimp"><a name="p816mcpsimp"></a><a name="p816mcpsimp"></a>gain_norm_en</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p818mcpsimp"><a name="p818mcpsimp"></a><a name="p818mcpsimp"></a>AWB最终增益是否做归一化，使能后，可提高低照、低色温下的信噪比。</p>
</td>
</tr>
<tr id="row819mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p821mcpsimp"><a name="p821mcpsimp"></a><a name="p821mcpsimp"></a>rg_strength</p>
<p id="p822mcpsimp"><a name="p822mcpsimp"></a><a name="p822mcpsimp"></a>bg_strength</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p824mcpsimp"><a name="p824mcpsimp"></a><a name="p824mcpsimp"></a>AWB校正强度，推荐rg_strength= bg_strength，<span xml:lang="en-US" id="ph825mcpsimp"><a name="ph825mcpsimp"></a><a name="ph825mcpsimp"></a>且设置值</span>&lt;=0x80<span xml:lang="en-US" id="ph826mcpsimp"><a name="ph826mcpsimp"></a><a name="ph826mcpsimp"></a>。</span></p>
<p xml:lang="sv-SE" id="p827mcpsimp"><a name="p827mcpsimp"></a><a name="p827mcpsimp"></a>rg_strength=0x80<span xml:lang="en-US" id="ph828mcpsimp"><a name="ph828mcpsimp"></a><a name="ph828mcpsimp"></a>时</span>，<span xml:lang="en-US" id="ph829mcpsimp"><a name="ph829mcpsimp"></a><a name="ph829mcpsimp"></a>白色恢复为白色</span>；</p>
<p xml:lang="sv-SE" id="p830mcpsimp"><a name="p830mcpsimp"></a><a name="p830mcpsimp"></a>rg_strength&gt;0x80<span xml:lang="en-US" id="ph831mcpsimp"><a name="ph831mcpsimp"></a><a name="ph831mcpsimp"></a>时</span>，<span xml:lang="en-US" id="ph832mcpsimp"><a name="ph832mcpsimp"></a><a name="ph832mcpsimp"></a>白色与光源反向</span>，<span xml:lang="en-US" id="ph833mcpsimp"><a name="ph833mcpsimp"></a><a name="ph833mcpsimp"></a>低色温偏蓝</span>，<span xml:lang="en-US" id="ph834mcpsimp"><a name="ph834mcpsimp"></a><a name="ph834mcpsimp"></a>高色温偏红</span>；</p>
<p id="p835mcpsimp"><a name="p835mcpsimp"></a><a name="p835mcpsimp"></a><span xml:lang="sv-SE" id="ph836mcpsimp"><a name="ph836mcpsimp"></a><a name="ph836mcpsimp"></a>rg_strength&lt;0x80</span>时<span xml:lang="sv-SE" id="ph837mcpsimp"><a name="ph837mcpsimp"></a><a name="ph837mcpsimp"></a>，</span>白色与光源同向<span xml:lang="sv-SE" id="ph838mcpsimp"><a name="ph838mcpsimp"></a><a name="ph838mcpsimp"></a>，</span>低色温偏红<span xml:lang="sv-SE" id="ph839mcpsimp"><a name="ph839mcpsimp"></a><a name="ph839mcpsimp"></a>，</span>高色温偏蓝。</p>
</td>
</tr>
<tr id="row840mcpsimp"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p842mcpsimp"><a name="p842mcpsimp"></a><a name="p842mcpsimp"></a>cb_cr_track</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p844mcpsimp"><a name="p844mcpsimp"></a><a name="p844mcpsimp"></a>不同ISO下白点条件，cr_max, cr_min, cb_max, cb_min等四组查找表。</p>
<p xml:lang="sv-SE" id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>推荐用户针对sensor调整以上参数，可优化低照度效果。</p>
</td>
</tr>
</tbody>
</table>

**表 3**  AWB Ext扩展参数

<a name="table846mcpsimp"></a>
<table><thead align="left"><tr id="row852mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p854mcpsimp"><a name="p854mcpsimp"></a><a name="p854mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p856mcpsimp"><a name="p856mcpsimp"></a><a name="p856mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row858mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p860mcpsimp"><a name="p860mcpsimp"></a><a name="p860mcpsimp"></a>tolerance</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p862mcpsimp"><a name="p862mcpsimp"></a><a name="p862mcpsimp"></a>帧间相关的容忍度。设置为0时，AWB每2帧刷新一次增益系数；设置为非0值时，AWB判断场景是否有变化，仅在变化时刷新增益系数。</p>
</td>
</tr>
<tr id="row863mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p865mcpsimp"><a name="p865mcpsimp"></a><a name="p865mcpsimp"></a>zone_radius</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p867mcpsimp"><a name="p867mcpsimp"></a><a name="p867mcpsimp"></a>分块统计信息分类的半径。不同亮度灰色块感光一致性较差时，可适当放大该参数。WDR模式下，可适当放大该参数。</p>
</td>
</tr>
<tr id="row868mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p870mcpsimp"><a name="p870mcpsimp"></a><a name="p870mcpsimp"></a>light_info</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p872mcpsimp"><a name="p872mcpsimp"></a><a name="p872mcpsimp"></a>支持特殊光源点。</p>
</td>
</tr>
<tr id="row873mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p875mcpsimp"><a name="p875mcpsimp"></a><a name="p875mcpsimp"></a>in_or_out</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p877mcpsimp"><a name="p877mcpsimp"></a><a name="p877mcpsimp"></a>室内外检测参数。推荐客户根据sensor感光调整out_thresh参数。感光较弱的sensor，可适当放大该参数。</p>
</td>
</tr>
</tbody>
</table>

### 关键参数\(SPECAWB\)<a name="ZH-CN_TOPIC_0000002424202306"></a>

**表 1**  SPECAWB标定参数

<a name="table3346mcpsimp"></a>
<table><thead align="left"><tr id="row3352mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p3354mcpsimp"><a name="p3354mcpsimp"></a><a name="p3354mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p3356mcpsimp"><a name="p3356mcpsimp"></a><a name="p3356mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3358mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p3360mcpsimp"><a name="p3360mcpsimp"></a><a name="p3360mcpsimp"></a>wb_center</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p3362mcpsimp"><a name="p3362mcpsimp"></a><a name="p3362mcpsimp"></a>光源权重分布表坐标系中心位置，由标定得到</p>
</td>
</tr>
<tr id="row3363mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p3365mcpsimp"><a name="p3365mcpsimp"></a><a name="p3365mcpsimp"></a>black_body_tbl</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p3367mcpsimp"><a name="p3367mcpsimp"></a><a name="p3367mcpsimp"></a>普朗克曲线坐标(WB Gain值描述),由标定得到</p>
</td>
</tr>
<tr id="row3368mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p3370mcpsimp"><a name="p3370mcpsimp"></a><a name="p3370mcpsimp"></a>fact_element</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p3372mcpsimp"><a name="p3372mcpsimp"></a><a name="p3372mcpsimp"></a>光源权重分布表，由标定得到</p>
</td>
</tr>
<tr id="row3373mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p3375mcpsimp"><a name="p3375mcpsimp"></a><a name="p3375mcpsimp"></a>fono</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p3377mcpsimp"><a name="p3377mcpsimp"></a><a name="p3377mcpsimp"></a>镜头光圈大小F1.4=14,F2.8=28,F36 =360...，该值需要根据具体使用的镜头光圈大小来设定。</p>
</td>
</tr>
</tbody>
</table>

**表 2**  SPECAWB参数

<a name="table3378mcpsimp"></a>
<table><thead align="left"><tr id="row3384mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p3386mcpsimp"><a name="p3386mcpsimp"></a><a name="p3386mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p3388mcpsimp"><a name="p3388mcpsimp"></a><a name="p3388mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3390mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p3392mcpsimp"><a name="p3392mcpsimp"></a><a name="p3392mcpsimp"></a>kelvin_con</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p3394mcpsimp"><a name="p3394mcpsimp"></a><a name="p3394mcpsimp"></a>色温转换表，支持根据不同bv值配置最多8组原色温与目的色温，当结果色温落入转换表覆盖范围内，会以线性差值的方式将色温转换为用户设定的目的色温</p>
<p id="p3395mcpsimp"><a name="p3395mcpsimp"></a><a name="p3395mcpsimp"></a>原色温与目的色温的取值范围[2000,15000]。</p>
</td>
</tr>
<tr id="row3396mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p3398mcpsimp"><a name="p3398mcpsimp"></a><a name="p3398mcpsimp"></a>wb_cnv_tbl</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p3400mcpsimp"><a name="p3400mcpsimp"></a><a name="p3400mcpsimp"></a>Firmware中实际使用的色温转换lut,用户需要使用PQ工具结合学习库与标定结果来生成。</p>
</td>
</tr>
</tbody>
</table>

### 调试步骤<a name="ZH-CN_TOPIC_0000002457840989"></a>

准确的标定系数，是AWB正常工作的前提。确认镜头、滤光片等器件正常后，按照[《图像质量调试工具使用指南》](../ai/图像质量调试工具使用指南.md)完成AWB标定工作。

标定完成后，测试标准光源下AWB精度，评估客观指标。出现偏色后，需要检查以下参数配置是否合理。

AWB:

-   检测色温是否在\[low\_color\_temp、 high\_color\_temp\]范围内，如果不在，调整色温上下限。
-   室内外检测是否正确，如果检测错误，调整out\_thresh参数。
-   打开PQ Tools的AWB分析界面，观察白色点是否在当前参数划定的白色区域内，如果不在，调整参数，扩大白色区域，将其概括进来。对特殊的光源，可通过添加独立光源点的方式支持。
-   场景内是否有敏感色\(肤色、暗绿色、浅黄色、浅蓝色等\)干扰了AWB表现。
-   低照度下出现了偏色，需要调整cb\_cr\_track的cr\_max, cr\_min, cb\_max, cb\_min等四组查找表。

SPECAWB:

-   检查统计信息配置，SPECAWB将统计信息cr\_max，cb\_max设定为4095； cr\_min，cb\_min设定为0。WhiteLevel设定为61000。该统计信息配置为SPECAWB算法需要，若被修改为不同值，需要将其复原。
-   检查色温转换表配置，打开PQ Tools的WB info界面获取当前色温及环境bv值。然后进入SpecAwb色温转换曲线设定界面找到该bv所属的色温转换曲线，观察当前环境色温是否被色温转换曲线进行了较大的shift。
-   参考[《ISP 颜色调优说明》](ISP 颜色调优说明.md)中关于SPECAWB调试步骤的说明。

## CCM<a name="ZH-CN_TOPIC_0000002424202278"></a>




### 功能描述<a name="ZH-CN_TOPIC_0000002424202326"></a>

Sensor RGB三分量对光谱的响应，与人眼对光谱的响应通常是有偏差的，可通过一个色彩校正矩阵校正光谱响应的交叉效应和响应强度，使前端捕获的图片与人眼视觉在色彩上保持一致。

CCM标定工具支持对24色卡进行3x3 Color Correction Matrix的预校正。Hi3403V100支持多组不同色温的CCM，在ISP运行时，FW根据当前的光照强度，调整饱和度，实现CCM（Color Correction Matrix）矩阵系数的动态调整。

### 关键参数<a name="ZH-CN_TOPIC_0000002457841045"></a>

**表 1**  CCM关键参数

<a name="table954mcpsimp"></a>
<table><thead align="left"><tr id="row960mcpsimp"><th class="cellrowborder" valign="top" width="46%" id="mcps1.2.3.1.1"><p id="p962mcpsimp"><a name="p962mcpsimp"></a><a name="p962mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.3.1.2"><p id="p964mcpsimp"><a name="p964mcpsimp"></a><a name="p964mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row966mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p968mcpsimp"><a name="p968mcpsimp"></a><a name="p968mcpsimp"></a>iso_act_en</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p970mcpsimp"><a name="p970mcpsimp"></a><a name="p970mcpsimp"></a>是否使能低照度下CCM Bypass功能。</p>
</td>
</tr>
<tr id="row971mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p973mcpsimp"><a name="p973mcpsimp"></a><a name="p973mcpsimp"></a>temp_act_en</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p975mcpsimp"><a name="p975mcpsimp"></a><a name="p975mcpsimp"></a>是否使能高、低色温下CCM Bypass功能。</p>
</td>
</tr>
<tr id="row976mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p978mcpsimp"><a name="p978mcpsimp"></a><a name="p978mcpsimp"></a>color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p980mcpsimp"><a name="p980mcpsimp"></a><a name="p980mcpsimp"></a>当前配置的CCM对应的色温。</p>
<p id="p981mcpsimp"><a name="p981mcpsimp"></a><a name="p981mcpsimp"></a>取值范围：[500, 30000]</p>
</td>
</tr>
<tr id="row982mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p984mcpsimp"><a name="p984mcpsimp"></a><a name="p984mcpsimp"></a>ccm[OT_ISP_CCM_MATRIX_SIZE]</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p986mcpsimp"><a name="p986mcpsimp"></a><a name="p986mcpsimp"></a>不同色温下的颜色校正矩阵，<span xml:lang="sv-SE" id="ph987mcpsimp"><a name="ph987mcpsimp"></a><a name="ph987mcpsimp"></a>8bit</span>小数精度。bit 15是符号位，0表示正数，1表示负数，例如0x8010表示-16。</p>
<p id="p988mcpsimp"><a name="p988mcpsimp"></a><a name="p988mcpsimp"></a>取值范围：[0x0, 0xFFFF]</p>
</td>
</tr>
<tr id="row989mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p991mcpsimp"><a name="p991mcpsimp"></a><a name="p991mcpsimp"></a>ccm_tab_num</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p993mcpsimp"><a name="p993mcpsimp"></a><a name="p993mcpsimp"></a>当前配置的CCM的组数。</p>
<p id="p994mcpsimp"><a name="p994mcpsimp"></a><a name="p994mcpsimp"></a>取值范围：[3, 7]</p>
</td>
</tr>
<tr id="row995mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p997mcpsimp"><a name="p997mcpsimp"></a><a name="p997mcpsimp"></a>ccm_tab[OT_ISP_CCM_MATRIX_NUM]</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p999mcpsimp"><a name="p999mcpsimp"></a><a name="p999mcpsimp"></a>不同色温下的颜色校正矩阵和对应的色温值。</p>
</td>
</tr>
<tr id="row1000mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1002mcpsimp"><a name="p1002mcpsimp"></a><a name="p1002mcpsimp"></a>sat_en</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p1004mcpsimp"><a name="p1004mcpsimp"></a><a name="p1004mcpsimp"></a>手动CCM模式下，饱和度是否生效。</p>
</td>
</tr>
<tr id="row1005mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p id="p1007mcpsimp"><a name="p1007mcpsimp"></a><a name="p1007mcpsimp"></a>ccm[OT_ISP_CCM_MATRIX_SIZE]</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p1009mcpsimp"><a name="p1009mcpsimp"></a><a name="p1009mcpsimp"></a>手动颜色校正矩阵，<span xml:lang="sv-SE" id="ph1010mcpsimp"><a name="ph1010mcpsimp"></a><a name="ph1010mcpsimp"></a>8bit</span>小数精度。bit 15是符号位，0表示正数，1表示负数，例如0x8010表示-16。</p>
<p id="p1011mcpsimp"><a name="p1011mcpsimp"></a><a name="p1011mcpsimp"></a>取值范围：[0x0, 0xFFFF]</p>
</td>
</tr>
<tr id="row1012mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p id="p1014mcpsimp"><a name="p1014mcpsimp"></a><a name="p1014mcpsimp"></a>sat[OT_ISP_AUTO_ISO_NUM]</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p1016mcpsimp"><a name="p1016mcpsimp"></a><a name="p1016mcpsimp"></a><span xml:lang="en-US" id="ph1017mcpsimp"><a name="ph1017mcpsimp"></a><a name="ph1017mcpsimp"></a>自动</span>饱和度值。</p>
</td>
</tr>
</tbody>
</table>

### 调试步骤<a name="ZH-CN_TOPIC_0000002457840921"></a>

按照[《图像质量调试工具使用指南》](../ai/图像质量调试工具使用指南.md)完成CCM标定工作。

在标准D50光源下，调整光源亮度，确定sat 自动饱和度联动数组取值。

## CAC<a name="ZH-CN_TOPIC_0000002457881105"></a>




### 功能概述<a name="ZH-CN_TOPIC_0000002457880989"></a>

色差\(Chromatic Aberration\)是指光学上透镜无法将各种波长的光聚焦在同一点上的现象，是一种与镜头有关的缺陷，它产生的主要原因是不同波长的光具有不同的折射率（色散现象）。

**图 1**  色差图解<a name="fig253220313565"></a>  
<img src="figures/色差图解.png" alt="" />

如[图1](#fig253220313565)所示，色差可以分为两类：

-   轴向色差（Axial Chromatic Aberration）
    -   不同波长的光经由光学系统之后聚焦在不同的焦平面上，大口径镜头容易产生这种色差，缩小光圈可以减弱轴向色差
    -   人眼对于G通道更敏感，一般G通道可以正确对焦，从而引起R、B的模糊，造成高光区与低光区交界处出现明显的紫边表现
    -   轴向色差具有明显的局部特性，因此在校正时采用Local CAC对其进行校正

-   横向色差\(Lateral Chromatic Aberration\)
    -   透镜的放大倍数也与折射率有关，它使得不同波长光线的像高不同，即不同波长的光会聚焦在焦平面上不同的位置，会造成R、G、B 3通道具有不同的影像高度，在影像上产生色的错位，横向色差严重时，会使得物体的像带有彩色的边缘
    -   越偏离图像中心，横向色差越明显，一般横向色差表现为物体相对两侧边缘出现不同的颜色，但具体表现为什么颜色与镜头组密切相关，不同的镜头组会表现出不同种类的颜色边缘
    -   具有全局特性，在校正时采用ACAC

### Local CAC<a name="ZH-CN_TOPIC_0000002424362014"></a>

Local CAC主要用来消除图像中出现的紫边问题。




#### 关键参数<a name="ZH-CN_TOPIC_0000002457881129"></a>

**表 1**  Local CAC关键参数

<a name="table1118mcpsimp"></a>
<table><thead align="left"><tr id="row1123mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p1125mcpsimp"><a name="p1125mcpsimp"></a><a name="p1125mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p1127mcpsimp"><a name="p1127mcpsimp"></a><a name="p1127mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1129mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1131mcpsimp"><a name="p1131mcpsimp"></a><a name="p1131mcpsimp"></a>en</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1133mcpsimp"><a name="p1133mcpsimp"></a><a name="p1133mcpsimp"></a>紫边校正使能。</p>
<p id="p1134mcpsimp"><a name="p1134mcpsimp"></a><a name="p1134mcpsimp"></a>取值范围：[0, 1]</p>
</td>
</tr>
<tr id="row1135mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1137mcpsimp"><a name="p1137mcpsimp"></a><a name="p1137mcpsimp"></a>purple_detect_range</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1139mcpsimp"><a name="p1139mcpsimp"></a><a name="p1139mcpsimp"></a>紫色检测的范围</p>
<p id="p1140mcpsimp"><a name="p1140mcpsimp"></a><a name="p1140mcpsimp"></a>值越大，越多非高亮区域的紫色被界定为紫边区域</p>
<p id="p1141mcpsimp"><a name="p1141mcpsimp"></a><a name="p1141mcpsimp"></a>取值范围：[0, 410]</p>
</td>
</tr>
<tr id="row1142mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1144mcpsimp"><a name="p1144mcpsimp"></a><a name="p1144mcpsimp"></a>var_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1146mcpsimp"><a name="p1146mcpsimp"></a><a name="p1146mcpsimp"></a>边缘检测阈值</p>
<p id="p1147mcpsimp"><a name="p1147mcpsimp"></a><a name="p1147mcpsimp"></a>取值范围：[0, 4095]</p>
</td>
</tr>
<tr id="row1148mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1150mcpsimp"><a name="p1150mcpsimp"></a><a name="p1150mcpsimp"></a>r_detect_threshold [3]</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1152mcpsimp"><a name="p1152mcpsimp"></a><a name="p1152mcpsimp"></a>高亮区域检测R分量阈值</p>
<p id="p1153mcpsimp"><a name="p1153mcpsimp"></a><a name="p1153mcpsimp"></a>取值范围：[0, 4095]</p>
</td>
</tr>
<tr id="row1154mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1156mcpsimp"><a name="p1156mcpsimp"></a><a name="p1156mcpsimp"></a>g_detect_threshold [3]</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1158mcpsimp"><a name="p1158mcpsimp"></a><a name="p1158mcpsimp"></a>高亮区域检测G分量阈值</p>
<p id="p1159mcpsimp"><a name="p1159mcpsimp"></a><a name="p1159mcpsimp"></a>取值范围：[0, 4095]</p>
</td>
</tr>
<tr id="row1160mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1162mcpsimp"><a name="p1162mcpsimp"></a><a name="p1162mcpsimp"></a>b_detect_threshold [3]</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1164mcpsimp"><a name="p1164mcpsimp"></a><a name="p1164mcpsimp"></a>高亮区域检测B分量阈值</p>
<p id="p1165mcpsimp"><a name="p1165mcpsimp"></a><a name="p1165mcpsimp"></a>取值范围：[0, 4095]</p>
</td>
</tr>
<tr id="row1166mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1168mcpsimp"><a name="p1168mcpsimp"></a><a name="p1168mcpsimp"></a>l_detect_threshold [3]</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1170mcpsimp"><a name="p1170mcpsimp"></a><a name="p1170mcpsimp"></a>高亮区域检测亮度阈值</p>
<p id="p1171mcpsimp"><a name="p1171mcpsimp"></a><a name="p1171mcpsimp"></a>取值范围：[0, 4095]</p>
</td>
</tr>
<tr id="row1172mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1174mcpsimp"><a name="p1174mcpsimp"></a><a name="p1174mcpsimp"></a>cb_cr_ratio [3]</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1176mcpsimp"><a name="p1176mcpsimp"></a><a name="p1176mcpsimp"></a>紫边检测，区域颜色配置下限</p>
<p id="p1177mcpsimp"><a name="p1177mcpsimp"></a><a name="p1177mcpsimp"></a>取值范围：[-2048, 2047]</p>
</td>
</tr>
<tr id="row1178mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1180mcpsimp"><a name="p1180mcpsimp"></a><a name="p1180mcpsimp"></a>op_type</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1182mcpsimp"><a name="p1182mcpsimp"></a><a name="p1182mcpsimp"></a>紫边校正工作模式</p>
<p id="p1183mcpsimp"><a name="p1183mcpsimp"></a><a name="p1183mcpsimp"></a>取值范围：[0, 1]</p>
</td>
</tr>
<tr id="row1184mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1186mcpsimp"><a name="p1186mcpsimp"></a><a name="p1186mcpsimp"></a>de_purple_cr_strength</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p1188mcpsimp"><a name="p1188mcpsimp"></a><a name="p1188mcpsimp"></a>R通道的校正强度</p>
<p id="p1189mcpsimp"><a name="p1189mcpsimp"></a><a name="p1189mcpsimp"></a>取值范围：[0, 8]</p>
</td>
</tr>
<tr id="row1190mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p xml:lang="sv-SE" id="p1192mcpsimp"><a name="p1192mcpsimp"></a><a name="p1192mcpsimp"></a>de_purple_cb_strength</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p xml:lang="sv-SE" id="p1194mcpsimp"><a name="p1194mcpsimp"></a><a name="p1194mcpsimp"></a>B通道的校正强度</p>
<p id="p1195mcpsimp"><a name="p1195mcpsimp"></a><a name="p1195mcpsimp"></a>取值范围：[0, 8]</p>
</td>
</tr>
</tbody>
</table>

#### 调试步骤<a name="ZH-CN_TOPIC_0000002424202314"></a>

紫边表现与镜头特性有直接关系，有些镜头的紫边会扩散至十多个像素，受限于算法能力，很难在不引入副作用的情况下对其完全的校正，可以遵循如下的步骤进行调试，以期减弱紫边的表现：

-   r\_detect\_threshold、g\_detect\_threshold、b\_detect\_threshold、l\_detect\_threshold、cb\_cr\_ratio均有可调节的3个节点，其实际生效值由purple\_detect\_range的大小决定，purple\_detect\_range的值越大，越多非高亮区域的紫色被界定为紫边区域。
-   首先依据场景中的紫边表现以及校正需求，来调整purple\_detect\_range：如果采用默认值，高亮处有明显紫边没有被检测出来校正掉，需要适当增大purple\_detect\_range使得更多的区域被检测为紫边区域；相反的如果图像中有正常非明显高亮处的紫色被校正掉，则需要减小purple\_detect\_range的值，来保护正常区域的紫色表现。
-   [图1](#fig1513620551827)展示了purple\_detect\_range取不同值时图像的紫边效果，为0时检测范围最小，图像中的紫边基本上没有被检测到；为60时灯管上的紫边被检测出来，并且风车紫色叶片没有出现误检；继续增大purple\_detect\_range的值，比如为410时，可以看到风车紫色叶片出现明显灰度化。

**图 1**  purple\_detect\_range效果图<a name="fig1513620551827"></a>  
<img src="figures/purple_detect_range效果图.png" alt="" />

-   若只需要校正强边缘处的紫色，则可以增加var\_threshold的值；var\_threshold的值越小，所能校正的紫边的范围越大，如[图2](#fig133951171378)所示，var\_threshold=0时所能检测的紫边范围不受强边缘条件的现在，所能检测校正的范围较宽，而当var\_threshold=200时，只能检测靠近灯管边缘的几个紫边像素能被检测校正掉。

**图 2**  var\_threshold效果图<a name="fig133951171378"></a>  
<img src="figures/var_threshold效果图.png" alt="" />

-   在配置完上述的检测参数之后，可以调整de\_purple\_cr\_strength、de\_purple\_cb\_strength来确定R、B通道的校正强度，校正强度调节的太大，可能会造成紫边处明显的灰度化，如[图3](#fig4334816181020)所示，调节至可接受的紫边校正强度即可。一般紫边的颜色表现为蓝紫色，即在高光区过渡到低光区时，B通道的衰减更慢，对于紫边出现的贡献更大，这个时候就需要将de\_purple\_cb\_strength的值调整的更大一些。

**图 3**  de\_purple\_cb\_strength效果图<a name="fig4334816181020"></a>  
<img src="figures/de_purple_cb_strength效果图.png" alt="" />

#### 注意事项<a name="ZH-CN_TOPIC_0000002457880941"></a>

紫边表现与镜头特性有直接关系，有些镜头的紫边会扩散至十多个像素，受限于算法能力，在紫边很宽的时候，CAC容易引入锯齿问题和紫色块和蓝色块噪声跳动问题。其中，锯齿问题是因为紫边太宽导致部分紫边去除，部分紫边残留而形成锯齿。紫色块和蓝色块噪声跳动问题是因为CAC调试太强，导致紫色块和蓝色块的部分颜色去除，部分没有去除而形成噪声跳动。所以在WDR模式下调节CAC要注意var\_threshold的调节：

-   var\_threshold 是指区域方差的阈值，在非宽动态场景，曝光比比较小的情况下，此时短帧上的噪声较小，var\_threshold可以调比较小，可以去除比较多的紫边，降低锯齿的风险。
-   在曝光比较大的情况下，短帧上的噪声大，var\_threshold要相应的调高，才能区分边缘和平坦区域。从而解决因为CAC误判断导致蓝色块和紫色块噪声跳动问题。
-   有一些紫边比较严重的场景，R或者B容易出现饱和的情况，这时，b\_detect\_threshold或者r\_detect\_threshold在最大值附近有去除紫边不平滑的现象。需要跟de\_purple\_cr\_strength和de\_purple\_cb\_strength联合调整，比如把de\_purple\_cr\_strength和de\_purple\_cb\_strength调小。

### ACAC<a name="ZH-CN_TOPIC_0000002457840841"></a>

ACAC不仅可以对纵向色差校正，还可以对横向色差校正。




#### 关键参数<a name="ZH-CN_TOPIC_0000002457840949"></a>

**表 1**  ACAC关键参数

<a name="table2778mcpsimp"></a>
<table><thead align="left"><tr id="row2783mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="p2785mcpsimp"><a name="p2785mcpsimp"></a><a name="p2785mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="p2787mcpsimp"><a name="p2787mcpsimp"></a><a name="p2787mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2789mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2791mcpsimp"><a name="p2791mcpsimp"></a><a name="p2791mcpsimp"></a>en</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2793mcpsimp"><a name="p2793mcpsimp"></a><a name="p2793mcpsimp"></a>色差校正使能。</p>
<p id="p2794mcpsimp"><a name="p2794mcpsimp"></a><a name="p2794mcpsimp"></a>取值范围：[0,1]</p>
</td>
</tr>
<tr id="row2795mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2797mcpsimp"><a name="p2797mcpsimp"></a><a name="p2797mcpsimp"></a>detect_mode</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2799mcpsimp"><a name="p2799mcpsimp"></a><a name="p2799mcpsimp"></a>边缘检测的模式，它有2种模式。</p>
<p id="p2800mcpsimp"><a name="p2800mcpsimp"></a><a name="p2800mcpsimp"></a>0：普通模式。</p>
<p id="p2801mcpsimp"><a name="p2801mcpsimp"></a><a name="p2801mcpsimp"></a>1：宽紫边模式。</p>
<p id="p2802mcpsimp"><a name="p2802mcpsimp"></a><a name="p2802mcpsimp"></a>默认为0.不建议调试。</p>
</td>
</tr>
<tr id="row2803mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2805mcpsimp"><a name="p2805mcpsimp"></a><a name="p2805mcpsimp"></a>op_type</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2807mcpsimp"><a name="p2807mcpsimp"></a><a name="p2807mcpsimp"></a>ACAC的工作模式：</p>
<a name="ul2808mcpsimp"></a><a name="ul2808mcpsimp"></a><ul id="ul2808mcpsimp"><li>OT_OP_MODE_AUTO：自动；</li><li>OT_OP_MODE_MANUAL：手动。</li></ul>
<p id="p2811mcpsimp"><a name="p2811mcpsimp"></a><a name="p2811mcpsimp"></a>默认值为OT_OP_MODE_AUTO。</p>
</td>
</tr>
<tr id="row2812mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2814mcpsimp"><a name="p2814mcpsimp"></a><a name="p2814mcpsimp"></a>edge_threshold[OT_ISP_ACAC_THR_NUM]</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2816mcpsimp"><a name="p2816mcpsimp"></a><a name="p2816mcpsimp"></a>ACAC的边缘检测阈值，两个阈值分别代表高低阈值，小于edge_thd[0]的为平坦区域，大于edge_thd[1]的是强边缘。</p>
<p id="p2817mcpsimp"><a name="p2817mcpsimp"></a><a name="p2817mcpsimp"></a>取值范围：[0,4095]</p>
</td>
</tr>
<tr id="row2818mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2820mcpsimp"><a name="p2820mcpsimp"></a><a name="p2820mcpsimp"></a>edge_gain</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2822mcpsimp"><a name="p2822mcpsimp"></a><a name="p2822mcpsimp"></a>ACAC的边缘检测强度，该值越大，检测的边缘越多。</p>
<p id="p2823mcpsimp"><a name="p2823mcpsimp"></a><a name="p2823mcpsimp"></a>取值范围：[0,1023]</p>
</td>
</tr>
<tr id="row2824mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2826mcpsimp"><a name="p2826mcpsimp"></a><a name="p2826mcpsimp"></a>purple_upper_limit</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2828mcpsimp"><a name="p2828mcpsimp"></a><a name="p2828mcpsimp"></a>ACAC的紫色检测范围上限，具体见下图示意。其中purple_upper_limit必须大于purple_lower_limit。</p>
<p id="p2829mcpsimp"><a name="p2829mcpsimp"></a><a name="p2829mcpsimp"></a>取值范围：[-511,511]</p>
</td>
</tr>
<tr id="row2830mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2832mcpsimp"><a name="p2832mcpsimp"></a><a name="p2832mcpsimp"></a>purple_lower_limit</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2834mcpsimp"><a name="p2834mcpsimp"></a><a name="p2834mcpsimp"></a>ACAC的紫色检测范围下限，具体见下图示意。</p>
<p id="p2835mcpsimp"><a name="p2835mcpsimp"></a><a name="p2835mcpsimp"></a>取值范围：[-511,511]</p>
</td>
</tr>
<tr id="row2836mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2838mcpsimp"><a name="p2838mcpsimp"></a><a name="p2838mcpsimp"></a>purple_sat_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2840mcpsimp"><a name="p2840mcpsimp"></a><a name="p2840mcpsimp"></a>ACAC的紫色检测饱和度阈值。大于该阈值的方为紫色的区域。</p>
<p id="p2841mcpsimp"><a name="p2841mcpsimp"></a><a name="p2841mcpsimp"></a>取值范围：[0, 2047]</p>
</td>
</tr>
<tr id="row2842mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2844mcpsimp"><a name="p2844mcpsimp"></a><a name="p2844mcpsimp"></a>purple_alpha</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2846mcpsimp"><a name="p2846mcpsimp"></a><a name="p2846mcpsimp"></a>ACAC参考紫色的权重。该值越大，表示ACAC参考紫色进行校正色差的越多。</p>
<p id="p2847mcpsimp"><a name="p2847mcpsimp"></a><a name="p2847mcpsimp"></a>取值范围：[0, 63]</p>
</td>
</tr>
<tr id="row2848mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2850mcpsimp"><a name="p2850mcpsimp"></a><a name="p2850mcpsimp"></a>edge_alpha</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2852mcpsimp"><a name="p2852mcpsimp"></a><a name="p2852mcpsimp"></a>ACAC参考边缘的权重。该值越大，表示ACAC参考边缘进行校正色差的越多。</p>
<p id="p2853mcpsimp"><a name="p2853mcpsimp"></a><a name="p2853mcpsimp"></a>取值范围：[0, 63]</p>
</td>
</tr>
<tr id="row2854mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2856mcpsimp"><a name="p2856mcpsimp"></a><a name="p2856mcpsimp"></a>fcc_y_strength</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2858mcpsimp"><a name="p2858mcpsimp"></a><a name="p2858mcpsimp"></a>ACAC根据亮度进行校正的强度，该值越大，表示ACAC校正越强。</p>
<p id="p2859mcpsimp"><a name="p2859mcpsimp"></a><a name="p2859mcpsimp"></a>取值范围：[0, 4095]</p>
</td>
</tr>
<tr id="row2860mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2862mcpsimp"><a name="p2862mcpsimp"></a><a name="p2862mcpsimp"></a>fcc_rb_strength</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p2864mcpsimp"><a name="p2864mcpsimp"></a><a name="p2864mcpsimp"></a>ACAC根据R,B通道强弱进行校正的强度，该值越大，表示ACAC校正越强。</p>
<p id="p2865mcpsimp"><a name="p2865mcpsimp"></a><a name="p2865mcpsimp"></a>取值范围：[0, 511]</p>
</td>
</tr>
</tbody>
</table>

#### 调试步骤<a name="ZH-CN_TOPIC_0000002457881017"></a>

紫边表现与镜头特性有直接关系，有些镜头的紫边会扩散至十多个像素，受限于算法能力，很难在不引入副作用的情况下对其完全的校正，可以遵循如下的步骤进行调试，以期减弱紫边的表现：

1.  紫色判断机制是在色度平面上根据Cr和Cb的比值将蓝紫色的区域划分出，依据场景中的紫边的颜色，一般有偏紫红色的，也有偏蓝色的，这时候可以调整purple\_upper\_limit和purple\_lower\_limit，一般建议，偏紫红的紫边，把purple\_upper\_limit调大一点，识别区域包含更多紫红色，偏蓝色的情况，把purple\_lower\_limit调小一点，识别区域包含更多蓝色。
2.  根据紫边的严重程度调整fcc\_y\_strength，fcc\_rb\_strength以及purple\_alpha。这四个参数的效果都是调试越大，去除越干净。他们的调试步骤可以这样，purple\_alpha调最大，然后再慢慢调大fcc\_y\_strength，fcc\_rb\_strength。
3.  如果图像出现纵向色差引入的非紫色的边缘，这时候，需要调整edge\_gain和edge\_alpha以及fcc\_y\_strength，fcc\_rb\_strength去实现色差校正。调整的步骤可以如下：先把edge\_alpha为63，保持步骤2中fcc\_y\_strength，fcc\_rb\_strength的值，看色差校正情况，如果去除过多引入了副作用，则慢慢减少edge\_alpha的值，如果去除还不够，则慢慢增大edge\_gain的值，再增大fcc\_y\_strength，fcc\_rb\_strength的值。
4.  如果紫边很严重，步骤2.3都去除不了，则需要结合LCAC一起去除。具体LCAC的调试方法参考LCAC的调试步骤。

    **图 1**  紫色检测范围示意图<a name="fig3343mcpsimp"></a>  
    <img src="figures/紫色检测范围示意图.png" alt="" />

#### 注意事项<a name="ZH-CN_TOPIC_0000002457881021"></a>

-   若场景中有一些较严重的紫边，需要加强去除紫边能力，将fcc\_y\_strength，fcc\_rb\_strength的值设置得较大，且edge\_alpha也设置得较大，注意这种情况下容易导致正常的物体边缘颜色呈灰色。
-   当fcc\_y\_strength调节不足时可能出现紫边分层的现象。
-   detect\_mode建议调试为0模式，1模式下只针对紫边做了扩充，对其他颜色的边，如红边，黄边，绿边作用可能减弱，若要去除镜头色差产生其他颜色的边建议采用0模式。

## CA<a name="ZH-CN_TOPIC_0000002424362058"></a>




### 功能概述<a name="ZH-CN_TOPIC_0000002457881145"></a>

颜色调整模块支持在YUV空间进行色域调整的操作，这个模块下有两个模式，一个是CA模式，另外一个是CP模式（热成像上色），工作的时候，两者只能二选一。

在CA模式下，通过下面的公式可以将一个像素点（Y，U，V）映射到另一个像素点（Y', U', V'）。

Y'=Y;  U'=aU;  V'=aV;

其中a是转换系数，采用这组公式可以在一定程度上保持亮度和色调的恒定，对像素点的饱和度做一个调整。转换系数a和像素点亮度Y联系，就可以根据亮度的变化来调整饱和度，达到局部调整饱和度的目的，亮处的颜色更鲜艳，暗处的色噪不明显。同时在CP模式下，热成像的图像只有亮度信息，该模式下通过亮度信息Y查找上色的色板，查找对应的YUV的值作为输出的值。其中，色板是通过YUV格式存储的，转换系数a和ISP的ISO值联系，达到降低低照度下的暗处色噪的目的。

### 关键参数<a name="ZH-CN_TOPIC_0000002424362022"></a>

**表 1**  CA关键参数

<a name="table388mcpsimp"></a>
<table><thead align="left"><tr id="row393mcpsimp"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.3.1.1"><p id="p395mcpsimp"><a name="p395mcpsimp"></a><a name="p395mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="84%" id="mcps1.2.3.1.2"><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row399mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.3.1.1 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>y_ratio_lut</p>
</td>
<td class="cellrowborder" valign="top" width="84%" headers="mcps1.2.3.1.2 "><p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>CA模式，根据亮度Y查找的调整色度UV的增益。意思是将亮度划分成256等分，对应的设定256个调整系数A，用于调整UV的值。建议调整的时候Y值越小（也就是比较暗的地方）对应的增益A越小，这样可以有效的抑制暗区的色噪。亮度的增益设置大一些，亮区的颜色会鲜艳一些。</p>
<p id="p404mcpsimp"><a name="p404mcpsimp"></a><a name="p404mcpsimp"></a>取值范围：[0, 2047]</p>
</td>
</tr>
<tr id="row405mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.3.1.1 "><p id="p407mcpsimp"><a name="p407mcpsimp"></a><a name="p407mcpsimp"></a>iso_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="84%" headers="mcps1.2.3.1.2 "><p id="p409mcpsimp"><a name="p409mcpsimp"></a><a name="p409mcpsimp"></a>CA模式，根据ISO值查找的调整色度UV的增益B。这是一个全局的增益，也就是ISO固定，图像所有像素点的UV的调整增益都是B。建议在低ISO的时候对应的增益B可以设置大一些，高ISO（低照度）对应的增益B可以设置小一些，可以降低低照度下的暗处色噪的目的。</p>
<p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>取值范围：[0, 2047]</p>
</td>
</tr>
<tr id="row411mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.3.1.1 "><p id="p413mcpsimp"><a name="p413mcpsimp"></a><a name="p413mcpsimp"></a>cp_lut_y</p>
</td>
<td class="cellrowborder" valign="top" width="84%" headers="mcps1.2.3.1.2 "><p id="p415mcpsimp"><a name="p415mcpsimp"></a><a name="p415mcpsimp"></a>CP模式，根据亮度Y查找色板中的Y值，色板有256个YUV值，一般来说，色板有固定的模板，可以参考色板的颜色转换成YUV填写对应的Y值。</p>
<p id="p416mcpsimp"><a name="p416mcpsimp"></a><a name="p416mcpsimp"></a>取值范围：[0,255]</p>
</td>
</tr>
<tr id="row417mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.3.1.1 "><p id="p419mcpsimp"><a name="p419mcpsimp"></a><a name="p419mcpsimp"></a>cp_lut_u</p>
</td>
<td class="cellrowborder" valign="top" width="84%" headers="mcps1.2.3.1.2 "><p id="p421mcpsimp"><a name="p421mcpsimp"></a><a name="p421mcpsimp"></a>CP模式，根据亮度Y查找色板中的U值，色板有256个YUV值，一般来说，色板有固定的模板，可以参考色板的颜色转换成YUV填写对应的U值。</p>
<p id="p422mcpsimp"><a name="p422mcpsimp"></a><a name="p422mcpsimp"></a>取值范围：[0,255]</p>
</td>
</tr>
<tr id="row423mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.3.1.1 "><p id="p425mcpsimp"><a name="p425mcpsimp"></a><a name="p425mcpsimp"></a>cp_lut_v</p>
</td>
<td class="cellrowborder" valign="top" width="84%" headers="mcps1.2.3.1.2 "><p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>CP模式，根据亮度Y查找色板中的V值，色板有256个YUV值，一般来说，色板有固定的模板，可以参考色板的颜色转换成YUV填写对应的V值。</p>
<p id="p428mcpsimp"><a name="p428mcpsimp"></a><a name="p428mcpsimp"></a>取值范围：[0,255]</p>
</td>
</tr>
</tbody>
</table>

### 注意事项<a name="ZH-CN_TOPIC_0000002424202238"></a>

CA和CP只能开其中的一个，并不能同时打开。

## Expander<a name="ZH-CN_TOPIC_0000002424362090"></a>




### 功能描述<a name="ZH-CN_TOPIC_0000002457880925"></a>

部分sensor内部会做多帧曝光的融合，融合后数据位宽会增大，导致输出成本增大。为减少输出的成本，sensor内部会做数据分段压缩，将数据压缩到一个比较小的位宽。在ISP中为了将数据还原，需要将sensor内部压缩的数据，进行解压缩。

### 关键参数<a name="ZH-CN_TOPIC_0000002424362150"></a>

**表 1**  Expander关键参数

<a name="table3404mcpsimp"></a>
<table><thead align="left"><tr id="row3410mcpsimp"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p3412mcpsimp"><a name="p3412mcpsimp"></a><a name="p3412mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p3414mcpsimp"><a name="p3414mcpsimp"></a><a name="p3414mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3416mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p3418mcpsimp"><a name="p3418mcpsimp"></a><a name="p3418mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p3420mcpsimp"><a name="p3420mcpsimp"></a><a name="p3420mcpsimp"></a>Expander功能使能。</p>
<p id="p3421mcpsimp"><a name="p3421mcpsimp"></a><a name="p3421mcpsimp"></a>0：关闭；</p>
<p id="p3422mcpsimp"><a name="p3422mcpsimp"></a><a name="p3422mcpsimp"></a>1：开启；</p>
</td>
</tr>
<tr id="row3423mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p3425mcpsimp"><a name="p3425mcpsimp"></a><a name="p3425mcpsimp"></a>bit_depth_in</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p3427mcpsimp"><a name="p3427mcpsimp"></a><a name="p3427mcpsimp"></a>输入数据位宽，取值范围：[0xC,0x14]</p>
</td>
</tr>
<tr id="row3428mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p3430mcpsimp"><a name="p3430mcpsimp"></a><a name="p3430mcpsimp"></a>bit_depth_out</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p3432mcpsimp"><a name="p3432mcpsimp"></a><a name="p3432mcpsimp"></a>输出数据位宽。取值范围：[0xC,0x14]</p>
</td>
</tr>
<tr id="row3433mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p3435mcpsimp"><a name="p3435mcpsimp"></a><a name="p3435mcpsimp"></a>knee_point_num</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p3437mcpsimp"><a name="p3437mcpsimp"></a><a name="p3437mcpsimp"></a>拐点坐标的数目。取值范围：[1,256]</p>
</td>
</tr>
<tr id="row3438mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p3440mcpsimp"><a name="p3440mcpsimp"></a><a name="p3440mcpsimp"></a>knee_point_coord[256]</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p3442mcpsimp"><a name="p3442mcpsimp"></a><a name="p3442mcpsimp"></a>解压的拐点（包括横纵坐标）</p>
</td>
</tr>
</tbody>
</table>

### 调试过程<a name="ZH-CN_TOPIC_0000002424202286"></a>

在sensor手册中会给出sensor内部压缩时使用的拐点，Expander的配置需要将这几个拐点进行转换，然后配置到cmos\_ex.h中即可。

转换原则如下：

-   knee\_point\_coord的横坐标x需要根据sensor压缩曲线转换到0\~256之间（8bit），例如sensor压缩输出的后有效数据位宽是12bit，则需要将sensor压缩曲线拐点的纵坐标右移4bit得到knee\_point\_coord的横坐标x；
-   knee\_point\_coord的纵坐标y需要根据sensor压缩曲线转换到0\~1048576之间（20bit），例如sensor合成有效数据未压缩之前有效位宽是16bit，则需要将sensor压缩曲线的拐点的横坐标左移4bit，得到knee\_point\_coord的纵坐标y。

## Radial Crop<a name="ZH-CN_TOPIC_0000002424202250"></a>




### 功能描述<a name="ZH-CN_TOPIC_0000002424202402"></a>

Hi3403V100是在YUV域对图像进行radial crop操作，将设定半径之外的地方直接拉黑掉。

### 关键参数<a name="ZH-CN_TOPIC_0000002457880961"></a>

**表 1**  Radial Crop关键参数

<a name="table883mcpsimp"></a>
<table><thead align="left"><tr id="row888mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p890mcpsimp"><a name="p890mcpsimp"></a><a name="p890mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p892mcpsimp"><a name="p892mcpsimp"></a><a name="p892mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row894mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p896mcpsimp"><a name="p896mcpsimp"></a><a name="p896mcpsimp"></a>en</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p898mcpsimp"><a name="p898mcpsimp"></a><a name="p898mcpsimp"></a>使能Radial Crop 功能。</p>
<p id="p899mcpsimp"><a name="p899mcpsimp"></a><a name="p899mcpsimp"></a>取值范围：[0,1]</p>
<p id="p900mcpsimp"><a name="p900mcpsimp"></a><a name="p900mcpsimp"></a>0：禁止；1：使能。默认值0</p>
</td>
</tr>

<tr id="row1037mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p id="p1039mcpsimp"><a name="p1039mcpsimp"></a><a name="p1039mcpsimp"></a>b_gain_limit</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p1041mcpsimp"><a name="p1041mcpsimp"></a><a name="p1041mcpsimp"></a>CRB自动蓝色通道增益。</p>
<p id="p1042mcpsimp"><a name="p1042mcpsimp"></a><a name="p1042mcpsimp"></a>取值范围：[0x1FF, 0x7FF]</p>
</td>
</tr>
</tbody>
</table>

### 调试步骤<a name="ZH-CN_TOPIC_0000002424362122"></a>

在WDR模式下，高亮区域附近的暗区会发生偏红的现象，如需减弱这种现象，可以调节r\_gain\_limit来减弱红色。1024为1.0倍增益，建议根据偏红的程度来调节，r\_gain\_limit最大不超过0.9倍增益，b\_gain\_limit在1.0倍附近调节。

在WDR模式下，暗区偏红的问题一般会随着曝光比的增大而变严重。可以调节好各个曝光比下需要的r\_gain\_limit，b\_gain\_limit。自动参数对应的10挡曝光比分别为：128, 256, 512, 1024, 1536, 2048, 2560, 3072, 3584, 4096。

