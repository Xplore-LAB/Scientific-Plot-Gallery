# -*- coding: utf-8 -*-
# B07 · 雨云图 (Raincloud Plot)
# 用途：原始样本、密度和统计量
# 推荐方法：ptitprince
# 规范提示：半小提琴、散点与箱线需对齐同一横轴
# 分类：B 分布统计
# 本脚本由 Scientific Plot Gallery 生成；数据为模拟数据，仅用于演示上色效果。

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

plt.style.use("styles/paper.mplstyle")   # 统一期刊样式；见仓库根目录
colors = ["#F8CCEF", "#C1BFFE", "#8E9CFD", "#8EC0FD", "#01A2FD"]
plt.rcParams["axes.prop_cycle"] = cycler(color=colors)
rng = np.random.default_rng(20261125)

fig, ax = plt.subplots()

data = [rng.normal(k, .8, 60) for k in range(len(colors))]
bp = ax.boxplot(data, patch_artist=True)
for patch, c in zip(bp["boxes"], colors):
    patch.set_facecolor(c)

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("B07_raincloud_plot.pdf")
fig.savefig("B07_raincloud_plot.png", dpi=150)
