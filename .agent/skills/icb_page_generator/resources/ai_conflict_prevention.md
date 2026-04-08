# AI 知識衝突防護指南

> [!IMPORTANT]
> 本文件是 AI 協作的「防護牆」。所有進入本專案的 AI（Copilot、ChatGPT、Gemini、Claude、OpenCode）都必須在開始任何 Odoo 頁面任務前讀取此文件，確保輸出完全符合本專案的規格，而非任何主流框架的預設慣例。

---

## 一、主流 LLM 常見誤用範例（針對本系統非主流慣例）

以下是 AI 在未掌握本專案規格時最容易發生的典型錯誤：

### 1. Bootstrap 版本混亂
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 輸出 Bootstrap 5 的 `mb-3`、`g-4`（gutter）、`col-lg-auto` | 嚴格使用 **Bootstrap 4.5** 語法；間距用 `pt8`/`pb16` 等 Odoo 自有 class |
| 使用 `fs-2`（Bootstrap 5 字體工具類） | 使用 Bootstrap 4 的 `h2`、`lead` 語義標籤 |
| 使用 `btn-close`（Bootstrap 5） | 使用 `×`（`&times;`）或 FA 圖示 |

### 2. 按鈕結構錯誤
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| `<button class="btn btn-primary">` | **只用 `<a class="btn btn-primary">`**，絕對不使用 `<button>` |
| 自創 class：`<a class="cta-btn btn">` | 只用系統允許的組合：`btn` + 樣式class + 尺寸class + 形狀class |
| Inline style：`style="background:#f00"` | 顏色由 `--o-cc1-btn-primary` 等 SCSS 變數控管 |

### 3. XML / QWeb 結構缺失
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 直接輸出裸 HTML，沒有 QWeb 外框 | 所有頁面必須有 `<t t-name="..."><t t-call="website.layout">...<div id="wrap">` |
| 在 XML 內寫 `<style>...</style>` | **嚴禁**在 XML 內寫 `<style>`；所有樣式放獨立 `.scss` 檔 |
| 首頁沒有 `pageName` 設定 | 首頁需加 `<t t-set="pageName" t-value="'homepage'"/>` |

### 4. Snippet 骨架自行發明
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 用 Bootstrap `card` 結構模擬 Odoo 產品卡 | 動態產品必須對接 `s_dynamic_snippet_products`；靜態卡使用 `o_carousel_product_card`（Odoo 專屬 class） |
| 為 Snippet 自訂骨架 | 必須從 `templates/` 或 `snippet_rules.md` 中選擇對應 snippet，**不可自行發明骨架** |
| 在動態 snippet 內手刻假卡片 | 動態 snippet 的 locked 結構**不可修改內部 DOM** |

### 5. SCSS 通靈發明
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 憑空發明 CSS 動畫或 class（如 `.fade-in-section`） | SCSS 來源**絕對是** `templates/improved/` 對應的 `.scss` 檔案 |
| 用 `position: absolute` 而未加保護前綴 | 所有會造成重疊的 SCSS 必須加 `#wrapwrap:not(.odoo-editor-editable)` 前綴 |
| 用 `media (max-width: 768px)` 自訂斷點 | 使用 Bootstrap 4.5 mixin 或 `user_custom_rules.scss` 的自訂斷點變數 |

### 6. 顏色與主題系統誤用
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 在 SCSS 硬寫 HEX 顏色值（如 `color: #3498db`） | 使用 `o_cc` class 系統（`o_cc1`~`o_cc5`）與 CSS 變數 |
| 移除 `o_cc` class 後另外加 `text-white` | 使用 `o_ccX` 時**不加**手動 `text-white` 或 `text-dark` |
| 把 carousel 遮罩樣式搬到 SCSS | `.o_we_bg_filter` 顏色屬性**必須保留為 XML 行內樣式**（後台可調） |

### 7. Icon 系統混亂
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 使用 Font Awesome v5/v6（如 `fas fa-star`、`fa-solid fa-star`） | **只用 Font Awesome v4**（`fa fa-star`） |
| 使用 Bootstrap Icons 或 Material Icons | 主圖示系統固定為 FA v4，特例需明確標注 |

### 8. 輸出位置錯誤
| 主流 AI 可能的錯誤行為 | 本專案正確做法 |
|---|---|
| 將客製化草稿寫入 `templates/` | `templates/` 是靈感庫，**嚴禁**將草稿寫入；產出一律放 `outputs/` |
| 輸出沒有日期時間的檔名 | 輸出檔名**必須**包含日期時間（如 `page-20260408-1200.xml`） |

---

## 二、讓 AI 輸出封裝進可控工作流的方法

