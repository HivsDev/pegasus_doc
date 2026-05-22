#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import re
import json
from collections import Counter

result = subprocess.run(
    ['mkdocs', 'build', '-f', 'mkdocs.yml'],
    capture_output=True, text=True, encoding='utf-8', errors='replace',
    cwd=r'D:/work/07 项目/02 文档整改_output/ss928v100-docs'
)

missing_md = set()
source_counts = Counter()

for line in result.stderr.split('\n'):
    if 'contains a link' in line and ('no such anchor' in line or 'is not found' in line):
        m_src = re.search(r"Doc file '(.+?)'", line)
        m_tgt = re.search(r"(?:target|anchor) '(.+?)'", line)
        if m_src and m_tgt:
            source_counts[m_src.group(1)] += 1
            if m_tgt.group(1).endswith('.md'):
                missing_md.add(m_tgt.group(1))

by_dir = Counter()
for f in missing_md:
    d = f.split('/')[0] if '/' in f else f
    by_dir[d] += 1

summary = {
    'total_warnings': len([l for l in result.stderr.split('\n') if 'contains a link' in l]),
    'missing_md_count': len(missing_md),
    'missing_md_by_dir': dict(by_dir.most_common()),
    'missing_md_files': sorted(missing_md),
    'top_source_files': dict(source_counts.most_common(20)),
}

with open(r'D:/work/07 项目/02 文档整改_output/ss928v100-docs/missing_targets.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"Total warnings: {summary['total_warnings']}")
print(f"Missing .md files: {summary['missing_md_count']}")
print("By directory:")
for d, c in by_dir.most_common():
    print(f"  {c:>5}  {d}/")
print(f"Saved to missing_targets.json")
