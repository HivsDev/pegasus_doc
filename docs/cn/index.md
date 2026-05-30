# Hi3403V100 专业 Ultra-HD Smart IP Camera SoC

<div class="hero-banner" markdown>

<div class="hero-left" markdown>

**10.4 TOPS AI 算力 · 4K60 旗舰级智能视觉芯片**

Hi3403V100 是海思面向高端安防监控、AI 边缘计算、多目拼接相机等场景的专业 SoC。集成双引擎异构 NPU、4K60 AI ISP、4 路视频硬件拼接及丰富外设接口，典型功耗仅 5.2 W。

<div class="hero-actions" markdown>

[:material-rocket-launch: 快速上手](#quickstart){ .md-button .md-button--primary }
[:fontawesome-brands-github: GitHub](https://github.com/HivsDev/pegasus_doc){ .md-button }

</div>

</div>

<div class="hero-right" markdown>

<figure class="hero-chip-image" markdown>
![Hi3403V100 芯片](../assets/images/chip-hero.png)
</figure>

</div>

</div>

<div class="spec-strip" markdown>

<div class="spec-two-col" markdown>

<div class="spec-col" markdown>

- :material-cpu-64-bit: **CPU**&ensp;四核 Cortex A55 @ 1.4 GHz，内置 32bit MCU @ 500 MHz，支持 TrustZone
- :material-brain: **NPU**&ensp;双引擎异构，10.4 TOPS INT8 / 15.2 TOPS INT4，双核 Vision Q6 DSP
- :material-camera-iris: **ISP**&ensp;4K60 AI ISP，3F WDR，6-DoF 数字防抖，超感光降噪 (HNR)
- :material-video-3d: **编解码**&ensp;H.265/H.264 4K60 编码，10 路 1080p 解码，JPEG 编解码
- :material-wall: **拼接**&ensp;4 路硬件全景拼接，支持 2×4K 或 4×2.6K 输入
- :material-memory: **存储**&ensp;DDR4/LPDDR4x 最大 8 GB，eMMC 5.1 最大 2 TB，SPI/NAND Flash

</div>

<div class="spec-col" markdown>

- :material-lan: **网络**&ensp;双千兆以太网 (RGMII/RMII)，2× USB 3.0 / USB 2.0
- :material-expansion-card: **接口**&ensp;2-Lane PCIe 2.0 (RC/EP)，2× SDIO 3.0，HDMI 2.0 输出
- :material-camera: **输入**&ensp;8-Lane MIPI/LVDS/Sub-LVDS/HiSPi，最高 4 路 sensor，最大 8192×8192
- :material-shield-lock: **安全**&ensp;安全启动、TrustZone TEE、AES/RSA/SHA/HMAC、30 Kbit OTP
- :material-power-plug: **功耗**&ensp;典型 5.2 W (4K30 + 4TOPS)，先进低功耗工艺
- :material-package-variant: **封装**&ensp;FC-BGA 23×23 mm，0.65 mm 管脚间距

</div>

</div>

</div>

---

## :material-rocket-launch: 快速入门 { #quickstart }

<div class="step-grid" markdown>

<div class="step-card" markdown>
<div class="step-number">1</div>

### 硬件准备

- **供电**：USB-C 5V / 2A，或 12V DC 适配器
- **必备配件**：USB-TTL 串口模块（3.3 V）、Micro SD 卡（≥ 8 GB，Class 10）
- **可选外设**：HDMI 显示器、以太网线、CSI/DSI 摄像头

</div>

<div class="step-card" markdown>
<div class="step-number">2</div>

### 搭建开发环境

一键安装 SDK 与交叉编译工具链：

```bash
git clone https://github.com/HivsDev/pegasus_doc.git
cd pegasus_doc && ./setup.sh
```

:material-microsoft-windows: [Windows 指南](getting-started/Hi3403V100环境搭建指南.md) ·
:material-apple: [macOS 指南](getting-started/Hi3403V100环境搭建指南.md) ·
:material-linux: [Linux 指南](getting-started/Hi3403V100环境搭建指南.md)

</div>

<div class="step-card" markdown>
<div class="step-number">3</div>

### 烧写第一个程序

**LED Blink** — 10 分钟跑通完整开发流程：

```bash
cd examples/led_blink
make && make flash
```

:material-arrow-right: [详细教程](getting-started/快速上手指南.md)

成功点亮 LED 后，继续尝试 [应用开发指南](getting-started/应用开发指南.md)。

</div>

</div>

---

## :material-bookshelf: 文档资源

<div class="grid cards" markdown>

-   :material-rocket-launch: **快速入门**

    ---

    - [快速上手指南](getting-started/快速上手指南.md) — 30 分钟快速上手开发流程
    - [Hi3403V100 环境搭建指南](getting-started/Hi3403V100环境搭建指南.md) — 开发工具链配置与 SDK 安装
    - [应用开发指南](getting-started/应用开发指南.md) — 应用层开发框架与 API 参考
    - [图形开发用户指南](getting-started/图形开发用户指南.md) — 图形子系统与 UI 开发
    - [安全子系统使用说明](getting-started/安全子系统使用说明.md) — 安全启动与加密配置

-   :material-cog-outline: **系统架构**

    ---

    - [产品简介](system-architecture/产品简介.md) — Hi3403V100/SS927V100 SoC 核心规格与关键特性
    - [SDK 安装与升级](system-architecture/SDK安装与升级.md) — SDK 环境搭建与版本管理
    - [SS928V100 产品简介](getting-started/SS928V100%20超高清智能网络录像机%20SoC%20产品简介.md) — SS928V100 产品规格
    - [SS928V100/SS927V100 SDK 安装升级](getting-started/SS928V100╱SS927V100%20SDK%20安装以及升级使用说明.md) — SDK 安装详细说明

-   :material-memory: **硬件手册**

    ---

    - [外围设备驱动](hardware/外围设备驱动%20操作指南.md) — GPIO / I2C / SPI / UART 操作
    - [DDR 小型化指南](hardware/DDR%20小型化指南.md) — DDR 布局与布线优化
    - [U-Boot 移植开发](hardware/U-boot%20移植应用开发指南.md) — Bootloader 移植指南
    - [安全启动](hardware/安全启动使用指南.md) — 安全启动配置与验证
    - [内存布局调整](hardware/内存布局调整指南.md) — 内存分区与地址映射

-   :material-code-json: **模块 API**

    ---

    - [媒体处理 MPP](modules/mpp/01%20概述.md) — 视频/音频/图形处理子系统
    - [ISP 图像处理器](modules/isp/ISP%20开发参考（1--2）.md) — 图像信号处理开发参考
    - [IVE/IVS 智能视觉](modules/ive/IVE%20API%20参考（1--2）.md) — 智能视觉加速 API
    - [智能分析引擎](modules/ai/SVP2.0%20开发指南.md) — SVP2.0 NN 推理与 ATC 工具
    - [芯片参考 API](modules/reference/CIPHER%20API%20参考.md) — CIPHER / KLAD / OTP / TDE

-   :material-lightbulb-on-outline: **样例中心**

    ---

    - [小型系统移植案例](getting-started/小型系统SS928V100移植案例.md) — SS928V100 小型系统完整移植
    - [开机画面使用指南](getting-started/开机画面使用指南.md) — 开机动画与 Logo 配置
    - [抓拍使用指南](getting-started/抓拍%20使用指南.md) — 图像抓拍与快照功能

-   :material-wrench: **工具平台**

    ---

    - [BurnTool 烧录工具](tools/BurnTool%20工具使用指南.md) — 固件烧录与分区管理
    - [ToolPlatform 工具平台](tools/ToolPlatform工具平台使用指南.md) — 芯片调试与配置平台
    - [MindCmd 命令行工具](tools/MindCmd%20使用指南.md) — 命令行调试与诊断
    - [DIS 调试指南](tools/DIS%20调试指南.md) — 数字防抖调试与参数配置

</div>

---

## :material-code-braces: 示例项目

<div class="examples-section" markdown>

<div class="grid cards" markdown>

-   :fontawesome-brands-github: **官方示例仓库**

    ---

    外设驱动（:material-chip: GPIO · I2C · SPI · UART）、多媒体（:material-video: VI/VO/VENC）、 AI 推理（:material-brain: SVP2.0）等完整示例，开箱即用。

    [:octicons-arrow-right-24: pegasus_doc](https://github.com/HivsDev/pegasus_doc)

-   :material-account-group: **社区项目精选**

    ---

    **:material-robot: AI 视觉门禁** — 基于 Hi3403V100 的人脸识别门禁系统

    **:material-factory: 工业缺陷检测** — 边缘端实时产品缺陷检测

    **:material-camera: 4K 网络摄像头** — 超低延迟 4K60 视频流传输

</div>

</div>

---

<div class="footer-strip" markdown>

<div class="footer-col" markdown>

### :material-storefront: 购买与资源

- :material-cart: 官方淘宝店
- :material-package-variant: 授权分销商
- :material-download: [SDK 下载](https://developers.hisilicon.com)

</div>

<div class="footer-col" markdown>

### :material-forum: 社区与支持

- :fontawesome-brands-github: [提交 Issue](https://github.com/HivsDev/pegasus_doc/issues)
- :material-file-document-edit: [贡献文档](https://github.com/HivsDev/pegasus_doc)
- :material-chat-question: [海思开发者社区](https://developers.hisilicon.com)

</div>

<div class="footer-col" markdown>

### :material-update: 更新动态

- **v1.1-beta3** — 新增 MPP FAQ、Sensor 调试指南
- **v1.1-beta2** — ISP 颜色调优、双路融合开发指南
- **v1.0-beta1** — 首批文档发布：MPP / ISP / AI

[:octicons-arrow-right-24: 完整更新日志](other/Pegasus-v1.1-beta3.md)

</div>

</div>