### 2-1. 強制「先讀文件再動手」的決策流程

```
任務進入
    │
    ├─► 讀 AGENTS.md（全域硬規則）
    ├─► 讀 TODO.md（目前未完成項目）
    ├─► 讀 docs/design/PROJECT_THEME.css（配色）
    │
    ├─ 任務屬於頁面生成？
    │   ├─ /page → 讀 page_templates.md + snippet_rules.md
    │   └─ /create → Phase A 文字骨架（等待確認）→ Phase B XML+SCSS
    │
    ├─ 任務屬於動態區塊？→ 讀 dynamic_rules.md + locked 骨架
    ├─ 任務屬於按鈕？→ 讀 button_styles.md
    ├─ 任務屬於 JS 元件？→ 讀 component_library.md
    ├─ 任務屬於 Header/Footer？→ 讀 header_footer_rules.md
    ├─ 任務屬於 Blog/Shop？→ 讀 system_pages_scss.md
    └─ 需要 SCSS？→ 讀 scss_reference.md
```

### 2-2. Task Contract（每次任務前的檢查清單）

AI 在生成代碼前，必須在內部確認以下項目（不需輸出，僅用於推理）：

```
□ 此任務的輸出類型？（XML+SCSS / SCSS only / JS）
□ 目標頁面類型？（一般頁面 / 首頁 / 系統頁面）
□ 是否涉及動態 Snippet？（如是，使用 locked 骨架）
□ 使用 Bootstrap 版本確認：4.5（非 5）
□ 圖示版本確認：FA v4（非 v5/v6）
□ SCSS 是否有可重用的全域樣式？（查 user_custom_rules.scss）
□ 輸出位置：outputs/（非 templates/）
□ 輸出檔名是否含日期時間？
```

### 2-3. 三層防護架構

```
Layer 1 — 系統硬規則（AGENTS.md）
  └── QWeb 外框、輸出位置、Bootstrap 4.5、FA v4
  └── 這層規則不可被任何任務覆寫

Layer 2 — 知識庫 + Index（resources/）
  └── 依任務類型動態載入最小必要知識
  └── 使用 templates_index.json 精準定位模板片段

Layer 3 — 任務限制（Task Contract）
  └── 每次生成前在推理中確認的臨時限制清單
  └── 例如：此次任務禁止自訂 class、此次只輸出 SCSS
```

---

## 三、AI 自動 Context 修正規則

### 3-1. 七個「雷達偵測」指標

當 AI 注意到自己可能要違反以下指標時，必須立即停止生成並自我修正：

| 指標 | 偵測條件 | 修正動作 |
|------|----------|----------|
| `<button>` 出現 | 要輸出按鈕時 | 改為 `<a class="btn ...">` |
| Bootstrap 5 class | `g-*`、`fs-*`、`btn-close` 等 | 換成 Bootstrap 4.5 對等語法 |
| XML 內有 `<style>` | 寫入樣式時 | 移出到獨立 `.scss` 檔 |
| QWeb 外框缺失 | 輸出 XML 時 | 補上 `<t t-name>` + `website.layout` 外框 |
| SCSS 硬寫 HEX | 設定顏色時 | 改用 `o_cc` class 或 CSS 變數 |
| 草稿寫入 `templates/` | 輸出路徑 | 改為 `outputs/` |
| FA v5/v6 class | 使用圖示時 | 改為 `fa fa-[name]`（v4） |

### 3-2. 衝突優先序

當 AI 從其訓練資料（主流 LLM 知識）和本專案規格發生衝突時，優先順序如下：

```
本專案規格（AGENTS.md + SKILL.md）
    > 本專案知識庫（resources/ 下的各 .md 文件）
    > 本專案模板（templates/ 實際結構）
    > Odoo 15 官方文件
    > Bootstrap 4.5 官方文件
    > LLM 通用訓練知識（最低優先）
```

---

## 四、各 AI 角色職責矩陣

不同 AI 工具在本專案中扮演不同角色，具有不同的「能做 / 不做」範圍：

### Copilot（GitHub Copilot Coding Agent）

**整合點：** `.agents/skills/icb_page_generator/SKILL.md`

| 職責 | 說明 |
|------|------|
| ✅ 主要負責 | 代碼生成、文件修改、Script 執行、PR 審查回應 |
| ✅ 可做 | 修改 `sources/skill/icb_skill.source.json` + 執行 `sync_icb_skill.py` |
| ✅ 可做 | 建立/更新 `resources/` 下的知識庫文件 |
| ✅ 可做 | 輸出到 `outputs/` |
| ❌ 不做 | 直接手改 `.agent/skills/icb_page_generator/SKILL.md` |
| ❌ 不做 | 在 XML 內寫 `<style>` |
| ❌ 不做 | 修改 `templates/base/` 的 locked 結構 |

