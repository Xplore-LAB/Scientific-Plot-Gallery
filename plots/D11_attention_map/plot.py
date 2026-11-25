# -*- coding: utf-8 -*-
# D11 · 注意力热力图 (Attention Map)
# 用途：注意力权重可视化
# 推荐方法：sns.heatmap()
# 规范提示：行列标签需可读；注明 head / layer 与掩码规则
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

data = rng.normal(size=(len(colors), len(colors)))
im = ax.imshow(data, cmap="viridis", aspect="auto")
fig.colorbar(im, ax=ax)

ax.set_xlabel("x"); ax.set_ylabel("y")
if ax.get_legend_handles_labels()[0]:
    ax.legend(frameon=False)
fig.savefig("D11_attention_map.pdf")
fig.savefig("D11_attention_map.png", dpi=150)
