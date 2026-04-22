# AI Build Conversion Notes (2026-04-22)

來源：本次與使用者逐步對稿的補充規則，供後續自動化腳本與人工校對使用。

## 1) 結構與 Snippet

- 當同一視覺區塊需拆成兩個獨立 section 時，外層用 `s_vertical_layout` 包組。
- `Category Expertise` 類輪播區塊：使用 `s_static_carousel` 標準骨架，不用簡化自組輪播。
- 輪播控制元件使用獨立 `carousel-control-prev/next` 錨點結構，且 `data-target` 對應唯一 ID。
- 動態資料區塊中間不可插入破壞結構的中介層。

## 2) Class 命名範圍

- `s_custom_*` 主要用於 section/snippet 層。
- section 內部元素 class 優先使用一般語義命名（不要滿場 `s_custom_*`）。
- 內層樣式用 section scope 控制（例如 `.s_custom_Code04 .categoryRow { ... }`）。

## 3) Section 間距與容器

- section 本身不可加 `px-*`。
- section 之間的距離要保留（可用 `pt/pb`，且採 8 的倍數）。
- 內容寬度由 `container` / `container-fluid` 承擔。

## 4) SEO 與文字標籤

- 同一區塊內避免標題跳級（例如 `h2` 下面不要直接 `h4/h5`）。
- 若需要較大視覺字級，改用 `p.h*`。
- `text-xs` 類型優先轉 `<small>`。
- `span` 在 Odoo 可能被清掉，需改為可存活標籤（`p` / `small` / `strong` 等）。

## 5) Tailwind 對應補充

- `w-full` -> `w-100`
- `h-full` -> `h-100`
- `lg:flex-row` -> `flex-lg-row`
- `order-1 lg:order-2` -> `order-1 order-lg-2`（反向同理）
- `max-w-[200px]` -> `max-width: 200px`（SCSS）

## 6) Tailwind Config 特例

- `fontFamily` 忽略（交由系統主題控制）。
- `borderRadius.full` 若設定為 `0.75rem`，則 `rounded-full` 不可盲轉圓形（應對應該值）。

## 7) 輪播與既有全域樣式

- 若已存在全域箭頭規則（例如 `.s_carousel a[class*='carousel-control'] > .fa`），優先靠 class 套用，不重寫局部樣式。
- 已有可用 class（如 `s_custom_imgNoPadding`, `s_custom_scaleL`）優先沿用。

## 8) 視覺一致性補充

- Technical Capabilities 與 Category 卡片的內距、邊界距離、圓角語意要一致。
- 卡片外層與圖片內層圓角需分層處理（外層 rounded-2xl、內層 rounded-xl）。

## 9) RWD 補強方向

- 固定高度/寬度（`h-*`, `w-*`）需逐步降級為斷點策略。
- 浮動絕對定位元素需在小尺寸降級，避免遮擋內容。
