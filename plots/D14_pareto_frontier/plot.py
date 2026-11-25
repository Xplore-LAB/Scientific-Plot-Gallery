# -*- coding: utf-8 -*-
# D14 · Pareto 前沿图 (Pareto Frontier)
# 用途：多目标优化、性能权衡
# 推荐方法：ax.scatter()
# 规范提示：坐标轴注明优化方向；标出非支配解
# 分类：D 机器学习
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
fig.savefig("D14_pareto_frontier.pdf")
fig.savefig("D14_pareto_frontier.png", dpi=150)
