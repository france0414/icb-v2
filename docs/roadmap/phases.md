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
- [x] 補一份 `/create` 外部網址自動化驗證清單（抽樣頁面、動態區塊、QWeb 外框、RWD）
- [x] 實作 `.agent/skills/icb_page_generator/resources/indexes/templates_index.json` 中介層，對應「結構分析特徵 (Skill)」與「落地模板 (Template)」
- [x] 建立 AI 知識衝突防護指南（`.agent/skills/icb_page_generator/resources/ai_conflict_prevention.md`）：LLM 誤用範例、可控工作流封裝方法、自動 context 修正規則、各模型角色職責矩陣、SKILL SSOT 同步機制

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
