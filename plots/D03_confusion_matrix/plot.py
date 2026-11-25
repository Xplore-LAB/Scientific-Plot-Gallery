# -*- coding: utf-8 -*-
# D03 · 混淆矩阵 (Confusion Matrix)
# 用途：分类错误分析
# 推荐方法：ConfusionMatrixDisplay
# 规范提示：归一化需注明按行 / 按列；格子内标数值
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

t = np.linspace(0, 1, 40)
for k in range(len(colors)):
    y = .2 + .6 * (k + 1) / len(colors) + .08 * np.sin(t * 8 + k)
    ax.plot(t, y, color=colors[k], lw=1.5, label=f"series {k+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("D03_confusion_matrix.pdf")
fig.savefig("D03_confusion_matrix.png", dpi=150)
