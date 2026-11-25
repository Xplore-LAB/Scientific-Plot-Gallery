# -*- coding: utf-8 -*-
# E12 · 工艺流程图 (Process Flow Diagram)
# 用途：工业过程与装置机理
# 推荐方法：Draw.io / Visio / CAD
# 规范提示：遵循 ISA 符号标准；标出设备位号与物流方向
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
fig.savefig("E12_process_flow_diagram.pdf")
fig.savefig("E12_process_flow_diagram.png", dpi=150)
