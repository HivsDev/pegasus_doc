# 海思 SS928V100 芯片开发文档

> 海思 SS928V100 / SS927V100 超高清智能网络录像机 SoC 完整开发文档社区

<!-- 快速上手快捷入口 -->
<div class="quick-start-strip">
<h3><span class="qs-icon">⚡</span> 快速上手</h3>
<div class="quick-start-links">
  <a href="getting-started/快速上手指南.md"><span class="qs-icon">🚀</span> 快速上手指南</a>
  <a href="getting-started/Hi3403V100环境搭建指南.md"><span class="qs-icon">🔧</span> 环境搭建指南</a>
  <a href="getting-started/应用开发指南.md"><span class="qs-icon">💻</span> 应用开发指南</a>
  <a href="getting-started/图形开发用户指南.md"><span class="qs-icon">🎨</span> 图形开发指南</a>
  <a href="system-architecture/SDK安装与升级.md"><span class="qs-icon">📦</span> SDK 安装与升级</a>
</div>
</div>

<!-- 芯片概览 -->
## 芯片概览

SS928V100 是一颗面向超高清智能网络录像机场景的专业 SoC 芯片。

| 特性 | 规格 |
|------|------|
| **处理器内核** | 四核 ARM Cortex A55 @ 1.4GHz + 单核 MCU |
| **智能加速** | 双 NN 引擎，最高 10.4 TOPS INT8 |
| **视频编解码** | 4K60 H.265/H.264 编解码 |
| **图像能力** | 4K60 ISP，3F WDR，多级降噪，六轴防抖 |
| **高速接口** | USB3.0、PCIe2.0、MIPI、HDMI |
| **封装工艺** | 12nm FC-BGA 23mm x 23mm |

## 详细文档

### 一、系统架构

::: info 架构文档

了解芯片整体架构、组件划分、开发工具链。

:::

| 文档 | 说明 |
|------|------|
| [产品简介](system-architecture/产品简介.md) | SS928V100/SS927V100 SoC 核心规格与关键特性 |
| [SDK 安装与升级](system-architecture/SDK安装与升级.md) | SDK 环境搭建与版本管理 |

### 二、快速入门

::: tip 快速上手

从零开始，搭建环境，编译运行 Hello World。

:::

| 文档 | 说明 |
|------|------|
| [快速上手指南](getting-started/快速上手指南.md) | 快速开始开发流程 |
| [Hi3403V100 环境搭建指南](getting-started/Hi3403V100环境搭建指南.md) | 开发工具链配置 |
| [应用开发指南](getting-started/应用开发指南.md) | 应用层开发框架 |
| [图形开发用户指南](getting-started/图形开发用户指南.md) | 图形子系统开发 |
| [安全子系统使用说明](getting-started/安全子系统使用说明.md) | 安全启动与加密 |

### 三、样例中心

::: note 案例参考

各类功能案例、综合案例，直接可运行。

:::

| 示例 | 说明 |
|------|------|
| [小型系统 SS928V100 移植案例](getting-started/小型系统SS928V100移植案例.md) | 小型系统移植完整案例 |
| [开机画面使用指南](getting-started/开机画面使用指南.md) | 开机动画配置 |
| [抓拍使用指南](getting-started/抓拍 使用指南.md) | 图像抓拍功能演示 |

### 四、模块 / API {#模块-api}

::: success 核心开发文档

各模块软硬件功能介绍、API 使用样例、开发指南。

:::

#### 媒体处理 (MPP)

