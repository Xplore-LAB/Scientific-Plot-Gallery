# -*- coding: utf-8 -*-
# A07 · 点图 (Dot Plot)
# 用途：多方法精确数值对比
# 推荐方法：ax.scatter()
# 规范提示：按数值排序；与误差棒图例区分清楚
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

for k in range(len(colors)):
    ax.scatter(rng.normal(k * 1.4, .5, 30), rng.normal(k * .6, .5, 30),
               color=colors[k], s=28, alpha=.8, label=f"cluster {k+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("A07_dot_plot.pdf")
fig.savefig("A07_dot_plot.png", dpi=150)
