# -*- coding: utf-8 -*-
# F03 · 三维线框图 (3D Wireframe)
# 用途：模型响应曲面
# 推荐方法：ax.plot_wireframe()
# 规范提示：网格密度适中；可叠加等高线投影
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

X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-2, 2, 60))
Z = np.sin(X) * np.cos(Y)
cs = ax.contourf(X, Y, Z, levels=len(colors), cmap="viridis")
fig.colorbar(cs, ax=ax)

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("F03_3d_wireframe.pdf")
fig.savefig("F03_3d_wireframe.png", dpi=150)
