#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gold set setup helper：建 _gold_lang/ 语料（zh+en，各 7 段 + CC BY 4.0）供 ifu 扫描测试。"""
import os
LANG_DIR = os.path.join(os.getcwd(), "_gold_lang")
os.makedirs(LANG_DIR, exist_ok=True)
SECTIONS = ["产品标识", "预期用途", "禁忌症", "警告", "清洁灭菌", "追溯", "不良事件"]


def body(title):
    lines = [f"# {title} 骨科植入物 IFU（gold 样本）\n", "CC BY 4.0 · 贡献者：MedXpert (@stevenzhao07)\n"]
    for s in SECTIONS:
        lines.append(f"### {s}\n占位内容。\n")
    return "\n".join(lines)


for lang, title in (("zh", "中文"), ("en", "English")):
    with open(os.path.join(LANG_DIR, f"ortho-ifu.{lang}.md"), "w", encoding="utf-8") as f:
        f.write(body(title))
print("wrote", LANG_DIR)
