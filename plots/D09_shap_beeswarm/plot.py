# -*- coding: utf-8 -*-
# D09 · SHAP 蜂群图 (SHAP Beeswarm)
# 用途：特征贡献及其分布
# 推荐方法：shap.plots.beeswarm()
# 规范提示：特征值高低应使用连续色阶，不要用分类色板
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

data = [rng.normal(k, .8, 60) for k in range(len(colors))]
bp = ax.boxplot(data, patch_artist=True)
for patch, c in zip(bp["boxes"], colors):
    patch.set_facecolor(c)

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("D09_shap_beeswarm.pdf")
fig.savefig("D09_shap_beeswarm.png", dpi=150)
