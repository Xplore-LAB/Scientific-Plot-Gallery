#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""查询科研绘图图谱目录：人用表格，智能体用 --json。"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser(description="Query Scientific Plot Gallery catalog")
    ap.add_argument("--list", action="store_true", help="列出全部图")
    ap.add_argument("--category", help="按类筛选，如 C 或 A")
    ap.add_argument("--priority", help="按优先级筛选，如 P0")
    ap.add_argument("--id", help="按编号精确查询，如 A06")
    ap.add_argument("--search", help="按中文名/英文名/用途搜索")
    ap.add_argument("--json", action="store_true", help="输出 JSON（智能体友好）")
    args = ap.parse_args()

    rows = CAT["plots"]
    if args.id:
        rows = [p for p in rows if p["id"].upper() == args.id.upper()]
    if args.category:
        rows = [p for p in rows if p["category"].upper() == args.category.upper()]
    if args.priority:
        rows = [p for p in rows if (p.get("priority") or "").upper() == args.priority.upper()]
    if args.search:
        q = args.search.lower()
        rows = [p for p in rows if q in (p["name"] + p["name_cn"] + p["description"]).lower()]

    if args.json:
        print(json.dumps(rows if len(rows) != 1 or args.list or args.category or args.priority or args.search else rows[0],
                         ensure_ascii=False, indent=2))
        return
    if not rows:
        print("没有匹配的图表。")
        return
    print(f"{'编号':<5}{'分类':<4}{'中文名':<12}{'English':<28}{'用途':<20}{'优先级':<5}")
    print("-" * 80)
    for p in rows:
        print(f"{p['id']:<5}{p['category']:<4}{p['name_cn']:<12}{p['name']:<28}{p['description']:<20}{p.get('priority') or '-':<5}")
    print(f"\n共 {len(rows)} 条（总计 {CAT['total_plots']}）")


if __name__ == "__main__":
    main()
