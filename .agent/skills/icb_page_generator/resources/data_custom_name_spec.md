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
> [!IMPORTANT]
> 本文件是 `data-custom-name` 屬性的**唯一權威規範**。
> 所有 AI、開發者、設計師在使用此屬性前，必須遵守以下規則。

---

## 1. 為什麼需要 `data-custom-name`？

Odoo 的網頁編輯器在儲存頁面時，會**自動清除**它不認識的 CSS class（即 `s_custom_*` 系列）。
`data-custom-name` 就是告訴 Odoo：「這些自訂 class 是刻意加上去的，請保留它們。」

**結論：沒有 `data-custom-name` 的 `s_custom_*` class，儲存後會消失。**

---

## 2. 只能加在哪裡？（最重要的規則）

### ✅ 允許加在 `<section>` 元素上

`data-custom-name` **只能**加在 `<section>` 元素上，包含：

- 頁面頂層的自訂 `<section>` 區塊
- 作為 Snippet 使用的嵌套 `<section>`（例如 `s_text_block`、`s_embed_code`、`s_vertical_layout` 等帶有 `data-snippet` 屬性的 section）

```xml
<!-- ✅ 正確：加在頂層 <section> 上 -->
<section class="s_text_block o_cc o_cc3 pt64 pb64 s_custom_HeroNavigator"
         data-snippet="s_text_block"
         data-name="Hero Navigator"
         data-custom-name="HeroNavigator">
  <div class="container">
    <!-- 內容 -->
  </div>
</section>

<!-- ✅ 正確：加在作為 Snippet 的嵌套 <section> 上 -->
<section class="s_text_block pt0 pb0 s_custom_boxWrap"
         data-snippet="s_text_block"
         data-name="Text"
         data-custom-name="boxWrap">
  <!-- 內容 -->
</section>

<!-- ✅ 正確：加在動態 Snippet <section> 上 -->
<section class="s_dynamic_snippet_products s_dynamic o_colored_level s_custom_scaleL s_custom_nameHoverUnderLine"
         data-snippet="s_dynamic_snippet_products"
         data-name="Products"
         data-custom-name="scaleL nameHoverUnderLine">
  <!-- 動態內容 -->
</section>
```

### ❌ 禁止加在以下元素上

以下元素**絕對不可以**加 `data-custom-name`：

| 禁止的元素 | 說明 |
|-----------|------|
| `.container` / `.container-fluid` | 容器 div，非 section |
| `.row` | 網格列，非 section |
| `.col-*` | 欄位，非 section |
| 一般 `<div>` | 非 section 元素 |
| `<p>`, `<h1>`~`<h6>` | 文字元素 |
| `<a>`, `<img>`, `<button>` | 行內或互動元素 |
| Odoo 系統原生區塊（沒有 `s_custom_*`） | 見第 3 節 |

```xml
<!-- ❌ 錯誤：加在 .container 上 -->
<div class="container s_custom_myBox" data-custom-name="myBox">
  <!-- 不可以！ -->
</div>

<!-- ❌ 錯誤：加在 .row 上 -->
<div class="row s_custom_myRow" data-custom-name="myRow">
  <!-- 不可以！ -->
</div>

<!-- ❌ 錯誤：加在 <p> 上 -->
<p class="s_custom_myText" data-custom-name="myText">文字</p>
```

---

## 3. 系統頁面與系統區塊禁止使用

以下情況**絕對禁止**加 `data-custom-name` 或 `s_custom_*`：

- Odoo 系統頁面：`/shop`（商品列表）、`/blog`（部落格列表）、`/contactus` 等
- Odoo Header / Navbar 的 XML 結構
- 所有 **非自訂** 的 Odoo 原生 Snippet（即沒有加自訂 class 的情況下）

> **理由：** 系統頁面的 HTML 由 Odoo 後端動態生成，任意加入 class 會被覆蓋，且可能破壞 Odoo 內部邏輯。如需客製這些頁面，請只輸出 SCSS，不要改 XML。

---

## 4. 命名格式

### 單一語意名稱（Section 命名）

用於識別一個自訂區塊的身份，格式為 **PascalCase**：

