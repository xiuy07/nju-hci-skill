# 交互设计与实验分析 · v2.0.0

[English](README.en.md) · [中文技能入口](skills/hci-design-research/SKILL.md) · [English skill](locales/en/skills/hci-design-research/SKILL.md)

`hci-design-research` 用于实际交互项目：将原则落实到界面与流程，评审可用性，设计用户研究和对照实验，分析数据并解释对设计的意义。适用于真实产品中的交互改进与设计研究。

## 本版更新

- 完整中文和英文两版，每版均含入口、UI 元数据和七份参考资料，保持相同能力与调用名。
- 正式记录 `2.0.0` 版本，补充升级、回退、语言切换，以及项目、平台、规范、量表和数据版本适配。
- 扩展异步状态、未知结果、错误恢复、信息架构、无障碍交互、远程研究、实验数据质量、重复测量、效应与不确定性。
- 增加 AI 协作界面的能力预期、控制、纠错与端到端效用评估。
- 方法来源与外部参考集中在 README，技能工作文件专注实际任务。

## 适用场景与预期结果

| 场景 | 输入示例 | 输出重点 |
| --- | --- | --- |
| 新界面/功能设计 | 需求、用户目标、现有技术栈 | 主任务、状态、原型或实现、验收条件 |
| 交互流程改进 | 实际界面、截图、复现步骤 | 有证据的问题、影响、取舍、修改与复验 |
| 用户研究 | 需要支持的设计决策与目标人群 | 方法、招募条件、任务、协议与指标 |
| 比较实验 | A/B 方案、变量、资源限制 | 分配、样本规划、控制、主指标与分析计划 |
| 数据分析 | 原始数据、字段、实验说明 | 质量检查、合适的推断单位、效应区间、实际含义 |
| 效率预测 | 明确任务、起始状态、输入设备 | GOMS/KLM/Fitts 序列、参数、计算与局限 |
| 版本适配 | 锁文件、平台版本、已有规范基线 | 行为差异、最小适配、验证状态 |

可用于 Web、移动、桌面与含 AI 的交互产品；具体实现仍服从项目平台。纯视觉风格创作和不含交互决策的编码不需要调用。截图审查、专家推断、模型预测和真实用户实测的证据强度不同；本包不提供无障碍认证或行业合规结论。

## 选择语言与安装

| 版本 | 仓库目录 | 安装后的调用名 |
| --- | --- | --- |
| 中文，默认 | `skills/hci-design-research` | `$hci-design-research` |
| English | `locales/en/skills/hci-design-research` | `$hci-design-research` |

两版可以独立使用，只安装其中一版。将所选目录完整复制到 `$CODEX_HOME/skills/hci-design-research`；未设置 `CODEX_HOME` 时通常为 `~/.codex/skills/hci-design-research`。不要把两个同名包同时放进发现路径。安装语言不限制最终回复语言。

也可请求安装工具：

```text
从 xiuy07/nju-hci-skill 安装 skills/hci-design-research。
```

英文版将路径改为 `locales/en/skills/hci-design-research`。私有仓库读取需要现有权限。安装后在下一轮尝试调用；若客户端未刷新，重新打开聊天或重启客户端。方法包无需额外运行时或指定模型；分析和实现使用当前环境已有工具。

## 版本适配与升级

`VERSION` 和 `manifest.json` 记录发布版本、语言入口和包布局。版本号采用本项目约定：主版本用于布局/工作流不兼容变化，次版本用于能力扩展，修订号用于兼容修正。它不是自动升级机制。

从 v1 升级：先备份安装目录并保留本地定制，再用完整 v2 包替换。调用名不变；实验分析拆为独立文件，新增兼容和 AI 交互，旧 `references/provenance.md` 不再属于当前安装包。直接覆盖若遗留旧文件，应在确认备份后清理，避免语言或版本混用。回退使用完整备份或旧提交 `4e21c59b919d1ebad61ba732494b159705639c6e`。

| 层面 | 本包处理 | 验证范围 |
| --- | --- | --- |
| Skill 客户端 | Markdown 入口与相对引用；可选 `agents/openai.yaml` | 已做本地结构检查，不承诺全部客户端或模型版本 |
| 操作系统 | 包内容不含特定系统执行脚本 | 本地在 Windows 检查；其他系统未实机验证 |
| Web/原生框架 | 从项目锁文件和目标环境识别版本 | 不提供通用最低浏览器/框架版本，不静默升级 |
| 无障碍标准 | 可明确选择 WCAG 2.2；按项目既有基线适配 | 不是完整符合性审核，模式指南不等于规范 |
| 分析软件 | 方法无特定库依赖；实现核对已安装 API | 本次未运行真实研究数据，也未验证所有库版本 |
| 研究与数据 | 记录构建、协议、量表、埋点和模式版本 | 无可比依据时不强行合并 |

