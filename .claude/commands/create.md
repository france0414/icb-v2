# create (創作模式)

設計新版面。三階段流程：Phase 0 內容解析 → Phase A 文字骨架 → Phase B 分段生成。輸入可為純文字或外部網址。

## Steps

0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. **Terse prompt 偵測（experimental）**：輸入少於 20 字或僅有抽象形容詞（「歐美簡約」「工業風」）而無具體指示時，優先呼叫 `design-director` 子代理反問 3 題並擴寫 brief；若環境不支援 subagent，改由主流程直接反問同一組 3 題後再產 brief。具體輸入則跳過此步。
2. 讀 `.agent/skills/icb_page_generator/SKILL.md`
3. **Phase 0 — 內容解析（中介層）**：若 Step 1 已產 brief 則跳過；否則解析輸入抽出 business/keyAssets/mustHaves/excluded/visualDirection，輸出 `outputs/<日期時間>_brief.json`，停下等使用者確認
4. **Phase A — 文字骨架 / Layout HTML**：從 brief 推導版面（不再套 home_recipes），每個區塊選擇必須引用 brief 欄位理由；列出 Bootstrap Grid 對應與 Snippet 類型。若使用者表示骨架想直接看版型，應優先提供 layout-only HTML；停下等確認
5. **Phase B — 分段生成 XML + SCSS**：拆 2–3 段，每段寫完立即 preview 確認再下一段；骨架先行、文案後填
6. 產品/Blog 區塊預設可先用靜態 sheet + row/col；僅在明確要求動態資料時才對接 `s_dynamic_snippet*`
7. 每個 section 必須明確使用 pt-*/pb-* 間距 utility；標題字級用 var(--h1)~var(--h6)，禁止硬編 clamp/rem
8. 嚴禁覆蓋既有 `templates/`，產出統一存放 `outputs/`

## brief.json 格式

```json
{
  "business": { "type": "", "industry": "", "market": "", "tone": [] },
  "keyAssets": { "productCategories": [], "trustSignals": [], "applications": [] },
  "mustHaves": [],
  "excluded": [],
  "visualDirection": { "palette": "", "typography": "", "imagery": "" }
}
```
