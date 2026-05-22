#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copy missing images from pegasus-master/docs/zh-CN to the new docs structure.
"""
import os, re, shutil

OLD_ROOT = r'D:/work/03 开发板/pegasus-master/docs/zh-CN'
NEW_DOCS = r'D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs'

# Build old doc dir -> figures path mapping
old_dirs = {}
for d in os.listdir(OLD_ROOT):
    dp = os.path.join(OLD_ROOT, d)
    if os.path.isdir(dp) and os.path.isdir(os.path.join(dp, 'figures')):
        old_dirs[d] = os.path.join(dp, 'figures')

print(f'Found {len(old_dirs)} old doc directories with figures\n')

# Mapping: our md filename -> list of old directory name candidates
doc_map = {
    '应用开发指南.md': ['应用开发指南'],
    '图形开发用户指南.md': ['图形开发用户指南'],
    '安全子系统使用说明.md': ['安全子系统使用说明'],
    '抓拍 使用指南.md': ['抓拍使用指南'],
    '抓拍使用指南.md': ['抓拍使用指南'],
    '快速上手指南.md': ['快速上手指南'],
    '开机画面使用指南.md': ['开机画面使用指南'],
    'Hi3403V100环境搭建指南.md': ['Hi3403V100环境搭建指南', '驱动和开发环境安装指南'],
    '小型系统SS928V100移植案例.md': ['OpenHarmony Small系统集成Hi3403V100移植案例'],
    '外围设备驱动 操作指南.md': ['外围设备驱动操作指南'],
    'SYS_CONFIG 配置指南.md': ['SYS_CONFIG配置指南'],
    '内存布局调整指南.md': ['内存布局调整指南'],
    'DDR 小型化指南.md': ['DDR 小型化指南'],
    'U-boot 移植应用开发指南.md': ['SS928V100╱SS927V100 U-boot 移植应用开发指南'],
    '3DNR参数配置说明.md': ['SS928V100╱SS927V100 3DNR参数配置说明'],
    '安全启动使用指南.md': ['SS928V100╱SS927V100 安全启动使用指南'],
    'ISP 开发参考（1--2）.md': ['ISP 开发参考'],
    'ISP 开发参考（3--5）.md': ['ISP 开发参考'],
    'ISP 开发参考（6）.md': ['ISP 开发参考'],
    'ISP 开发参考（7--14）.md': ['ISP 开发参考'],
    'ISP 图像调优指南.md': ['ISP 图像调优指南'],
    'ISP 颜色调优说明.md': ['ISP 颜色调优说明'],
    'ISP FAQ.md': ['ISP FAQ'],
    'Sensor 调试指南.md': ['Sensor调试指南'],
    '黑白彩色双路融合 开发参考.md': ['黑白彩色双路融合 开发参考'],
    '黑白彩色双路融合调试指南.md': ['黑白彩色双路融合调试指南'],
    '00 前言.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '01 概述.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '02 系统控制.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '03 视频输入.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '04 视频输出（4.1--4.3）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '04 视频输出（4.4--4.5）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '05 视频处理子系统.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '06 视频编码（6.1--6.3）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '06 视频编码（6.4--6.5）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '07 视频解码.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '08 区域管理.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '09 音频（9.1--9.3）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '09 音频（9.4--9.5）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '10 视频图形子系统.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '11 几何畸变矫正子系统.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '12 拼接.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '13 Proc调试信息（13.1--13.14.15）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    '13 Proc调试信息（13.16--13.29）.md': ['MPP 媒体处理软件 V5.0 开发参考'],
    'MPP 媒体处理软件 V5.0 FAQ.md': ['MPP 媒体处理软件 V5.0 FAQ'],
    'IVE API 参考（1--2）.md': ['IVE API 参考'],
    'IVE API 参考（3--6）.md': ['IVE API 参考'],
    'IVS API参考.md': ['IVS API参考'],
    'SVP2.0 开发指南.md': ['SVP2.0开发指南'],
    'SVP2.0 API 参考.md': ['SVP2.0 API 参考'],
    'ATC工具使用指南.md': ['ATC工具使用指南'],
    'ATC Graph开发指南.md': ['ATC Graph开发指南'],
    'ATC自定义算子开发指南.md': ['ATC自定义算子开发指南'],
    'AMCT使用指南（Caffe）.md': ['AMCT使用指南（Caffe）'],
    'AMCT使用指南（PyTorch）.md': ['AMCT使用指南（PyTorch）'],
    'DPU2.0 工具使用指南.md': ['DPU2.0 工具使用指南'],
    'Profiling工具使用指南.md': ['Profiling工具使用指南'],
    '精度比对工具使用指南.md': ['精度比对工具使用指南'],
    '图像分析引擎2与图像分析引擎1使用差异说明.md': ['图像分析引擎2与图像分析引擎1使用差异说明'],
    '图像质量调试工具使用指南.md': ['图像质量调试工具使用指南'],
    'HDMI 开发参考.md': ['HDMI 开发参考'],
    'MIPI 使用指南.md': ['MIPI 使用指南'],
    'MotionFusion 开发参考.md': ['MotionFusion 开发参考'],
    'PCIE级联 应用指南.md': ['PCIE级联应用指南'],
    '拼接 FAQ.md': ['拼接 FAQ'],
    'CIPHER API 参考.md': ['CIPHER API 参考'],
    'GFBG API 参考.md': ['GFBG API 参考'],
    'KLAD API 参考.md': ['KLAD API 参考'],
    'OTP API 参考.md': ['OTP API 参考'],
    'TDE API参考.md': ['TDE API参考'],
    '音频组件 API参考.md': ['音频组件API参考'],
    'BurnTool 工具使用指南.md': ['BurnTool 工具使用指南'],
    'ToolPlatform工具平台使用指南.md': ['ToolPlatform工具平台使用指南'],
    'MindCmd 使用指南.md': ['MindCmd 使用指南'],
    'DIS 调试指南.md': ['DIS 调试指南'],
    'BSP FAQ.md': ['BSP FAQ'],
    '产品简介.md': ['SS928V100 超高清智能网络录像机 SoC 产品简介'],
    'SDK安装与升级.md': ['SS928V100╱SS927V100 SDK 安装以及升级使用说明'],
}

# Scan all docs, find missing images, try to copy from old source
total_missing = 0
total_copied = 0
total_not_found = 0
not_found_details = []
copied_details = []

for root, dirs, files in os.walk(NEW_DOCS):
    for fn in files:
        if fn.endswith('.md'):
            fp = os.path.join(root, fn)
            with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            for m in re.finditer(r'!\[([^\]]*)\]\(([^()]*)\)', content):
                url = m.group(2).strip()
                if ' ' in url:
                    url = url.split()[0]
                abs_path = os.path.normpath(os.path.join(os.path.dirname(fp), url))
                if not os.path.exists(abs_path):
                    total_missing += 1
                    found = False
                    for old_dir_name in doc_map.get(fn, []):
                        if old_dir_name in old_dirs:
                            old_figures = old_dirs[old_dir_name]
                            img_name = os.path.basename(url)
                            old_img = os.path.join(old_figures, img_name)
                            if os.path.exists(old_img):
                                target_dir = os.path.dirname(abs_path)
                                os.makedirs(target_dir, exist_ok=True)
                                shutil.copy2(old_img, abs_path)
                                total_copied += 1
                                found = True
                                copied_details.append((fn, url))
                                break
                    if not found:
                        total_not_found += 1
                        rel = os.path.relpath(fp, NEW_DOCS)
                        not_found_details.append((rel, url))

print(f'Total missing image refs: {total_missing}')
print(f'Copied from old source: {total_copied}')
print(f'Still not found: {total_not_found}')
print()
if not_found_details:
    print(f'Still missing images ({total_not_found}):')
    for f, u in sorted(not_found_details)[:50]:
        print(f'  {f} -> {u}')
    if total_not_found > 50:
        print(f'  ... and {total_not_found - 50} more')