# -*- coding: utf-8 -*-
"""仓库一致性校验：catalog ↔ plots 目录 ↔ 每图必备文件。"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))


class TestCatalog(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(CAT["total_plots"], 67)
        self.assertEqual(len(CAT["plots"]), 67)
        self.assertEqual(CAT["category_count"], 6)

    def test_unique_ids(self):
        ids = [p["id"] for p in CAT["plots"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_id_format(self):
        import re
        for p in CAT["plots"]:
            self.assertRegex(p["id"], r"^[A-F]\d{2}$")

    def test_category_links(self):
        cats = {c["id"]: c for c in CAT["categories"]}
        for p in CAT["plots"]:
            self.assertIn(p["category"], cats)
            self.assertIn(p["id"], cats[p["category"]]["plot_ids"])


class TestFiles(unittest.TestCase):
    def test_plot_dirs_exist(self):
        for p in CAT["plots"]:
            d = ROOT / p["directory"]
            self.assertTrue(d.is_dir(), f"missing {d}")

    def test_required_files(self):
        for p in CAT["plots"]:
            d = ROOT / p["directory"]
            for f in ["metadata.yaml", "plot.py", "example.csv", "README.md"]:
                self.assertTrue((d / f).is_file(), f"missing {d / f}")

    def test_scripts_compile(self):
        import ast
        for p in CAT["plots"]:
            src = (ROOT / p["script"]).read_text(encoding="utf-8")
            ast.parse(src, filename=p["script"])

    def test_metadata_has_id(self):
        for p in CAT["plots"]:
            meta = (ROOT / p["directory"] / "metadata.yaml").read_text(encoding="utf-8")
            self.assertIn("id: " + p["id"], meta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
