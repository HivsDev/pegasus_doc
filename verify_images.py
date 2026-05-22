#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re

DOCS = "D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs"
# Just check one file
f = "getting-started/快速上手指南.md"
fp = os.path.join(DOCS, f)

print(f"File: {fp}")
print(f"File exists: {os.path.exists(fp)}")
print(f"Dir exists: {os.path.exists(os.path.dirname(fp))}")
print(f"Dir exists: {os.path.exists('D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs/getting-started')}")

with open(fp, "r", encoding="utf-8", errors="replace") as fh:
    content = fh.read()

total = 0
valid = 0
broken = []

for m in re.finditer(r"!\[([^\]]*)\]\(([^()]*)\)", content):
    url = m.group(2)  # group(2) = URL inside ()
    total += 1
    base = os.path.dirname(fp)
    # Use os.path.join which handles Windows path separators
    target = os.path.normpath(os.path.join(base, url))
    exists = os.path.exists(target)
    if exists and url.strip():
        valid += 1
    else:
        broken.append((url, exists))

print(f"Total images: {total}, Valid: {valid}, Broken: {len(broken)}")
for url, exists in broken[:5]:
    print(f"  BROKEN: url='{url}' exists={exists}")
if valid > 0:
    print(f"  Valid sample: found {valid} valid images")
