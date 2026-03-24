# Odoo 14 版面設計模式 (Layout Patterns)

> 此文件提供常見設計模式的組合策略，幫助 AI 選擇最佳 Snippet 組合。

---

## 設計策略

### A. 層級原則 (Hierarchy Principle)

| 位置 | 推薦 Snippet | 背景色 |
|------|-------------|--------|
| **Hero** | `s_banner` / `s_cover` / `s_carousel` | `o_cc1`~`o_cc5` 依需求 |
| **介紹** | `s_column_layout`（左標題/右描述） | `o_cc1` |
| **特色** | `s_three_columns` / `s_features_grid` + `s_custom_scaleL` | `o_cc2` |
| **社會證明** | `s_references` / `s_quotes_carousel` | `o_cc1` |
| **收尾 CTA** | `s_call_to_action` | `o_cc3` |

### B. 色彩節奏 (Color Rhythm)

交替背景色創造視覺節奏：
```
o_cc1 (白) → o_cc2 (灰) → o_cc1 (白) → o_cc3 (主色) → o_cc1 (白) → o_cc5 (深)
```

### C. 經典組合模式

| 模式 | Snippet 組合 |
|------|-------------|
| **現代列表** | `s_static_snippet` + `s_blog_post_card` + `s_custom_GapM` + `s_custom_scaleL` |
| **產品展示** | `s_static_carousel` + `s_product_product_centered` + `s_custom_nameHoverUnderLine` |
| **水平特色** | `s_static_snippet` + `s_product_product_horizontal` + `s_custom_reverse`（交替行） |
| **上下交疊** | `s_column_layout` + `s_custom_upperNext` + 下一個 section 自動上移 |

---

## 佈局模式範例

### 1. 垂直排版 (Vertical Layout)
**用途：** 單欄，適合 Hero 或一般文字區
```xml
<section data-snippet="s_vertical_layout" class="s_vertical_layout pt32 pb32 o_colored_level" data-name="Vertical Layout">
    <div class="container-fluid">
        <div class="oe_structure oe_structure_not_nest oe_empty">
            <!-- 拖入子 snippet -->
        </div>
    </div>
</section>
```

### 2. 水平排版 + Sticky (Column Layout)
**用途：** 左右兩欄，左側黏著
```xml
<section class="s_column_layout o_auto_screen_height o_colored_level" data-sticky="used" data-snippet="s_column_layout" data-name="Horizontal Layout">
    <div class="col-wrapper container">
        <div class="row d-flex align-items-stretch">
            <div class="col-lg-4 s_col_no_bgcolor col-left">
                <div class="s_column_layout_content oe_structure oe_structure_not_nest oe_empty col-sticky">
                    <!-- 左側：標題區（可黏著） -->
                </div>
            </div>
            <div class="col-lg-8 col-right o_colored_level">
                <div class="s_column_layout_content oe_structure oe_structure_not_nest oe_empty">
                    <!-- 右側：主要內容 -->
                </div>
            </div>
        </div>
    </div>
</section>
```

### 3. 收合排版 (Collapse Layout)
**用途：** 可展開/收合的內容
```xml
<section class="s_collapse_layout pt32 pb32 o_colored_level" data-preview-height="200px" data-snippet="s_collapse_layout" data-name="Collapse Layout">
    <div class="container-fluid">
        <div class="s_collapse_height_wrap" style="height: 200px;" id="myUniqueCollapseID">
            <div class="s_collapse_content_wrap">
                <div class="s_collapse_content oe_structure oe_structure_not_nest oe_empty">
                     <!-- 隱藏內容 -->
                </div>
            </div>
            <div class="s_collapse_btn_wrap justify-content-center d-flex w-100 pt24 pb24">
                <div class="s_collapse_btn" data-content-wrap="myUniqueCollapseID">
                    <div class="btn btn-primary o_not-animable s_collapse_btn_expand">
                        <span class="o_default_snippet_text">More</span>
                    </div>
                    <div class="btn btn-primary o_not-animable s_collapse_btn_reduce">
                        <span class="o_default_snippet_text">Close</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
```

