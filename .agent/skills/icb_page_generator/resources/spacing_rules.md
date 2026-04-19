# 區塊間距規則（Odoo 15）

> 直接套表、不需每次重新決定。`pt{px}` / `pb{px}` 格式，px 為 8 的倍數、**無 dash**。禁止 Bootstrap `pt-4` / `pt-5` 寫法。

## 1. Section 外層預設配方

設計師未特別指定時直接套：

| 類型 | 間距 |
|---|---|
| Hero / 首屏 / CTA 滿版主視覺 | `pt96 pb96` |
| 一般 section（產品、特色、應用、介紹） | `pt80 pb80` |
| 次要 section（stats、strengths、pre-footer、小型 CTA） | `pt64 pb64` |
| 緊湊型（breadcrumb、標題引導、細長 banner） | `pt48 pb48` |
| Footer 主體 | `pt96 pb48`（上寬下收） |
| 手機 RWD | SCSS 內 `@include media-breakpoint-down(md) { padding: 48px !important; }` |

## 2. 內層 col 預設 `pt0 pb0`

- col 的上下 padding 一律由 section 外層負責。
- `<div class="col-*">` **不自行加** pt/pb，避免雙重堆疊造成節奏亂。

## 3. 真正用內距的元素

- 卡片 body / 文字 wrap / list item / 按鈕群組
- 用 `pt8 / pt16 / pt24 / pt32` 搭 `pb8 ~ pb32`
- `h2` 與內文之間建議 `pb16`
- 段落群組 `pt24 pb24`

## 4. col 例外加 pt/pb 的情況

僅下列情況才允許，且 **XML 註解必須寫理由**：

- (a) 雙欄版面某一欄視覺下沉/上浮的錯位效果
- (b) col 內含 image 需與旁欄對齊
- (c) 小型 card-like col 需獨立呼吸感

## 5. 偏離預設配方的情況

僅下列情況才允許，且 **XML 註解必須寫理由**（例：`<!-- pt128: 品牌 hero 需呼吸感 -->`）：

- (a) 使用者 / brief.json 明確指定距離
- (b) 相鄰兩區背景色相同需視覺分隔，上移一級
- (c) 特殊 storytelling 要求 `pt128 pb128`
