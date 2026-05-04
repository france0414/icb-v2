# /create 外部網址自動化驗證清單

> 目的：當 `/create` 來源是外部網址或抓站草稿時，用一套固定檢查確認輸出可在 Odoo 15 正常編輯、可預覽、可上線。

## 0) 抽樣策略（必做）

- 每次至少抽樣 3 種頁面：
  - Hero + 多 section 長頁（一般品牌頁）
  - 含輪播/卡片密集區塊頁（互動或複雜排版）
  - 含產品或消息需求頁（需判斷是否改用 dynamic snippet）
- 每種至少跑 1 個來源，共 >= 3 筆樣本；若同類型連續 2 次失敗，先修規則再繼續擴樣。

## 1) 轉換與預覽流程

1. 執行轉換（輸入可為資料夾或 HTML）：
   - `python3 tools/stitch_odoo_converter/convert.py --input <path> --output outputs --container-mode auto`
2. 產生可預覽檔（避免 `<odoo><template>` 直接白畫面）：
   - `python3 scripts/auto_convert_preview.py --input <path> --no-open`
3. 檢查輸出是否齊全：
   - `outputs/*.xml`
   - `outputs/*.report.md`
   - `outputs/*.mapping.scss`（若有 position/offset 對應）
   - `preview/<時間>_<名稱>.html`（同時更新 `preview/index.html` 作為最新預覽捷徑）

## 2) QWeb 外框驗證（硬性）

- 頁面 XML 必須符合：
  - `<t t-name="website.xxxxxx">`
  - `<t t-call="website.layout">`
  - `<div id="wrap" class="oe_structure oe_empty">`（或含 oe_structure 的等效包覆）
- 若是首頁，必須存在：
  - `<t t-set="pageName" t-value="'homepage'"/>`
- 任一缺失即判定失敗，不進下一步。

## 3) 結構規則驗證（Section / Container / 命名）

- 每個 `<section>` 內必須明確有 `.container` 或 `.container-fluid`。
- 自訂 section 命名需符合：`s_custom_PascalCase` + `data-custom-name="PascalCase"`。
- Snippet 層需有 `data-snippet` 與 `data-name`。
- 禁止產生 `s_icb_code_*` 這類臨時命名。

## 4) 元素合法性驗證（Odoo 可編輯）

- 按鈕一律 `<a>`，禁止 `<button>`。
- 文字承載不得依賴 `span`（系統可能清除）；改用 `p/div/strong/h*`。
- 禁止在 XML 內新增 `<style>`；樣式應在獨立 `.scss`。
- 若有重疊/絕對定位，SCSS 必須加：
  - `#wrapwrap:not(.odoo-editor-editable)` 保護編輯模式可點選。

## 5) 動態區塊驗證（產品/消息）

- 當需求明確要動態資料時：
  - 產品必須用 `s_dynamic_snippet_products` 系列骨架。
  - 消息/部落格必須用 `s_dynamic_snippet_blog_posts` 系列骨架。
- 不可用純靜態假卡片冒充 dynamic。
- 若需求未要求 dynamic，可保留靜態結構，但需在報告標註「未啟用 dynamic」原因。

## 6) RWD 驗證（Bootstrap 4.5）

- 至少檢查三個 viewport：
  - Desktop：`1366x768`
  - Tablet：`1024x1366`
  - Mobile：`390x844`
- 驗證項目：
  - 無水平捲軸（非設計刻意情境）
  - 主要 CTA 可見可點
  - 標題與段落不重疊、不裁切
  - 圖片比例與卡片內容不崩壞
- SCSS 斷點需使用 Bootstrap mixin（或專案自訂 mixin），禁止硬寫 `@media (max-width: Npx)`。

## 7) 輪播/互動區塊驗證

- 若頁面含 carousel/slider，優先比對 `templates/base/base-Static-Snippet.xml` 結構。
- 檢查控制器（prev/next/indicator）在桌機與手機都可操作。
- 檢查編輯模式下不會因 overlay 擋住可編輯文字或圖片。

## 8) 驗收輸出（每筆樣本）

- `outputs/<timestamp>_<name>.xml`
- `outputs/<timestamp>_<name>.scss`
- `outputs/<timestamp>_<name>.report.md`（差異與風險）
- 若為 1:1 strict：另附差異摘要（無法完全一致處需列出）

## 9) 失敗處理規則

- 同一類型問題連續出現 2 次（例如 container 遺漏、button 殘留、dynamic 誤判），必須先修 converter/規則，再重新抽樣。
- 修正後至少回歸 1 筆舊樣本 + 1 筆新樣本，兩者皆通過才可關閉。