| 規則 | 說明 | 範例 |
|------|------|------|
| ✅ PascalCase | 每個單字大寫開頭 | `HeroNavigator`, `NewsCards`, `ProductGrid` |
| ❌ 含空格 | 空格是分隔符，不能用在單一名稱內 | ~~`Hero Navigator`~~ |
| ❌ 含連字號 | Odoo 不支援 | ~~`hero-navigator`~~ |
| ❌ 含底線 | Odoo 不支援 | ~~`hero_navigator`~~ |
| ❌ 全小寫 | 建議 PascalCase | ~~`heronavigator`~~ |

### 功能修飾詞（Modifier 快捷詞）

用於套用預設的 `s_custom_*` 功能 class，通常為 **camelCase**（第一個單字小寫）：

| 修飾詞 | 對應 Class | 說明 |
|--------|-----------|------|
| `scaleL` | `s_custom_scaleL` | Hover 放大 1.05 倍 |
| `scaleS` | `s_custom_scaleS` | Hover 縮小 0.95 倍 |
| `cardRadius` | `s_custom_cardRadius` | 卡片大圓角 (20px) |
| `cardRadiusS` | `s_custom_cardRadiusS` | 卡片小圓角 (10px) |
| `nameHoverUnderLine` | `s_custom_nameHoverUnderLine` | 標題 hover 底線 |
| `hoverUnderLine` | `s_custom_hoverUnderLine` | 部落格卡片標題 hover 底線 |
| `borderHover` | `s_custom_borderHover` | Hover 顯示框線 |
| `imgNoMargin` | `s_custom_imgNoMargin` | 圖片無 padding |
| `noRemove` | `s_custom_noRemove` | 編輯模式警示「請勿刪除」|
| `jqCode` | `s_custom_jqCode` | JS 嵌入區塊標識 |

> 完整的修飾詞清單請參閱 `.agent/skills/icb_page_generator/resources/scss_reference.md`

---

## 5. 多個名稱：空格分隔

一個 `<section>` 可以同時有多個自訂名稱或修飾詞，使用**空格**分隔：

```xml
<!-- ✅ 正確：多個名稱空格分隔 -->
<section class="s_dynamic_snippet_products s_dynamic o_colored_level 
                s_custom_scaleL s_custom_nameHoverUnderLine s_custom_arrowRight"
         data-snippet="s_dynamic_snippet_products"
         data-name="Products"
         data-custom-name="scaleL nameHoverUnderLine arrowRight">
  <!-- 動態產品 -->
</section>

<!-- ✅ 正確：語意名稱 + 修飾詞混合 -->
<section class="s_text_block o_cc5 pt64 pb64 
                s_custom_NewsCards s_custom_cardRadius s_custom_borderHover"
         data-snippet="s_text_block"
         data-name="News Cards"
         data-custom-name="NewsCards cardRadius borderHover">
  <!-- 新聞卡片 -->
</section>
```

---

## 6. class 與 `data-custom-name` 必須同步

`class` 屬性中的 `s_custom_[Name]` 與 `data-custom-name` 中的 `[Name]` 必須**完全對應**：

| `data-custom-name` 的值 | 對應的 `class` |
|------------------------|---------------|
| `Foo` | `s_custom_Foo` |
| `Foo Bar` | `s_custom_Foo s_custom_Bar` |
| `scaleL cardRadius` | `s_custom_scaleL s_custom_cardRadius` |

```xml
<!-- ✅ 正確：class 與 data-custom-name 同步 -->
<section class="s_text_block pt48 pb48 s_custom_HeroSection s_custom_scaleL"
         data-snippet="s_text_block"
         data-custom-name="HeroSection scaleL">

<!-- ❌ 錯誤：data-custom-name 漏掉了 scaleL -->
<section class="s_text_block pt48 pb48 s_custom_HeroSection s_custom_scaleL"
         data-snippet="s_text_block"
         data-custom-name="HeroSection">
  <!-- ❌ s_custom_scaleL 儲存後會消失 -->

<!-- ❌ 錯誤：class 用完整前綴，data-custom-name 也不可以 -->
<section class="s_text_block s_custom_Foo"
         data-snippet="s_text_block"
         data-custom-name="s_custom_Foo">
  <!-- ❌ data-custom-name 不可含 s_custom_ 前綴 -->
```

> **規則：`data-custom-name` 只填後綴名稱（不含 `s_custom_` 前綴）**

---

## 7. Snippet 必須同時具備的屬性

