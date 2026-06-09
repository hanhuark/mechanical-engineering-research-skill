# 热流体研究工作流插件

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

**面向热流体机械工程研究的 AI 领域严谨性插件。**

通用研究代理可以总结论文、整理提纲、润色文字。这个插件关注更难的一层：检查传热与流体力学假设、经验关联式适用范围、CFD 可信度、实验不确定度、机理解释、工程权衡，以及结论是否被证据真正支持。

当答案不仅要写得流畅，还要在热流体物理上站得住脚时，使用这个插件。

[![Version](https://img.shields.io/badge/version-v0.2.0-blue?style=for-the-badge)](CHANGELOG.md)
[![Codex Plugin](https://img.shields.io/badge/Codex-Plugin-blue?style=for-the-badge)](.codex-plugin/plugin.json)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple?style=for-the-badge)](.claude-plugin/plugin.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

如果这个项目对你的研究工作流有帮助，欢迎给仓库点 star，方便更多机械工程研究者发现它。

## 两分钟演示

安装后可以直接输入：

```text
Use the mechanical-engineering-research skill to review this claim:

"The CFD model proves that the new microchannel heat sink is optimal because
the average Nusselt number is 40% higher than the baseline. The simulation used
k-epsilon turbulence, a coarse wall mesh, constant water properties, and three
flow rates between Re = 350 and 900. Pressure drop is not discussed."
```

理想输出应当指出：

- Re = 350-900 可能处于层流或过渡区，不能默认使用 k-epsilon 湍流模型。
- 粗网格和缺失壁面处理信息会削弱 Nusselt 数可信度。
- 常物性假设需要说明温度范围和参考温度。
- 只报告传热增强而不讨论压降、泵功和热阻，无法证明设计更优。
- “optimal” 需要设计空间、目标函数、约束条件和不确定度或网格独立性证据。

## 工作流

工作流图见英文 README 的 [Workflow](README.md#workflow)。可编辑 Mermaid 源文件在 [`assets/workflow.mmd`](assets/workflow.mmd)。

核心逻辑：

```text
通用学术研究工作流 = 过程脚手架
mechanical-engineering-research = 热流体领域判断层
```

## 它会重点检查什么

- 经验关联式是否超出 Reynolds、Prandtl、Rayleigh、Nusselt、几何、粗糙度、方向或相变范围。
- CFD 是否缺少网格独立性、壁面处理、收敛、边界条件、物性模型或验证证据。
- 实验是否缺少传感器标定、不确定度传播、重复性、热损失修正或流动发展段检查。
- AI/ML 工作流是否存在视频、表面、实验、几何、压力或仿真族之间的数据泄漏。
- 文献综述是否只是按论文罗列，而不是按机理、方法、性能指标和未解决问题综合。
- 结果讨论是否只描述趋势，而没有解释主导物理机制。
- 申请书是否只写宏大目标，而没有把技术障碍、能力、验证、指标、风险和影响串起来。

## 快速安装

### OpenAI Codex

让 Codex 从 GitHub 安装插件：

```text
Install the Codex plugin from https://github.com/hanhuark/mechanical-engineering-research-skill
```

如果当前 Codex 环境还不支持从 GitHub 安装社区插件，可以安装 skill 文件夹：

```text
Install the Codex skill from GitHub repo hanhuark/mechanical-engineering-research-skill, path skills/mechanical-engineering-research.
```

Windows 手动安装：

```powershell
git clone https://github.com/hanhuark/mechanical-engineering-research-skill.git
cd mechanical-engineering-research-skill
Copy-Item -Recurse .\skills\mechanical-engineering-research "$env:USERPROFILE\.codex\skills\mechanical-engineering-research" -Force
```

### Claude Code

```bash
git clone https://github.com/hanhuark/mechanical-engineering-research-skill.git
claude --plugin-dir ./mechanical-engineering-research-skill
```

常用命令示例：

```text
/thermal-fluid-research-workflow:me-cfd-review
/thermal-fluid-research-workflow:me-correlation-check
/thermal-fluid-research-workflow:me-experiment-plan
/thermal-fluid-research-workflow:me-figure-discussion
```

## 工作流命令

| 命令 | 用途 |
|---|---|
| [`me-correlation-check.md`](commands/me-correlation-check.md) | 检查方程、关联式和无量纲数是否在适用范围内。 |
| [`me-cfd-review.md`](commands/me-cfd-review.md) | 审查 CFD 设置、网格、壁面处理、收敛、验证和结论强度。 |
| [`me-experiment-plan.md`](commands/me-experiment-plan.md) | 规划传感器、标定、不确定度、重复性、热损失修正和安全检查。 |
| [`me-lit-matrix.md`](commands/me-lit-matrix.md) | 建立按机理组织的文献矩阵。 |
| [`me-figure-discussion.md`](commands/me-figure-discussion.md) | 将图表结果改写为有物理解释的讨论。 |
| [`me-proposal-aims.md`](commands/me-proposal-aims.md) | 将申请书目标改写为可评审的技术目标。 |
| [`me-code-sanity.md`](commands/me-code-sanity.md) | 审查研究代码中的单位、可复现性、数据泄漏和物理 sanity check。 |

## 示例

公开安全的合成示例在 [`examples/showcase/`](examples/showcase/)：

- CFD 审查备忘录
- 换热器设计矩阵
- 沸腾文献矩阵
- 申请书 aims 改写
- 图表讨论 before/after

## 验证

```powershell
python scripts\validate_repo.py
```

## 许可证

MIT License。见 [`LICENSE`](LICENSE)。
