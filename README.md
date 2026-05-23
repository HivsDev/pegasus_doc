# Hi3403V100 芯片开发文档社区

[![MkDocs](https://img.shields.io/badge/MkDocs-1.6.1-brightgreen)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material-9.7.6-blue)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-deployed-success)](https://HivsDev.github.io/pegasus_doc/)

海思 Hi3403V100 / SS927V100 / SS928V100 超高清智能网络录像机 SoC 完整开发文档社区。

## 站点地址

[https://HivsDev.github.io/pegasus_doc/](https://HivsDev.github.io/pegasus_doc/)

## 文档内容

| 板块 | 内容 |
|------|------|
| **系统架构** | 产品简介、SDK 安装与升级 |
| **快速入门** | 环境搭建、应用开发、图形开发、安全子系统 |
| **样例中心** | 移植案例、开机画面、抓拍使用指南 |
| **模块 / API** | MPP 媒体处理、ISP 图像处理、视频处理、智能分析引擎、芯片参考 API |
| **硬件手册** | DDR、U-Boot、OpenHarmony 适配、3DNR、安全启动 |
| **工具平台** | 烧录工具、命令行工具、调试指南 |

## 本地构建

```bash
# 安装依赖
pip install mkdocs mkdocs-material

# 本地预览
mkdocs serve

# 构建静态页面
mkdocs build
```

## 部署

```bash
mkdocs gh-deploy --force
```

## 贡献指南

欢迎提交 Issue 或 Pull Request 来完善文档：

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/xxx`)
3. 提交你的修改 (`git commit -m 'feat: add xxx'`)
4. 推送到分支 (`git push origin feature/xxx`)
5. 提交 Pull Request

## 反馈与建议

文档如有不足之处，或您有任何改进建议，欢迎通过 [GitHub Issues](https://github.com/HivsDev/pegasus_doc/issues) 提交反馈。每个建议都对我们非常重要，期待大家的参与让文档越来越好！