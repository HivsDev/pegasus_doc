#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Replace SS928V100 / SS928 product references with Hi3403V100 / Hi3403V100.
Preserve: paths, commands, file names, compilation parameters.
"""
import os
import re

DOCS_DIR = r"D:/work/07 项目/02 文档整改_output/ss928v100-docs/docs"

# Strings to NOT replace (context keywords indicating path/command)
PROTECT_KEYWORDS = [
    # Path segments
    "platform/ss928",
    "device/board/hisilicon/ss928",
    "device/soc/hisilicon/ss928",
    "vendor/hisilicon/hispark_ss928",
    "soc/hisilicon/ss928",
    # Build/compile contexts
    "CHIP=ss928",
    "BOOT_MEDIA=emmc CHIP=ss928",
    # SDK variant names
    "ss928v100_clang",
    "ss928v100_gcc",
    # File names
    "u-boot-ss928",
    "uImage_ss928",
    "rootfs_ss928",
    "load_ss928",
    "ss928v100_sdk_patch",
    "oh_ss928",
    "patch_ss928",
    # Sysroot/PATH exports (command context)
    "SYSROOT_PATH",
    "export PATH=",
    # OpenHarmony build paths
    "hispark_ss928v100",
    "hispark_ss928",
    # Directory references in paths
    "open_source/",
    "osdrv/",
    "/out/",
    "/prebuilts/",
    # Build script context
    "build.sh",
    ".gn",
    "BUILD.gn",
    "fs.yml",
]

stats = {"files": 0, "replacements": 0}

for src_root, src_dirs, src_files in os.walk(DOCS_DIR):
    for src_fn in src_files:
        if not (src_fn.endswith(".md") or src_fn.endswith(".css")):
            continue

        src_path = os.path.join(src_root, src_fn)
        with open(src_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        new_lines = []
        file_replaced = False

        for line in lines:
            # Check if this line contains any protected keywords
            line_lower = line.lower()
            is_protected = False

            for keyword in PROTECT_KEYWORDS:
                if keyword.lower() in line_lower:
                    is_protected = True
                    break

            if is_protected:
                # Don't modify this line - skip
                new_lines.append(line)
                continue

            # Safe to replace on this line
            original_line = line
            count = 0

            # 1. Replace SS928V100 -> Hi3403V100
            line, c = re.subn(r"SS928V100", "Hi3403V100", line)
            count += c

            # 2. Replace SS928 (uppercase) -> Hi3403V100 (standalone product ref)
            # Only when not in a protected context (already filtered above)
            line, c = re.subn(r"\bSS928\b", "Hi3403V100", line)
            count += c

            # 3. Replace ss928v100 -> hi3403v100 in descriptive text only
            # Be very careful: only when not in a path/command context
            # Use a function to check each match
            def replace_ss928v100_desc(m):
                return "hi3403v100"

            # Replace ss928v100 in lower context
            line, c = re.subn(r"ss928v100", "hi3403v100", line)
            count += c

            if count > 0:
                file_replaced = True
                stats["replacements"] += count

            new_lines.append(line)

        if file_replaced:
            with open(src_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            stats["files"] += 1
            print(f"Modified: {os.path.relpath(src_path, DOCS_DIR).replace(chr(92), '/')}")

print(f"\nTotal: {stats['replacements']} replacements in {stats['files']} files")
