# -*- coding: utf-8 -*-
# D08 · 消融实验图 (Ablation Study)
# 用途：模型组件贡献比较
# 推荐方法：ax.bar()
# 规范提示：与完整模型作差；注明指标方向（越大/越小越好）
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

x = np.arange(len(colors))
values = rng.uniform(.4, .95, len(colors))
for xi, v in zip(x, values):
    ax.bar(xi, v, color=colors[xi % len(colors)], label=f"M{xi+1}")

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("D08_ablation_study.pdf")
fig.savefig("D08_ablation_study.png", dpi=150)