### 2. s_color_blocks_2 (盒狀)
Odoo 原生提供的色塊堆疊 snippet，結構比 Masonry 正常。
- 特性：`row` 搭配 `col` 排列，不會有複雜的負 span 問題。
- 編輯：客戶可直覺點擊更換各色塊背景 `o_cc`。

---

## 🛑 特殊避坑指南：Masonry Block (磚狀瀑布流) 的替代方案

> [!WARNING]
> **Odoo 原生的 `s_masonry_block` 是一個極易破版的結構地雷！**
> 它過度依賴寫死的 `.row` 負 margin、Bootstrap padding 清零，以及硬撐容器高度的方式。在手機版（內容變多時）極易發生文字溢出或破版！

**【AI 生成 Masonry / 拼貼佈局的鐵律】**
當設計師要求「磚塊排版 / 瀑布流 / 左一右四格」等佈局時，AI **禁止** 盲目吐出 Odoo 原生那一長串套娃的 `s_masonry_block` 代碼！

**必須改用「現代 CSS Grid」架構，但【必須 100% 保留客戶編輯權限】！**

### 實作步驟：

1. **結構外殼依然符合 Odoo 規範：**
   使用 `<section class="s_custom_smart_grid o_colored_level">`。
2. **遵守全域邊距：**
   內層必須有 `<div class="container-fluid">` 或 `<div class="container">` 負責承受 `--container-pd-x`。
3. **保留「可編輯圖文」的 Class (最重要！)：**
   - 文字：必須帶有 `o_default_snippet_text`
   - 背景圖：必須使用包含 `oe_img_bg o_bg_img_center o_colored_level` 以及 `style="background-image: ..."` 的標準格式。
   - 背景色：支援 `o_cc o_cc1` 等系列。
4. **CSS 邏輯 (Grid + Flex)：**
   在 SCSS 裡面用 `display: grid` 取代 `.col` 系統。對於文字方塊，使用 `display: flex; flex-direction: column; justify-content: center;` 讓高度自由伸展。

**架構示意：**
```xml
<section class="s_custom_smart_grid o_colored_level pt32 pb32" data-snippet="s_custom_smart_grid" data-name="Smart Grid">
  <div class="container-fluid">
    <div class="modern-grid-wrapper">
      
      <!-- 區塊1: 滿版圖片 (客戶可換圖) -->
      <div class="grid-cell img-cell oe_img_bg o_bg_img_center o_colored_level" style="background-image: url('...');">
        <p><br/></p> <!-- 佔位符，讓圖片可視 -->
      </div>
      
      <!-- 區塊2: 文字區塊 (客戶可編輯文字與背景色) -->
      <div class="grid-cell text-cell o_cc o_cc2 o_colored_level p-4 p-md-5">
        <h3 class="o_default_snippet_text">編輯這段標題</h3>
        <p class="o_default_snippet_text">客戶可以在這裡自由換行打字，高度會自適應，不會破版！</p>
      </div>
      
    </div>
  </div>
</section>
```
這樣既解決了 RWD 破版問題，又達成了 Odoo 最核心的教條：「最終客戶必須能自己看圖說故事、拖拉修改內容」！

---

## 嵌入 JS 區塊的標準結構

```xml
<section class="s_embed_code o_colored_level s_custom_jqCode s_custom_noRemove" 
         data-snippet="s_embed_code" 
         data-name="Embed Code" 
         data-custom-name="jqCode noRemove">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      // JavaScript code here
    </script>
  </div>
</section>
```

**規則：**
1. **必須加** `s_custom_noRemove` 防止被刪除
2. **必須更新** `data-custom-name` 包含 `noRemove`
3. **不加**可見文字，SCSS 會透過 `::before` 在編輯模式顯示「重要 Code，請勿刪除」
