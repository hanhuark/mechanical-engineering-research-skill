# 熱流體研究工作流外掛

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

**面向熱流體機械工程研究的 AI 領域嚴謹性外掛。**

通用研究代理可以摘要論文、整理大綱、潤飾文字。這個外掛關注更困難的一層：檢查傳熱與流體力學假設、經驗關聯式適用範圍、CFD 可信度、實驗不確定度、機理解釋、工程取捨，以及結論是否真的被證據支持。

當答案不只要寫得順，還要在熱流體物理上站得住腳時，使用這個外掛。

[![Version](https://img.shields.io/badge/version-v0.2.0-blue?style=for-the-badge)](CHANGELOG.md)
[![Codex Plugin](https://img.shields.io/badge/Codex-Plugin-blue?style=for-the-badge)](.codex-plugin/plugin.json)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple?style=for-the-badge)](.claude-plugin/plugin.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

如果這個專案對你的研究工作流有幫助，歡迎替倉庫點 star，讓更多機械工程研究者找到它。

## 兩分鐘示範

安裝後可以直接輸入：

```text
Use the mechanical-engineering-research skill to review this claim:

"The CFD model proves that the new microchannel heat sink is optimal because
the average Nusselt number is 40% higher than the baseline. The simulation used
k-epsilon turbulence, a coarse wall mesh, constant water properties, and three
flow rates between Re = 350 and 900. Pressure drop is not discussed."
```

理想輸出應該指出：

- Re = 350-900 可能位於層流或過渡區，不能直接預設使用 k-epsilon 紊流模型。
- 粗網格和缺少壁面處理資訊會削弱 Nusselt 數可信度。
- 常物性假設需要說明溫度範圍和參考溫度。
- 只報告傳熱增強而不討論壓降、泵功和熱阻，無法證明設計更優。
- 「optimal」需要設計空間、目標函數、限制條件，以及不確定度或網格獨立性證據。

## 工作流

工作流圖見英文 README 的 [Workflow](README.md#workflow)。可編輯 Mermaid 原始檔在 [`assets/workflow.mmd`](assets/workflow.mmd)。

核心邏輯：

```text
通用學術研究工作流 = 流程腳手架
mechanical-engineering-research = 熱流體領域判斷層
```

## 它會重點檢查什麼

- 經驗關聯式是否超出 Reynolds、Prandtl、Rayleigh、Nusselt、幾何、粗糙度、方向或相變範圍。
- CFD 是否缺少網格獨立性、壁面處理、收斂、邊界條件、物性模型或驗證證據。
- 實驗是否缺少感測器校正、不確定度傳播、重複性、熱損失修正或流動發展段檢查。
- AI/ML 工作流是否存在影片、表面、實驗、幾何、壓力或模擬族之間的資料洩漏。
- 文獻回顧是否只是按論文羅列，而不是按機理、方法、性能指標和未解問題整合。
- 結果討論是否只描述趨勢，而沒有解釋主導物理機制。
- 研究計畫是否只寫宏大目標，而沒有把技術障礙、能力、驗證、指標、風險和影響串起來。

## 快速安裝

### OpenAI Codex

請 Codex 從 GitHub 安裝外掛：

```text
Install the Codex plugin from https://github.com/hanhuark/mechanical-engineering-research-skill
```

如果目前 Codex 環境還不支援從 GitHub 安裝社群外掛，可以安裝 skill 資料夾：

```text
Install the Codex skill from GitHub repo hanhuark/mechanical-engineering-research-skill, path skills/mechanical-engineering-research.
```

Windows 手動安裝：

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
| [`me-correlation-check.md`](commands/me-correlation-check.md) | 檢查方程、關聯式和無因次數是否在適用範圍內。 |
| [`me-cfd-review.md`](commands/me-cfd-review.md) | 審查 CFD 設定、網格、壁面處理、收斂、驗證和結論強度。 |
| [`me-experiment-plan.md`](commands/me-experiment-plan.md) | 規劃感測器、校正、不確定度、重複性、熱損失修正和安全檢查。 |
| [`me-lit-matrix.md`](commands/me-lit-matrix.md) | 建立按機理組織的文獻矩陣。 |
| [`me-figure-discussion.md`](commands/me-figure-discussion.md) | 將圖表結果改寫為有物理解釋的討論。 |
| [`me-proposal-aims.md`](commands/me-proposal-aims.md) | 將研究計畫目標改寫為可評審的技術目標。 |
| [`me-code-sanity.md`](commands/me-code-sanity.md) | 審查研究程式中的單位、可重現性、資料洩漏和物理 sanity check。 |

## 示例

公開安全的合成示例在 [`examples/showcase/`](examples/showcase/)：

- CFD 審查備忘錄
- 熱交換器設計矩陣
- 沸騰文獻矩陣
- 研究計畫 aims 改寫
- 圖表討論 before/after

## 驗證

```powershell
python scripts\validate_repo.py
```

## 授權

MIT License。見 [`LICENSE`](LICENSE)。
