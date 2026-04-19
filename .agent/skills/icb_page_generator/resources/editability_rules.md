# 自訂結構可編輯性強制規則

> 新建 `s_custom_*` 結構必須保持 Odoo 編輯器可操作。違反任一條都會讓使用者無法在後台修改內容。

## 七條紅線

1. **文字必須在真實 HTML 元素內**
   使用者文字放 `h1~h6 / p / span / li / a`。禁止用 CSS `content: "..."` 承載文字。

2. **圖片必須可替換**
   用 `<img src>` 或 Odoo 行內 `style="background-image:url(...)"`。**禁止**在 SCSS 寫死 `background-image: url(...)`。

3. **偽元素只做裝飾**
   `::before` / `::after` 只能承載裝飾（遮罩、色塊、編號裝飾線），**不可承載使用者會想改的資訊**。

4. **Wrapper 最多兩層**
   `outer + inner` 為上限，不要層層包裹。

5. **Overlay / 絕對定位必加守護**
   overlay、`position: absolute` 一律加 `#wrapwrap:not(.odoo-editor-editable)` 前綴，編輯模式下自動解開重疊。

6. **Pointer-events 不得阻擋**
   自訂 class 不能擋住 pointer-events 到文字 / 圖片層（否則編輯器點不到）。

7. **需拖拉高度或多欄混排用 `s_text`**
   `<div class="s_text" data-snippet="s_text">` 提供 Odoo 原生拖拉高度與多欄混排能力。

## 可點卡片 overlay 專用模式

產品分類、應用/解決方案等「整張可點」卡片：

- 父層加 `position-relative s_custom_clickableCard`
- 既有 `<a>`（按鈕或圖片連結）加 `s_custom_cardLink`
- SCSS：`#wrapwrap:not(.odoo-editor-editable) .s_custom_cardLink::before { inset: 0; position: absolute; }`
- **禁止** `stretched-link`，**禁止**把按鈕改成 `<span>`
