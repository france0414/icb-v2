# AI 生成頁面 1:1 轉換模式（Strict）

適用情境：使用者要求「盡可能一模一樣」重現 AI 生成網站（Stitch、Framer AI、其他 HTML 輸出）。

## 結論先說

- 可以啟用 **Strict 1:1 模式**，大幅提高還原度。
- 但在 Odoo 15 + Bootstrap 4.5 + 可編輯性限制下，無法保證 100% 像素級完全一致。
- 目標是：**視覺 1:1、結構可編輯、後台可維護** 三者平衡。

## 啟用方式（指令）

```text
/create [需求]，啟用 1:1 strict 模式
```

或：

```text
幫我轉換 clientinfo/<project>/code.html，直接做 Final，啟用 1:1 strict
```

## 1:1 strict 規則

1. 先對照來源畫面做區塊映射（Header/Hero/Features/Carousel/About/Footer）
2. 優先保持原版型比例、間距節奏、階層、互動位置
3. 輪播必須對照 `templates/base/base-Static-Snippet.xml` 既有結構
4. 文字容器避免 `span`（系統可能清除），改用 `p/div/strong`
5. 色彩優先對照來源 DESIGN.md / 設計稿 token
6. 圓角、陰影、按鈕尺寸與 icon 位置逐區塊對齊
7. 若與 Odoo 編輯器衝突，優先保留可編輯性（並註記差異）

## 交付內容

- `outputs/<timestamp>_xxx_final.xml`
- `outputs/<timestamp>_xxx_final.scss`
- 差異摘要（最多 10 條）：列出無法 100% 重現的原因與替代方案
