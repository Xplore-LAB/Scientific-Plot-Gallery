# D 机器学习

机器学习与人工智能实验

共 14 类图表。

| 编号 | 中文名 | English | 用途 | 推荐方法 | 优先级 | 目录 |
|---|---|---|---|---|---|---|
| D01 | ROC 曲线 | ROC Curve | 分类能力评价 | `sklearn.metrics.RocCurveDisplay` | — | [D01](../plots/D01_roc_curve/) |
| D02 | PR 曲线 | Precision-Recall Curve | 不平衡分类评价 | `PrecisionRecallDisplay` | — | [D02](../plots/D02_precision_recall_curve/) |
| D03 | 混淆矩阵 | Confusion Matrix | 分类错误分析 | `ConfusionMatrixDisplay` | P1 | [D03](../plots/D03_confusion_matrix/) |
| D04 | PCA 投影图 | PCA Projection | 线性降维 | `sklearn.decomposition.PCA` | — | [D04](../plots/D04_pca_projection/) |
| D05 | t-SNE 图 | t-SNE Plot | 高维特征分布 | `sklearn.manifold.TSNE` | P1 | [D05](../plots/D05_t_sne_plot/) |
| D06 | UMAP 图 | UMAP Plot | 高维表征可视化 | `umap-learn` | — | [D06](../plots/D06_umap_plot/) |
| D07 | 训练收敛曲线 | Learning Curve | 训练稳定性与收敛性 | `ax.plot()` | — | [D07](../plots/D07_learning_curve/) |
| D08 | 消融实验图 | Ablation Study | 模型组件贡献比较 | `ax.bar()` | P1 | [D08](../plots/D08_ablation_study/) |
| D09 | SHAP 蜂群图 | SHAP Beeswarm | 特征贡献及其分布 | `shap.plots.beeswarm()` | P1 | [D09](../plots/D09_shap_beeswarm/) |
| D10 | SHAP 瀑布图 | SHAP Waterfall | 单样本决策解释 | `shap.plots.waterfall()` | — | [D10](../plots/D10_shap_waterfall/) |
| D11 | 注意力热力图 | Attention Map | 注意力权重可视化 | `sns.heatmap()` | — | [D11](../plots/D11_attention_map/) |
| D12 | 校准曲线 | Calibration Curve | 预测概率可靠性 | `CalibrationDisplay` | — | [D12](../plots/D12_calibration_curve/) |
| D13 | 临界差异图 | Critical Difference Diagram | 多算法统计比较 | `CD Diagram` | — | [D13](../plots/D13_critical_difference_diagram/) |
| D14 | Pareto 前沿图 | Pareto Frontier | 多目标优化、性能权衡 | `ax.scatter()` | P1 | [D14](../plots/D14_pareto_frontier/) |
