# Changelog

本仓遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

> 首次纳入版本化记录。**尚未打 tag / 发 Release**（须所有者批准后执行）。

### Added
- `--selftest`：端到端自测（真实调用 + 内容断言 + **负对照**），可脱离门户单仓运行。
- `SECURITY.md`、`CODE_OF_CONDUCT.md`：补齐社区治理文件。
- `module.json` 增加机器可读的 `stage` / `stage_name`，标明本模块在医疗器械生命周期中的位置。

### Changed
- 文档勘误：移除与实际实现不符的表述（详见项目级 `PROJECT_ATTRIBUTION.md` 与门户 README）。
- `ifu_index.py` 段数计量修正：① 读文件改用 `utf-8-sig`（zh/en 语料带 UTF-8 BOM，原 `^#{1,3}` 正则漏数 H1）；② 段数按 H2 计，对齐 README 声明的「7 段对齐结构」语义（H1 是文档标题不是段）。修正前 zh/en 显「段=7」、其余 12 语显「段=8」，系测量伪影；修正后 14 语一致显「段=7」。语料文件零改动，实测 14 语 × 7 段全部合规（2026-10-30）。
