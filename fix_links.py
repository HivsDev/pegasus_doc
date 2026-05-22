#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fix MkDocs broken links by processing all markdown links.
"""
import os
import re
import subprocess

DOCS_DIR = r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs"

# Step 1: Get existing .md files AND images
existing = set()
image_exts = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp'}
for root, dirs, files in os.walk(DOCS_DIR):
    for fn in files:
        rel = os.path.relpath(os.path.join(root, fn), DOCS_DIR).replace("\\", "/")
        if fn.endswith(".md") or any(fn.lower().endswith(ext) for ext in image_exts):
            existing.add(rel)

print(f"Existing .md files: {len(existing)}")

# Step 2: Fix each .md file
print("Fixing links...")
stats = {"count": 0, "files": 0}

for src_root, src_dirs, src_files in os.walk(DOCS_DIR):
    for src_fn in src_files:
        if not src_fn.endswith(".md"):
            continue
        src_path = os.path.join(src_root, src_fn)

        with open(src_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Process [text](url) links, [[url]] wiki-links, and ![alt](url) image links
        # First pass: fix [text](url) - but NOT image links
        def fix_square_link(match):
            link_text = match.group(1)
            url = match.group(2)
            # Skip if preceded by ! (image link)
            return match.group(0)

        # Actually let's handle image links separately first
        # Image links: ![alt](url) - remove dead image references
        def fix_image_link(match):
            alt = match.group(1)
            url = match.group(2)
            url_no_anchor = url.split("#")[0]
            src_dir = os.path.dirname(src_path)
            target_path = os.path.normpath(os.path.join(src_dir, url_no_anchor)).replace("\\", "/")
            if target_path in existing:
                return match.group(0)
            stats["count"] += 1
            return ""  # Remove dead image

        pattern_img = re.compile(r'!\[([^\]]*)\]\(([^()]*)\)')
        new_content = pattern_img.sub(fix_image_link, content)

        # Now fix [text](url) - text links only (not images)
        def fix_square_link2(match):
            link_text = match.group(1)
            url = match.group(2)
            url_no_anchor = url.split("#")[0]
            src_dir = os.path.dirname(src_path)
            target_path = os.path.normpath(os.path.join(src_dir, url_no_anchor)).replace("\\", "/")
            if target_path in existing:
                return match.group(0)
            stats["count"] += 1
            return f"[{link_text}]"

        pattern1 = re.compile(r'\[([^\]]*)\]\(([^()]*)\)')
        new_content = pattern1.sub(fix_square_link2, new_content)

        # Second pass: fix [[url]] wiki-links
        def fix_wiki_link(match):
            url = match.group(1)
            url_no_anchor = url.split("#")[0]
            src_dir = os.path.dirname(src_path)
            target_path = os.path.normpath(os.path.join(src_dir, url_no_anchor)).replace("\\", "/")
            if target_path in existing:
                return match.group(0)
            stats["count"] += 1
            return url_no_anchor

        pattern2 = re.compile(r'\[\[([^\[\]]+)\]\]')
        new_content = pattern2.sub(fix_wiki_link, new_content)

        if new_content != content:
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            stats["files"] += 1

print(f"Fixed {stats['count']} links in {stats['files']} files")

# Step 3: Verify
print("\nVerifying...")
result = subprocess.run(
    ["mkdocs", "build", "-f", "mkdocs.yml"],
    capture_output=True, text=True, encoding="utf-8", errors="replace",
    cwd=os.path.dirname(DOCS_DIR)
)
warnings = [l for l in result.stderr.split("\n") if "contains a link" in l]
print(f"Remaining warnings: {len(warnings)}")
if warnings:
    print("\nRemaining warnings sample:")
    for w in warnings[:5]:
        print(f"  {w[:200]}")
