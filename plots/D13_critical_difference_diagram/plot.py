# -*- coding: utf-8 -*-
# D13 · 临界差异图 (Critical Difference Diagram)
# 用途：多算法统计比较
# 推荐方法：CD Diagram
# 规范提示：注明检验方法、显著性水平与平均秩
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

# 结构图建议用「推荐方法」里的专用工具绘制，这里给出配色导出
for k, c in enumerate(colors):
    ax.scatter([k], [0], s=260, color=c)
ax.set_xticks(range(len(colors)))

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("D13_critical_difference_diagram.pdf")
fig.savefig("D13_critical_difference_diagram.png", dpi=150)
