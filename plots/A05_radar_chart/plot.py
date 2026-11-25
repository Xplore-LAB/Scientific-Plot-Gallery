# -*- coding: utf-8 -*-
# A05 · 雷达图 (Radar Chart)
# 用途：多维性能比较
# 推荐方法：自定义多边形坐标
# 规范提示：指标需统一方向与尺度；推荐 4–8 维；面积易误导
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

t = np.linspace(0, 1, 40)
for k in range(len(colors)):
    y = .2 + .6 * (k + 1) / len(colors) + .08 * np.sin(t * 8 + k)
    ax.plot(t, y, color=colors[k], lw=1.5, label=f"series {k+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("A05_radar_chart.pdf")
fig.savefig("A05_radar_chart.png", dpi=150)
