# 設計師操作手冊（ICB Odoo 15 專案）

這份文件給設計師快速上手：在本專案中，如何用 AI 指令生成可貼進 Odoo 的頁面 XML + SCSS。

## 1) 先知道三個資料夾

- `clientinfo/`：客戶素材（文字、圖片、PPT、Excel）
- `templates/`：靈感與積木庫（參考用，不是直接成品庫）
- `outputs/`：AI 產出檔（XML、SCSS、brief 等）

## 2) 指令怎麼選

### A. 套版模式（快）

- `/page [需求]`：一般頁快速套版
- `/page-home [1-4] [需求]`：首頁配方套版（自動含 `pageName='homepage'`）

適合：需求明確、趕時間、先求可用版。

### B. 創作模式（設計）

- `/create [需求]`：內頁創作（原三階段流程）
- `/create-home [需求]`：首頁創作（含 `pageName` + Footer 獨立輸出）

適合：需要重新設計區塊順序、視覺重心、品牌節奏。

### C. 內頁對稿模式（可選）

- `/create [需求]，先做 Layout-first（灰色色塊占位）`

說明：
- 這是 **可選模式**，不是預設強制。
- 會先做版型骨架（灰色色塊、不放彩圖），給客戶先看排版。
- 確認後再做 Final（套入客戶圖片與文案）。

## 3) 設計流程（建議）

### 首頁流程

1. `/create-home ...` 產生 brief
2. 看 Phase A 骨架（先確認區塊順序與資訊層級）
3. 進 Phase B 分段生成與逐段確認，但最終合併輸出 single full 檔
4. 產出 Footer 獨立檔

首頁常用排序（可調整）：

- Hero
- 服務亮點 / 主要特色
- 產品/案例
- 解決方案 / 產業應用
- 關於我們
- Blog
- 全站共用 CTA（Pre-Footer）+ Footer

### 內頁流程

1. `/create ...`（一般流程）或 `/create ...，先做 Layout-first`
2. 確認骨架與間距
3. 套入客戶素材
4. 輸出 XML + SCSS

## 4) 產品 / Blog 區塊規則

- 若你**沒有明確要求 dynamic**：預設用一般靜態 `section + row/col`（sheet 方式）
- 只有你明確說要動態資料時，才使用 `s_dynamic_snippet*`

## 5) Hero 重要規則

- 內層用 Bootstrap Grid，欄寬總和一定是 `12`
- 可用比例：`3:9`、`4:8`、`5:7`、`6:6`（依視覺需求調整）
- 同一組輪播需維持一致高度策略（避免 CLS 跳動）
- 小螢幕看不到的裝飾元素可以直接隱藏，不要硬撐

## 6) 必守硬規則（避免返工）

- 禁用 git worktree（不要建立 `.worktrees/`）
- 所有頁面 XML 必須有 QWeb 外框（`<t t-name>` + `website.layout` + `#wrap`）
- 新樣式寫在 SCSS，不在 XML 寫 `<style>`
- 字級用 `var(--h1)~var(--h6)`，不要硬寫 clamp/rem/px
- 檔案輸出一律放 `outputs/`，檔名需含日期時間

## 7) 常用指令範例

```bash
# 首頁創作（正式）
/create-home B2B 工業品牌首頁，主打交期與客製能力

# 內頁創作（正式）
/create 解決方案內頁：半導體產線應用

# 內頁先對稿（灰色色塊）
/create 產品總覽頁，先做 Layout-first（灰色色塊占位）

# 首頁套版（快速）
/page-home 2 高階工業感
```

## 8) 交付前檢查清單

- 結構：section / row / col 是否合理、欄寬總和是否正確
- 間距：pt/pb 節奏是否一致
- 可編輯性：文字可改、圖片可換、按鈕可點
- 響應式：手機版無內容遮擋、無關鍵資訊消失
- 輸出：XML + SCSS 是否都在 `outputs/`

---

若你不確定該用 `/page` 還是 `/create`，先用這個判斷：

- 只要想「快速套版」→ `/page`
- 只要想「重新設計」→ `/create`
