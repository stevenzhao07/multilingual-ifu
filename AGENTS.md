# AGENTS.md · multilingual-ifu

> 机器可发现入口（AI 编码代理 / Codex / Claude / Cursor）。单一事实源：本文件。

## 这是什么
MedXpert 把骨科植入物/器械使用说明（IFU）做成中→英/德/日/阿/法/西/意/葡/俄/韩/泰/印尼/越 13 外语对照的开源语料库，每段严格对齐 7 段结构（产品标识/预期用途/禁忌症/警告/清洁灭菌/追溯/不良事件）。13 外语覆盖是本模块的主要差异化方向（多数同类项目仅英文）。

## 运行
```bash
python scripts/ifu_index.py --demo
python scripts/ifu_index.py --help
```

## 扩展契约（lgd-skeleton/1.0）
- **一切即插件**：仅依赖声明式 `module.json`，零配置。
- **按需装（lazy）**：仅 triggers 命中时加载。
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由。
- **扩展点**：`plugins/`(新增语种：复制 `ortho-ifu.zh.md` 为 `ortho-ifu.<lang>.md` 并对齐 7 段；校验脚本自动纳入。)

## 红线
纯技术贡献，不含商业营销；MedXpert 仅作为贡献者署名（@stevenzhao07）。
