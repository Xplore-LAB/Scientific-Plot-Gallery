# -*- coding: utf-8 -*-
# E07 · 系统架构图 (System Architecture)
# 用途：软件、智能体系统
# 推荐方法：Draw.io
# 规范提示：模块边界与数据流方向需标注；配色区分层次
# 分类：E 关系结构
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
fig.savefig("E07_system_architecture.pdf")
fig.savefig("E07_system_architecture.png", dpi=150)
