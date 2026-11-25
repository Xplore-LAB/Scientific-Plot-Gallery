# -*- coding: utf-8 -*-
# F01 · 三维散点图 (3D Scatter Plot)
# 用途：三维特征分布
# 推荐方法：mplot3d.scatter()
# 规范提示：注明视角与坐标轴；必要时补二维投影
# 分类：F 空间优化
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
fig.savefig("F01_3d_scatter_plot.pdf")
fig.savefig("F01_3d_scatter_plot.png", dpi=150)
