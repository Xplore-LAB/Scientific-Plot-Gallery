# -*- coding: utf-8 -*-
# A10 · 带误差棒柱状图 (Bar with Error Bars)
# 用途：重复实验结果比较
# 推荐方法：ax.bar(yerr=...)
# 规范提示：注明 n、误差类型（SD/SE/CI）与显著性检验
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
fig.savefig("A10_bar_with_error_bars.pdf")
fig.savefig("A10_bar_with_error_bars.png", dpi=150)
