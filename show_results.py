#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, sys

# Force UTF-8 on stdout
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open(r'D:/work/07 项目/02 文档整改_output/ss928v100-docs/missing_targets.json', encoding='utf-8') as f:
    data = json.load(f)

print('=== Top 15 source files with most broken links ===')
for fname, count in list(data['top_source_files'].items())[:15]:
    print(f'  {count:>4}  {fname}')

print()
print('=== All missing .md files (first 80 of {}) ==='.format(len(data['missing_md_files'])))
for f in data['missing_md_files'][:80]:
    print(f'  {f}')
if len(data['missing_md_files']) > 80:
    print(f'  ... and {len(data["missing_md_files"]) - 80} more')
