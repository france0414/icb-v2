# Odoo 14 Header & Footer 樣式開發規範
此文件規範了如何在「保留 Odoo 原生編輯功能」與「客製化高質感 RWD 佈局」之間取得平衡。

## 1. Header (Navbar) 核心架構原則
Odoo 的 Header 是系統核心元件，包含了登入狀態、多語系、購物車等動態功能，因此 **絕對不可以直接取代或刪除原生 HTML 結構**。我們必須透過 SCSS 覆寫來達成設計需求。

> [!IMPORTANT]
> **AI 執行指令：當被要求生成或修改 Header 時**
> AI **只能輸出 SCSS**，絕對不要輸出任何 `<header>` 的 XML。設計基準應基於 Odoo 的**第一組 Header 選項 (First Option)**。

### 1-1. 必須保留與保護的原生 Classes
在任何自訂 Header 的 SCSS 中，必須保留對以下 class 的支援：
- **容器與主結構**: `header#top`, `.navbar`, `#top_menu_container`, `#top_menu`
- **選單項目**: `.nav-item`, `.nav-link`, `.dropdown-menu`, `.dropdown-item`, `.o_mega_menu`
- **系統動態注入項目 (絕對不可隱藏其功能)**:
  - `.o_wsale_quote_cart` (購物車)
  - `.o_portal_header_sign_in` / `.o_portal_header_user_dropdown` (登入/使用者選單)
  - `.js_language_selector` (語系切換)
  - `.addon_nav_searchbar` (全站搜尋)
- **客製化內容注入區**: `.oe_structure_solo` (通常用於 Header 上的聯絡資訊或 CTA 按鈕)

## 2. Desktop (PC端) 佈局策略：CSS Grid 魔法
為了解決 Odoo 預設 Bootstrap 4 排版導致的結構限制，我們在 Desktop 端 (`>= lg`) 完全依賴 `display: grid` 來重新排列 `#top_menu_container` 內的元素，**不更動任何原生 DOM 順序**。

### 示範：使用 Grid 徹底翻轉 Header 順序
```scss
header#top {
    #top_menu_container {
        @include media-breakpoint-up(lg) {
            max-width: 100%;
            display: grid;
            // 定義欄位：左方 Logo (例如 200px) / 中間彈性空間 (1fr) / 右方客製化區塊 (auto)
            grid-template-columns: 200px 1fr auto;
            grid-template-areas:
                "logo top-menu contact"    // 上半部佈局
                "logo main-menu contact"; // 下半部佈局
            grid-template-rows: 0.5fr 0.5fr;
            grid-auto-flow: row;
            padding-right: 0;
            
            // 指定各元素對應的 Grid Area
            .logo { grid-area: logo; }
            .oe_structure_solo { grid-area: contact; } // 客戶自行放入的結構
            .navbar-collapse { grid-area: main-menu; } // 主選單
            #navbar_subnav { grid-area: top-menu; }    // 次選單與語系、會員
        }
    }
}
```

## 3. Mobile (手機端) 佈局策略：極致的滿版覆蓋體驗
Odoo 原生的手機選單體驗較差 (向下推開內容)，我們透過攔截 `.navbar-collapse` 並將其轉化為 Fixed 滿版覆蓋層 (Full-screen Overlay) 來實現現代感設計。

### 3-1. 動態高度計算 (處理 Odoo 頂部編輯工具列)
Odoo 登入後頂部會出現 `--o-we-toolbar-height`。為了自適應不同的 Header 設計高度，我們必須**宣告 CSS 變數 `--hd-h`**（Header Height），並透過它來精準計算手機選單的 `top` 與 `height`，確保選單完美貼齊 Header 底部且不被截斷。

> [!TIP]
> **確保手機端 Header 高度固定（停止滾動變小）**
> Odoo 預設在向下滾動 (`.o_header_is_scrolled`) 時會縮小 Logo。為了維持手機端選單高度計算的一致性，我們**必須強制 `< 991px` (md) 的 Logo 高度始終一致**，這樣 Header 在滾動時才不會忽大忽小。

