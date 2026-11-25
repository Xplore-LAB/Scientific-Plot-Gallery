---
name: scientific-plot-gallery
description: 根据科研表达任务选择图表类型、获取可运行的 Matplotlib 模板与配色，用于论文作图或绘图代码生成。当用户要画科研图表、选择图表类型、挑选 SCI 配色、套用期刊样式或询问某类图怎么画时使用。
---

# Scientific Plot Gallery · 科研绘图图谱

用途：把「要表达什么」映射到「用哪类图 + 哪组配色 + 哪份可运行模板」。

## 什么时候用
- 用户说：画个柱状图/箱线图/热力图/ROC/混淆矩阵/UMAP/桑基图……但没给代码。
- 用户说：帮我挑一组适合 SCI 论文的配色 / 这指标该用什么图展示。
- 用户要：统一样式、期刊字号、导出 PDF/SVG。

## 怎么用（工作流）

1. **读目录**：打开 `catalog.json`（或运行 `python tools/query.py --list`），得到 6 类 67 图的稳定索引。
2. **按任务选图**：`category` 是科研表达任务，不是外观：
   - A 基础对比 → B 分布统计 → C 时序动态 → D 机器学习 → E 关系结构 → F 空间优化。
   - 用 `python tools/query.py --search 关键词` 或 `--category C --priority P0` 缩小范围。
3. **取元数据**：`python tools/query.py --id A06 --json` 拿到该图的 `method` / `limitations` / `directory`。
4. **套模板**：读 `plots/<directory>/plot.py`，它是可运行骨架；`example.csv` 是数据结构示意（模拟数据）。
5. **配色**：从 `palettes/curated.json` 选一组 HEX，替换脚本里的 `colors = [...]`；`styles/paper.mplstyle` 保证字号/线宽/导出统一。
6. **规范提示**：务必遵守该图 `limitations`（例如柱状图基线从 0 起、箱线图注明须线定义、热力图带 colorbar）。

## 关键约定
- 每图路径固定：`plots/<ID>_<slug>/`，`slug` 来自英文名小写下划线化。
- `priority` 为 `P0`/`P1` 表示第一阶段优先完善的 20 种，其余为空。
- 所有示例为模拟数据；生成交付物时提醒用户替换为真实数据。
- 配色值以 HEX 为准；不要从预览 PNG 反取色。

## 输出建议
给用户代码时：附上所选图的 `id`、用途一句、一条 `limitations`，并注明数据需替换。不要把 67 张图一次性倒给用户。
