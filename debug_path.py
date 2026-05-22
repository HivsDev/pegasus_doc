#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

fp = "D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs/getting-started/快速上手指南.md"
url = "figures/zh-cn_image_0000002446762205.png"

# Resolve path
base = os.path.dirname(fp)
target = os.path.join(base, url)
print(f"Base: {base}")
print(f"URL: {url}")
print(f"Target: {target}")
print(f"Exists: {os.path.exists(target)}")

# Normalize
target_norm = os.path.normpath(target)
print(f"Norm: {target_norm}")
print(f"Exists norm: {os.path.exists(target_norm)}")

# Check directory
print(f"Directory exists: {os.path.exists(base)}")
if os.path.exists(base):
    imgs = [f for f in os.listdir(base) if f.endswith('.png')]
    print(f"PNG files in dir: {len(imgs)}")
    print(f"First 3: {imgs[:3]}")
