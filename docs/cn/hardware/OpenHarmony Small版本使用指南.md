# 前言<a name="ZH-CN_TOPIC_0000002374732936"></a>

**概述<a name="section191mcpsimp"></a>**

本文档基于OpenHarmony 5.1.0 Release版本适配Hi3403V100/Hi3403V100，支持OpenHarmony Small型系统运行媒体、图形基本功能，支持XTS认证。

> **说明：** 
>-   本文以Hi3403V100为例，未有特殊说明，SS927V100与Hi3403V100内容一致。
>-   在Hi3403V100和SS927V100上运行OpenHarmony依赖Hi3403V100\_SDK版本包。

**产品版本<a name="section196mcpsimp"></a>**

与本文档相对应的产品版本如下。

<a name="table199mcpsimp"></a>
<table><thead align="left"><tr id="row204mcpsimp"><th class="cellrowborder" valign="top" width="21.029999999999998%" id="mcps1.1.3.1.1"><p id="p206mcpsimp"><a name="p206mcpsimp"></a><a name="p206mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="78.97%" id="mcps1.1.3.1.2"><p id="p208mcpsimp"><a name="p208mcpsimp"></a><a name="p208mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row9557295316"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.3.1.1 "><p id="p18558211536"><a name="p18558211536"></a><a name="p18558211536"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="78.97%" headers="mcps1.1.3.1.2 "><p id="p8554215538"><a name="p8554215538"></a><a name="p8554215538"></a>V100</p>
</td>
</tr>

</tbody>
</table>

**符号约定**

在本文中可能出现下列标志，它们所代表的含义如下。

| 符号 | 说明 |
|------|------|
| :material-alert: **危险** | 表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。 |
| :material-alert-circle: **警告** | 表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。 |
| :material-information: **注意** | 表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。 |
| :material-information-outline: **须知** | 用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。"须知"不涉及人身伤害。 |

#### 设备端需具备条件<a name="ZH-CN_TOPIC_0000002374572984"></a>

1.  连接HDMI显示设备，如显示器、电视。
2.  确认板端能访问到测试需要文件。例如，通过tftp进行网络的挂载，或者使用SD卡。
3.  确认设备驱动gfbg.ko、ot\_tde.ko已加载（可在板端使用lsmod命令查看）。
4.  \(如需支持鼠标\)执行“echo host\>/proc/10320000.usb30drd/mode”。
5.  执行"wms\_server &"，确认wms\_server进程正常启动（在板端top命令查看当前运行进程是否存在该进程，且显示器点亮为蓝屏），移动鼠标，如果无鼠标，执行“cat /dev/input/event0”。

### 实例应用说明<a name="ZH-CN_TOPIC_0000002408332477"></a>



#### sample\_window<a name="ZH-CN_TOPIC_0000002408332429"></a>

验证步骤

1.  配置网络；

    ```
    ifconfig eth0 **.***.**.**
    ```

2.  挂载可执行文件；

    ```
    mount -t nfs -o addr=**.***.**.**,nolock,tcp **.***.**.**:$ sample_window所在路径 /mnt
    ```

3.  执行sample\_window。

    ```
    ./sample_window
    ```

#### sample\_ui<a name="ZH-CN_TOPIC_0000002374573100"></a>

1.  配置网络

    ```
    ifconfig eth0 **.***.**.**
    ```

2.  挂载资源

    ```
    mount -t nfs -o addr=**.***.**.**,nolock,tcp **.***.**.**:$资源所在服务器路径 /user/data
    ```

    表1中描述了对应资源文件的板端路径，需要按该表把资源复制到对应板端路径

    **表 1**  资源说明表

    <a name="table440mcpsimp"></a>
    <table><thead align="left"><tr id="row445mcpsimp"><th class="cellrowborder" valign="top" width="45.050000000000004%" id="mcps1.2.3.1.1"><p id="p447mcpsimp"><a name="p447mcpsimp"></a><a name="p447mcpsimp"></a>文件名</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.949999999999996%" id="mcps1.2.3.1.2"><p id="p449mcpsimp"><a name="p449mcpsimp"></a><a name="p449mcpsimp"></a>板端路径</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row450mcpsimp"><td class="cellrowborder" valign="top" width="45.050000000000004%" headers="mcps1.2.3.1.1 "><p id="p452mcpsimp"><a name="p452mcpsimp"></a><a name="p452mcpsimp"></a>line_cj.brk</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.3.1.2 "><p id="p454mcpsimp"><a name="p454mcpsimp"></a><a name="p454mcpsimp"></a>/user/data</p>
    </td>
    </tr>
    <tr id="row455mcpsimp"><td class="cellrowborder" valign="top" width="45.050000000000004%" headers="mcps1.2.3.1.1 "><p id="p457mcpsimp"><a name="p457mcpsimp"></a><a name="p457mcpsimp"></a>SourceHanSansSC-Regular.otf</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.3.1.2 "><p id="p459mcpsimp"><a name="p459mcpsimp"></a><a name="p459mcpsimp"></a>/user/data</p>
    </td>
    </tr>
    <tr id="row460mcpsimp"><td class="cellrowborder" valign="top" width="45.050000000000004%" headers="mcps1.2.3.1.1 "><p id="p462mcpsimp"><a name="p462mcpsimp"></a><a name="p462mcpsimp"></a>图片资源</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.3.1.2 "><p id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a>/storage/data</p>
    </td>
    </tr>
    </tbody>
    </table>

1.  挂载可执行文件

    ```
    mount -t nfs -o addr=**.***.**.**,nolock,tcp **.***.**.**:$ sample_ui所在路径 /mnt
    ```

2.  执行sample\_ui，显示如[图1](#fig042845495519)画面。

    ```
    ./sample_ui
    ```

    **图 1**  启动画面结果<a name="fig042845495519"></a>  
    <img src="figures/启动画面结果.png" alt="" />

