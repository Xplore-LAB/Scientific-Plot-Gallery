# -*- coding: utf-8 -*-
# B10 · 累积分布图 (ECDF Plot)
# 用途：分位数及性能分布比较
# 推荐方法：sns.ecdfplot()
# 规范提示：阶梯步长随样本量变化，勿做平滑处理
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
    ax.hist(rng.normal(k * .6, .7, 300), bins=24, density=True,
            histtype="step", color=colors[k], label=f"group {k+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("B10_ecdf_plot.pdf")
fig.savefig("B10_ecdf_plot.png", dpi=150)
