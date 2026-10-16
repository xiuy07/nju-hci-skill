# 来源、范围与校订

**整理自南京大学人机交互系统课程。** 非官方整理，不代表南京大学或任课教师意见。

整理日期：2026-10-17。依据的课程笔记共 33 页；本包不含原 PDF、全文提取文本或截图。页码指该版 PDF 页序。知识摘要为重述，需求表、报名案例、验收写法、交付核对及实际应用建议是本包补充，不声称课件原文。

## 使用范围

适合实际交互系统的需求与流程设计、界面方案和实现、可用性评审、用户研究、实验方案与数据分析，以及 GOMS/KLM/Fitts 效率建模。以用户任务、设计原则和研究证据支持决策，不以课程复习为主要用途。它不是完整现代 HCI 教材，不替代真实用户证据、统计专项审查、无障碍认证或行业合规评估。纯视觉风格和不涉及交互决策的编码不属于主要触发场景。

## 疑点与处理

| 页码 | 笔记疑点 | 本包处理 |
| --- | --- | --- |
| 5–6、24–26 | 专家 3–5、5 人约 80%、用户 20–30 混用 | 分开评估者与用户，依研究目的定人数，不承诺发现比例 |
| 14、27 | 7±2 硬套分组，记忆时长固定 | 保留课程背景，不作菜单数量标准 |
| 5 | 可用性客观、UX 主观 | 说明是入门简化，不作严格二分 |
| 6–8 | 两套规则硬对应，“结束”译成对话框 | 分别使用，结束为流程闭环反馈 |
| 8、10 | 原型所属阶段不清，高保真同技术 | 原型贯穿迭代，保真度与技术分开 |
| 19–21 | 研究分类仅凭组数；组内样本减半 | 结合操纵和分配判断，不保证人数比例 |
| 26–27、33 | 用户测试与实证研究互斥 | 说明交集，实证包含观察研究 |
| 30 | P/P1 混淆、K 点击可能重复 | 明确 P 指向、B 按钮及版本约定 |
| 31 | MT 中 ID 缺字，IP 分母缺 T | 写全 MT=a+b×ID、IP=ID/MT，区分两种 ID 形式 |
| 32–33 | NASA-TLX 当满意度；协作走查强归无用户类 | 区分工作负荷与满意度，按实际参与者说明 |

删除口语重复和考试猜测，修复可确定的符号缺失，无法确认时标明边界。当前考试要求需另查，不从“重要”批注推定。

## 核对的一手来源

核对日期 2026-10-17，仅核对相关概念，不表示整份课程资料已完成全面学术审校：

- [Jakob Nielsen：十项启发式](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Ben Shneiderman：八条黄金规则](https://www.cs.umd.edu/users/ben/goldenrules.html)
- [Jakob Nielsen：测试人数](https://www.nngroup.com/articles/how-many-test-users/)
- [Jakob Nielsen：短时记忆与网页可用性](https://www.nngroup.com/articles/short-term-memory-and-web-usability/)
- [Soukoreff & MacKenzie：Fitts 公式对照](https://www.yorku.ca/mack/gflmb_chi95.html)
- [MacKenzie：吞吐量](https://www.yorku.ca/mack/FittsLawSoftware/doc/Throughput.html)
- [SciPy：独立样本与 Welch t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)、[配对 t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)、[Wilcoxon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html)
- [statsmodels：McNemar](https://www.statsmodels.org/stable/generated/statsmodels.stats.contingency_tables.mcnemar.html)

其他补充是解释与应用建议，正式研究或争议细节需进一步核验。本包未对原课程材料声明开源许可，也未据此授予原资料再分发权。
