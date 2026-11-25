# -*- coding: utf-8 -*-
# B04 · 散点图 (Scatter Plot)
# 用途：变量关联与样本分布
# 推荐方法：ax.scatter()
# 规范提示：点需透明或抖动避免遮挡；注明回归/拟合方法
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

for k in range(len(colors)):
    ax.scatter(rng.normal(k * 1.4, .5, 30), rng.normal(k * .6, .5, 30),
               color=colors[k], s=28, alpha=.8, label=f"cluster {k+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("B04_scatter_plot.pdf")
fig.savefig("B04_scatter_plot.png", dpi=150)
