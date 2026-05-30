# 🧠 Mental Filter (心聆) 

> **An Interpretable AI Psychological Assessment & Intervention Agent**
> **基于大语言模型与计算精神病学的双轨制心理干预智能体**

**Creator:** 周鹏云 (Zhou Pengyun) | **Affiliation:** Hebei University (Applied Psychology)

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Dual--Track-success)
![Status](https://img.shields.io/badge/Status-Concept_Proof-orange)

---

## 📌 1. 项目简介 (Project Overview)

**Mental Filter** 是一个部署在工作流引擎（如 COZE/Dify）并结合飞书多维表格（Feishu Base）闭环的 AI 心理动态监测与干预智能体。

针对中学生（12-18岁）群体，本项目致力于解决当前数字心理健康领域的两大痛点：
1. **传统量表的局限**：如 KADS-11 等自评量表存在回顾性偏差，易激起防御心理。
2. **AI 陪伴的“黑盒”风险**：纯聊天 AI 的评估缺乏可解释性（幻觉严重），且极易在重度危机（如自伤意念）时因过度共情而错过现实世界的物理干预。

通过**生态瞬时评估（EMA）**与**准时化自适应干预（JITAI）**，本系统不仅是一个日常情绪树洞，更是一个极其严谨的临床预警雷达。

## ⚙️ 2. 核心架构与业务流 (Core Architecture & Flow)

本项目采用独特的**“双轨异步处理架构 (Dual-Track Asynchronous Architecture)”**，将 AI 的感性陪伴与理性诊断彻底剥离。

* **💬 [轨一] 前台干预 (Front-end Empathy)**：LLM 扮演非指导性心理辅导员，屏蔽诊断逻辑，提供无条件积极关注与极速情绪抚慰。
* **🩻 [轨二] 后台测绘 (Back-end Clinical Extraction)**：静默读取前台对话，强制剥离感性信息，严格按照 KADS-11 量表的 11 个临床症状维度提取结构化 JSON 字典（0 或 1）。
* **🧮 白盒计分模型 (White-box Scoring)**：彻底摒弃 LLM 黑盒打分。使用 Python 代码节点执行基于真实样本拟合的**多元线性回归方程** ($Y = \Sigma(\beta_i * X_i)$)。同时设立极高危（自杀意念）**一票否决预警机制**，确保评估绝对透明且可解释。
* **🔄 自动化闭环 (Automated Loop)**：数据按“用户ID+日期”作为联合主键脱敏落库。结合定时任务，实现针对极高危人群的**真人加急报警**与针对普通人群的 **AI 自动定时复诊**。

## 📂 3. 仓库文件结构 (Repository Structure)

本项目开源了系统的核心 Prompt 与统计算法代码，可直接移植到任意 LLM 工作流平台。

```text
📦 Mental-Filter-Agent
 ┣ 📂 Prompts                  # 核心大模型驱动提示词
 ┃ ┣ 📜 front_end_empathy.md        # [前台] 柔性共情与非指导性陪伴 Prompt
 ┃ ┣ 📜 back_end_extraction.md      # [后台] KADS-11 临床特征强规则提取 Prompt
 ┃ ┗ 📜 synthetic_data_prompt.md    # [数据] 用于合成多维临床语料的大模型 Prompt
 ┣ 📂 Scoring_Module           # 计分算法与评估中枢
 ┃ ┗ 📜 linear_regression.py        # [代码] Python 线性回归计分与高危阻断节点
 ┣ 📂 Data                     # 数据样本
 ┃ ┗ 📜 sample_synthetic_data.csv   # [数据] AI合成的模拟脱敏结构化测试数据
 ┗ 📜 README.md                # 项目说明文档