#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remove lines containing dead image links."""
import os, re

files = [
    r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs/modules/isp/ISP 开发参考（1--2）.md",
    r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs/modules/mpp/06 视频编码（6.1--6.3）.md",
]

for fp in files:
    if not os.path.exists(fp):
        print(f"SKIP: {fp}")
        continue

    with open(fp, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Pattern: ![](path.png "alt") or ![alt](path.png "info")
    img_pattern = re.compile(r"!\[.*?\]\(.*?\.png.*?\)")

    removed = [0]

    def remove_dead_img(m):
        full = m.group(0)
        # Extract path: from opening ( to .png
        paren_start = full.index("(")
        dot_png = full.index(".png") + 4
        path_part = full[paren_start + 1:dot_png]
        abs_path = os.path.normpath(os.path.join(os.path.dirname(fp), path_part))
        if not os.path.exists(abs_path):
            removed[0] += 1
            return ""
        return full

    new_content = img_pattern.sub(remove_dead_img, content)

    if removed[0] > 0:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed {removed[0]} broken image links from {os.path.basename(fp)}")
    else:
        print(f"No broken images in {os.path.basename(fp)}")