```scss
@include media-breakpoint-down(md) {
    // 1. 強制鎖定手機端 (包含滾動時) 的 Logo 高度，確保 Header 總高度不變
    :root {
        --hd-h: 70px; // 依設計稿或實際 Header 高度給定一個固定值
    }
    header#top .navbar-brand img,
    .o_header_is_scrolled header#top .navbar-brand img {
        height: 40px !important; // 固定 Logo 高度避免撐開 Header
    }

    /* 登入狀態：扣除 Odoo 編輯器工具列高度與自訂 Header 高度 */
    body.o_connected_user {
        header#top .navbar-collapse {
            top: calc(var(--o-we-toolbar-height) + var(--hd-h)); 
            height: calc(100dvh - (var(--o-we-toolbar-height) + var(--hd-h))); 
        }
    }

    /* 未登入狀態 (一般訪客) */
    body:not(.o_connected_user) {
        header#top .navbar-collapse {
            top: var(--hd-h); 
            height: calc(100dvh - var(--hd-h)); 
        }
    }
}
```

### 3-2. 滿版展開選單核心 CSS
```scss
header#top {
    .navbar-collapse {
        position: fixed;
        width: 100%;
        left: 0;
        background: white;
        z-index: 999;
        opacity: 0;
        visibility: hidden;
        max-height: none; // 覆寫 BS4 預設限制
        transition: opacity 0.5s ease-in-out, transform 0.5s, visibility 0.5s;
        
        &.show {
            opacity: 1;
            visibility: visible;
        }
        &.collapsing {
            // 修正 BS4 預設過渡動畫造成的卡頓
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.2s ease-in-out, visibility 0.2s;
        }
    }
}
```

### 3-3. 手機端安全邊距 (Safe Area)
所有下拉選單、內部元件都必須遵守統一的安全邊距變數 `--container-pd-x`：
```scss
@include media-breakpoint-down(md) {
    header#top .show #top_menu {
        > .nav-item > a.nav-link {
            padding: 10px var(--container-pd-x); // 確保文字不貼邊
        }
        .dropdown-menu:not(.o_mega_menu) {
            margin: 0 var(--container-pd-x); // 確保次選單有左右邊距
        }
    }
}
```

## 4. 動態元件樣式覆寫 (Search, Language, User)
在重構 Header 時，Odoo 的內建按鈕通常帶有非必要的邊框與原生文字，我們透過 CSS 替換為純潔的 FontAwesome 圖標：
```scss
// 語系切換：隱藏原生 img 與文字，替換成地球 Icon
.js_language_selector .btn-outline-secondary {
    color: var(--o-color-5);
    border: 0; // 隱藏原本的 button btn-outline 邊框
    &::before {
        content: "\f0ac"; // 地球 Icon
        font-family: "fontawesome";
        font-size: calc(var(--header-font-size) + 0.2rem);
    }
    img, span.align-middle, &::after { display: none !important; }
}

// 搜尋按鈕：調整圖示大小與對齊
.addon_nav_searchbar .dropdown-toggle > .fa-search::before {
    font-size: calc(var(--header-font-size) + 0.2rem);
}
```

## 5. Header 特殊功能注入區 `.oe_structure_solo`
這個區塊是保留給設計師與客戶放入自訂內容的地方（例如：頂部的跑馬燈、聯絡電話、或 Call to Action 大按鈕）。在 SCSS 中我們常見會將其設為：
- **桌面版 (Desktop)**：配置在 Grid 的特定區域（如 `contact` 區塊）。
- **手機版 (Mobile)**：設計成在螢幕頂部或菜單展開底部的跑馬燈，甚至使用 `overflow-x: auto` 形成可水平滑動的頂端小工具列（如 Menu 2 的實作）。

---

## 6. Footer 核心架構與 Mobile 手風琴 (Accordion) 策略
Odoo 的 Footer 通常包含大量的連結清單。為了兼顧「手機端易於收起 (Accordion)」與「桌面端全展開 (Grid 排列)」，以及「原生功能可編輯」，我們統一採用 Odoo **原生 `s_faq_collapse` (FAQ/手風琴) Snippet 來建構 Footer 選單。** 

> [!IMPORTANT]
> **AI 執行指令：當被要求生成 Footer 時**
> AI 必須提供**完整的 XPath XML 與 SCSS**。XML 結構必須基於 Odoo 的 **"Links" (連結) Footer 選項**，利用多個 `col-lg-*` 欄位並搭配 `.list-unstyled` > `li` 結構，同時確保手機版使用 `s_faq_collapse` 轉換。

### 6-1. 原理與 HTML 結構要求
在 `footer.xml` 中，我們直接借用 Bootstrap 的 `.accordion` 與 `.card` 結構：
- 最外層包覆 `<section class="s_faq_collapse ... s_custom_footerTab" data-custom-name="footerTab">`。
- 每一個選單群組都是一個 `.card`。
- 點擊觸發點是 `<a role="tab" data-toggle="collapse" ...>`。
- 次選單內容放在 `.collapse .card-body` 中，裡面使用 `.list-unstyled` > `li.list-item`。

