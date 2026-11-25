# -*- coding: utf-8 -*-
# F08 · 平行坐标图 (Parallel Coordinates)
# 用途：高维多目标比较
# 推荐方法：Plotly
# 规范提示：各维需归一化，否则尺度差异会误导结论
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

# 结构图建议用「推荐方法」里的专用工具绘制，这里给出配色导出
for k, c in enumerate(colors):
    ax.scatter([k], [0], s=260, color=c)
ax.set_xticks(range(len(colors)))

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("F08_parallel_coordinates.pdf")
fig.savefig("F08_parallel_coordinates.png", dpi=150)