| 文档 | 模块 |
|------|------|
| [00 前言](modules/mpp/00%20前言.md) | MPP 整体架构 |
| [01 概述](modules/mpp/01%20概述.md) | 框架概述 |
| [02 系统控制](modules/mpp/02%20系统控制.md) | 系统控制接口 |
| [03 视频输入](modules/mpp/03%20视频输入.md) | VI 视频采集 |
| [04 视频输出（4.1-4.3）](modules/mpp/04%20视频输出（4.1--4.3）.md) | VO 显示输出 |
| [04 视频输出（4.4-4.5）](modules/mpp/04%20视频输出（4.4--4.5）.md) | VO 高级功能 |
| [05 视频处理子系统](modules/mpp/05%20视频处理子系统.md) | VPU 视频处理 |
| [06 视频编码（6.1-6.3）](modules/mpp/06%20视频编码（6.1--6.3）.md) | VENC 编码 |
| [06 视频编码（6.4-6.5）](modules/mpp/06%20视频编码（6.4--6.5）.md) | VENC 高级 |
| [07 视频解码](modules/mpp/07%20视频解码.md) | VDEC 解码 |
| [08 区域管理](modules/mpp/08%20区域管理.md) | Region 区域 |
| [09 音频（9.1-9.3）](modules/mpp/09%20音频（9.1--9.3）.md) | AIO 音频基础 |
| [09 音频（9.4-9.5）](modules/mpp/09%20音频（9.4--9.5）.md) | AIO 高级 |
| [10 视频图形子系统](modules/mpp/10%20视频图形子系统.md) | VGPU |
| [11 几何畸变矫正子系统](modules/mpp/11%20几何畸变矫正子系统.md) | GDC |
| [12 拼接](modules/mpp/12%20拼接.md) | 视频拼接 |
| [13 Proc调试信息 (1)](modules/mpp/13%20Proc调试信息（13.1--13.14.15）.md) | 调试信息(1) |
| [13 Proc调试信息 (16-29)](modules/mpp/13%20Proc调试信息（13.16--13.29）.md) | 调试信息(2) |
| [MPP FAQ](modules/mpp/MPP%20媒体处理软件%20V5.0%20FAQ.md) | MPP 常见问题 |

#### ISP 图像处理器

| 文档 | 说明 |
|------|------|
| [ISP 开发参考（1-2）](modules/isp/ISP%20开发参考（1--2）.md) | ISP 架构与开发 |
| [ISP 开发参考（3-5）](modules/isp/ISP%20开发参考（3--5）.md) | ISP 开发进阶 |
| [ISP 开发参考（6）](modules/isp/ISP%20开发参考（6）.md) | ISP 专题 |
| [ISP 开发参考（7-14）](modules/isp/ISP%20开发参考（7--14）.md) | ISP 扩展 |
| [ISP 图像调优指南](modules/isp/ISP%20图像调优指南.md) | 图像参数调优 |
| [ISP 颜色调优说明](modules/isp/ISP%20颜色调优说明.md) | 颜色调优 |
| [ISP FAQ](modules/isp/ISP%20FAQ.md) | ISP 常见问题 |
| [Sensor 调试指南](modules/isp/Sensor%20调试指南.md) | 传感器适配 |
| [黑白彩色双路融合开发参考](modules/isp/黑白彩色双路融合%20开发参考.md) | RGB-IR 双路融合 |
| [黑白彩色双路融合调试指南](modules/isp/黑白彩色双路融合调试指南.md) | RGB-IR 调试 |

#### 图像

| 文档 | 文档 |
|------|------|
| [SVP2.0 开发指南](modules/ai/SVP2.0%20开发指南.md) | 智能分析引擎开发 |
| [SVP2.0 API 参考](modules/ai/SVP2.0%20API%20参考.md) | SVP2.0 API |
| [ATC 工具使用指南](modules/ai/ATC工具使用指南.md) | 模型转换工具 |
| [ATC Graph 开发指南](modules/ai/ATC%20Graph开发指南.md) | Graph 开发 |
| [ATC 自定义算子开发指南](modules/ai/ATC自定义算子开发指南.md) | 自定义算子 |
| [AMCT 使用指南（Caffe）](modules/ai/AMCT使用指南（Caffe）.md) | Caffe 量化 |
| [AMCT 使用指南（PyTorch）](modules/ai/AMCT使用指南（PyTorch）.md) | PyTorch 量化 |
| [DPU2.0 工具使用指南](modules/ai/DPU2.0%20工具使用指南.md) | DPU 工具 |
| [Profiling 工具使用指南](modules/ai/Profiling工具使用指南.md) | 性能分析 |
| [精度比对工具使用指南](modules/ai/精度比对工具使用指南.md) | 精度对比 |
| [图像分析引擎2与引擎1差异说明](modules/ai/图像分析引擎2与图像分析引擎1使用差异说明.md) | 引擎差异 |
| [图像质量调试工具使用指南](modules/ai/图像质量调试工具使用指南.md) | 图像质量工具 |

#### 视频处理子系统

| 文档 | 说明 |
|------|------|
| [HDMI 开发参考](modules/video/HDMI%20开发参考.md) | HDMI 接口开发 |
| [MIPI 使用指南](modules/video/MIPI%20使用指南.md) | MIPI 接口开发 |
| [MotionFusion 开发参考](modules/video/MotionFusion%20开发参考.md) | 运动融合 |
| [PCIE级联 应用指南](modules/video/PCIE级联%20应用指南.md) | PCIe 级联 |
| [拼接 FAQ](modules/video/拼接%20FAQ.md) | 拼接常见问题 |

