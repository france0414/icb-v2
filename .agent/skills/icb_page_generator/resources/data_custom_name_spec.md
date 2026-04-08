---
description: data-custom-name 屬性完整規範（開發者 / AI / 設計師通用）
---

# `data-custom-name` 屬性規範

> **目標讀者：** 開發者、AI（Copilot / Claude / Gemini / OpenCode）、設計師
>
> **一句話摘要：** `data-custom-name` 是 Odoo 編輯器的「自訂 class 記憶機制」——沒有它，存檔後所有 `s_custom_*` class 會被系統清空。

---

## 1. 為什麼需要 `data-custom-name`

Odoo Website Builder 在儲存頁面時，會掃描每個 `<section>` 的 class 清單。  
任何**不在 Odoo 白名單**內的 class，都會被移除。

`data-custom-name` 的值告訴 Odoo：「這些 token 對應的 `s_custom_*` class 是合法的，請保留。」

| 沒有 `data-custom-name` | 有正確的 `data-custom-name` |
|---|---|
| 存檔後 `s_custom_scaleL` 消失 | 存檔後 `s_custom_scaleL` 保留 ✅ |
| 視覺效果失效 | 視覺效果正常 ✅ |

---

## 2. 可以加在哪裡

> [!IMPORTANT]
> **`data-custom-name` 只能加在 `<section>` 元素（Odoo snippet 根節點）上。**

| 元素 | 是否允許 |
|---|---|
| `<section data-snippet="...">` | ✅ 允許（唯一合法位置） |
| `<div>`、`<p>`、`<span>` 等子元素 | ❌ 禁止 |
| 系統頁面（`/shop`、`/blog`、Header、Footer 系統區塊） | ❌ 禁止 |
| 系統 Snippet（非自訂、直接從 Odoo 官方拖入且未加自訂 class） | ❌ 不需要加 |

---

## 3. 命名格式規則

### 3-1. Token 格式

- **格式：** `PascalCase`（大寫開頭，後接駝峰）
- **對應 class：** `s_custom_{Token}`
- **禁止：** Token 內不可含空格、`-`（連字號）、`_`（底線）

| 合法 Token | 對應 class |
|---|---|
| `ScaleL` | `s_custom_ScaleL` |
| `TitleUnderLine` | `s_custom_TitleUnderLine` |
| `FullContainer` | `s_custom_fullContainer` |
| `HeroNavigator` | `s_custom_HeroNavigator` |

> [!NOTE]
> 部分已存在於 `user_custom_rules.scss` 的預設 class（如 `scaleL`、`titleUnderLine`、`fullContainer`）其 Token 習慣以小寫駝峰開頭，遵循既有命名即可，不須強制轉大寫。詳見 [scss_reference.md](./scss_reference.md)。

### 3-2. 多個 Token

多個自訂 class 以**空格分隔**（不用逗號）。

```xml
data-custom-name="ScaleL TitleUnderLine FullContainer"
```

對應 class：
```
s_custom_ScaleL s_custom_TitleUnderLine s_custom_fullContainer
```

---

## 4. 同步規則（class ↔ data-custom-name 必須一致）

每個 `s_custom_*` class 都必須在 `data-custom-name` 中有對應的 Token；反之亦然。

**正確範例：**
```xml
<section
  class="s_text_block o_colored_level pt0 pb0 s_custom_titleUnderLine s_custom_tabEffectTitle"
  data-snippet="s_text_block"
  data-name="Text"
  data-custom-name="titleUnderLine tabEffectTitle">
```

**錯誤範例（class 有但 token 沒有）：**
```xml
<!-- ❌ s_custom_scaleL 在 class 裡，但 data-custom-name 裡沒有 scaleL -->
<section
  class="s_static_snippet o_colored_level s_custom_scaleL"
  data-snippet="s_static_snippet"
  data-name="Static Snippet"
  data-custom-name="">
```

**錯誤範例（token 有但 class 沒有）：**
```xml
<!-- ❌ data-custom-name 多了 scaleL，class 裡卻沒有 s_custom_scaleL -->
<section
  class="s_text_block o_colored_level pt0 pb0"
  data-snippet="s_text_block"
  data-name="Text"
  data-custom-name="scaleL titleUnderLine">
```

---

## 5. 套用流程（AI 與開發者操作步驟）

```
1. 確認此 <section> 是「可編輯自訂區塊」（非系統頁面/系統區塊）
2. 決定要套用哪些視覺效果（參考 scss_reference.md）
3. 在 class 加上對應的 s_custom_* class
4. 在 data-custom-name 填入對應的 Token（空格分隔）
5. 若 user_custom_rules.scss 無對應樣式，在輸出 SCSS 補上
```

---

## 6. 使用情境完整範例

### 6-1. 動態新聞 Snippet（多個效果組合）

```xml
<section
  data-snippet="s_dynamic_snippet"
  class="s_dynamic_snippet s_dynamic o_colored_level s_blog_post_card pt0 pb0
         s_custom_GapM s_custom_cardRadius s_custom_borderHover s_custom_hoverUnderLine"
  data-name="Dynamic Snippet"
  data-filter-id="1"
  data-template-key="website_blog.dynamic_filter_template_blog_post_card"
  data-number-of-elements="4"
  data-number-of-elements-small-devices="1"
  data-number-of-records="4"
  data-custom-name="GapM cardRadius borderHover hoverUnderLine">
  <!-- inner DOM 由 Odoo 動態生成，禁止手寫 -->
</section>
```

### 6-2. 文字區塊（單一效果）

