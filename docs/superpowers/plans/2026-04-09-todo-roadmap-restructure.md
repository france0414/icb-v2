# TODO Roadmap Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move long-term roadmap detail out of `TODO.md` into `docs/roadmap/` while keeping `TODO.md` as a lightweight execution entrypoint with links.

**Architecture:** Documentation-only change. Introduce `docs/roadmap/` as the canonical long-term roadmap store with a README index, consolidate all Phase detail into `phases.md`, and move discussion snapshots into `discussion-snapshots.md`. Keep `TODO.md` minimal with Phase summaries and active unchecked items.

**Tech Stack:** Markdown, git

---

## File Structure

- Create: `docs/roadmap/README.md`
- Create: `docs/roadmap/phases.md`
- Create: `docs/roadmap/discussion-snapshots.md`
- Modify: `TODO.md`

---

### Task 1: Create roadmap index

**Files:**
- Create: `docs/roadmap/README.md`

- [ ] **Step 1: Ensure directory exists**

Run:
```bash
mkdir -p docs/roadmap
```
Expected: no output

- [ ] **Step 2: Write `docs/roadmap/README.md`**

```markdown
# Roadmap

This folder stores the long-term roadmap detail and historical discussion for this project.

## Files
- `phases.md`: Full Phase details (completed + in-progress items).
- `discussion-snapshots.md`: Historical discussion snapshots and decisions.

## Editing rules
- Add long-term roadmap items to `phases.md`.
- Keep `TODO.md` short; only near-term active items and links should live there.
```

- [ ] **Step 3: Commit**

```bash
git add docs/roadmap/README.md
git commit -m "docs: add roadmap index"
```

---

### Task 2: Consolidate Phase details

**Files:**
- Create: `docs/roadmap/phases.md`

- [ ] **Step 1: Write `docs/roadmap/phases.md`**

```markdown
# Roadmap Phases

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
- [ ] 實作 `templates/catalogs/templates_index.json` 中介層，對應「結構分析特徵 (Skill)」與「落地模板 (Template)」
- [x] 建立 AI 知識衝突防護指南（`resources/ai_conflict_prevention.md`）：LLM 誤用範例、可控工作流封裝方法、自動 context 修正規則、各模型角色職責矩陣、SKILL SSOT 同步機制

---

## Phase 7：Skill 知識庫與自動化流程 ✅ 已完成

- [x] 建立 `skill_devops_process.md`：Skill 編寫角色分工表、DevOps 自動部署流程圖（純文字）、腳本組織建議、GitHub Actions 配置建議
- [x] 補充 `snippet_rules.md`：新增「Snippet 三大類型」分類表（排版型/基本型/內容型）、`o_colored_level` 正式定義與使用規則、`s_text` 容器說明與使用時機
- [x] 更新 `icb_skill.source.json`：新增 3 條 core_rules（Snippet 三類型 + o_colored_level、s_text、按鈕規範）、新增 knowledge_map 條目、新增 resource_files 條目
- [x] 執行 `sync_icb_skill.py` 同步至 Gemini/Copilot/OpenCode/Claude 所有入口

---

## 備忘

- Bootstrap 4 響應式間距（`pt-md-5` 等）已列入 SCSS 知識庫，對 Section 內部使用
- 自訂 class 必須搭配 `data-custom-name` 屬性，否則編輯模式存檔後會消失
- 外掛模組（產品分類、特殊頁面）採用「設計師即時提供 HTML → AI 讀取後產出 SCSS」策略，不需要預先存入知識庫
- Skill 同步指令：`python3 scripts/sync_icb_skill.py`（macOS/Linux）或 `py -3 scripts/sync_icb_skill.py`（Windows）
- 已補 `.agent/skills/icb_page_generator/resources/scss_reference.md`：動態新聞/產品 class 對照、箭頭 class 清單與適用範圍、修正 hoverUnderLine 針對部落格卡片標題
```

- [ ] **Step 2: Commit**

```bash
git add docs/roadmap/phases.md
git commit -m "docs: move phase details to roadmap"
```

---

### Task 3: Move discussion snapshots

**Files:**
- Create: `docs/roadmap/discussion-snapshots.md`

- [ ] **Step 1: Write `docs/roadmap/discussion-snapshots.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add docs/roadmap/discussion-snapshots.md
git commit -m "docs: move discussion snapshots"
```

---

### Task 4: Slim down TODO entrypoint

**Files:**
- Modify: `TODO.md`

- [ ] **Step 1: Update `TODO.md`**

Replace the file content with:

```markdown
# Odoo AI 知識庫 — 待完成工作

> 給任何帳號的 Gemini：請先讀 `AGENTS.md` 和 `.agent/skills/icb_page_generator/SKILL.md`，
> 再使用這份清單繼續以下的知識庫補充工作。

---

## Roadmap 入口

- 詳細內容請見 `docs/roadmap/README.md`
- Phase 詳情請見 `docs/roadmap/phases.md`
- 討論共識快照請見 `docs/roadmap/discussion-snapshots.md`

---

## Phase 4：系統模板知識庫 ✅ 已完成

- 已完成，詳見 `docs/roadmap/phases.md`

## Phase 5：OpenCode 設定 ✅ 已完成

- 已完成，詳見 `docs/roadmap/phases.md`

## Phase 6：待辦

- [ ] 補一份 `/create` 外部網址自動化驗證清單（抽樣頁面、動態區塊、QWeb 外框、RWD）
- [ ] 實作 `templates/catalogs/templates_index.json` 中介層，對應「結構分析特徵 (Skill)」與「落地模板 (Template)」
- 其餘已完成，詳見 `docs/roadmap/phases.md`

## Phase 7：Skill 知識庫與自動化流程 ✅ 已完成

- 已完成，詳見 `docs/roadmap/phases.md`
```

- [ ] **Step 2: Verify content locations (manual)**

Checklist:
- `TODO.md` only has the two remaining unchecked items plus links.
- All Phase details live in `docs/roadmap/phases.md`.
- All discussion snapshots live in `docs/roadmap/discussion-snapshots.md`.

- [ ] **Step 3: Commit**

```bash
git add TODO.md
git commit -m "docs: slim TODO and link roadmap"
```

---

## Self-Review

Spec coverage:
- All roadmap detail moved into `docs/roadmap/` with stable links in `TODO.md`.

Placeholder scan:
- No TBD/TODO placeholders introduced.

Type consistency:
- File names match across all references.