#### IVE/IVS 智能视觉

| 文档 | 说明 |
|------|------|
| [IVE API 参考（1-2）](modules/ive/IVE%20API%20参考（1--2）.md) | IVE API (1-2) |
| [IVE API 参考（3-6）](modules/ive/IVE%20API%20参考（3--6）.md) | IVE API (3-6) |
| [IVS API 参考](modules/ive/IVS%20API参考.md) | IVS API |

#### 芯片参考 API

| 文档 | 说明 |
|------|------|
| [CIPHER API 参考](modules/reference/CIPHER%20API%20参考.md) | 加密算法 |
| [GFBG API 参考](modules/reference/GFBG%20API%20参考.md) | 图形背景 |
| [KLAD API 参考](modules/reference/KLAD%20API%20参考.md) | 密钥管理 |
| [OTP API 参考](modules/reference/OTP%20API%20参考.md) | 一次性编程 |
| [TDE API 参考](modules/reference/TDE%20API参考.md) | 2D 图形引擎 |
| [音频组件 API 参考](modules/reference/音频组件%20API参考.md) | 音频 API |

### 五、硬件手册

::: info 硬件资料

硬件设计参考、开发板文档、底层适配。

:::

| 文档 | 说明 |
|------|------|
| [DDR 小型化指南](hardware/DDR%20小型化指南.md) | DDR 小型化设计 |
| [U-Boot 移植应用开发指南](hardware/U-boot%20移植应用开发指南.md) | U-Boot 移植 |
| [OpenHarmony Small 版本使用指南](hardware/OpenHarmony%20Small版本使用指南.md) | OpenHarmony 适配 |
| [OpenHarmony 内核适配（内核6.6）](hardware/OpenHarmony内核适配SS928V100%20SDK%20内核6.6特性指导文档.md) | 内核适配指南 |
| [3DNR 参数配置说明](hardware/3DNR参数配置说明.md) | 3DNR 参数配置 |
| [安全启动使用指南](hardware/安全启动使用指南.md) | 安全启动 |
| [内存布局调整指南](hardware/内存布局调整指南.md) | 内存管理 |
| [SYS_CONFIG 配置指南](hardware/SYS_CONFIG%20配置指南.md) | 系统配置 |
| [外围设备驱动操作指南](hardware/外围设备驱动%20操作指南.md) | 外设驱动 |

### 六、工具平台

::: note 开发工具

烧录、调试、配置等工具使用指南。

:::

| 文档 | 说明 |
|------|------|
| [BurnTool 工具使用指南](tools/BurnTool%20工具使用指南.md) | 固件烧录工具 |
| [ToolPlatform 工具平台使用指南](tools/ToolPlatform工具平台使用指南.md) | 工具平台 |
| [MindCmd 使用指南](tools/MindCmd%20使用指南.md) | 命令行工具 |
| [DIS 调试指南](tools/DIS%20调试指南.md) | 调试工具 |

### 七、其他

::: info 参考资源

FAQ、版本说明、开发者贡献指南等。

:::

| 文档 | 说明 |
|------|------|
| [BSP FAQ](other/BSP%20FAQ.md) | 板级支持包常见问题 |
| [Pegasus v1.0-beta1 版本说明](other/Pegasus-v1.0-beta1.md) | 早期版本发布 |
| [Pegasus v1.1-beta2 版本说明](other/Pegasus-v1.1-beta2.md) | 版本更新 |
| [Pegasus v1.1-beta3 版本说明](other/Pegasus-v1.1-beta3.md) | 版本更新 |
| [快速参考索引](other/quick-reference.md) | 快速查找 |

---

## 设计原则

- **以开发者为中心** — 围绕开发者经历逐层递进，以场景化任务驱动
- **简单易用** — 代码先行，可复现、通俗易懂、模块化可扩展
- **行业规范** — 坚持正确、标准规范，支持共建、复用成熟文档

## 相关资源

- [华为海思官网](https://www.hisilicon.com)
- [海思开发者社区](https://developers.hisilicon.com)
- [版本发布说明](other/Pegasus-v1.0-beta1.md)

---

::: info 反馈与支持

如有文档问题或开发疑问，请联系技术支持或通过仓库提交 Issue。

:::
