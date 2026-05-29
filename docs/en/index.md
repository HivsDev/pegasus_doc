# Hi3403V100 Professional Ultra-HD Smart IP Camera SoC

<div class="hero-banner" markdown>

<div class="hero-left" markdown>

**10.4 TOPS AI · 4K60 Flagship Intelligent Vision Chip**

The Hi3403V100 is HiSilicon's professional SoC for high-end surveillance, AI edge computing, and multi-sensor panoramic cameras. It integrates a dual-engine heterogeneous NPU, 4K60 AI ISP, 4-channel hardware video stitching, and rich peripherals — with typical power consumption of just 5.2 W.

<div class="hero-actions" markdown>

[:material-rocket-launch: Quick Start](#quickstart){ .md-button .md-button--primary }
[:fontawesome-brands-github: GitHub](https://github.com/HivsDev/pegasus_doc){ .md-button }

</div>

</div>

<div class="hero-right" markdown>

<figure class="hero-chip-image" markdown>
![Hi3403V100 Chip](../assets/images/chip-hero.png)
</figure>

</div>

</div>

<div class="spec-strip" markdown>

<div class="spec-two-col" markdown>

<div class="spec-col" markdown>

- :material-cpu-64-bit: **CPU**&ensp;Quad Cortex A55 @ 1.4 GHz, built-in 32bit MCU @ 500 MHz, TrustZone
- :material-brain: **NPU**&ensp;Dual-engine, 10.4 TOPS INT8 / 15.2 TOPS INT4, dual Vision Q6 DSP
- :material-camera-iris: **ISP**&ensp;4K60 AI ISP, 3F WDR, 6-DoF EIS, ultra-low-light HNR
- :material-video-3d: **Codec**&ensp;H.265/H.264 4K60 encode, 10-ch 1080p decode, JPEG codec
- :material-wall: **Stitching**&ensp;4-ch hardware panoramic stitching, 2×4K or 4×2.6K input
- :material-memory: **Storage**&ensp;DDR4/LPDDR4x up to 8 GB, eMMC 5.1 up to 2 TB, SPI/NAND Flash

</div>

<div class="spec-col" markdown>

- :material-lan: **Network**&ensp;Dual GbE (RGMII/RMII), 2× USB 3.0 / USB 2.0
- :material-expansion-card: **Interfaces**&ensp;2-Lane PCIe 2.0 (RC/EP), 2× SDIO 3.0, HDMI 2.0 output
- :material-camera: **Input**&ensp;8-Lane MIPI/LVDS/Sub-LVDS/HiSPi, up to 4 sensors, max 8192×8192
- :material-shield-lock: **Security**&ensp;Secure boot, TrustZone TEE, AES/RSA/SHA/HMAC, 30 Kbit OTP
- :material-power-plug: **Power**&ensp;Typ. 5.2 W (4K30 + 4TOPS), advanced low-power process
- :material-package-variant: **Package**&ensp;FC-BGA 23×23 mm, 0.65 mm pitch

</div>

</div>

</div>

---

## :material-rocket-launch: Quick Start { #quickstart }

<div class="step-grid" markdown>

<div class="step-card" markdown>
<div class="step-number">1</div>

### Hardware Setup

- **Power**: USB-C 5V / 2A, or 12V DC adapter
- **Essential**: USB-TTL serial module (3.3V), Micro SD card (≥ 8 GB, Class 10)
- **Optional**: HDMI display, Ethernet cable, CSI/DSI camera

</div>

<div class="step-card" markdown>
<div class="step-number">2</div>

### Dev Environment

Install SDK and cross-compilation toolchain:

```bash
git clone https://github.com/HivsDev/pegasus_doc.git
cd pegasus_doc && ./setup.sh
```

:material-microsoft-windows: [Windows Guide](getting-started/Hi3403V100环境搭建指南.md) ·
:material-apple: [macOS Guide](getting-started/Hi3403V100环境搭建指南.md) ·
:material-linux: [Linux Guide](getting-started/Hi3403V100环境搭建指南.md)

</div>

<div class="step-card" markdown>
<div class="step-number">3</div>

### Flash Your First Program

**LED Blink** — complete dev flow in 10 minutes:

```bash
cd examples/led_blink
make && make flash
```

:material-arrow-right: [Full Tutorial](getting-started/快速上手指南.md)

Once the LED lights up, explore the [Application Development Guide](getting-started/应用开发指南.md).

</div>

</div>

---

## :material-bookshelf: Documentation

<div class="grid cards" markdown>

-   :material-cpu-64-bit: **Hardware**

    ---

    - [Product Overview](system-architecture/产品简介.md) — Chip specs & features
    - [Peripheral Drivers](hardware/外围设备驱动%20操作指南.md) — GPIO / I2C / SPI / UART
    - [DDR Miniaturization](hardware/DDR%20小型化指南.md) — DDR layout & routing
    - [HDMI Reference](modules/video/HDMI%20开发参考.md) — HDMI output config
    - [MIPI Guide](modules/video/MIPI%20使用指南.md) — MIPI DSI/CSI interface

-   :material-code-tags: **Software**

    ---

    - [SDK Setup](system-architecture/SDK安装与升级.md) — SDK environment setup
    - [App Development](getting-started/应用开发指南.md) — Framework & API
    - [Media Processing](modules/mpp/01%20概述.md) — Video/Audio/Graphics
    - [SVP2.0 Guide](modules/ai/SVP2.0%20开发指南.md) — NN inference engine
    - [Chip API Reference](modules/reference/CIPHER%20API%20参考.md) — Low-level API

-   :material-tools: **Tools**

    ---

    - [ATC Tool Guide](modules/ai/ATC工具使用指南.md) — Model conversion
    - [BurnTool](tools/BurnTool%20工具使用指南.md) — Firmware flashing
    - [Profiling Tool](modules/ai/Profiling工具使用指南.md) — Performance analysis
    - [Accuracy Comparison](modules/ai/精度比对工具使用指南.md) — Model accuracy
    - [Image Quality Tool](modules/ai/图像质量调试工具使用指南.md) — ISP tuning

-   :material-help-circle: **FAQ**

    ---

    - :material-alert-circle: No serial output? Check TX/RX swap, baud rate 115200
    - :material-alert-circle: Driver install failed? Disable driver signature enforcement (Windows)
    - :material-alert-circle: Flashing stuck? Verify USB cable supports data transfer
    - :material-alert-circle: SDK build errors? Check cross-compiler toolchain version
    - :material-alert-circle: DTS not applying? Rebuild and reflash dtb partition

    [:octicons-arrow-right-24: View All FAQs](other/BSP%20FAQ.md)

</div>

---

## :material-code-braces: Example Projects

<div class="examples-section" markdown>

<div class="grid cards" markdown>

-   :fontawesome-brands-github: **Official Examples**

    ---

    Peripheral drivers (:material-chip: GPIO · I2C · SPI · UART), multimedia (:material-video: VI/VO/VENC), AI inference (:material-brain: SVP2.0), and more — ready to use out of the box.

    [:octicons-arrow-right-24: pegasus_doc](https://github.com/HivsDev/pegasus_doc)

-   :material-account-group: **Community Highlights**

    ---

    **:material-robot: AI Door Access** — Face recognition access control powered by Hi3403V100

    **:material-factory: Industrial Inspection** — Real-time defect detection at the edge

    **:material-camera: 4K IP Camera** — Ultra-low latency 4K60 video streaming

</div>

</div>

---

<div class="footer-strip" markdown>

<div class="footer-col" markdown>

### :material-storefront: Purchase

- :material-cart: Official Store
- :material-package-variant: Distributors
- :material-download: [SDK Downloads](https://developers.hisilicon.com)

</div>

<div class="footer-col" markdown>

### :material-forum: Community

- :fontawesome-brands-github: [Issue Tracker](https://github.com/HivsDev/pegasus_doc/issues)
- :material-file-document-edit: [Contribute](https://github.com/HivsDev/pegasus_doc)
- :material-chat-question: [Developer Community](https://developers.hisilicon.com)

</div>

<div class="footer-col" markdown>

### :material-update: Changelog

- **v1.1-beta3** — Added MPP FAQ, Sensor debug guide
- **v1.1-beta2** — ISP color tuning, dual fusion dev guide
- **v1.0-beta1** — Initial docs: MPP / ISP / AI

[:octicons-arrow-right-24: Full Changelog](other/Pegasus-v1.1-beta3.md)

</div>

</div>
