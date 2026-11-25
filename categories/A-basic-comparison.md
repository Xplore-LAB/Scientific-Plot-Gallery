# A 基础对比

基础数据与实验结果对比

共 10 类图表。

| 编号 | 中文名 | English | 用途 | 推荐方法 | 优先级 | 目录 |
|---|---|---|---|---|---|---|
| A01 | 柱状图 | Bar Chart | 模型性能比较 | `ax.bar()` | — | [A01](../plots/A01_bar_chart/) |
| A02 | 分组柱状图 | Grouped Bar Chart | 多模型、多指标比较 | `ax.bar()` | P0 | [A02](../plots/A02_grouped_bar_chart/) |
| A03 | 堆叠柱状图 | Stacked Bar Chart | 组成比例、消耗构成 | `ax.bar(bottom=...)` | — | [A03](../plots/A03_stacked_bar_chart/) |
| A04 | 折线图 | Line Chart | 参数变化、训练过程 | `ax.plot()` | — | [A04](../plots/A04_line_chart/) |
| A05 | 雷达图 | Radar Chart | 多维性能比较 | `自定义多边形坐标` | P0 | [A05](../plots/A05_radar_chart/) |
| A06 | 热力图 | Heatmap | 实验矩阵、相关性 | `sns.heatmap()` | P0 | [A06](../plots/A06_heatmap/) |
| A07 | 点图 | Dot Plot | 多方法精确数值对比 | `ax.scatter()` | — | [A07](../plots/A07_dot_plot/) |
| A08 | 棒棒糖图 | Lollipop Chart | 排名、性能差异 | `ax.stem()` | — | [A08](../plots/A08_lollipop_chart/) |
| A09 | 瀑布图 | Waterfall Chart | 性能增益分解 | `ax.bar()` | — | [A09](../plots/A09_waterfall_chart/) |
| A10 | 带误差棒柱状图 | Bar with Error Bars | 重复实验结果比较 | `ax.bar(yerr=...)` | P0 | [A10](../plots/A10_bar_with_error_bars/) |
