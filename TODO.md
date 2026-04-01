# Odoo AI 知識庫 — 待完成工作

> 給任何帳號的 Gemini：請先讀 `AGENTS.md` 和 `.agent/skills/icb_page_generator/SKILL.md`，
> 再使用這份清單繼續以下的知識庫補充工作。

---

## Phase 4：系統模板知識庫 ✅ 已完成

### 4-1. 產品列表 / Blog 列表 SCSS 規則
- [x] 建立 `.agent/skills/icb_page_generator/resources/system_pages_scss.md`
- 內容：Odoo `/shop`、`/blog` 系統頁面的 HTML 骨架 + CSS Selector 規則
- 規則：AI **絕對不能** 為這些頁面輸出 XML，只能輸出 SCSS

### 4-2. Header / Footer 模塊規則
- [x] 建立 `.agent/skills/icb_page_generator/resources/header_footer_rules.md`
- Header：AI **只能**輸出 SCSS（基於第一組 Header 選項）
- Footer：AI **必須**輸出完整 XPath XML（基於 Links 選項）+ 配套 SCSS

### 4-3. 聯絡表單規則
- [x] 建立 `.agent/skills/icb_page_generator/resources/form_rules.md`
- 佈局外殼 (Layout) + 原生表單投放 (Dropzone) 分離策略

### 4-4. 首頁樣板配方
- [x] 建立 `.agent/skills/icb_page_generator/resources/page_templates.md`
- Home 1~4 的組裝配方 (Recipes)

---

## Phase 5：OpenCode 設定 ✅ 已完成

- [x] 建立 `opencode.json`（由 `scripts/sync_icb_skill.py` 自動同步）
- [x] `.opencode/commands/` 六個指令已建好（page, dynamic, btn, js, block, icb）

---

## Phase 6：待辦

- [x] 導入 MCP Scraper 基礎能力（Playwright MCP）
- [x] 建立抓站轉化 Free-First 規則（`/create` 預設先用 Playwright，非必要不啟用付費服務）
- [x] 建立草稿沙盒原則（抓站結果只落在 `outputs/`，不自動寫入 `templates/`）
- [x] 建立 Promotion 保守機制（僅在使用者明確要求時才晉升公版/元件化）
- [ ] 補一份 `/create` 外部網址自動化驗證清單（抽樣頁面、動態區塊、QWeb 外框、RWD）

---

## 備忘

- Bootstrap 4 響應式間距（`pt-md-5` 等）已列入 SCSS 知識庫，對 Section 內部使用
- 自訂 class 必須搭配 `data-custom-name` 屬性，否則編輯模式存檔後會消失
- 外掛模組（產品分類、特殊頁面）採用「設計師即時提供 HTML → AI 讀取後產出 SCSS」策略，不需要預先存入知識庫
- Skill 同步指令：`python3 scripts/sync_icb_skill.py`（macOS/Linux）或 `py -3 scripts/sync_icb_skill.py`（Windows）
- 已補 `.agent/skills/icb_page_generator/resources/scss_reference.md`：動態新聞/產品 class 對照、箭頭 class 清單與適用範圍、修正 hoverUnderLine 針對部落格卡片標題

---

## 討論共識快照（2026-04-01）

1. **大一統 `/create` 哲學（Odoo 承重牆）**：
   正式廢除 `/clone`。外站網址抓取只是 `/create` 的一種輸入方式。AI 嚴禁 1:1 照抄 DOM，而是必須「借鑑視覺」，將其轉譯為符合 Odoo 承重牆（Bootstrap Grid、QWeb 架構、Dynamic Snippet locked 特性）的全新架構。
2. **AI 防智力退化（Lobotomy）政策**：
   決議「不」將底層指令檔裡的「Odoo 15」全面替換為「ICB」。因為「Odoo 15」是呼叫 LLM 內部龐大 QWeb 與 Bootstrap 4 預訓練知識庫的鑰匙，保留它能確保產出的代碼品質與穩定性。
3. **抓站 Free-First 策略**：
   全面整合 Browser MCP（如 Playwright, Google Chrome DevTools MCP）。當 `/create` 需要解析外站時，強制優先在本地端使用免付費工具，目前無限期擱置 Firecrawl。
4. **SSOT (單一知識來源) 全覆蓋**：
   確立 `icb_skill.source.json` 為唯一大腦。同步腳本 `sync_icb_skill.py` 現已覆蓋 Gemini、Copilot、OpenCode，以及**開局強制讀取的 `CLAUDE.md`**，確保多平台 AI 開發知識 100% 零落差。

---

## 討論共識快照（2026-03-20）

### 目標
- 讓 AI 真正理解 ICB 結構，並同時支援：
  - 自創排版畫面
  - 引用既有公版資源
- 降低知識檢索成本，避免一次讀太多資源造成 token 浪費與準確度下降

### 三層架構方向（先小步落地）
- Layer 1 System（固定、極簡）：放不可違反規則（QWeb 外框、輸出位置、模式規範、動態鎖定規則）
- Layer 2 Retrieval（動態）：由 index 決定最小檢索集合，不再全量掃描 templates/
- Layer 3 Task（每次變）：每次任務產生 task contract（可用資源、禁止操作、輸出格式）

### 目前硬規則（優先）
- Header：不可改 XML，僅允許 SCSS 覆寫（基於同一結構的 4 種樣式）
- Footer：以提供的 2 份模板為基準，輸出完整 XPath XML + SCSS
- Dynamic Products：`templates/base/base-dynamic-products.xml` 為鎖定結構，不可額外添加 inner 結構
- Dynamic News：`templates/base/base-dynamic-news.xml` 為鎖定結構，不可額外添加 inner 結構
- 動態資料的 HTML 結構可作為樣式參考（用於對應渲染後的 class）：
  - `templates/base/base-dynamic-products.html`
  - `templates/base/base-dynamic-news.html`

### 落地順序（先做這三類）
1. Header/Footer schema v1（先把不可做/可做寫清楚）✅
2. Dynamic lock validator（檢查是否誤改 locked 結構）✅
3. 擴充 templates index 欄位，支援 pipeline 最小檢索✅

### 後續待辦（片段規格）
- 填寫 `docs/design/snippet_spec_template.md` 1-2 份範例，作為特殊 snippet 組合與編輯規範的起點