### Claude（claude.ai / claude-code）

**整合點：** `CLAUDE.md` + `.claude/commands/`

| 職責 | 說明 |
|------|------|
| ✅ 主要負責 | 頁面創作（`/create`）、Snippet 組裝（`/page`）、多步驟對話式生成 |
| ✅ 可做 | 抓站轉化（`/create` + Browser MCP）並放入 `outputs/` |
| ✅ 可做 | 修改 `sources/skill/icb_skill.source.json` + 執行同步腳本 |
| ❌ 不做 | 直接手改 CLAUDE.md 的 ICB_SKILL_INSTRUCTIONS 區塊 |
| ❌ 不做 | 使用 git worktree |
| ❌ 不做 | 自動晉升草稿到 `templates/`（除非使用者明確要求） |

### Gemini（Google AI / Gemini CLI）

**整合點：** `.agent/skills/icb_page_generator/SKILL.md`

| 職責 | 說明 |
|------|------|
| ✅ 主要負責 | 快速原型生成、頁面排版、知識庫查詢與補充 |
| ✅ 可做 | 執行所有 `/page`、`/create`、`/btn`、`/js`、`/dynamic`、`/block` 指令 |
| ✅ 可做 | 讀取並分析 `clientInfo/` 素材 |
| ❌ 不做 | 直接手改 `.agent/skills/icb_page_generator/SKILL.md` |

### OpenCode

**整合點：** `opencode.json` + `.opencode/commands/`

| 職責 | 說明 |
|------|------|
| ✅ 主要負責 | 代碼補全、SCSS 覆寫、快速修改 |
| ✅ 可做 | 使用 `.opencode/commands/` 下的指令 |
| ✅ 可做 | 讀取 `resources/` 知識庫 |
| ❌ 不做 | 直接手改 `opencode.json` 的 instructions（由 sync 腳本管理） |

### 共同職責（所有 AI 必須遵守）

| 規則 | 說明 |
|------|------|
| 開局讀取 | 先讀 `AGENTS.md` → `TODO.md` → `PROJECT_THEME.css` |
| 知識庫查詢 | 依任務類型動態讀取 `resources/` 對應文件，不一次讀全部 |
| 輸出隔離 | 客製化草稿放 `outputs/`，靈感庫 `templates/` 不可寫入 |
| 同步規則 | 修改 Skill 規則時，只改 `sources/skill/icb_skill.source.json`，再執行 `sync_icb_skill.py` |
| 模板節流 | 不直接讀大型 XML 模板，先查 `templates_index.json` 取得行號範圍再精準讀取 |

---

## 五、SKILL 知識同步機制

### 單一來源（SSOT）架構

```
sources/skill/icb_skill.source.json  ← 唯一修改點
    │
    └── scripts/sync_icb_skill.py
        │
        ├── .agent/skills/icb_page_generator/SKILL.md   → Gemini 讀取
        ├── .agents/skills/icb_page_generator/SKILL.md  → Copilot 讀取
        ├── opencode.json (instructions 欄位)           → OpenCode 讀取
        ├── .claude/commands/*.md                        → Claude 指令
        └── CLAUDE.md (ICB_SKILL_INSTRUCTIONS 區塊)     → Claude 讀取
```

### 發布流程

```bash
# 1. 修改來源
vim sources/skill/icb_skill.source.json

# 2. 同步發布到所有 AI 模型
python3 scripts/sync_icb_skill.py    # macOS/Linux
py -3 scripts/sync_icb_skill.py      # Windows

# 3. Commit（同步產生的檔案需一起提交）
git add .
git commit -m "skill: update [description]"
```

### 各模型入口文件對照表

| AI 工具 | 入口文件 | 自動同步？ |
|---------|---------|-----------|
| Gemini | `.agent/skills/icb_page_generator/SKILL.md` | ✅ `sync_icb_skill.py` |
| Copilot | `.agents/skills/icb_page_generator/SKILL.md` | ✅ `sync_icb_skill.py` |
| Claude | `CLAUDE.md` 的 ICB 區塊 + `.claude/commands/` | ✅ `sync_icb_skill.py` |
| OpenCode | `opencode.json` instructions | ✅ `sync_icb_skill.py` |

> [!WARNING]
> 永遠不要直接手改 SKILL.md、CLAUDE.md 的 ICB 區塊、或 opencode.json 的 instructions。  
> 這些是自動產生的檔案，手改在下次 sync 時會被覆蓋。  
> **唯一安全的修改入口是 `sources/skill/icb_skill.source.json`。**
