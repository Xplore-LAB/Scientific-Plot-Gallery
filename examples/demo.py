#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""入门示例：用一组精选配色画一张柱状图。"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "plots" / "A01_bar_chart"))

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

plt.style.use(str(ROOT / "styles" / "paper.mplstyle"))
colors = ["#4477AA", "#EE6677", "#228833", "#CCBB44", "#66CCEE"]
plt.rcParams["axes.prop_cycle"] = cycler(color=colors)

labels = ["M1", "M2", "M3", "M4", "M5"]
values = [0.72, 0.81, 0.65, 0.90, 0.77]
fig, ax = plt.subplots()
for i, (lb, v) in enumerate(zip(labels, values)):
    ax.bar(i, v, color=colors[i % len(colors)], label=lb)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels)
ax.set_ylabel("Accuracy")
ax.set_ylim(0, 1)
ax.legend(frameon=False)
fig.savefig(ROOT / "examples" / "demo.png", dpi=150)
print("已生成 examples/demo.png")
