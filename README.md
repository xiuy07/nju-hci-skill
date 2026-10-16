# HCI Design & Research — 交互设计与实验分析

**整理自南京大学人机交互系统课程。** 非官方整理，不代表南京大学或任课教师意见。仓库不附原 PDF。

`hci-design-research` 是用于实际项目的 Codex skill：设计界面和交互流程时遵循人机交互原则，评审已有系统，设计研究与实验，并分析实验数据。课程是知识来源，技能的主要用途是设计和研究工作。

## 使用场景与范围

| 场景 | 具体作用 |
| --- | --- |
| 新界面或交互功能 | 从用户目标推导流程和状态，将反馈、一致性、防错、撤销、认知负担落实到方案或实现 |
| 已有系统改进 | 启发式评估、认知走查；提供具体问题、证据、用户影响和验证办法 |
| 需求与原型 | 人物角色、场景、HTA、可验证需求、原型选择与设计取舍 |
| 用户研究与实验 | DECIDE、访谈、观察、任务测试、组内/组间及析因实验方案 |
| 实验数据分析 | 检查数据质量与实验结构，选择适当方法，报告效应与不确定性，解释实际设计意义 |
| 效率预测 | GOMS、KLM、Fitts；声明假设、参数、单位和预测边界 |

适用于 Web、移动端和桌面等交互式系统的设计与研究。纯视觉风格创作和不涉及交互决策的编码不是主要触发场景。专家推断不能替代真实用户证据，模型预测不能当实测，不提供无障碍或行业合规认证。

## 安装与使用

将 `skills/hci-design-research` 目录完整复制到：

```text
~/.codex/skills/hci-design-research/
```

若设置了 `CODEX_HOME`，使用其下的 `skills/hci-design-research`。Windows 默认通常是用户目录下的 `.codex\skills\hci-design-research`。安装后下一轮对话可用；未刷新时重新打开聊天或重启 Codex。

也可请求 Codex：

```text
使用 skill-installer 从 Finn-307/nju-hci-skill 安装 skills/hci-design-research。
```

私有仓库需有读取权限。此包无额外运行时依赖；实现界面或分析数据时使用当前环境已有工具。默认允许相关任务自动匹配。

```text
使用 $hci-design-research 设计报名流程，把反馈、防错和错误恢复落实到页面。
使用 $hci-design-research 评审这份原型，给出有依据的交互改进建议。
使用 $hci-design-research 设计比较两种导航方式的实验，明确变量与分析方法。
使用 $hci-design-research 分析这份组内实验数据，报告效应量、置信区间和设计含义。
使用 $hci-design-research 比较鼠标菜单与快捷键的操作效率，说明模型假设。
```

## 内容与来源

[SKILL.md](skills/hci-design-research/SKILL.md) 是入口，五份参考资料按任务读取：需求与设计、原则与评审、研究与实验分析、交互模型、来源与校订。来源保留原笔记的页码线索，并补充实际工作流程与自拟示例。

对样本人数、7±2、公式符号和研究分类等易误用内容作了说明。完整范围见[来源与校订](skills/hci-design-research/references/provenance.md)。本包未对原课程资料声明开源许可。
