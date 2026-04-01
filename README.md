# ICB AI Workflow - ODOO 15 頁面生成工具包

## 📋 專案描述

本專案是一個 **AI 協作工具包**，讓設計師透過 AI 終端機工具（OpenCode、Claude Code 等）快速生成符合 Odoo 15 規範的頁面 XML + SCSS。

核心功能：
- **套版模式 `/page`**：從 `templates/` 挑選配方與積木，直接組裝現成頁面。
- **創作模式 `/create`**：AI 全新設計版面（接受純文字描述 或 外部網址/截圖）。AI 會執行結構解析，並嚴格轉換為 Odoo 的 Bootstrap 4 QWeb 架構。

## 🏗️ 專案架構

```
icb-v2/
│
├── ── AI 工具入口（同步產物，勿手改）──────────
├── .agent/                          # Gemini Agent
│   ├── skills/icb_page_generator/   #   SKILL.md + resources/
│   └── workflows/                   #   指令型工作流程
├── .agents/                         # Copilot Agent
│   └── skills/icb_page_generator/   #   SKILL.md
├── .claude/commands/                # Claude 指令
├── .opencode/commands/              # OpenCode 指令
│
├── ── 單一來源（要改規則改這裡）─────────────
├── sources/
│   └── skill/
│       └── icb_skill.source.json    # Skill 主來源
│
├── ── 零件倉庫 ──────────────────────────
├── templates/
│   ├── improved/                    # 改良版（可直接組裝）
│   │   ├── banners/
│   │   ├── content-sections/
│   │   ├── carousels/
│   │   ├── home-recipes/
│   │   ├── footers/
│   │   ├── forms/
│   │   ├── timelines/
│   │   ├── headers/
│   │   ├── buttons/
│   │   └── dynamic/
│   │       ├── products/
│   │       └── news/
│   ├── base/                        # 原生 Odoo snippet 骨架
│   └── catalogs/                    # 分類目錄（AI 按需讀取）
│
├── ── 知識文件 ──────────────────────────
├── docs/
│   └── design/                      # 設計規範
│       ├── PROJECT_THEME.css
│       ├── user_custom_rules.scss
│       ├── COLOR_USAGE_GUIDELINES.md
│       ├── COLOR_EXCEPTIONS.md
│       ├── BUTTON_LINK_GUIDELINES.md
│       └── snippet_spec_template.md
│
├── ── 客戶素材 & 產出 ────────────────────
├── clientinfo/                      # 客戶素材（gitignored）
├── outputs/                         # AI 產出的 XML/SCSS（gitignored）
│
├── ── 工具 & 雜項 ────────────────────────
├── scripts/
│   ├── sync_icb_skill.py           # Skill 同步腳本
│   ├── sync_icb_skill.sh           # macOS/Linux 快捷
│   ├── sync_icb_skill.bat          # Windows 快捷
│   ├── build_preview.py
│   └── validate_dynamic_lock.py
├── playground/                      # 實驗草稿區（gitignored）
├── _archived/                       # 歸檔區（gitignored）
│
├── AGENTS.md                        # 全域規則
├── CLAUDE.md                        # Claude 專屬設定（自動同步）
├── TODO.md                          # 待完成項目
└── opencode.json                    # OpenCode 設定（同步產物）
```

## 🧠 核心設計哲學 (Core Philosophy)

本專案遵循三大核心開發哲學，以確保 AI 協作的高效與系統穩定：

1. **Odoo 只是「承重牆」**：
   我們不是要蓋跟競品一模一樣的 HTML 房子，而是要借鑑其設計概念，生出符合 Odoo「承重牆」（Bootstrap Grid、QWeb 限定外框、Dynamic Snippet 動態鎖定區塊）的建築。嚴禁直接複製外部 HTML。
2. **大一統的 `/create` 創作模式**：
   無論是憑空想像（純文字）還是模仿抓站（給網址 URL/截圖），一律使用 `/create`。AI 會自動啟動 Fetch 或 Browser MCP 抓取內容，並強制執行 Phase A（先出骨架設計報表），由設計師確認水電管線沒亂拉後，才產生 `outputs/` 沙盒草稿。
3. **保留原廠框架提詞以維持 AI 智商**：
   專案對外品牌為 ICB，但在底層指令中堅持保留「Odoo 15」字眼。這是解鎖 LLM 大型語言模型內 Bootstrap 4 與 QWeb 深層預訓練知識的「密碼」，能有效防止 AI 憑空發明錯誤代碼（AI Lobotomy）。

## 🚀 使用方式

### 1. 設計師操作

開啟 AI 終端機工具，輸入指令：

```bash
/page 首頁                    # 用現成模板配方快速組裝首頁
/create 關於我們               # AI 自由設計新版面（純文字靈感）
/create https://example.com   # AI 自動抓站，並轉譯為 Odoo 相容草稿
/dynamic                      # 快速加入動態產品/新聞區塊
/btn                          # 套用按鈕風格
/js                           # 加入互動 JS 元件
/block                        # 呼叫歷史客製化區塊
```

### 2. 放置客戶素材

把客戶的文字、圖片、PPT 等放到 `clientinfo/`，AI 會自動讀取。

### 3. 取得產出

AI 產出的 XML + SCSS 會放在 `outputs/`，設計師複製貼入 Odoo 後台即可。

## 🛠️ Skill 維護方式

### 單一來源 + 自動同步

所有 AI 工具（Gemini、Copilot、Claude、OpenCode）共用同一套規則。

**真正要修改的檔案：**
```
sources/skill/icb_skill.source.json
```

**不要直接手改的檔案（同步產物）：**
- `.agent/skills/icb_page_generator/SKILL.md`
- `.agents/skills/icb_page_generator/SKILL.md`
- `.claude/commands/*.md`
- `opencode.json`

### 修改後同步

```bash
# macOS/Linux
python3 scripts/sync_icb_skill.py

# Windows
py -3 scripts/sync_icb_skill.py
```

或使用 VS Code task：`Sync Odoo Skill`

## 🎨 樣式規範

- 所有樣式獨立寫在 SCSS，不要在 XML 內寫 `<style>`
- 設計規範文件在 `docs/design/`
- 共用客製樣式在 `docs/design/user_custom_rules.scss`

## 📖 Template 架構

| 分類 | 路徑 | 說明 |
|------|------|------|
| 改良版 | `templates/improved/` | 你的改良成品，可直接組裝 |
| 原生版 | `templates/base/` | Odoo 原生 snippet 骨架參考 |
| 目錄 | `templates/catalogs/` | AI 用的分類目錄索引 |

## 🔄 版本歷史
- **v2.0** - 架構重整：templates 分類、sources 單一來源、路徑統一
- **v1.0** - 第一版 ICB 拖曳模板訓練基礎架構
