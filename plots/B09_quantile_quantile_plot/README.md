# B09 · Q-Q 图 (Quantile-Quantile Plot)

- 分类：B 分布统计
- 用途：分布假设检验
- 推荐方法：`scipy.stats.probplot()`
- 优先级：—

## 规范提示
参考线为 y=x；尾部偏离需单独讨论

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
