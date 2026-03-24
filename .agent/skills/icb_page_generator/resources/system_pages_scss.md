# Odoo 14 系統頁面 (Blog / Shop) 開發規範

在 Odoo 中，像「部落格文章列表 (Blog List)」、「部落格內頁 (Blog Post)」、「商品列表 (Shop)」這類頁面，其 HTML 結構是由系統的核心模組與 Controller 在後端動態生成的。

> [!WARNING]
> **絕對禁止修改系統頁面的底層 XML 結構！**
> 如果我們硬改系統底層的 XML，在 Odoo 版本升級或安裝其他相依模組時，非常容易造成系統崩潰（View Conflict）。因此，針對這些系統頁面，**我們唯一且最強大的武器就是 SCSS。**

---

## 1. 核心觀念：純 SCSS 攔截與覆寫

設計師在 Figma 等工具中畫出的漂亮 Blog 卡片或 Shop 網格，我們必須透過 SCSS，強行套用在 Odoo 原本生硬的 HTML 結構上。

在 Odoo 的前台編輯器中，通常會有原生選項允許客戶切換版面（例如「清單視圖」或「網格視圖」）。我們的 SCSS 必須能夠**聰明地偵測並相容這些原生選項**。

---

## 2. Blog 列表頁 (Blog List) 樣式覆寫策略

當我們在 Odoo 建立 Blog 頁面時，通常會有一層 `.o_wblog_page` 或類似的 wrapper。我們需要針對系統預設的文章區塊 `.o_wblog_post` 進行整型。

### 2-1. 關鍵 Selector
- `.website_blog` / `.o_wblog_page`（最外層範圍）
- `.o_wblog_post_list`（列表容器）
- `article.o_wblog_post`（單篇卡片）
- `.o_record_cover_container`（封面圖片）
- `.o_wblog_post_content`（內文與標題）

### 2-2. 常見覆寫需求（短片段）
```scss
.website_blog {
    .o_wblog_post_list {
        display: grid;
        gap: 30px;
        grid-template-columns: 1fr;

        @include media-breakpoint-up(md) { grid-template-columns: repeat(2, 1fr); }
        @include media-breakpoint-up(lg) { grid-template-columns: repeat(3, 1fr); }

        > article {
            max-width: none !important;
            flex: none !important;
            width: 100% !important;
        }
    }

    article.o_wblog_post {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
}
```

### 2-3. 部落格內頁 (Blog Post Detail)
常見覆寫點：標題區、內容寬度、作者/時間/標籤等資訊區。
```scss
#o_wblog_post_main {
    .o_wblog_post_content { max-width: 800px; margin: 0 auto; }
    .o_wblog_author_avatar { display: none !important; }
}
```

---

## 3. 電商商品列表 (Shop List) 樣式覆寫策略

電商頁面 (`/shop`) 是 Odoo 中最複雜的模組之一，包含了左側過濾器 (Sidebar)、頂部排序搜尋、以及商品網格。

### 3-1. 關鍵 Selector
- `.o_wsale_products_main_row`（主列）
- `#products_grid_before`（左側 Filter）
- `#products_grid`（右側商品清單）
- `.oe_product` / `.oe_product_card`（商品卡片）
- `.product_price`（價格）
- `#wsale_products_categories_collapse`（分類清單）
- `#product_detail`（商品內頁）

### 3-2. 常見覆寫需求（短片段）
```scss
.o_wsale_products_main_row {
    @include media-breakpoint-up(lg) {
        display: grid;
        grid-template-columns: 280px 1fr;
        gap: 40px;

        > #products_grid_before,
        > #products_grid {
            flex: none;
            max-width: none;
            width: 100%;
        }
    }
}

#products_grid .oe_product {
    border-radius: 8px;
    overflow: hidden;
}

#product_detail {
    .row { @include media-breakpoint-up(lg) { gap: 50px; } }
    h1[itemprop="name"] { font-size: 2.5rem; }
}
```

### 3-3. 加入購物車 (詢價車) 飛行動畫定位修復
在 Shop 點擊「加入購物車」時，Odoo 原生的 JavaScript 會有一個商品圖片飛向導覽列購物車圖示 (`.o_wsale_quote_cart`) 的動畫。

