#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ifu_index.py — 骨科 IFU 多语种语料完整性校验与索引
====================================================
清点 ortho-ifu.<lang>.md 全部语种，校验每段结构（>=7 个标题），
确认含 CC BY 4.0 披露注释，并产出 index.json。

零依赖（仅 Python 3.8+ 标准库）。
"""
from __future__ import annotations
import sys
import argparse
import glob
import json
import os
import re

EXPECTED_SECTIONS_MIN = 7
DISCLOSURE_RE = re.compile(r"CC\s*BY\s*4\.0", re.I)


def scan(lang_dir: str) -> list[dict]:
    rows = []
    for path in sorted(glob.glob(os.path.join(lang_dir, "ortho-ifu.*.md"))):
        lang = os.path.basename(path).replace("ortho-ifu.", "").replace(".md", "")
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        headings = re.findall(r"^#{1,3}\s+\S", text, re.M)
        rows.append({
            "lang": lang,
            "file": os.path.basename(path),
            "bytes": len(text.encode("utf-8")),
            "words": len(text.split()),
            "headings": len(headings),
            "has_disclosure": bool(DISCLOSURE_RE.search(text)),
            "sections_ok": len(headings) >= EXPECTED_SECTIONS_MIN,
        })
    return rows


SECTIONS = ["产品标识", "预期用途", "禁忌症", "警告", "清洁灭菌", "追溯", "不良事件"]

# 推荐追加段（法规锚点已 web 一手核实 2026-10-12）：
#   MR 安全性标注 —— ASTM F2503（现行版 F2503-26；MR Safe/MR Conditional/MR Unsafe
#     三类术语，MR Compatible 已废止；IEC 体系等同 IEC 62570:2025）
#   植入卡信息   —— EU MDR Article 18（器械名/SN/LOT/UDI/型号/制造商名址网；
#     12 类豁免；卡尺寸 85.60×53.98mm 见 MDCG 2019-8 v2）
#   材料信息     —— EU MDR Annex I 23.4(u)（植入器械物质定性定量）
# 注：全球无法规强制固定语种数量/集合（EU MDR Art.10(11) 按成员国语言；
# FDA 21 CFR 801.15 强制英语、外语可选；IEC/IEEE 82079-1:2019 按销售国法律）。
# 本仓库 13 外语为业界常见覆盖实践（无法规依据），按目标市场增删。
RECOMMENDED_SECTIONS = [
    ("MR 安全性标注", "ASTM F2503-26 / IEC 62570:2025"),
    ("植入卡信息", "EU MDR Article 18 + MDCG 2019-8 v2"),
    ("材料信息", "EU MDR Annex I 23.4(u)"),
]


def _demo() -> int:
    print("骨科 IFU 多语种语料 · 7 段对齐结构:")
    for i, s in enumerate(SECTIONS, 1):
        print(f"  {i}. {s}")
    print("\n支持语种: zh(母版) + en/de/ja/ar/fr/es/it/pt/ru/ko/th/id/vi（13 外语）")
    print("（注：13 外语为业界常见覆盖实践，无法规强制固定语种集合）")
    print("\n推荐追加段（法规锚点，语料可按需补齐）:")
    for name, src in RECOMMENDED_SECTIONS:
        print(f"  + {name}  [{src}]")
    print("\n校验本地语料: python scripts/ifu_index.py --lang-dir . --out index.json")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="骨科 IFU 多语种语料索引/校验")
    ap.add_argument("--demo", action="store_true", help="打印 7 段结构与语种覆盖")
    ap.add_argument("--selftest", action="store_true", help="跑内置自测（断言 + 负对照 + xfail）")
    ap.add_argument("--lang-dir", default=".", help="含 ortho-ifu.*.md 的目录")
    ap.add_argument("--out", default="index.json", help="输出索引路径")
    args = ap.parse_args()
    if getattr(args, "selftest", False):
        return _selftest()

    if args.demo:
        return _demo()

    rows = scan(args.lang_dir)
    if not rows:
        print("[warn] 未发现 ortho-ifu.*.md 文件")
        return 2

    bad = [r for r in rows if not (r["sections_ok"] and r["has_disclosure"])]
    index = {
        "total_languages": len(rows),
        "expected_sections_min": EXPECTED_SECTIONS_MIN,
        "languages": sorted(r["lang"] for r in rows),
        "entries": rows,
        "all_ok": not bad,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"语种数: {len(rows)}  全部合规: {not bad}")
    for r in rows:
        flag = "OK" if (r["sections_ok"] and r["has_disclosure"]) else "XX"
        print(f"  [{flag}] {r['lang']:3} 段={r['headings']:2} 字={r['words']:4} 披露={'Y' if r['has_disclosure'] else 'N'}")
    print(f"索引已写: {args.out}")
    return 0 if not bad else 1


# ==================== 内置自测（--selftest） ====================
# 由 conformance 补丁于 2026-10-14 生成（生成器 v2）。
# 特性：端到端 CLI 调用 + 内容断言 + 负对照 + xfail（已知缺陷显式标注，不掩盖）。
_SELFTEST_CASES = [(['--demo'], 0, [], [], None), (['--lang-dir', '.'], 0, [], [], None)]


def _selftest() -> int:
    import os as _os
    import subprocess as _sp
    _here = _os.path.dirname(_os.path.abspath(__file__))
    # 仓库根：脚本位于 <repo>/scripts/ 时取上一级；否则取脚本所在目录
    _root = _os.path.dirname(_here) if _os.path.basename(_here) == "scripts" else _here
    _script = _os.path.abspath(__file__)
    _fail, _xfail, _n = [], [], 0
    for _case in _SELFTEST_CASES:
        _args, _rc, _must, _mustnot = _case[0], _case[1], _case[2], _case[3]
        _reason = _case[4] if len(_case) > 4 else None
        _n += 1
        _p = _sp.run([sys.executable, _script] + _args, capture_output=True, cwd=_root)
        _out = _p.stdout.decode("utf-8", "replace")
        _bad = []
        if _p.returncode != _rc:
            _bad.append(f"rc={_p.returncode} 期望 {_rc}")
        for _m in _must:
            if _m not in _out:
                _bad.append(f"输出缺少 {_m!r}")
        for _m in _mustnot:
            if _m in _out:
                _bad.append(f"输出含禁止内容 {_m!r}")
        if _rc == 0 and not _out.strip():
            _bad.append("rc=0 但输出为空（假绿）")
        if _bad:
            if _reason:
                _xfail.append(f"xfail args={_args}：{'；'.join(_bad)} ← 已知缺陷：{_reason}")
            else:
                _fail.append(f"args={_args}：{'；'.join(_bad)}")
    # 通用负对照：未知参数必须非零
    _n += 1
    _p = _sp.run([sys.executable, _script, "--__nonexistent_flag__"], capture_output=True, cwd=_root)
    if _p.returncode == 0:
        _fail.append("负对照失败：未知参数竟返回 0")
    for _x in _xfail:
        print("[selftest][xfail] " + _x)
    if _fail:
        print(f"[selftest] FAILED {len(_fail)}/{_n}")
        for _f in _fail:
            print("  - " + _f)
        return 1
    print(f"[selftest] PASS {_n - len(_xfail)}/{_n}（含负对照；xfail {len(_xfail)} 项为已知缺陷）")
    return 0


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
