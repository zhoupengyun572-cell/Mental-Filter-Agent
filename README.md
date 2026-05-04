# Mental Filter (心聆) 🧠🤖

> **An Interpretable AI Psychological Assessment & Intervention Agent**
> **基于大语言模型与计算精神病学的双轨制心理智能体**

**Creator:** 周鹏云 (Zhou Pengyun) | **Affiliation:** Hebei University (Applied Psychology)

---

## 📌 项目简介 (Project Overview)
**Mental Filter** 是一个部署在 COZE 平台并结合飞书多维表格闭环的 AI 心理干预智能体。它致力于解决传统心理量表（如 KADS-11）的“回顾性偏差”与现有陪伴型 AI 的“黑盒幻觉”问题。

项目采用独特的**“双轨异步处理架构 (Dual-Track Asynchronous Architecture)”**，将感性陪伴与理性诊断剥离，实现日常化、去病理化的生态瞬时评估（EMA）与准时化自适应干预（JITAI）。

## ⚙️ 核心架构 (Core Architecture)
1. **前台干预轨 (Front-end Empathy)**：大模型扮演非指导性咨询师，提供无条件积极关注与极速情绪抚慰。
2. **后台测绘轨 (Back-end Clinical Extraction)**：静默提取对话中的 KADS-11 临床症状，输出结构化 JSON 字典。
3. **白盒计分模型 (White-box Scoring)**：使用多元线性回归 ($Y = \Sigma(\beta_i * X_i)$) 替代大模型黑盒打分，确保评估的可解释性，并设立高危（自杀意念）一票否决预警机制。
4. **自动化闭环 (Automated Loop)**：数据自动脱敏落库飞书，结合定时任务实现极高危真人报警与 AI 自动复诊跟进。

## 📂 仓库结构 (Repository Structure)
* `/Prompts`：包含前后台大模型核心驱动提示词（系统人设、KADS-11 症状强制提取规则）。
* `/Scoring_Module`：包含基于统计学权重的 Python 线性回归计分与预警节点代码。
* `/Docs`：系统架构图及详细的 PRD（产品需求文档）。

## ⚠️ 临床伦理与数据声明 (Ethical Disclaimer)
* **非医疗工具**：本项目定位为情绪辅助支持工具，绝不能替代专业精神科诊断。
* **隐私安全**：本仓库中不包含任何真实患者的交互数据或临床打分，所有数据拟合与联调均基于大模型合成数据 (Synthetic Data) 完成。
