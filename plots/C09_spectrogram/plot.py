# -*- coding: utf-8 -*-
# C09 · 时频谱图 (Spectrogram)
# 用途：非平稳信号分析
# 推荐方法：scipy.signal.ShortTimeFFT
# 规范提示：注明窗长、重叠率与频率分辨率
# 分类：C 时序动态
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
fig.savefig("C09_spectrogram.pdf")
fig.savefig("C09_spectrogram.png", dpi=150)
