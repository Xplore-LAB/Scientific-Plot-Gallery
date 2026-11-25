# -*- coding: utf-8 -*-
# A06 · 热力图 (Heatmap)
# 用途：实验矩阵、相关性
# 推荐方法：sns.heatmap()
# 规范提示：连续色阶需感知均匀；务必带 colorbar 与行列标签
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

data = rng.normal(size=(len(colors), len(colors)))
im = ax.imshow(data, cmap="viridis", aspect="auto")
fig.colorbar(im, ax=ax)

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("A06_heatmap.pdf")
fig.savefig("A06_heatmap.png", dpi=150)
