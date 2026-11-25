# E11 · 维恩图 (Venn Diagram)

- 分类：E 关系结构
- 用途：少量集合的交集
- 推荐方法：`matplotlib-venn`
- 优先级：—

## 规范提示
仅适用 ≤3 个集合；面积尽量与集合大小成比例

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