這種做法的好處是：**客戶在 Odoo 編輯模式中，可以直接點擊展開編輯每個列表，且結構不會因為客戶打字而壞掉。**

### 6-2. SCSS 魔法：電腦版強制展開、手機版維持收合
我們不需要寫任何外掛 JS 來控制視窗縮放。純 CSS 解法如下：

```scss
.s_custom_footerTab {
    .accordion {
        /* 手機端 (sm 以下) : 維持手風琴預設行為 */
        .card {
            border: 0; // 去除預設邊框
            .card-header {
                // 自訂收合圖示
                &.collapsed:before { content: "\f107"; } // 向下箭頭
                &::before { content: "\f106"; }          // 向上箭頭
            }
        }

        /* 桌面端 (md 以上) : 解除手風琴，強制變為並排網格 */
        @include media-breakpoint-up(md) {
            display: flex;       // 或使用 grid
            flex-wrap: wrap;     // 確保多欄位自動換行
            
            .card {
                flex: 1;              // 平分寬度
                
                .card-header::before {
                    display: none;    // 隱藏展開/收合箭頭
                }

                /* 關鍵魔法：強制展開所有選單內容 */
                .collapse,
                .collapsing {
                    display: block !important;
                }
            }
            .card-body:first-child {
                padding: 0; // 消除展開後的內距
            }
        }
    }
}
```

### 6-3. Footer 區塊佈局重構 (Grid/Flex Order)
Footer 除了連結清單，通常還包含 Logo、聯絡資訊。我們同樣使用 `flex-direction` 或 `grid-template-areas` 與 `order` 來應對 Mobile/Desktop 順序反轉的需求。

例如，在 HTML 中依序為 `[收合選單]` -> `[聯絡我們]` -> `[Logo與基本資料]`，但在桌面上，我們希望 `[Logo]` 出現在最左邊：
```scss
.o_footer .s_text_block > .container > .row {
        // 目標：將 [Logo與基本資料] 移動到最左邊
        @include media-breakpoint-up(md) {
            order: -1; 
        }
    }
}
```

---

## 7. Global Pre-Footer CTA (全站共用行動呼叫區塊)

在許多 B2B 或企業網站中，每個頁面的最下方（Footer 正上方）通常會有一個「準備好開始了嗎？聯絡我們」的橫幅 (Call to Action, CTA)。

如果讓設計師在每個頁面手動拉這個 Snippet，未來要修改文案或按鈕連結時會需要逐頁修改。因此，我們採用**「編輯器排版 $\rightarrow$ 提取結構 $\rightarrow$ 寫死入 Footer XML」**的全局共用策略。

### 7-1. 實作流程
1. **獨立製作**：在隨便一個測試頁面，利用 Odoo 編輯器拖出一個 `s_text_block`，設定好背景圖、標題、描述文字以及聯絡我們按鈕。
2. **提取 HTML**：進入開發者模式 (HTML/CSS Editor)，將剛才做好的 `<section>` 整個複製下來。
3. **注入 Global Footer**：打開控制全站 Footer 的 XML 檔案（通常繼承 `website.layout`），將這段 `<section>` 貼到 `<div id="footer">` 裡的最上方位置（緊鄰原本的 Footer 連結區塊之上）。

### 7-2. 結構範例
```xml
<data inherit_id="website.layout" name="Links" active="False">
  <xpath expr="//div[@id='footer']" position="replace">
    <div id="footer" class="oe_structure oe_structure_solo" t-ignore="true" t-if="not no_footer">
      
      <!-- 1. 注入的 Global CTA 區塊 -->
      <section class="s_text_block o_cc o_cc3 pt72 pb72 parallax s_custom_ftContact" data-custom-name="ftContact">
        <div class="container">
          <div class="row">
            <div class="col-lg-12 text-center">
              <h2>What can we do to help?</h2>
              <p>Get in touch with us! We provide help and support.</p>
              <a href="/contactus" class="btn btn-fill-primary rounded-circle">Contact Today !</a>
            </div>
          </div>
        </div>
      </section>

      <!-- 2. 原本的 Footer 導覽列與公司資訊區塊 -->
      <section class="s_text_block pt48 pb16 s_custom_footerTab" data-custom-name="footerTab">
          <!-- Accordion to Grid 結構... -->
      </section>

    </div>
  </xpath>
</data>
```
這樣做最大的好處是：**全站 CTA 自動生效，與底層 Footer 緊密結合，未來只需修改一支 XML 檔案即可套裝全網。**
