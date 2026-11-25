# Scientific Plot Gallery

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![plots](https://img.shields.io/badge/plots-67-green.svg)](catalog.json)

**67 类科研图表 · 按科研表达任务分类 · 可运行代码模板 · 面向人与智能体**

一个长期可复用的科研绘图图谱与代码模板库。每类图表都保留统一字段：编号、中英文名、科研用途、推荐绘图方法、投稿规范提示、示例数据、可运行 Python 模板与预览图。既可人工按分类查阅，也可被 Codex / Claude 等智能体通过机器可读的 `catalog.json` 与 `SKILL.md` 直接调用。

## 快速开始（人）

```bash
git clone https://github.com/Xplore-LAB/Scientific-Plot-Gallery.git
cd Scientific-Plot-Gallery
pip install -r requirements.txt
python examples/demo.py            # 随机挑一组配色画一张图
cd plots/A01_bar_chart && python plot.py   # 运行某类图模板
```

- 按类别浏览：[`categories/`](categories/)（A 基础对比 / B 分布统计 / C 时序动态 / D 机器学习 / E 关系结构 / F 空间优化）
- 查某一类图：`plots/<编号>_<slug>/`，例如 [`plots/A01_bar_chart/`](plots/A01_bar_chart/)
- 统一样式：[`styles/paper.mplstyle`](styles/paper.mplstyle)（字号、线宽、导出格式）
- 精选色板与完整色卡：[`palettes/`](palettes/)
- 机器可读总目录：[`catalog.json`](catalog.json)，结构见 [`catalog.schema.json`](catalog.schema.json)

## 快速开始（智能体）

本仓库同时是一份 agent skill。入口文件：

- [`SKILL.md`](SKILL.md) — 技能说明：如何根据科研表达任务选图、如何取模板与配色
- [`AGENTS.md`](AGENTS.md) — 仓库级协作约定与目录解析规则
- [`catalog.json`](catalog.json) — 结构化索引（67 条，字段稳定）
- [`tools/query.py`](tools/query.py) — 命令行查询，例如：

```bash
python tools/query.py --list
python tools/query.py --category C --priority P0
python tools/query.py --id A06 --json
python tools/query.py --search 箱线
```

## 每类图保留的字段

```yaml
id: A05
name: Radar Chart
name_cn: 雷达图
category: performance_comparison
description: 多维性能比较
use_cases: [多算法性能评价, 多任务场景比较]
method: 自定义多边形坐标
implementation: { language: python, libraries: [numpy, matplotlib], script: plot.py }
output: [figure.pdf, figure.png]
preview: preview.png
limitations: [需要统一指标尺度, 面积易误导]
```

## 数据来源与边界

- 图谱分类与规范提示整理自公众号「观科研」*科研配色* 系列及科研绘图通用规范。
- **所有示例与预览均为模拟数据**，用于检验一组配色画在真实图表类型上的上色效果，不是论文真实案例。
- 配色值以仓库内 `palettes/` 的 HEX 为准；RGB 由 HEX 反算。
- 本仓库是 [Xplore-LAB 科研配色专题](https://xplore-lab.github.io/palettes/) 的配套代码库。

## 目录结构

```
Scientific-Plot-Gallery/
├── README.md / SKILL.md / AGENTS.md / LICENSE / requirements.txt
├── catalog.json                 # 机器可读总目录（人/智能体共用）
├── catalog.schema.json          # JSON Schema
├── categories/                  # A–F 六类中文说明与索引
├── plots/<ID>_<slug>/           # 67 个逐图目录
│   ├── metadata.yaml            # 结构化元数据
│   ├── plot.py                  # 可运行模板
│   ├── example.csv              # 示例数据（模拟）
│   ├── preview.png              # 预览图
│   └── README.md                # 单图说明
├── palettes/                    # 精选色板 + 完整色卡 JSON/CSV
├── styles/paper.mplstyle        # 统一样式
├── examples/demo.py             # 入门示例
├── tools/query.py               # 查询 CLI
└── tests/                       # 一致性校验
```

## License

MIT · Xplore-LAB · 2026
