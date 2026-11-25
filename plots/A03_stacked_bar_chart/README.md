# A03 · 堆叠柱状图 (Stacked Bar Chart)

- 分类：A 基础对比
- 用途：组成比例、消耗构成
- 推荐方法：`ax.bar(bottom=...)`
- 优先级：—

## 规范提示
段数不宜超过 6；小段需直接标注数值

## 运行

```bash
python plot.py
```

依赖：`numpy`、`matplotlib`、`cycler`（见根目录 `requirements.txt`）。
样式加载自 `../../styles/paper.mplstyle`，在仓库根目录运行脚本即可。

## 文件

| 文件 | 说明 |
|---|---|
| `plot.py` | 可运行 Python 模板 |
| `metadata.yaml` | 机器可读元数据 |
| `example.csv` | 示例数据结构（模拟数据） |
| `preview.png` | 预览图（由 plot.py 生成） |

> 注意：示例为模拟数据，仅演示配色上色效果，不是真实论文案例。
