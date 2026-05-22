#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copy remaining 8 SS928V100-named images from old source, renaming to Hi3403V100.
"""
import os, shutil, glob

OLD = r'D:/work/03 开发板/pegasus-master/docs/zh-CN'
NEW = r'D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs'

# Build index of ALL old images
old_index = {}  # filename -> full path
for root, dirs, files in os.walk(OLD):
    for fn in files:
        if fn.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            old_index[fn] = os.path.join(root, fn)

# Show what we're working with
import re
print("=== Finding SS928V100 images in old source ===")
ss928_files = {k: v for k, v in old_index.items() if 'SS928V100' in k}
for fn, fp in sorted(ss928_files.items()):
    print(f"  {fn}")

print()
print("=== Finding still-missing images in new docs ===")
new_missing = []
for root, dirs, files in os.walk(NEW):
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
                    img_name = os.path.basename(url)
                    rel = os.path.relpath(fp, NEW)
                    new_missing.append((img_name, abs_path, rel))

for img_name, abs_path, rel in sorted(new_missing, key=lambda x: x[0]):
    print(f"  {img_name}")

print()

# Now try to match each missing image to an SS928V100-named old file
copied = 0
still_missing = []

for img_name, abs_path, rel in new_missing:
    matched = False

    # Strategy: For each missing Hi3403V100-named image, look for SS928V100 version
    # First convert to SS928V100 naming
    ss_name = img_name.replace('Hi3403V100', 'SS928V100')

    if ss_name in old_index:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        shutil.copy2(old_index[ss_name], abs_path)
        print(f"  COPIED (exact swap): {img_name}")
        copied += 1
        continue

    # Try with full-width parentheses
    # The old source might use (SS928V100) while we want （SS928V100）
    # Convert our Hi3403V100 name to use half-width parens with SS928V100
    import unicodedata

    # Normalize to half-width
    half_name = ''
    for c in img_name:
        if unicodedata.east_asian_width(c) in ('W', 'F'):
            # Try to find half-width equivalent
            code = ord(c)
            if 0xFF01 <= code <= 0xFF5E:
                half_name += chr(code - 0xFEE0)
            else:
                half_name += c
        else:
            half_name += c

    ss_half = half_name.replace('Hi3403V100', 'SS928V100')
    if ss_half in old_index:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        shutil.copy2(old_index[ss_half], abs_path)
        print(f"  COPIED (half-width): {img_name}")
        copied += 1
        continue

    # Check all SS928V100 files for a match on the non-chip parts
    core_name = img_name.replace('Hi3403V100', '').replace('（', '').replace('）', '').replace('(', '').replace(')', '')
    for oname, opath in sorted(ss928_files.items()):
        old_core = oname.replace('SS928V100', '').replace('（', '').replace('）', '').replace('(', '').replace(')', '')
        # Check if cores match (ignoring the chip name difference)
        if core_name == old_core:
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            shutil.copy2(opath, abs_path)
            print(f"  COPIED (core match): {img_name} <- {oname}")
            copied += 1
            matched = True
            break

    # Special: 内核（以SS928V100为例）.png vs 内核修改（以Hi3403V100为例）.png
    if not matched and '内核' in img_name and 'SS928V100' in str(old_index.keys()):
        for oname, opath in sorted(ss928_files.items()):
            if '内核' in oname and 'SS928' in oname:
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                shutil.copy2(opath, abs_path)
                print(f"  COPIED (special - kernel): {img_name} <- {oname}")
                copied += 1
                matched = True
                break

    if not matched:
        still_missing.append((rel, img_name))

print(f"\nTotal copied this pass: {copied}")
print(f"Total still missing: {len(still_missing)}")
for rel, img_name in still_missing:
    print(f"  {img_name} in {rel}")