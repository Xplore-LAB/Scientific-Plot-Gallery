# AGENTS.md · Scientific Plot Gallery

面向 Codex / Claude Code / 其他智能体的仓库协作约定。

## 仓库定位
这是一个科研绘图图谱与代码模板库，兼具「人可读文档」与「机器可读数据源」两种接口。任何改动都要保持二者一致。

## 目录解析规则
- `catalog.json` 是唯一权威索引；`plots/` 下的目录名必须与 `catalog.json` 每条的 `directory` 一致。
- 每类图目录固定含：`metadata.yaml`、`plot.py`、`example.csv`、`preview.png`、`README.md`。
- `categories/` 是 A–F 六类的人类可读索引，由 `catalog.json` 生成，不要手写维护。
- 新增一类图：先更新数据源（博客配色页的 PLOTS 注册表），再跑 `python tools/build_from_source.py` 重新生成，避免只改一处。

## 推荐调用方式
- 查询：`python tools/query.py --id A06 --json`
- 校验：`python -m unittest discover -s tests -v`
- 预览：`cd plots/<dir> && python plot.py`（依赖见 requirements.txt）

## 编辑约束
- 不要手改 `preview.png` / `example.csv` 的内容语义；它们是生成物。
- 不要引入外部网络依赖；所有模板须离线可运行。
- 配色一律用 HEX；RGB 由 HEX 反算。
- 所有示例数据都是模拟数据，交付给用户时要显式声明。

## 提交规范
`feat(plots): ...` / `docs: ...` / `fix(query): ...`；改动生成物时同时在 PR 描述里注明来源。