當網站在手機版 (Mobile) 時，如果主導覽選單被收合 (`#top_menu_collapse`)，或者我們有設計獨立的手機版 Header 雙排選單，這個飛行動畫會找不到目標，或是飛向奇怪的隱藏區塊。

**解法**：我們無法去改 Odoo 的 JS，但我們可以透過 SCSS，**把隱藏在 Collapse 裡面的原生 `.o_wsale_quote_cart` 強制設為 `display: block !important` 與 `position: absolute`，然後定位到「視覺上」的手機版購物車圖示正上方**，並將透明度設為 0 (或 `pointer-events: none`) 讓它作為純粹的「動畫降落靶心」。

```scss
// 針對未展開的標頭 (Mobile 漢堡選單未點開時)
header:not(.o_top_menu_collapse_shown) {
    @include media-breakpoint-down(md) {
        height: unset !important;

        // 我們不希望整個下拉選單跑出來，所以強行設定高度為 0
        &#top #top_menu_collapse {
            height: 0 !important;
            padding: 0 !important;
            display: block !important;
            margin: 0 !important;
            opacity: 0 !important;
            pointer-events: none;
        }

        // 唯獨把這個「飛行動畫的靶心 (cart)」叫出來，放到畫面上正確的購物車圖示上
        &#top #top_menu_collapse #top_menu .o_wsale_quote_cart {
            display: block !important;
            position: absolute;
            // 以下數值必須根據實際的手機版 Header 高度與按鈕位置自行調整
            top: 15px; 
            right: 140px; 
            width: auto !important;
            pointer-events: none; // 不要阻擋點擊可以考慮加 opacity: 0
        }
    }
}
```

### 3-4. 購物車/詢價車 Checkout 頁面 (`/shop/cart` 或 `/quote/cart`)
當使用者點擊購物車進入結帳或詢價清單頁面時，系統會載入一個包含商品表格 (`#cart_products`) 與右側/下方結帳流程卡片的版面。

這個頁面的預設 Bootstrap 表格通常在手機版會發生嚴重跑版（水平卷軸或破版）。我們必須透過 SCSS 強制讓表格變成 RWD 卡片，或是隱藏不必要的欄位（例如稅金、折扣）。

```scss
// 針對結帳清單主區塊
.oe_cart {
    // 預設的購物車表格
    #cart_products {
        border-collapse: separate;
        border-spacing: 0 15px; // 讓每一列表格之間有空隙，呈現卡片感
        
        thead {
            // 在某些設計中，我們會隱藏標題列，讓畫面更乾淨
            display: none; 
        }

        tbody tr {
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            border-radius: 10px;
            
            td {
                border-top: none; // 移除預設 Bootstrap 表格線
                vertical-align: middle;
            }
            
            // 手機版：強制將表格轉為 Block 堆疊，避免水平卷軸
            @include media-breakpoint-down(sm) {
                display: flex;
                flex-wrap: wrap;
                position: relative;
                padding: 15px;
                
                td {
                    display: block;
                    width: 100%;
                    text-align: left !important;
                    
                    // 針對刪除按鈕 (Trash icon) 絕對定位到右上角
                    &.td-action {
                        position: absolute;
                        top: 10px;
                        right: 10px;
                        width: auto;
                    }
                }
            }
        }
    }
    
    // 下一步/結帳 按鈕美化
    .btn-primary.float-right {
        border-radius: 30px;
        padding: 12px 35px;
        font-weight: bold;
        letter-spacing: 1px;
    }
}
```

---

## 4. 開發流程摘要
1. **進入開發者模式 (Inspector)**：打開 Odoo 前台頁面，按 F12 觀察系統吐出了哪些 ID 與 Class（例如 `.o_wblog_page`, `#products_grid`）。
2. **尋找最外層容器**：在 SCSS 檔案中，先寫下最外層的 Wrapper，確保樣式只影響該系統頁面。
3. **取消預設結構 (Unset/Override)**：把不想要的 Bootstrap grid 屬性（如 `flex`, `max-width`, `margin`）設為 `none` 或 `0`。
4. **注入現代化 CSS**：改用 CSS Grid 或 Flexbox 重新排版，並套用陰影、圓角、懸停動畫等設計。
