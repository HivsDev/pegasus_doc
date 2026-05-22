#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re

files_to_check = [
    r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs/modules/isp/ISP 开发参考（1--2）.md",
    r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs/modules/mpp/06 视频编码（6.1--6.3）.md",
]
for fp in files_to_check:
    if not os.path.exists(fp):
        print(f"NOT FOUND: {fp}")
        continue
    with open(fp, encoding="utf-8", errors="replace") as f:
        content = f.read()
    lines = content.split("\n")
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"!\[[^\]]*\]\(([^()]*)\.png\)", line):
            url = m.group(1)
            url = url.replace("\\", "/")
            target = os.path.normpath(os.path.join(os.path.dirname(fp), url)).replace("\\", "/")
            if not os.path.exists(target):
                print(f"{os.path.basename(fp)}:{i}: {line.strip()[:150]}")
