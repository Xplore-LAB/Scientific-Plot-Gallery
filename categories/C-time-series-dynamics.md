# C 时序动态

时间序列与动态过程分析

共 12 类图表。

| 编号 | 中文名 | English | 用途 | 推荐方法 | 优先级 | 目录 |
|---|---|---|---|---|---|---|
| C01 | 单变量时序图 | Univariate Time Series | 过程变量变化 | `ax.plot()` | — | [C01](../plots/C01_univariate_time_series/) |
| C02 | 多变量时序图 | Multivariate Time Series | 多变量动态耦合 | `plt.subplots()` | P0 | [C02](../plots/C02_multivariate_time_series/) |
| C03 | 置信带曲线 | Uncertainty Band | 多次实验、不确定性 | `ax.fill_between()` | P0 | [C03](../plots/C03_uncertainty_band/) |
| C04 | 阶跃响应图 | Step Response | 控制系统动态性能 | `python-control` | P0 | [C04](../plots/C04_step_response/) |
| C05 | 轨迹对齐图 | Trajectory Alignment | 不同操作过程比较 | `ax.plot()` | P0 | [C05](../plots/C05_trajectory_alignment/) |
| C06 | 事件时间轴 | Event Timeline | 操作行为、故障事件 | `ax.broken_barh()` | P0 | [C06](../plots/C06_event_timeline/) |
| C07 | 相平面图 | Phase Portrait | 系统状态演化 | `ax.plot()` | — | [C07](../plots/C07_phase_portrait/) |
| C08 | 频谱图 | Spectrum Plot | 周期性、振荡分析 | `scipy.signal` | — | [C08](../plots/C08_spectrum_plot/) |
| C09 | 时频谱图 | Spectrogram | 非平稳信号分析 | `scipy.signal.ShortTimeFFT` | — | [C09](../plots/C09_spectrogram/) |
| C10 | 自相关图 | ACF Plot | 时间依赖性 | `statsmodels` | — | [C10](../plots/C10_acf_plot/) |
| C11 | Bode 图 | Bode Plot | 频域响应分析 | `python-control` | — | [C11](../plots/C11_bode_plot/) |
| C12 | 控制图 | Control Chart | 过程异常监测 | `matplotlib` | — | [C12](../plots/C12_control_chart/) |