```xml
<section
  class="s_text_block o_colored_level pt0 pb0 s_custom_titleUnderLine"
  data-snippet="s_text_block"
  data-name="Text"
  data-custom-name="titleUnderLine">
  <div class="container">
    <!-- 內容 -->
  </div>
</section>
```

### 6-3. 輪播（箭頭位置 + 縮放效果）

```xml
<section
  data-snippet="s_static_carousel"
  class="s_static_carousel o_colored_level pb0 pt0
         s_custom_arrowTop s_custom_arrowRight s_custom_scaleS"
  data-name="Static Carousel"
  data-custom-name="arrowTop arrowRight scaleS">
  <!-- ... -->
</section>
```

### 6-4. 自訂區塊命名（識別用途）

當一個 Section 是頁面上有語意的獨立區塊（例如首頁英雄區、新聞列表），可用 PascalCase 名稱標記，方便後續 SCSS 精準 Scope：

```xml
<section
  data-snippet="s_vertical_layout"
  class="s_vertical_layout o_colored_level pt80 pb72 s_custom_HeroNavigator"
  data-name="Vertical Layout"
  data-custom-name="HeroNavigator">
  <div class="container">
    <!-- ... -->
  </div>
</section>
```

對應 SCSS：
```scss
.s_custom_HeroNavigator {
  // 針對這個區塊的樣式，完全隔離不影響其他 section
}
```

---

## 7. 絕對禁止清單

| 禁止行為 | 原因 |
|---|---|
| 在 `<div>`、`<p>`、`<span>` 等子元素上加 `data-custom-name` | 只有 `<section>` 是 Odoo snippet 根節點，子元素的此屬性無效且會造成混淆 |
| 在系統區塊（`/shop`、`/blog`、Header、Footer 系統 XPath）上加 `data-custom-name` | 系統區塊由 Odoo 後台管理，強塞會導致樣式衝突或存檔錯誤 |
| `data-custom-name` token 與 class 不同步 | 不同步會導致存檔後 class 消失，視覺效果失效 |
| token 內含空格、`-`、`_` | Odoo 以空格切分 token，`-`/`_` 會使 token 被誤判 |
| 空的 `data-custom-name=""` 搭配 `s_custom_*` class | class 會被存檔清除 |

---

## 8. 快速對照：常用 Token 清單

以下 token 已在 `docs/design/user_custom_rules.scss` 有對應樣式，**可直接使用，無需另寫 SCSS**：

### 動態區塊 / 卡片
| Token | class | 效果 |
|---|---|---|
| `cardRadius` | `s_custom_cardRadius` | 卡片大圓角 (20px) |
| `cardRadiusS` | `s_custom_cardRadiusS` | 卡片小圓角 (10px) |
| `borderHover` | `s_custom_borderHover` | Hover 框線 |
| `scaleL` | `s_custom_scaleL` | Hover 放大 1.05x |
| `scaleS` | `s_custom_scaleS` | Hover 縮小 0.95x |
| `imgNoMargin` | `s_custom_imgNoMargin` | 圖片去 padding |
| `hoverUnderLine` | `s_custom_hoverUnderLine` | 標題 Hover 底線（部落格） |
| `nameHoverUnderLine` | `s_custom_nameHoverUnderLine` | 標題 Hover 底線（產品） |
| `titleLine` | `s_custom_titleLine` | 標題底線（部落格） |
| `blockLine` | `s_custom_blockLine` | List layout 分隔線 |
| `picTop` | `s_custom_picTop` | 圖片置頂 |
| `picBottom` | `s_custom_picBottom` | 圖片置底 |
| `dateTop` | `s_custom_dateTop` | 日期置頂 |
| `GapM` | `s_custom_GapM` | 欄間距 10px |
| `GapS` | `s_custom_GapS` | 欄間距 5px |

### 容器 / 版型
| Token | class | 效果 |
|---|---|---|
| `fullContainer` | `s_custom_fullContainer` | 去容器 padding（滿版） |
| `noGap` | `s_custom_noGap` | 欄間距歸零 |
| `reverse` | `s_custom_reverse` | Row 左右反轉 |
| `RWDscroll` | `s_custom_RWDscroll` | 手機版橫向捲軸 |

### 輪播箭頭
| Token | class | 效果 |
|---|---|---|
| `arrowNoLine` | `s_custom_arrowNoLine` | 無分隔線箭頭 |
| `arrowTop` | `s_custom_arrowTop` | 箭頭置頂 |
| `arrowBottom` | `s_custom_arrowBottom` | 箭頭置底 |
| `arrowLeft` | `s_custom_arrowLeft` | 箭頭靠左 |
| `arrowRight` | `s_custom_arrowRight` | 箭頭靠右 |
| `arrowRadius` | `s_custom_arrowRadius` | 箭頭圓角 |
| `arrowNoSeparate` | `s_custom_arrowNoSeparate` | 箭頭不分開 |
| `arrowNoGap` | `s_custom_arrowNoGap` | 箭頭無間距 |
| `arrowL` | `s_custom_arrowL` | 大尺寸箭頭 |

### 標題裝飾
| Token | class | 效果 |
|---|---|---|
| `titleUnderLine` | `s_custom_titleUnderLine` | 標題左側/置中裝飾底線 |

---

## 9. 相關文件

| 文件 | 內容 |
|---|---|
| `scss_reference.md` | 所有 `s_custom_*` class 詳細說明與 RWD 規範 |
| `dynamic_rules.md` | 動態 Snippet 的 `data-custom-name` 使用規則（Products / Blog） |
| `snippet_rules.md` | Section 命名規則與 Snippet 嵌套規則 |
| `docs/design/user_custom_rules.scss` | 所有已定義的 `s_custom_*` 樣式原始碼 |