外部文档访问记录为 2026-10-17。WCAG 2.2 使用可识别的正式版本作为参考；本次在线 SciPy 页面显示 1.18.0、statsmodels 显示 0.15.0，仅为查阅快照，不是安装要求或所有方法已验证的声明。

## 内容导航

两个语言包拥有相同参考文件名：

- `requirements-design.md`：目标、HTA、信息架构、状态、原型与设计取舍。
- `principles-review.md`：交互原则、走查、启发式评估、可访问交互与问题排序。
- `research-evaluation.md`：观察、访谈、问卷、可用性测试与指标。
- `experimental-analysis.md`：实验设计、数据合同、质量、方法选择、效应与结论。
- `interaction-models.md`：认知基础、GOMS、KLM、Fitts 与参数边界。
- `compatibility.md`：技能、项目、标准、研究和数据版本适配。
- `ai-interaction.md`：AI 能力预期、控制、纠错与效用验证，仅按需读取。

## 调用示例

```text
使用 $hci-design-research 设计报名流程，覆盖弱网、结果未知和恢复。
使用 $hci-design-research 评审这份原型，区分可见事实和待验证行为。
使用 $hci-design-research 设计两种导航方式的组内实验与分析计划。
使用 $hci-design-research 分析实验数据，保留配对结构并解释效应区间。
使用 $hci-design-research 根据当前组件库版本修复对话框焦点行为。
```

## 验证与维护

运行 `python scripts/validate_package.py` 检查两版布局、版本一致、引用完整、语言文件对应和出处位置。可另外使用 skill-creator 的 `quick_validate.py` 分别检查两个技能目录。结构检查不证明真实用户效果、翻译的测量等价性或全部平台兼容。

维护时同步更新两版语义与版本，核对变化涉及的官方资料，重新执行检查。升级前后记录真实行为；更新文案不等于问题已修复。变更记录见 [CHANGELOG.md](CHANGELOG.md)。

## 来源与参考

本项目将常用的人机交互方法整理为可执行的设计与研究流程，提供评审要点、实验方案和分析模板。

内容覆盖交互原则与目标、人物角色与场景、需求与原型、HTA、评估方法、实验设计、认知基础、GOMS/KLM/Fitts 和 UCD。

下列一手资料用于核对和补充，查阅日期 2026-10-17。链接按主题集中列出，正文不复制整套指南：

| 内容 | 一手参考 |
| --- | --- |
| 交互评审原则 | [Jakob Nielsen：十项启发式](https://www.nngroup.com/articles/ten-usability-heuristics/)、[Ben Shneiderman：八条黄金规则](https://www.cs.umd.edu/users/ben/goldenrules.html) |
| 测试方法与人数边界 | [NN/G：Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/)、[测试人数](https://www.nngroup.com/articles/how-many-test-users/)、[GOV.UK：主持式可用性测试](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) |
| 指标与设计决策 | [Rodden 等：HEART 与目标到指标，CHI 2010](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) |
| 信息架构 | [NN/G：卡片分类与树测试的区别](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/) |
| 在线实验质量 | [Microsoft ExP：实验期间的可信实验模式](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/) |
| 无障碍基线 | [W3C：WCAG 2.2 正式版本，2024-12-12](https://www.w3.org/TR/2024/REC-WCAG22-20241212/)、[APG 模式](https://www.w3.org/WAI/ARIA/apg/patterns/) |
| 目标、焦点和反馈 | [2.5.8 最小目标尺寸](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)、[2.4.11 焦点不被遮挡](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)、[4.1.3 状态消息](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)、[APG 模态框](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) |
| 效率模型 | [Soukoreff 与 MacKenzie：Fitts 公式](https://www.yorku.ca/mack/gflmb_chi95.html)、[MacKenzie：吞吐量](https://www.yorku.ca/mack/FittsLawSoftware/doc/Throughput.html) |
| 连续指标和区间 | [SciPy：独立/Welch t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)、[配对 t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)、[Wilcoxon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html)、[Bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html) |
| 配对与重复结构 | [statsmodels：McNemar](https://www.statsmodels.org/stable/generated/statsmodels.stats.contingency_tables.mcnemar.html)、[线性混合模型](https://www.statsmodels.org/stable/mixed_linear.html) |
| 人机 AI 协作 | [Amershi 等：Guidelines for Human-AI Interaction，CHI 2019](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)、[论文全文](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf) |

各项规范、设计模式和统计方法按其适用条件使用，第三方资料的授权条件以原发布页面为准。
