# 討論共識快照

## 討論共識快照（2026-04-08）

1. **AI 知識衝突防護（`ai_conflict_prevention.md`）**：
   建立了三大支柱文件，確保所有 AI 模型（Copilot、Claude、Gemini、OpenCode）在進入本專案後能自動對齊本地規格：
   - **誤用防護清單**：8 類主流 LLM 常見錯誤（Bootstrap 5 語法、`<button>` 元素、SCSS 通靈發明等）+ 本專案正確做法對照表。
   - **可控工作流封裝**：強制決策流程樹、Task Contract 七項確認清單、三層防護架構（System → Retrieval → Task）。
   - **自動 Context 修正**：七個雷達偵測指標（自我修正觸發點）+ 衝突優先序（本專案規格 > Odoo 15 > Bootstrap 4.5 > LLM 通用知識）。
   - **角色職責矩陣**：Copilot、Claude、Gemini、OpenCode 各自的「能做 / 不做」定義，以及所有 AI 共同職責（開局讀取、知識庫查詢、輸出隔離、同步規則）。
   - **SKILL SSOT 同步機制**：已透過 `sources/skill/icb_skill.source.json` + `scripts/sync_icb_skill.py` 自動發布到所有模型入口。

---

## 討論共識快照（2026-04-02）

1. **中介層 (Mediator) 策略**：
   確認將 `templates_index.json` 作為 Skill (意圖分析) 與 Template (落地骨架) 之間的橋樑。
   - **Skill (大腦)**：負責提取需求的「結構特徵」（例如：`has_carousel: true`, `column_count: 3`）。
   - **Mediator (中介層)**：負責將這些特徵硬性對應到最合適的模板路徑（SSOT 映射）。
   - **目的**：解決「AI 知道怎麼分析需求，卻不知道該對上哪個模板」的斷層，確保 `/create` 的精準度與結構標準化。

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
