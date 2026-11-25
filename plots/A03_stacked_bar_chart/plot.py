# -*- coding: utf-8 -*-
# A03 · 堆叠柱状图 (Stacked Bar Chart)
# 用途：组成比例、消耗构成
# 推荐方法：ax.bar(bottom=...)
# 规范提示：段数不宜超过 6；小段需直接标注数值
# 分类：A 基础对比
# 本脚本由 Scientific Plot Gallery 生成；数据为模拟数据，仅用于演示上色效果。

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

plt.style.use("styles/paper.mplstyle")   # 统一期刊样式；见仓库根目录
colors = ["#F8CCEF", "#C1BFFE", "#8E9CFD", "#8EC0FD", "#01A2FD"]
plt.rcParams["axes.prop_cycle"] = cycler(color=colors)
rng = np.random.default_rng(20261125)

fig, ax = plt.subplots()

x = np.arange(len(colors))
values = rng.uniform(.4, .95, len(colors))
for xi, v in zip(x, values):
    ax.bar(xi, v, color=colors[xi % len(colors)], label=f"M{xi+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("A03_stacked_bar_chart.pdf")
fig.savefig("A03_stacked_bar_chart.png", dpi=150)
