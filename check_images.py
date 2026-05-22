#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re

DOCS = r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs"
valid = set()
invalid = set()
for root, dirs, files in os.walk(DOCS):
    for fn in files:
        if fn.endswith(".md"):
            fp = os.path.join(root, fn)
            with open(fp, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            for m in re.finditer(r"!\[([^\]]*)\]\(([^()]*)\)", content):
                url = m.group(2)  # group(2) = URL inside ()
                rel = os.path.relpath(fp, DOCS).replace("\\", "/")
                abs_path = os.path.normpath(os.path.join(os.path.dirname(fp), url)).replace("\\", "/")
                if os.path.exists(abs_path):
                    valid.add((rel, url))
                else:
                    invalid.add((rel, url))

print(f"Valid image links: {len(valid)}")
print(f"Invalid (broken) image links: {len(invalid)}")
print()
print("Sample invalid:")
for f, url in sorted(invalid)[:50]:
    print(f"  {f} -> {url}")
if len(invalid) > 50:
    print(f"  ... and {len(invalid)-50} more")

# Group by directory
from collections import Counter
by_dir = Counter()
for f, url in invalid:
    d = f.split("/")[0]
    by_dir[d] += 1
print("\nInvalid images by directory:")
for d, c in by_dir.most_common():
    print(f"  {c:>4}  {d}/")
