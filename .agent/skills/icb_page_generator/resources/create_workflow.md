# /create 三階段流程

> `/create` 與 `/create-home` 皆使用三階段流程。首頁版另加 `pageName='homepage'` 與獨立 Footer 輸出。

## Phase 0：內容解析（Brief）

**輸出：** `outputs/<YYYY-MM-DD_HHMM>_brief.json`

**Schema：**

```json
{
  "business": { "type": "", "industry": "", "market": "", "tone": [] },
  "keyAssets": {
    "productCategories": [],
    "trustSignals": [],
    "applications": []
  },
  "mustHaves": [],
  "excluded": [],
  "visualDirection": {
    "palette": "",
    "typography": "",
    "imagery": "",
    "radius": ""
  },
  "designMoves": []
}
```

**停下等使用者確認 brief.json 後才進 Phase A。**

## Phase A：文字骨架

- 每個區塊選擇必須 **引用 brief 欄位** 說明理由
- 不依賴 `home_recipes` 套表
- 列出每個 section 的 Bootstrap Grid 與 Snippet 選擇
- 首頁必備：Hero → 服務亮點 → 產品/案例 → 關於我們 → 最新消息
- **停下等使用者確認**

## Phase B：生成 XML + SCSS

**Phase B 只處理頁面內容區（`<div id="wrap">` 內的 sections），不含 Footer。**

- 可依 section 數量分段思考與分段生成，以降低單次輸出壓力
- 若中途分段，允許逐段 preview 確認後再繼續下一段
- 但 **B1 / B2 / B3 只能是中間產物，不可作為最終交付**
- 收尾時必須將全部 sections 合併成單一 `outputs/<時間>_full.xml` 與 `outputs/<時間>_full.scss`
- 骨架先行、文案後填
- 首頁必加 `<t t-set="pageName" t-value="'homepage'"/>`

## Phase C：Footer 獨立輸出（只 /create-home 需要）

Footer **不是 Phase B 的一段**，是獨立檔案：

- `outputs/<時間>_footer.xml`：用 `<data inherit_id="website.layout" name="..." active="False"><xpath expr="//div[@id='footer']" position="replace">` 包覆
- `outputs/<時間>_footer.scss`：配套樣式
- 一般頁面（/create）**不輸出 Footer**，因為 Odoo 全站共用同一個 Footer，除非明確要求改

## designMoves 規範

`brief.json` 的 `designMoves` 欄位是跳脫制式網格的命名版面手法。

**規格：**
- 3–5 個，具名（例：`asymmetric-split-hero`、`spec-comparison-table`、`index-number-list`、`irregular-mask-grid`、`big-visual-app-swap`、`full-bleed-imagery`）
- 每個 move 要有簡短說明
- Phase A 骨架 **至少採用 2 個 designMoves**
- 對應提出自訂結構：`s_custom_PascalCase` + 內部 div 層次 + 關鍵 SCSS 宣告

**禁止：** 整頁 section 都直接套既有 `s_custom_*` class（等同樣板模式）。

## 抓站轉化規則（/create 提供外部網址）

- 嚴禁直接將草稿寫入 `templates/`，必須放在 `outputs/`
- 必須分離 `.xml` 與 `.scss`（不可寫 `<style id="scss-code">`）
- XML 最外圍必遵守 `<t t-name><t t-call="website.layout">` QWeb 標準層級
- 動態區塊（新聞、產品）必須對接 `s_dynamic_snippet_*`，嚴禁寫死前端假卡片
- 優先呼叫本地 Fetch 或 Browser MCP（Playwright, Chrome DevTools MCP）抓 HTML
