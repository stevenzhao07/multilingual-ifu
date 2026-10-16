# multilingual-ifu

> **Contributed by [@stevenzhao07](https://github.com/stevenzhao07) · Affiliation: MedXpert (medical-device RA & regulatory consultancy) · Pure technical input, no commercial promotion.**

MedXpert 把骨科植入物/器械使用说明（IFU）做成中→英/德/日/阿/法/西/意/葡/俄/韩/泰/印尼/越 13 外语对照的开源语料库，每段严格对齐 7 段结构（产品标识/预期用途/禁忌症/警告/清洁灭菌/追溯/不良事件）。13 外语覆盖是本模块的主要差异化方向（多数同类项目仅英文）。

这是 MedXpert 把"医疗 AI 信任"方法论工程化落地的可插拔模块之一——把抽象的合规要求变成一条可重复运行的命令或参考实现。方法论四要素（白话版）：**治理守护者 XCGS** ＝ 为 AI 留下可核验的治理证据；**立法者 A³ Laws** ＝ 给自主系统划权限 / 监督 / 追责三条硬边界；**护照官 AI 护照** ＝ 为模型签发可追溯的身份凭证；**人机共存** ＝ 明确人类与 AI 的分工与兜底。

---

## 可插拔模块契约（lgd-skeleton/1.0）

本仓库是一个 **`lgd-skeleton/1.0` 可插拔模块**：

- **一切即插件**：仅依赖声明式 `module.json`，零配置；
- **按需装（lazy）**：仅 triggers 命中时加载；
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由发现；
- **扩展点**：`plugins/`(新增语种：复制 `ortho-ifu.zh.md` 为 `ortho-ifu.<lang>.md` 并对齐 7 段；校验脚本自动纳入。)。

机器可发现入口：`AGENTS.md` · `CLAUDE.md` · `llms.txt`。

## 特性

- 14 个语言版本（zh 母版 + 13 外语 en/de/ja/ar/fr/es/it/pt/ru/ko/th/id/vi），均遵循 7 段对齐结构
- CC BY 4.0 可署名再分发，对商业主体友好
- 可插拔校验：`scripts/ifu_index.py` 自动清点 14 个语料（13 外语 + zh 母版）完整性、段数、字数并产出 `index.json`
- 署名披露：顶部 HTML 注释含 CC BY 4.0 + @stevenzhao07 关联披露

**上游投稿目标**：OpenRegulatory/templates（多语种）

## 内容说明

语料覆盖髋/膝关节置换相关骨科植入物与器械的使用说明要点，定位为「对照模板」而非某具体产品的注册标签；落地具体产品前须按目标辖区（NMPA/FDA/EU MDR/PMDA）法规二次审校。

## 免责声明

本工具仅提供结构化模板与计算能力，**不构成法规建议、临床建议或产品合规结论**。具体产品的注册、临床评价、灭菌验证、风险分析、软件分级等决策，须由合资格人员依据目标辖区（NMPA / FDA / EU MDR / PMDA）最新法规文本作出；条款与限值以官方发布文本为准。使用本工具产生的一切后果由使用者自行承担。

## 使用

```bash
# 校验全部语料完整性并生成 index.json
python scripts/ifu_index.py --lang-dir . --out index.json
```

## 快速开始（30 秒）

```bash
git clone https://github.com/stevenzhao07/multilingual-ifu.git && cd multilingual-ifu
python scripts/ifu_index.py --demo
```

> 想参与或遇到问题？[提 Issue](https://github.com/stevenzhao07/multilingual-ifu/issues) · 完整《AI 参与指南》见 [medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)。

## 路由（总入口）

本模块由 **[medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)** 作为 `lgd-skeleton/1.0` 总入口自动路由发现。

## 关联模块

- [samd-ra-toolkit](https://github.com/stevenzhao07/samd-ra-toolkit)
- [medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)

## 许可

CC-BY-4.0 — 见 [LICENSE](./LICENSE)。

## 关联（方法论来源）

- 理念溯源：个人专家关于医疗 AI 信任与治理的公开方法论（个人观点，不构成标准）
- 同账号系列：见 `medical-ai-toolkit` 导航
