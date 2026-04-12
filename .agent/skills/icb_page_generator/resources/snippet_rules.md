# Odoo 14 Snippet 完整清單與嵌套規則

> [!IMPORTANT]
> 此文件為所有 Snippet 的分類索引。AI 產出代碼時必須從此清單中選擇 Snippet，不可自行發明。

> [!CAUTION]
> **以下 Snippet 的內部結構有多種 template 變體，AI 禁止自行猜測結構！**
> - `s_static_carousel` — 內含 `static_snippet_template` + 多種卡片模板（如 `s_product_product_borderless_1`）
> - `s_static_snippet` — 同上，但無輪播
> - `s_blog_posts` — 內含多種模板（如 `s_blog_post_big_picture`）
> - `s_dynamic_snippet_products` / `s_dynamic_snippet_carousel` — 動態版本
>
> 這些 Snippet 的骨架使用 Odoo 專用 class（如 `o_carousel_product_card`、`o_carousel_product_img_link`），
> **與 Bootstrap 的 card 結構完全不同**。
> 生成前**先查 `resources/indexes/templates_index.json` 取得對應 XML 路徑**，再讀取該模板的必要片段；不可自行編寫骨架。

---

## 快速目錄

- [Snippet 三大類型](#snippet-types)
- [o_colored_level 說明](#o-colored-level)
- [s_text 內容容器說明](#s-text)
- [嵌套規則 (Nesting Hierarchy)](#nesting-hierarchy)
- [1. 基本 (Structure)](#structure)
- [2. 排版元件 (Layout)](#layout)
- [3. 動態內容 (Dynamic)](#dynamic)
- [4. 靜態模板 (Static)](#static)
- [5. 插入內容 (Inner Content)](#inner-content)
- [6. 全域工具 Class (Utility Classes)](#utility-classes)
- [Backgrounds (背景圖片與影片)](#backgrounds)

---

## Snippet 三大類型

<a id="snippet-types"></a>

Odoo 的 Snippet 依用途分為三種類型，AI 生成時必須先辨別類型，再決定結構：

| 類型 | 說明 | 是否自帶 `<section>` | 是否含 `o_colored_level` | 使用方式 |
|------|------|---------------------|--------------------------|---------|
| **排版型 (Layout)** | 頁面主要骨架區塊，可獨立存在 | ✅ 必有 | ✅ 通常有 | 獨立使用，作為頁面大區塊 |
| **基本型 (Structure/Base)** | 可獨立的標準內容區塊（如 Text Block、Banner、Card 列） | ✅ 通常有 | ✅ 通常有 | 獨立使用，作為頁面主要段落 |
| **內容型 (Inner Content)** | 小型元件，插入已存在的 section/col 內部使用 | ❌ 多數無 | ❌ 通常無 | 必須放在排版型或基本型 Snippet 內部 |

### 判斷口訣

```
有 section + 有 o_colored_level → 排版型或基本型 → 可獨立使用
無 section 或 無 o_colored_level → 內容型 → 必須放在父容器內
```

> **注意**：少數例外（有 `<section>` 但仍需依附父層），以 Odoo 編輯器實際行為為準。

---

## `o_colored_level` 說明

<a id="o-colored-level"></a>

### 定義與用途

`o_colored_level` 是 Odoo 的**主題色階標記 class**。凡加上此 class 的元素，Odoo 後台 UI 都可以讓使用者點擊切換主題配色（`o_cc1`~`o_cc5`）。

| 功能 | 說明 |
|------|------|
| 主題色切換 | 加上此 class 後，使用者可在編輯器中點選切換 `o_cc1`~`o_cc5` 背景色 |
| 識別獨立可著色區塊 | 代表此區塊是設計上「可獨立換膚」的單元 |
| 繼承色階 | 子元素可繼承父層 `o_colored_level` 的色彩系統 |

### 使用規則

```
✅ 適合加 o_colored_level 的位置：
   - 主要 section（頁面大區塊）
   - row（需要整行換色時）
   - col（需要單欄換色時）
   - card / 卡片容器（需要個別卡片換色時）

❌ 不需要加 o_colored_level 的位置：
   - 純排版用的 div（如 .container、.row 作為結構用時）
   - 固定白底/透明且不需要色彩切換的小型元件
   - 純文字段落（直接繼承父層即可）
```

### 範例

```xml
<!-- 主區塊：頁面段落，加 o_colored_level 讓使用者可切換背景色 -->
<section class="s_features o_colored_level pt32 pb32" data-snippet="s_features" data-name="Features">
    <div class="container">
        <div class="row o_colored_level">
            <!-- 子欄位也加 o_colored_level，支援欄位獨立換色 -->
            <div class="col-md-4 o_colored_level">
                <p>特色 A</p>
            </div>
            <div class="col-md-4 o_colored_level">
                <p>特色 B</p>
            </div>
        </div>
    </div>
</section>

<!-- 內容型插入區塊：不加 o_colored_level，繼承父層即可 -->
<div class="s_hr" data-snippet="s_hr">
    <hr/>
</div>
```

### `o_colored_level` 與 section 的關係

- **有 `o_colored_level` → 通常是排版型或基本型 Snippet → 主要區塊**
- **無 `o_colored_level` → 通常是內容型 Snippet → 插入型小元件**
- 參考：`templates/base/base-Static-Snippet.xml` 可看到 section、row、col、card 各層都帶 `o_colored_level`

---

## `s_text` 內容容器說明

<a id="s-text"></a>

### 定義與用途

`div.s_text`（`data-snippet="s_text"` / `data-name="Text"`）是 Odoo 的**標準文字容器 snippet**，具有以下特性：

- 在 Odoo 編輯器中，使用者可以**直接拖拉調整高度**
- 支援在內部放置 Bootstrap `.row` / `.col-*` 進行多欄排版
- 常作為「在已有 row/col 骨架內，再插入更多可調整內容」的解決方案

### 使用時機

```
✅ 適合使用 s_text 的情況：
   - 在現有 row/col 骨架內，需要「高度可調整的內容塊」
   - 在 Accordion（收折面板）等限制排版的容器內，需要自由插入圖文
   - 需要讓設計師可拖拉調整版面高度
   - 在 col 內需要再切分更細緻的結構

❌ 不適合使用 s_text 的情況：
   - 取代主 section 骨架（s_text 不是頁面主區塊）
   - 在已有充足排版控制的結構中再多加一層（避免過度嵌套）
```

### 基本結構

```xml
<div class="s_text" data-snippet="s_text" data-name="Text">
    <!-- 內部可放任何 Bootstrap 排版結構 -->
    <p>一般文字內容</p>
</div>
```

### 進階用法：在 col 內插入多欄排版

```xml
<!-- 在 row/col 內部，若需要更細緻的結構控制，用 s_text 包住 -->
<div class="row">
    <div class="col-md-8">
        <div class="s_text" data-snippet="s_text" data-name="Text">
            <!-- 在 s_text 內可再用 row/col 進行子排版 -->
            <div class="row">
                <div class="col-6">
                    <img src="https://picsum.photos/400/300" class="img-fluid" alt=""/>
                </div>
                <div class="col-6">
                    <h3>子標題</h3>
                    <p>說明文字，使用者可在編輯器拖拉調整高度</p>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="s_text" data-snippet="s_text" data-name="Text">
            <p>側欄內容</p>
        </div>
    </div>
</div>
```

### 在 Accordion 內實現圖文排版（特殊用法）

```xml
<!-- Accordion 的 card-body 預設只適合純文字。
     加上 s_text 後，內部就可以自由使用 row/col 做多欄圖文混排。 -->
<div class="collapse" id="collapseExample">
    <div class="card-body">
        <div class="s_text" data-snippet="s_text" data-name="Text">
            <div class="row">
                <div class="col-lg-4">
                    <img src="https://picsum.photos/400/300" class="img-fluid" alt=""/>
                </div>
                <div class="col-lg-8">
                    <p>在 Accordion 內實現圖文混排！</p>
                </div>
            </div>
        </div>
    </div>
</div>
```

---

## 嵌套規則 (Nesting Hierarchy)

<a id="nesting-hierarchy"></a>

```
section [data-snippet="xxx"]          ← 頂層 Snippet（排版型/基本型）
 └── .container / .container-fluid    ← 容器
      └── .row                        ← 列
           └── .col-lg-*              ← 欄
                └── div.s_text        ← 可選：靈活高度文字容器
                     └── Content      ← 最終內容
```

### 區塊層級判斷（獨立區塊 vs 內嵌內容）

- **排版型/基本型 Snippet**：通常有 `<section data-snippet="...">` + `o_colored_level`，可獨立成區塊，內部可再放內容。
- **內容型 Snippet**：多數沒有 `<section>` 外殼，只能插入到可獨立區塊內（如容器/欄位）。通常不含 `o_colored_level`。
- **例外**：少數有 `<section>` 的 snippet 仍被系統視為「不可獨立」，必須依附在可獨立區塊內。

**原則**：是否可獨立，最終以 Odoo 編輯器行為與官方 snippet 規則為準。

### Layout 容器（用來包住 section）

以下為 **Layout 層級** 的容器，用來承接/包住一般 `section.o_colored_level` 的內容：

- `s_vertical_layout`
  - `container`/`container-fluid` 內含 `oe_structure`（可插入多個 section）
- `s_column_layout`
  - 左右欄位各自含 `oe_structure`，用來承接內部 section
- `s_collapse_layout`
  - 可收合的大範圍容器，內含 `s_collapse_content` 的 `oe_structure` 用於承接多個 section

**補充：**
- `s_collapse_layout` 是「版面容器」(layout)
- `s_collapse` 是「內容型」收合區塊（通常放在可編輯容器內）

**重點：** 一般 `section.o_colored_level` 多為平行存在，若需要「包住多個 section」或「欄位內再放 section」，請使用上述 Layout 容器。

### 可編輯性控制 Class

| Class | 作用 |
|-------|------|
| `oe_structure` | 開啟拖放區，允許拖入 Snippet |
| `oe_structure oe_empty` | 拖放區 + 顯示「拖曳到這裡」提示 |
| `oe_structure_not_nest` | 可拖入 Snippet，但不可再往下嵌套 |
| `s_allow_columns` | 允許在容器內拖入多個欄位 |
| `o_not_editable` | 禁止編輯內容 |
| `oe_unremovable` | 禁止刪除區塊 |

### 容器尺寸

| Class | 寬度 | 用途 |
|-------|------|------|
| `.container` | Max 1550px, 桌面 90% | 標準內容 |
| `.container-fluid` | 100% 滿版 | 背景滿版區塊 |
| `.o_container_small` | Max 1200px | 文章/部落格 |

### 嵌套技巧

**讓不可編輯區域變可編輯：**
```xml
<!-- 在 col 內加入 oe_structure → 可拖入 snippet -->
<div class="col-lg-6">
    <div class="oe_structure oe_empty">
        <!-- 設計師可拖入任何 snippet -->
    </div>
</div>
```

**用 data-snippet 讓 div 可拖曳：**
```xml
<!-- 包成 snippet 後可以拖曳排序 -->
<section class="s_text_block" data-snippet="s_text_block" data-name="My Block">
    <div class="container s_allow_columns"><p>內容</p></div>
</section>
```

**突破限制：在手風琴 (Accordion) 內部實現圖文網格排版：**

→ 請參考文件頂部的 [`s_text` 內容容器說明](#s-text) 章節，內含完整範例。

---

## 1. 基本 (Structure)

<a id="structure"></a>

### Hero & 全版

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Banner | `s_banner` | 全寬視差滾動橫幅 + 標題框 |
| Cover | `s_cover` | 全螢幕滿版背景 + 遮罩 |
| Carousel | `s_carousel` | 輪播圖（需唯一 ID） |

#### `s_carousel_wrapper` / `s_carousel` 骨架與 Template Class

> **基礎模板：** `templates/base/banner-arrow.xml`

`s_carousel` 外層由 `section.s_carousel_wrapper` 包覆，內層 `.s_carousel` 透過 Template Class 控制外觀：

| Template Class | 說明 |
|---------------|------|
| `s_carousel_default` | 預設全寬背景輪播（無邊框） |
| `s_carousel_bordered` | 帶邊框的輪播 |
| `s_carousel_boxed` | 方塊風格輪播 |
| `s_carousel_rounded` | 圓角風格輪播 |

**骨架結構：**
```xml
<section class="s_carousel_wrapper" data-vxml="001" data-snippet="s_carousel" data-name="Carousel">
  <div class="s_carousel carousel slide s_carousel_default" id="唯一ID" data-ride="carousel" data-interval="10000" data-pause="false">
    <ol class="carousel-indicators o_we_no_overlay">
      <li data-slide-to="0" class="active" data-target="#唯一ID"/>
      <!-- 更多 indicator -->
    </ol>
    <div class="carousel-inner">
      <div class="carousel-item pt152 pb152 o_colored_level oe_img_bg o_bg_img_center active" data-name="Slide">
        <div class="container oe_unremovable">
          <div class="row content">
            <div class="carousel-content col-lg-6 o_colored_level">
              <!-- 文字內容 -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <a class="carousel-control-prev o_not_editable o_we_no_overlay" data-slide="prev" href="#唯一ID">
      <span class="carousel-control-prev-icon"/>
      <span class="sr-only o_default_snippet_text">Previous</span>
    </a>
    <a class="carousel-control-next o_not_editable o_we_no_overlay" data-slide="next" href="#唯一ID">
      <span class="carousel-control-next-icon"/>
      <span class="sr-only o_default_snippet_text">Next</span>
    </a>
  </div>
</section>
```

**規則：**
- `id`、`data-target`、`href` 必須同頁唯一（同 [輪播 ID 規則](#static)）
- 每個 `carousel-item` 自帶 `oe_img_bg o_bg_img_center o_colored_level`，背景圖透過 `style="background-image: url(...);"` 設定
- 控制按鈕含 `o_not_editable o_we_no_overlay`，不可省略
- AI 生成前**必須讀取** `templates/base/banner-arrow.xml` 的完整骨架，禁止自行編寫

### 文字 & 標題

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Title | `s_title` | 標題區塊 |
| Text Block | `s_text_block` | 一般文字區塊（最萬用） |
| Text - Image | `s_text_image` | 左文右圖 |
| Image - Text | `s_image_text` | 左圖右文 |
| Picture | `s_picture` | 上標題下大圖 |

### 多欄 & 卡片

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Three Columns | `s_three_columns` | 三欄卡片式佈局 |
| Features | `s_features` | 三欄圖標+標題 |
| Features Grid | `s_features_grid` | 網格狀功能特點 |
| Big Boxes | `s_color_blocks_2` | 雙欄大色塊 |
| Media List | `s_media_list` | 左圖右文列表 |
| Numbers | `s_numbers` | 數據統計 |
| Image Gallery | `s_image_gallery` | 相片牆 |
| Images Wall | `s_images_wall` | 瀑布式圖片牆（多圖） |

#### `s_image_gallery` 輪播模式 (o_slideshow) 箭頭指示器 Template Class

> **基礎模板：** `templates/base/banner-arrow.xml`

當 `s_image_gallery` 搭配 `o_slideshow` class 使用時，成為 **輪播模式**，可透過 Template Class 控制左右導覽按鈕樣式：

| 指示器 Template Class | 說明 |
|----------------------|------|
| `s_image_gallery_indicators_rounded` | 圓角縮圖指示器（基礎款） |
| `s_image_gallery_indicators_arrows_boxed` | 方塊箭頭指示器 |
| `s_image_gallery_indicators_arrows_rounded` | 圓角箭頭指示器 |

**輪播模式的 section 完整 class 組合：**
```
s_image_gallery o_slideshow s_image_gallery_show_indicators [指示器 Template Class] o_colored_level
```

**骨架結構（輪播模式）：**
```xml
<section class="s_image_gallery o_slideshow s_image_gallery_show_indicators s_image_gallery_indicators_rounded o_colored_level pt56"
         data-vcss="001" data-columns="3"
         style="height: 500px; overflow: hidden; background-image: none;"
         data-snippet="s_image_gallery" data-name="Image Gallery">
  <div class="container">
    <div id="唯一ID" class="carousel slide" data-ride="carousel" data-interval="0">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="img img-fluid d-block" src="..." data-name="Image" data-index="0" loading="lazy"/>
        </div>
        <!-- 更多 carousel-item -->
      </div>
      <ul class="carousel-indicators o_we_no_overlay">
        <li class="o_indicators_left text-center d-none active" aria-label="Previous" title="Previous"/>
        <li data-target="#唯一ID" data-slide-to="0" style="background-image: url(...)"/>
        <!-- 更多 indicator -->
        <li class="o_indicators_right text-center d-none" aria-label="Next" title="Next"/>
      </ul>
      <a class="carousel-control-prev o_we_no_overlay o_not_editable" href="#唯一ID" data-slide="prev">
        <span class="fa fa-chevron-left fa-2x text-white"/>
        <span class="sr-only o_default_snippet_text">Previous</span>
      </a>
      <a class="carousel-control-next o_we_no_overlay o_not_editable" href="#唯一ID" data-slide="next">
        <span class="fa fa-chevron-right fa-2x text-white"/>
        <span class="sr-only o_default_snippet_text">Next</span>
      </a>
    </div>
  </div>
</section>
```

**與靜態 `o_masonry` 模式的差異：**
- `o_slideshow`：輪播模式，有 `.carousel` / `.carousel-item` / `.carousel-indicators` / `.carousel-control-*`
- `o_masonry`（同檔也有範例）：磚塊靜態排列，用 `.row` + `.o_masonry_col.col-lg-*`，無輪播控制元件

**規則：**
- 輪播 ID 必須同頁唯一（同 [輪播 ID 規則](#static)）
- 箭頭按鈕使用 `fa fa-chevron-left` / `fa fa-chevron-right`（Font Awesome v4）
- AI 生成前**必須讀取** `templates/base/banner-arrow.xml` 的完整骨架，禁止自行編寫
| Masonry Block | `s_masonry_block` | Masonry 拼貼網格（結構較複雜，建議從既有模板/實例複製） |
| Showcase | `s_showcase` | 展示區（圖文組合） |
| Parallax | `s_parallax` | 視差背景效果區塊 |

---

## 2. 排版元件 (Layout)

<a id="layout"></a>

### 自訂佈局區塊

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Vertical Layout | `s_vertical_layout` | 單欄式，內含 `oe_structure` |
| Column Layout | `s_column_layout` | 左右兩欄，左側支援 sticky |
| Collapse Layout | `s_collapse_layout` | 可展開/收合的內容區 |

### 內容組織

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Tabs | `s_tabs` | 分頁切換內容 |
| Table of Content | `s_table_of_content` | 左側導航 + 右側內容 |
| Accordion | `s_faq_collapse` | QA 問答/收合（支援多種樣式） |
| Timeline | `s_timeline` | 時間軸 |
| Process Steps | `s_process_steps` | 步驟流程圖 |

### 行銷 & 商務

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Call to Action | `s_call_to_action` | 行動呼籲區塊 |
| Comparisons | `s_comparisons` | 價格/功能比較表 |
| Company Team | `s_company_team` | 團隊成員介紹 |
| References | `s_references` | 客戶 Logo 列表 |
| Product Catalog | `s_product_catalog` | 產品目錄/菜單 |
| Product List | `s_product_list` | 產品列表 |
| Quotes Carousel | `s_quotes_carousel` | 客戶見證輪播 |

---

## 3. 動態內容 (Dynamic)

<a id="dynamic"></a>

> 詳細規則請參考 → [dynamic_rules.md](.agent/skills/icb_page_generator/resources/dynamic_rules.md)

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Dynamic Products | `s_dynamic_snippet_products` | 動態產品列表 |
| Dynamic Blog | `s_dynamic_snippet` | 動態部落格/新聞 |
| Dynamic Carousel | `s_dynamic_snippet_carousel` | 動態輪播（產品或部落格） |
| Blog Posts | `s_blog_posts` | 部落格文章區塊 |

### 互動 & 表單

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Form | `s_website_form` | 聯絡表單 |
| Map | `s_map` | 地圖（依網站設定/金鑰可能切換不同模板） |
| Google Map | `s_google_map` | 地圖（Google Maps API Key 可用時） |
| Search Bar | `s_searchbar` | 站內搜尋（整條搜尋列） |
| Embed Code | `s_embed_code` | 嵌入 HTML/JS 代碼 |
| Popup | `s_popup` | 彈出視窗 |
| Newsletter | `s_newsletter` | 電子報訂閱 |
| Countdown | `s_countdown` | 倒數計時器 |
| Facebook Page | `s_facebook_page` | Facebook 粉專嵌入 |

---

## 4. 靜態模板 (Static)

<a id="static"></a>

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Static Snippet | `s_static_snippet` | 靜態內容模板容器 |
| Static Carousel | `s_static_carousel` | 靜態輪播模板容器 |

### 可用模板 Class（放在 `.static_snippet_template` 上）

| Template Class | 說明 |
|---------------|------|
| `s_product_product_centered` | 產品居中卡片 |
| `s_product_product_classic` | 經典產品卡片 |
| `s_product_product_horizontal` | 水平產品卡片 |
| `s_product_product_large_banner` | 大橫幅產品 |
| `s_product_product_borderless_1` | 無邊框產品 1 |
| `s_product_product_borderless_2` | 無邊框產品 2 |
| `s_blog_post_big_picture` | 部落格大圖 |
| `s_blog_post_card` | 部落格卡片 |

### 輪播 ID 規則（避免同頁衝突）
- 靜態/動態輪播的 `id` 必須在同一頁唯一
- 若模板內有固定 ID，輸出到頁面前必須改成唯一值
- 同步更新所有關聯屬性：
  - `data-target="#..."`（含 `type="button"` 的控制元件）
  - `href="#..."`
  - `aria-controls="..."`

---

## 5. 插入內容 (Inner Content)

<a id="inner-content"></a>

這些是小型元件，插入在大區塊內部使用：

| Snippet | `data-snippet` | 說明 |
|---------|---------------|------|
| Separator | `s_hr` | 分隔線 |
| Alert | `s_alert` | 警示訊息 |
| Badge | `s_badge` | 標籤徽章 |
| Rating | `s_rating` | 評分星星 |
| Card | `s_card` | 卡片容器（可放內容） |
| Text Highlight | `s_text_highlight` | 強調文字（提示/重點） |
| Blockquote | `s_blockquote` | 引言/引用文字 |
| Search Input | `s_searchbar_input` | 內嵌搜尋輸入框（小型元件） |
| Progress Bar | `s_progress_bar` | 進度條 |
| Chart | `s_chart` | 圖表 |
| Share | `s_share` | 分享按鈕 |

---

## 6. 全域工具 Class (Utility Classes)

<a id="utility-classes"></a>

### 間距
- `pt8`, `pt16`, `pt24`, `pt32`, `pt40`, `pt48`, `pt64`, `pt80`, `pt96`, `pt112`, `pt128` ... `pt256`
- `pb8`, `pb16` ... `pb256`（相同對應 padding-bottom）

### 背景色
- `o_cc1` (白底) → `o_cc2` (淺灰) → `o_cc3` (主色) → `o_cc4` (次色) → `o_cc5` (深色)
- **規則：** 使用 `o_ccX` 時**不要**手動加 `text-white` 或 `text-dark`

### 自訂效果
| Class | 效果 |
|-------|------|
| `s_custom_scaleL` / `s_custom_scaleS` | Hover 放大效果 |
| `s_custom_nameHoverUnderLine` | 標題 hover 底線 |
| `s_custom_reverse` | `.row` 反轉方向 |
| `s_custom_RWDscroll` | 手機版水平捲軸 |
| `s_custom_GapM` / `s_custom_GapS` | 欄位間距（10px / 5px） |
| `s_custom_noRemove` | 紅色指示器「請勿刪除」 |
| `s_custom_fullContainer` | 容器無左右 padding |
| `s_custom_upperNext` | 上下區塊交疊效果 |

### Section 命名規則
- **Format:** `PascalCase`（如 `HeroNavigator`, `NewsCards`）
- **禁止：** 名稱內不可有空格、`-`、`_`
- **多個名稱：** 空格分隔（如 `data-custom-name="NewsCards ScaleL"`）
- **對應 Class：** `s_custom_YourName`（如 `s_custom_HeroNavigator`）
- **套用位置：** 僅用於可編輯的自訂區塊（`<section>` 或 snippet）；系統頁面/系統區塊不可改

---

## Backgrounds (背景圖片與影片)

<a id="backgrounds"></a>
Odoo 原生支援任何 `<section>` 或外層容器套用背景圖或影片。

### 1. 背景圖片 (Background Image)
在你要套用的 `<section>` (例如 `s_vertical_layout`) 加上屬性：
```xml
<section class="... oe_img_bg o_bg_img_center"
         style="background-image: url('/web/image/.../bg.jpg');"
         data-original-src="/web/image/.../bg.jpg"
         data-mimetype="image/jpeg"
         data-resize-width="1920">
    <!-- 內容 -->
</section>
```
*   `oe_img_bg` 觸發 Odoo 背景設定介面。
*   `o_bg_img_center` 確保圖中置中。

### 1-1. 固定視差背景 (Parallax Fixed)
當設為固定視差背景時，Odoo 會在 `<section>` 內部新增以下同層元素：

- `.s_parallax_bg.oe_img_bg.o_bg_img_center`（背景圖容器）
- `.o_we_bg_filter`（濾色遮罩）

且 `<section>` 會改為類似以下 class：
`parallax s_parallax_is_fixed s_parallax_no_overflow_hidden`

**重點：** 以上元素與 `.container` 同層，不在 `.container` 內。

### 2. 背景影片 (Background Video)
若要套用影片，Odoo 會在 `<section>` 的第一層（內容之前）插入 `<div class="o_we_bg_filter">` 和 `o_bg_video_iframe` (YouTube/Vimeo) 或 `<video>`。
*   要在 AI 開發中讓使用者可以進入編輯器替換，可以加上：
```xml
<section class="... oe_img_bg o_bg_img_center" data-bg-video-src="影片網址(Youtube/Vimeo)">
    <div class="o_we_bg_filter bg-black-50"></div>
    <!-- 內容 -->
</section>
```
*   `o_we_bg_filter`: 控制遮罩透明度與顏色 (如 `bg-black-50` 半透明黑底)，幫助文字閱讀。