當一個 `<section>` 使用了 `data-custom-name`，通常也需要具備以下屬性才能在 Odoo 中正常運作：

| 屬性 | 是否必須 | 說明 |
|------|---------|------|
| `data-snippet` | ✅ 必須 | Snippet 類型識別碼（如 `s_text_block`） |
| `data-name` | ✅ 必須 | 在 Odoo 編輯器側欄顯示的名稱 |
| `data-custom-name` | ✅ 若有 `s_custom_*` | 配合 class 列表同步 |
| `class` | ✅ 必須含對應 `s_custom_*` | 實際套用的樣式 |

```xml
<!-- ✅ 完整正確的自訂 Section 範例 -->
<section class="s_text_block o_cc o_cc2 pt64 pb64 s_custom_FeatureCards s_custom_cardRadius"
         data-snippet="s_text_block"
         data-name="Feature Cards"
         data-custom-name="FeatureCards cardRadius">
  <div class="container">
    <!-- 內容 -->
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
---

## 8. 常見錯誤一覽表

| 錯誤類型 | 錯誤範例 | 正確做法 |
|---------|---------|---------|
| 加在非 section 元素 | `<div data-custom-name="myBox">` | 只加在 `<section>` |
| 包含 `s_custom_` 前綴 | `data-custom-name="s_custom_Foo"` | `data-custom-name="Foo"` |
| class 與屬性不同步 | class 有 `s_custom_Foo`，屬性沒有 `Foo` | 兩者必須完整對應 |
| 加在系統區塊 | 對 `/shop` 的 `.products` 加 `data-custom-name` | 系統頁面只能寫 SCSS |
| 名稱含連字號 | `data-custom-name="my-block"` | `data-custom-name="MyBlock"` |
| 名稱含底線 | `data-custom-name="my_block"` | `data-custom-name="MyBlock"` |
| 值為空字串 | `data-custom-name=""` | 沒有自訂 class 時不需要此屬性；有的話必須填值 |

---

## 9. 快速參考：正確的完整 XML 結構

### 靜態自訂 Section

```xml
<section class="s_text_block o_cc o_cc3 pt80 pb80 s_custom_AboutSection"
         data-snippet="s_text_block"
         data-name="About Section"
         data-custom-name="AboutSection">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-6">
        <h2>標題</h2>
        <p>內文</p>
      </div>
      <div class="col-lg-6">
        <img class="img-fluid" src="https://picsum.photos/800/600" alt=""/>
      </div>
    </div>
  </div>
</section>
```

### 動態產品 Section（含修飾詞）

```xml
<section
  class="s_dynamic_snippet_products s_dynamic o_colored_level s_product_product_borderless_1
         s_custom_scaleL s_custom_nameHoverUnderLine s_custom_cardRadius"
  data-snippet="s_dynamic_snippet_products"
  data-name="Products"
  data-filter-id="3"
  data-template-key="website_sale.dynamic_filter_template_product_product_borderless_1"
  data-product-category-id="all"
  data-number-of-elements="4"
  data-number-of-elements-small-devices="1"
  data-number-of-records="16"
  data-custom-name="scaleL nameHoverUnderLine cardRadius">
  <div class="o_not_editable container">
    <div class="css_non_editable_mode_hidden">
      <div class="missing_option_warning alert alert-info rounded-0 fade show d-none d-print-none o_default_snippet_text"></div>
    </div>
    <div class="dynamic_snippet_template"></div>
  </div>
</section>
```

### JS 嵌入區塊（必備 `noRemove`）

```xml
<section class="s_embed_code o_colored_level pt16 pb16 s_custom_jqCode s_custom_noRemove"
         data-snippet="s_embed_code"
         data-name="Embed Code"
         data-custom-name="jqCode noRemove">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      // JavaScript 代碼
    </script>
  </div>
</section>
```

---

## 10. 相關文件

| 文件 | 說明 |
|------|------|
| `resources/scss_reference.md` | 所有可用 `s_custom_*` class 清單與效果說明 |
| `resources/dynamic_rules.md` | 動態 Snippet 的自訂 class 可用清單 |
| `resources/component_library.md` | 互動元件的 `data-custom-name` 使用範例 |
| `resources/snippet_rules.md` | Snippet 嵌套規則與 Section 命名規則 |
| `docs/design/user_custom_rules.scss` | 實際 `s_custom_*` 樣式定義來源 |
