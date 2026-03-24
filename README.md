# ICB AI Workflow - ODOO 拖曳模板訓練專案

## 📋 專案描述
本專案旨在讓 AI Agent 執行 XML 結構時能夠：
- 先認識系統目前有的拖曳模板
- 陸續累積其他結構+樣式，訓練更多 Skill 能力
- 建立完整的 ODOO 頁面生成工作流程

## 🏗️ 專案架構

### 📁 主要資料夾結構
```
.agent/                         # Gemini / 通用 Agent 入口與 workflows
├── skills/icb_page_generator/ # Odoo skill 入口之一
└── workflows/                  # 指令型工作流程

.agents/                        # Copilot / VS Code agent skills
└── skills/icb_page_generator/ # Odoo skill 入口之一

.opencode/                      # OpenCode 指令與本地設定
└── commands/                   # page、dynamic、btn、js、block 等指令

.vscode/tasks.json              # VS Code task，含 Sync Odoo Skill

docs/                           # 專案配色與樣式規範
├── PROJECT_THEME.css
└── user_custom_rules.scss

scripts/                        # Skill 單一來源與同步工具
├── icb_skill_source.json      # 共用 skill 主來源
├── sync_icb_skill.py          # 自動同步腳本
└── sync_icb_skill.bat         # Windows 一鍵同步入口

outputs/                        # AI 產出的 XML / SCSS 成品

templates/                      # 公版結構庫（XML + 內嵌 SCSS），AI 讀取參考用

AGENTS.md                       # 全域規則
TODO.md                         # 知識庫待完成項目
opencode.json                   # OpenCode 全域 instructions（同步產物）
```

## 🚀 功能特點

### 🤖 AI Agent 技能
- **ODOO 頁面生成器**: 自動生成符合規範的 ODOO XML 結構
- **模板識別**: 理解現有的拖曳模板結構
- **樣式應用**: 自動應用符合品牌的樣式規範


### 📚 開發文檔
- **完整的 ODOO 開發規範**: 包含按鈕、版面、動態規則等
- **組件庫文檔**: 可重用的 XML 組件集合
- **AI 使用指南**: 如何與 AI 協作開發 ODOO 頁面

### 🎨 樣式撰寫規範
- **所有樣式請獨立寫在 SCSS 檔案**（如 docs/user_custom_rules.scss），**不要寫 CSS 或 style 於頁面 XML**。
- XML 只負責結構與 class，樣式由 SCSS 控制，方便使用者彈性合併與管理。

## 🛠️ 使用方式

### 1. 環境準備
```bash
# 克隆專案
git clone https://github.com/france0414/icb-Ai-workflow.git

# 進入專案目錄
cd icb-Ai-workflow
```

### 1-1. Worktree 使用規範
- 本專案**不使用** git worktree
- 請直接在專案根目錄工作，不要建立 `.worktrees/` 或其他 worktree 目錄
- 詳細規範請見 `CLAUDE.md`

### 2. 查看文檔
- 閱讀 `docs/` 資料夾中的開發規範
- 參考 `library/component_library.xml` 了解可用組件

### 2-1. 放置參考素材
- 若你要提供 AI 參考內容，請放到 `clientInfo/`；公版結構放在 `templates/`
- 可放文字資料、圖片資料、PPT、Excel 或其他需求整理檔
- `clientInfo/` 是輸入素材區，不是正式產出區
### 3. 使用 AI Agent
- 參考 `.agent/workflows/` 中的工作流程
- 使用 `.agent/skills/` 中定義的技能

### 4. 使用同步捷徑
- VS Code 可直接執行預設 task：`Sync Odoo Skill`
- 也可執行 `scripts/sync_icb_skill.bat`
- 或直接執行 `scripts/sync_icb_skill.py`

## Skill 維護方式

目前 Odoo skill 已改成「單一來源 + 自動同步」的維護方式，目的是讓 Gemini、Copilot 與 OpenCode 使用同一套規則。

### 1. 真正要修改的檔案
- `scripts/icb_skill_source.json`

這份檔案是共用 skill 的主來源。若要修改：
- skill 描述
- 核心規則
- 可用指令
- OpenCode instructions

都應該優先修改這裡。

### 2. 不要直接手改的檔案
- `.agent/skills/icb_page_generator/SKILL.md`
- `.agents/skills/icb_page_generator/SKILL.md`
- `opencode.json`

這三個檔案是同步產物，手改後很容易在下次同步時被覆蓋。

### 3. 修改後怎麼同步

修改完 `scripts/icb_skill_source.json` 後，執行以下其中一種方式：

```bash
C:/Users/france0414/AppData/Local/Programs/Python/Python313/python.exe scripts/sync_icb_skill.py
```

或使用：
- `scripts/sync_icb_skill.bat`
- VS Code task：`Sync Odoo Skill`

### 4. 同步後會更新哪些檔案
- `.agent/skills/icb_page_generator/SKILL.md`
- `.agents/skills/icb_page_generator/SKILL.md`
- `opencode.json`

### 4-1. 正式產出放哪裡
- AI 新生成的 XML、SCSS 與其他交付成品，統一放到 `outputs/`
- `clientInfo/` 保留給使用者投餵參考資料，`templates/` 放公版結構庫，不建議再當成正式輸出區

### 5. 這樣做的好處
- 只改一份主來源，避免多個 AI 入口規則分岔
- 讓 Gemini、Copilot、OpenCode 維持一致
- 後續更容易請 AI 協助維護 skill
- 出問題時更容易追查是主來源還是同步腳本有問題
## 📖 開發規範
- 遵循 ODOO 官方 XML 結構標準
- 使用專案定義的樣式規範
- 確保組件可重用性和維護性

## 🔄 版本歷史
- **v1.0** - 第一版本 ICB 拖曳模板訓練基礎架構

## 🤝 貢獻指南
歡迎提交 Issue 和 Pull Request 來改善本專案！

## 📝 備註
- 本地開發檔案不會同步到 GitHub（透過 .gitignore 設定）
- 僅核心開發檔案會進行版本控制
