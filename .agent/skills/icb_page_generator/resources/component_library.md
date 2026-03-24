# Odoo Interactive Component Library (AI Reference)

> [!IMPORTANT]
> 此文件為 **AI 生成代碼專用**的參考文件。
> - 設計師可在正式 Odoo 平台上使用視覺預覽頁面。
> - AI 生成時只需複製此文件中的 **XML 結構** 和 **SCSS**，不需要 `<style>` 標籤。

---

## Component Index

| # | Component Name | Custom Class | Description | Max Items |
|---|----------------|--------------|-------------|-----------|
| 01 | [Full Image Hover 1](#01-full-image-hover-1) | `s_custom_fullImgHoevr1` | Hover 切換大圖，左側導航按鈕 | 6 |
| 02 | [Full Image Hover 2](#02-full-image-hover-2) | `s_custom_fullImgHoevr2` | Hover 滑入顯示背景大圖 | 7 |
| 03 | [Exhibition Updates](#03-exhibition-updates) | `s_custom_exhibitionUpdates` | 右側固定滑入新聞面板 | - |
| 04 | [Product Right Scroll](#04-product-right-scroll) | `s_custom_productRightScroll` | 水平滾動產品卡片列 | 6 |
| 05 | [Interactive Map](#05-interactive-map) | `s_custom_mapEffect` | 地圖互動標記點 | 5 |
| 06 | [Sticky Background](#06-sticky-background) | `s_custom_stickyBG` | 內文固定 + 背景圖 fix | - |
| 07 | [Full Hover Background](#07-full-hover-background) | `s_custom_fullHoverBackground` | Icon 觸發背景圖切換 | 6 |
| 08 | [Worldwide Scroll](#08-worldwide-scroll) | `s_custom_worldwide` | 上圖下文卡片水平捲軸 | - |
| 09 | [Worldwide RWD Collapse](#09-worldwide-rwd-collapse) | `s_custom_worldwideRWDcollapse` | 桌機捲軸 / RWD 收合 | - |

### Utility Components

| Component | Custom Class | Description |
|-----------|--------------|-------------|
| Custom Dropdown | `s_custom_customDropdown` | 手風琴下拉清單 |
| Anchor Area | `s_custom_anchorArea` | 錨點導航區域 |
| Control Button | `s_custom_controlBtn` | 開關控制按鈕 |
| Fix Image | `s_custom_fixImg` | 固定定位圖片 |
| Align Icon | `s_text.align-icon` | 文字對齊小 icon |

---

## 01. Full Image Hover 1

**Custom Class:** `s_custom_fullImgHoevr1`  
**建議數量:** 最多 6 筆，適用短字串標題

### XML Structure

```xml
<section class="s_vertical_layout o_cc o_cc5 s_custom_fullImgHoevr1" 
         data-snippet="s_vertical_layout" 
         data-name="Full Image Hover 1"
         data-custom-name="fullImgHoevr1">
  <div class="container-fluid">
    <div class="oe_structure oe_structure_not_nest oe_empty">
      
      <!-- Repeat s_custom_boxWrap for each item (max 6) -->
      <section class="s_text_block o_colored_level pt0 pb0 s_custom_boxWrap" 
               data-snippet="s_text_block" 
               data-name="Text" 
               data-custom-name="boxWrap">
        <div class="s_allow_columns container-fluid">
          <!-- Image Section -->
          <div class="s_text img-wrap" data-snippet="s_text" data-name="Text">
            <div class="s_text img-content" data-name="Text">
              <img class="img-fluid o_we_custom_image" 
                   src="https://picsum.photos/1920/1080" 
                   alt="" loading="lazy"/>
            </div>
          </div>
          <!-- Button Navigation -->
          <div class="s_text btn-wrap" data-snippet="s_text" data-name="Text">
            <div>
              <p><a href="#">Button Title</a></p>
            </div>
          </div>
        </div>
      </section>
      <!-- End of item -->
      
    </div>
  </div>
</section>

<!-- JS Code Section (Required) -->
<section class="s_embed_code o_colored_level pb16 pt16 text-center s_custom_jqCode" 
         data-snippet="s_embed_code" 
         data-name="Embed Code"
         data-custom-name="jqCode">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      // Insert JavaScript from section below
    </script>
  </div>
</section>
```

### JavaScript

```javascript
const containers = document.querySelectorAll('.s_custom_fullImgHoevr1 .s_custom_boxWrap');
if (!document.body.classList.contains('editor_started')) {
    if (containers.length > 0) {
        const firstDiv = containers[0].querySelector('div');
        if (firstDiv) {
            firstDiv.classList.add('show');
        }
    }
    containers.forEach(container => {
        const btnWrap = container.querySelector('.btn-wrap');
        if (btnWrap) {
            btnWrap.addEventListener('mouseenter', function () {
                containers.forEach(otherContainer => {
                    const div = otherContainer.querySelector('div');
                    if (div) {
                        div.classList.remove('show');
                    }
                });
                const currentDiv = container.querySelector('div');
                if (currentDiv) {
                    currentDiv.classList.add('show');
                }
            });
        }
    });
}
```

### SCSS

```scss
//  ---------- Full Image Hover 1 ---------- //
.s_custom_fullImgHoevr1 {
    min-height: 100vh;
    display: flex;
    align-items: stretch;
    position: relative;
    overflow: hidden;
    @include media-breakpoint-down(md) {
        min-height: unset;
    }
    >.container-fluid {
        position: relative;
        display: flex;
        align-items: stretch;
    }
    .s_custom_boxWrap {
        flex-direction: column;
        display: flex;
        position: static;
        flex: 1;
        @include media-breakpoint-down(md) {
            flex: unset;
        }
        &:hover {
            .btn-wrap {
                >div::before {
                    width: 80%;
                }
            }
        }
    }
    .img-wrap {
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        opacity: 0;
        @include transition;
        &.show {
            @include media-breakpoint-up(lg) {
                opacity: 1;
            }
        }
        @include media-breakpoint-down(md) {
            position: relative;
            opacity: 1;
        }
    }
    .img-content {
        height: 100%;
        @include media-breakpoint-down(md) {
            height: auto;
        }
        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            @include media-breakpoint-down(md) {
                height: auto;
                max-height: 250px;
            }
        }
    }
    .btn-wrap {
        position: relative;
        z-index: 1;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding-bottom: 50px;
        @include media-breakpoint-down(lg) {
            padding: 15px 25px;
        }
        @include media-breakpoint-down(md) {
            padding: var(--container-pd-x);
        }
        >div {
            &::before {
                content: "";
                width: 0%;
                height: 1px;
                background: rgba(255, 255, 255, 0.3);
                display: block;
                opacity: 1;
                @include transition;
                @include media-breakpoint-down(md) {
                    display: none;
                }
            }
        }
        p {
            font-size: var(--h5);
            font-weight: 700;
            margin-bottom: 0;
            padding-top: 15px;
            a {
                color: #fff;
                @include media-breakpoint-down(md) {
                    color: $default;
                }
            }
        }
    }
}
```

---

## 02. Full Image Hover 2

**Custom Class:** `s_custom_fullImgHoevr2`  
**建議數量:** 最多 7 筆

### XML Structure

```xml
<section class="s_vertical_layout o_cc o_cc5 s_custom_fullImgHoevr2" 
         data-snippet="s_vertical_layout" 
         data-name="Full Image Hover 2"
         data-custom-name="fullImgHoevr2">
  <div class="container-fluid">
    <div class="oe_structure oe_structure_not_nest oe_empty">
      
      <!-- Repeat s_custom_boxWrap for each item (max 7) -->
      <section class="s_text_block o_colored_level pt0 pb0 s_custom_boxWrap" 
               data-snippet="s_text_block" 
               data-name="Text" 
               data-custom-name="boxWrap">
        <div class="s_allow_columns container-fluid">
          <!-- Image Section -->
          <div class="s_text img-wrap" data-snippet="s_text" data-name="Text">
            <div class="s_text img-content" data-name="Text">
              <img class="img-fluid o_we_custom_image" 
                   src="https://picsum.photos/1920/1080" 
                   alt="" loading="lazy"/>
            </div>
          </div>
          <!-- Content Section -->
          <div class="s_text content-wrap" data-snippet="s_text" data-name="Text">
            <div class="inner">
              <div class="s_text title" data-snippet="s_text" data-name="Text">
                <h4><a href="#">Content Header</a></h4>
              </div>
              <div class="s_text desc" data-snippet="s_text" data-name="Text">
                <p>Description text here...</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- End of item -->
      
    </div>
  </div>
</section>

<!-- JS Code Section -->
<section class="s_embed_code o_colored_level pb16 pt16 text-center s_custom_jqCode" 
         data-snippet="s_embed_code" 
         data-custom-name="jqCode">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      // Insert JavaScript from section below
    </script>
  </div>
</section>
```

### JavaScript

```javascript
document.addEventListener('DOMContentLoaded', function () {
  if (!document.body.classList.contains('editor_started')) {
    const containers = document.querySelectorAll('.s_custom_fullImgHoevr2 .s_custom_boxWrap');
    // 先移除所有 .container-fluid 的 show class
    containers.forEach(container => {
      const fluid = container.querySelector('.container-fluid');
      if (fluid) fluid.classList.remove('show');
    });
    // 預設第一個 section 的 .container-fluid 加上 show
    if (containers.length > 0) {
      const firstContainer = containers[0].querySelector('.container-fluid');
      if (firstContainer) {
        firstContainer.classList.add('show');
      }
    }
    // 滑入互動事件
    containers.forEach(container => {
      container.addEventListener('mouseenter', function () {
        containers.forEach(c => {
          const div = c.querySelector('.container-fluid');
          if (div) div.classList.remove('show');
        });
        const currentDiv = this.querySelector('.container-fluid');
        if (currentDiv) currentDiv.classList.add('show');
      });
    });
  }
});
```

### SCSS

```scss
//  ---------- Full Image Hover 2 ---------- //
.s_custom_fullImgHoevr2 {
    display: flex;
    min-height: 100vh;
    @include media-breakpoint-down(md) {
        flex-direction: column;
        min-height: unset;
    }
    >.container-fluid {
        display: flex;
        @include media-breakpoint-down(md) {
            flex-direction: column;
        }
    }
    .s_custom_boxWrap {
        position: static;
        flex: 1;
        @include media-breakpoint-down(md) {
            flex: unset;
        }
        >.container-fluid {
            display: flex;
            flex-direction: column;
            flex: 1;
            position: relative;
            z-index: 1;
            @include transition;
            @include media-breakpoint-down(md) {
                flex: unset;
            }
            &::after {
                content: "";
                width: 100%;
                height: 100%;
                position: absolute;
                left: 0;
                top: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(to left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.7));
                opacity: 0;
                @include transition;
                @include media-breakpoint-down(md) {
                    display: none;
                }
            }
        }
        &:hover {
            >.container-fluid {
                &::after {
                    opacity: 1;
                }
            }
            .content-wrap {
                &::after {
                    background: #fff;
                    right: 23px;
                    bottom: 23px;
                }
            }
        }
    }
    .img-wrap {
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        opacity: 0;
        z-index: -1;
        @include transition;
        @include media-breakpoint-down(md) {
            position: relative;
            opacity: 1;
        }
    }
    .img-content {
        height: 100%;
        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            @include media-breakpoint-down(md) {
                height: auto;
                object-fit: contain;
            }
        }
    }
    .content-wrap {
        display: flex;
        flex-direction: column;
        flex: 1;
        padding: 25px 50px;
        justify-content: flex-end;
        color: #fff;
        @include laptop-m {
            padding: 20px 30px;
        }
        @include media-breakpoint-down(md) {
            padding: var(--container-pd-x);
            color: $default;
        }
        &::after {
            content: "\f105";
            font-family: 'fontawesome';
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #fff;
            position: absolute;
            right: 30px;
            bottom: 30px;
            border-radius: var(--btn-border-radius-sm);
            @include transition;
            @include media-breakpoint-down(md) {
                width: 30px;
                height: 30px;
                right: var(--container-pd-x);
                bottom: 25px;
                border-color: $default;
                color: $default;
            }
        }
        h4 {
            font-weight: 700;
            margin-bottom: 10px;
            a {
                color: inherit;
            }
        }
        p {
            margin-bottom: 0;
            @include clamp-2;
        }
    }
}

body:not(.editor_started) {
    .s_custom_fullImgHoevr2 .s_custom_boxWrap>.container-fluid.show {
        .img-wrap {
            opacity: 1;
        }
    }
}
```

---

## 03. Exhibition Updates

**Custom Class:** `s_custom_exhibitionUpdates`  
**變體:** 加上 `s_custom_fixed` 可變成右側固定面板

### XML Structure

```xml
<section data-snippet="s_vertical_layout" 
         class="s_vertical_layout o_colored_level pt0 pb0 s_custom_exhibitionUpdates s_custom_fixed" 
         data-name="Vertical Layout"
         data-custom-name="exhibitionUpdates fixed">
  <div class="container-fluid">
    <div class="oe_structure oe_structure_not_nest oe_empty">
      
      <!-- Control Button -->
      <section class="s_text_block o_colored_level o_cc o_cc4 pt8 pb8 s_custom_controlBtn" 
               data-snippet="s_text_block" 
               data-name="Text" 
               data-custom-name="controlBtn">
        <div class="s_allow_columns container">
          <p><span class="fa fa-chevron-down"></span>&nbsp;News</p>
        </div>
      </section>
      
      <!-- Static Carousel or Dynamic Snippet -->
      <section data-snippet="s_static_carousel" 
               class="s_static_carousel o_colored_level pt0 pb0 bg-black-75 s_custom_default" 
               data-name="Static Carousel" 
               data-number-of-elements="1"
               data-custom-name="default">
        <div class="container">
          <div class="s_carousel carousel slide static_snippet_template s_product_product_borderless_1">
            <div class="carousel-inner">
              <div class="carousel-item o_colored_level pt24 pb16 active">
                <!-- Card content here -->
              </div>
            </div>
          </div>
        </div>
      </section>
      
    </div>
  </div>
</section>

<!-- JS Code Section -->
<section class="s_embed_code o_colored_level pb16 pt16 text-center s_custom_jqCode" 
         data-snippet="s_embed_code" 
         data-custom-name="jqCode">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      document.querySelector('.s_custom_controlBtn').addEventListener('click', function() {
        if (!document.body.classList.contains('editor_started')) {
          document.querySelector('.s_custom_exhibitionUpdates.s_custom_fixed').classList.toggle('active');
        }
      });
    </script>
  </div>
</section>
```

### SCSS

```scss
//  ---------- Exhibition Updates ---------- //
// 黏在 banner 底部
body:not(.editor_started) {
    .s_custom_exhibitionUpdates:not(.s_custom_fixed) {
        margin: -150px 0 30px auto;
        @include media-breakpoint-down(sm) {
            margin: 0;
        }
    }
}

.s_custom_exhibitionUpdates:not(.s_custom_fixed) {
    max-width: clamp(400px, 33vw, 500px);
    min-height: 220px;
    z-index: 5;
    padding-bottom: 10px !important;
    margin-left: auto;
    overflow: hidden;
    @include media-breakpoint-down(lg) {
        max-width: 50%;
        min-height: 80px;
        padding-bottom: 5px !important;
    }
    @include media-breakpoint-down(md) {
        max-width: 65%;
    }
    @include media-breakpoint-down(sm) {
        max-width: unset;
    }
}

// Fixed panel mode
body:not(.editor_started) {
    .s_custom_exhibitionUpdates.s_custom_fixed {
        @include media-breakpoint-up(md) {
            position: fixed;
            bottom: 10px;
            right: 0px;
            z-index: 5;
            margin: 0 23px 0px auto;
            @include transition;
        }
        .s_static_carousel,
        .s_dynamic_snippet_carousel {
            @include media-breakpoint-up(md) {
                opacity: 0;
            }
        }
        &.active {
            .s_static_carousel,
            .s_dynamic_snippet_carousel {
                @include media-breakpoint-up(md) {
                    opacity: 1;
                }
            }
            .fa-chevron-down {
                transform: rotate(180deg);
            }
        }
    }
}
```

---

## 04. Product Right Scroll

**Custom Class:** `s_custom_productRightScroll`  
**建議數量:** 最多 6 筆

### XML Structure

```xml
<section data-snippet="s_static_snippet" 
         class="s_static_snippet pt32 pb32 o_colored_level s_custom_productRightScroll" 
         data-name="Static Snippet"
         data-custom-name="productRightScroll">
  <div class="container-fluid">
    <div class="content"></div>
    <div class="static_snippet_template s_product_product_borderless_1">
      <div class="row my-4">
        
        <!-- Repeat for each product card -->
        <div class="d-flex flex-grow-0 flex-shrink-0 col-md-3 o_colored_level">
          <div class="o_carousel_product_card w-100 card-s p-3">
            <a class="o_carousel_product_img_link o_dynamic_product_hovered" href="#">
              <img class="o_carousel_product_card_img_top card-img-top" 
                   src="https://picsum.photos/400/400" 
                   alt="" loading="lazy"/>
            </a>
            <div class="o_carousel_product_card_body d-flex flex-wrap flex-column justify-content-between h-100">
              <div class="card-title mt-4">
                <h6>Product Title</h6>
              </div>
              <div>
                <div class="mt-2">
                  <p>Product description</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- End of product card -->
        
      </div>
    </div>
  </div>
</section>

<!-- JS Code Section (Required for horizontal scroll) -->
<section class="s_embed_code o_colored_level pb16 pt16 s_custom_jqCode text-center" 
         data-snippet="s_embed_code"
         data-custom-name="jqCode">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      // Full JS code - see JavaScript section below
    </script>
  </div>
</section>
```

### JavaScript

```javascript
document.addEventListener("DOMContentLoaded", function () {
    if (document.body.classList.contains("editor_started")) return;
    
    // 防抖函式
    function debounce(fn, delay) {
        let timer = null;
        return function (...args) {
            clearTimeout(timer);
            timer = setTimeout(() => fn.apply(this, args), delay);
        };
    }
    
    // 合併同一容器內多個 .row 的子元素
    function mergeRows(container) {
        const rows = Array.from(container.children).filter(child => child.classList.contains('row'));
        if (rows.length > 1) {
            const firstRow = rows[0];
            for (let i = 1; i < rows.length; i++) {
                const currentRow = rows[i];
                while (currentRow.firstElementChild) {
                    firstRow.appendChild(currentRow.firstElementChild);
                }
                currentRow.remove();
            }
        }
    }
    
    // 平滑滾動函式
    function smoothScrollBy(container, distance, duration = 300) {
        const start = container.scrollLeft;
        const startTime = performance.now();
        function scrollStep(timestamp) {
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
            container.scrollLeft = start + distance * ease;
            if (progress < 1) {
                requestAnimationFrame(scrollStep);
            }
        }
        requestAnimationFrame(scrollStep);
    }
    
    // Initialize row elements with scroll and arrow behavior
    function initRowElements() {
        const rowElements = document.querySelectorAll(".s_custom_productRightScroll >[class*=container]>[class*=_snippet_template]>.row");
        rowElements.forEach((rowElement) => {
            rowElement.style.overflowX = "auto";
            rowElement.style.overflowY = "hidden";
            rowElement.style.overscrollBehaviorX = "contain";
            
            // Create arrows if scrollable
            let leftArrow = rowElement.parentElement.querySelector('.carousel-arrow-left');
            let rightArrow = rowElement.parentElement.querySelector('.carousel-arrow-right');
            
            if (!leftArrow) {
                leftArrow = document.createElement("div");
                leftArrow.classList.add("carousel-arrow", "carousel-arrow-left");
                leftArrow.innerHTML = '<i class="fa fa-angle-left" aria-hidden="true"></i>';
                rowElement.parentElement.appendChild(leftArrow);
            }
            if (!rightArrow) {
                rightArrow = document.createElement("div");
                rightArrow.classList.add("carousel-arrow", "carousel-arrow-right");
                rightArrow.innerHTML = '<i class="fa fa-angle-right" aria-hidden="true"></i>';
                rowElement.parentElement.appendChild(rightArrow);
            }
            
            // Arrow click events
            leftArrow.addEventListener("click", function () {
                const scrollDistance = getComputedStyle(document.documentElement).getPropertyValue('--scroll-distance');
                const distance = parseFloat(scrollDistance) * window.innerWidth / 100;
                smoothScrollBy(rowElement, -distance);
            });
            rightArrow.addEventListener("click", function () {
                const scrollDistance = getComputedStyle(document.documentElement).getPropertyValue('--scroll-distance');
                const distance = parseFloat(scrollDistance) * window.innerWidth / 100;
                smoothScrollBy(rowElement, distance);
            });
        });
    }
    
    // Main process
    const containers = document.querySelectorAll('.s_custom_productRightScroll >[class*=container]>[class*=_snippet_template]');
    containers.forEach(container => mergeRows(container));
    initRowElements();
});
```

### SCSS

```scss
//  ---------- Product Right Scroll ---------- //
$showItem: 5; // 顯示幾個產品
$proListAspectRatio: 1;

:root {
  --scroll-distance: 38vw;
}
@include laptop {
  :root {
    --scroll-distance: 50vw;
  }
}
@include media-breakpoint-down(md) {
  :root {
    --scroll-distance: 80vw;
  }
}

.s_custom_productRightScroll {
    .carousel-arrow {
        height: var(--arrowWidth);
        width: var(--arrowWidth);
        border: 1px solid var(--arrowColor);
        border-radius: var(--arrowRadius);
        background: var(--arrowBg);
        position: absolute;
        top: calc(100vw / #{$showItem} / #{$proListAspectRatio} / 2);
        cursor: pointer;
        z-index: 2;
        @include transition;
        
        &:hover {
            background-color: var(--arrowBgHover);
            border-color: var(--arrowColorHover);
        }
        
        &.carousel-arrow-left {
            left: calc(var(--container-pd-x) * 2);
        }
        
        &.carousel-arrow-right {
            right: calc((100vw - #{$wrap-size}) / 2 + var(--container-pd-x));
        }
        
        &.disabled {
            opacity: 0;
        }
    }
    
    &.s_dynamic_snippet,
    &.s_static_snippet {
        .container-fluid {
            width: auto;
            padding-left: 0;
            padding-right: 0;
            @media (min-width: $wrap-size) {
                margin-left: calc((100% - 1500px) / 2) !important;
            }
        }
    }
}

#wrapwrap:not(.odoo-editor-editable) .s_custom_productRightScroll {
    &.s_dynamic_snippet,
    &.s_static_snippet {
        .row {
            flex-wrap: nowrap;
            scroll-snap-type: x mandatory;
            >div[class*="col"] {
                max-width: calc(100vw / #{$showItem} - 15px) !important;
                flex: 0 0 calc(100vw / #{$showItem} - 15px) !important;
            }
        }
    }
}
```

---

## 05. Interactive Map

**Custom Class:** `s_custom_mapEffect`  
**建議數量:** 最多 5 筆標記點

### XML Structure

```xml
<section class="s_text_block pt40 pb40 o_colored_level s_custom_mapEffect" 
         data-snippet="s_text_block" 
         data-name="Interactive Map"
         data-custom-name="map-Effect">
  <div class="container s_allow_columns">
    <div class="row">
      
      <!-- Map Image Column -->
      <div class="o_colored_level map-img-content col-lg-8 pt48">
        <div class="s_text map-brief-description" data-snippet="s_text" data-name="Text">
          <!-- Map markers - repeat for each location -->
          <div class="s_text" data-snippet="s_text" data-name="地圖標示區">
            <p>Headquarters</p>
          </div>
          <div class="s_text" data-snippet="s_text" data-name="地圖標示區">
            <p>Shanghai Branch</p>
          </div>
          <div class="s_text" data-snippet="s_text" data-name="地圖標示區">
            <p>US Branch</p>
          </div>
        </div>
        <div class="s_text map-img" data-snippet="s_text" data-name="Text">
          <p>
            <img class="img-fluid o_we_custom_image" 
                 src="https://picsum.photos/1000/600" 
                 alt="" loading="lazy"/>
          </p>
        </div>
      </div>
      
      <!-- Description Column -->
      <div class="o_colored_level map-description-content col-lg-4">
        <!-- Repeat for each location info -->
        <div class="s_text map-info" data-snippet="s_text" data-name="內容小區">
          <p class="h5">Headquarters</p>
          <p>Location description text...</p>
        </div>
        <div class="s_text map-info" data-snippet="s_text" data-name="內容小區">
          <p class="h5">Shanghai Branch</p>
          <p>Location description text...</p>
        </div>
        <div class="s_text map-info" data-snippet="s_text" data-name="內容小區">
          <p class="h5">US Branch</p>
          <p>Location description text...</p>
        </div>
      </div>
      
    </div>
  </div>
</section>

<!-- Custom CSS for marker positions -->
<section class="s_text_block o_colored_level pt0 pb0 s_custom_hidden" 
         data-snippet="s_text_block" 
         data-custom-name="hidden">
  <div class="s_allow_columns container">
    <section class="s_embed_code o_colored_level text-center pt0 pb0" data-snippet="s_embed_code">
      <div class="s_embed_code_embedded o_not_editable container">
        <style>
          /* Position markers on the map */
          body:not(.editor_started) .map-brief-description .s_text:nth-child(1) {
            right: 13%;
            top: 33.5%;
          }
          body:not(.editor_started) .map-brief-description .s_text:nth-child(2) {
            right: 14%;
            top: 29%;
          }
          body:not(.editor_started) .map-brief-description .s_text:nth-child(3) {
            left: 12%;
            bottom: 45%;
          }
        </style>
      </div>
    </section>
  </div>
</section>

<!-- JS Code Section -->
<section class="s_embed_code o_colored_level pb16 pt16 text-center s_custom_jqCode" 
         data-snippet="s_embed_code"
         data-custom-name="jqCode">
  <div class="s_embed_code_embedded o_not_editable container">
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        const body = document.body;
        if (!body.classList.contains("editor_started")) {
          const infoElements = document.querySelectorAll(".map-description-content > .s_text");
          const dotLists = document.querySelectorAll(".map-brief-description > .s_text");
          
          // Default active first items
          const defaultActiveInfo = document.querySelector(".map-description-content > .s_text:first-child");
          const defaultActiveDot = document.querySelector(".map-brief-description > .s_text:first-child");
          if (defaultActiveInfo && defaultActiveDot) {
            defaultActiveInfo.classList.add("active");
            defaultActiveDot.classList.add("active");
          }
          
          // Hover interaction
          infoElements.forEach((infoElement, index) => {
            infoElement.addEventListener("mouseenter", () => {
              infoElements.forEach(info => info.classList.remove("active"));
              dotLists.forEach(dot => dot.classList.remove("active"));
              const targetDot = dotLists[index];
              if (infoElement && targetDot) {
                infoElement.classList.add("active");
                targetDot.classList.add("active");
              }
            });
          });
        }
      });
    </script>
  </div>
</section>
```

### SCSS

```scss
//  ---------- Interactive Map ---------- //
.s_custom_mapEffect {
    @include media-breakpoint-down(md) {
        overflow: hidden;
    }
    >[class*=container]>.row {
        align-items: flex-start;
    }
}

body:not(.editor_started) {
    .map-brief-description {
        list-style: none;
        .s_text {
            width: 80px;
            height: 80px;
            position: absolute;
            @include media-breakpoint-down(xs) {
                width: 55px;
                height: 55px;
            }
            &::before {
                content: "";
                width: 10px;
                height: 10px;
                display: block;
                border-radius: 5px;
                background-color: var(--o-color-1);
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
                z-index: 1;
            }
            &::after {
                content: "";
                width: 80px;
                height: 80px;
                border-radius: 40px;
                background-color: color-mix(in srgb, var(--o-color-1) 70%, #fff 0%);
                display: block;
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
                opacity: 0;
                @include transition;
            }
            p {
                color: #fff;
                position: absolute;
                margin-bottom: 0;
                padding: 5px 30px;
                border-radius: 30px;
                background-color: var(--o-color-1);
                white-space: nowrap;
                font-size: 16px;
                opacity: 0;
                z-index: 2;
                top: -35px;
                right: 0;
                @include transition;
            }
            &.active {
                &::before {
                    background-color: #fff;
                }
                &::after {
                    animation: blink 1s infinite;
                }
                p {
                    opacity: 1;
                }
            }
        }
    }
}

.map-img-content {
    @include media-breakpoint-up(lg) {
        position: sticky;
        top: 150px;
    }
}

.map-description-content {
    @include media-breakpoint-up(xl) {
        padding-left: 50px;
    }
    .map-info {
        padding: 30px;
        border-radius: 8px;
        @include transition;
        &.active {
            color: #fff;
            background-color: var(--o-color-1);
        }
    }
}

@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0.5; }
    100% { opacity: 1; }
}
```

---

## 06. Sticky Background

**Custom Class:** `s_custom_stickyBG`  
**說明:** 內文固定 + 背景圖 fix 效果

### XML Structure

```xml
<section class="s_column_layout o_colored_level pb48 o_auto_screen_height pt48 s_custom_stickyBG" 
         data-sticky="used" 
         data-snippet="s_column_layout" 
         data-name="Horizontal Layout"
         data-custom-name="stickyBG">
  <div class="col-wrapper container">
    <div class="row d-flex align-items-stretch">
      
      <!-- Text Content Column -->
      <div class="col-right text-content o_colored_level col-lg-8">
        <div class="s_column_layout_content oe_structure oe_structure_not_nest oe_empty">
          <!-- Content sections here -->
        </div>
      </div>
      
      <!-- Sticky Image Column -->
      <div class="s_col_no_bgcolor col-left img-content col-lg-9 pt32">
        <div class="s_column_layout_content oe_structure oe_structure_not_nest oe_empty col-sticky" 
             style="top: 111px;">
          <section class="s_text_block o_colored_level pt0 pb0 s_custom_fixImg" 
                   data-snippet="s_text_block" 
                   data-custom-name="fixImg">
            <div class="s_allow_columns container">
              <p>
                <img class="img-fluid o_we_custom_image" 
                     src="https://picsum.photos/1200/800" 
                     alt="" loading="lazy" style="width: 100% !important;"/>
              </p>
            </div>
          </section>
        </div>
      </div>
      
    </div>
  </div>
</section>
```

### SCSS

```scss
//  ---------- Sticky Background ---------- //
.s_custom_stickyBG {
    .img-content {
        @include media-breakpoint-down(md) {
            z-index: -1;
        }
    }
}

body:not(.editor_started) {
    .s_custom_stickyBG {
        .col-sticky {
            z-index: -1;
            @include media-breakpoint-down(sm) {
                position: sticky;
            }
        }
        .text-content {
            margin-right: calc(100% / 12 * -5);
            @include media-breakpoint-down(md) {
                padding-top: 26vh;
                margin-right: -100%;
            }
        }
    }
    .s_custom_fixImg {
        margin-right: calc((#{$wrap-size} - 100vw) / 2);
        @media (max-width: $wrap-size) {
            margin-right: calc(var(--container-pd-x) * -1);
            margin-left: calc(var(--container-pd-x) * -1);
        }
    }
}
```

---

## 07. Full Hover Background

**Custom Class:** `s_custom_fullHoverBackground`  
**建議數量:** 最多 6 筆

> [!NOTE]
> 複製使用後請**手動移除**第一個 section 的 `s_custom_hidden` 樣式

### XML Structure

```xml
<section data-snippet="s_vertical_layout" 
         class="s_vertical_layout o_colored_level o_cc o_cc1 pb0 pt80 s_custom_fullHoverBackground" 
         data-name="Custom Vertical Layout"
         data-custom-name="fullHoverBackground">
  <div class="container-fluid">
    <div class="oe_structure oe_structure_not_nest oe_empty">
      
      <!-- Title Section -->
      <section class="s_text_block o_colored_level pt0 pb0 o_cc o_cc1 s_custom_textUppercase s_custom_textCenter" 
               data-snippet="s_text_block" 
               data-custom-name="textUppercase textCenter">
        <div class="s_allow_columns container">
          <h2 style="text-align: center;">Industries We Serve</h2>
        </div>
      </section>
      
      <!-- Static Snippet with Cards -->
      <section data-snippet="s_static_snippet" 
               class="s_static_snippet pt32 pb32 o_colored_level o_cc o_cc1 s_custom_indexApplication" 
               data-name="Static Snippet"
               data-staticsnippet-template="horizontal"
               data-custom-name="indexApplication">
        <div class="container">
          <div class="static_snippet_template s_product_product_horizontal">
            <div class="row my-4">
              <!-- Repeat card structure for each item -->
              <div class="d-flex flex-grow-0 flex-shrink-0 col-sm-6 col-md-6 col-lg-4 o_colored_level">
                <div class="o_carousel_product_card card-s w-100 bg-light p-3">
                  <div class="row h-100">
                    <div class="position-static o_colored_level col-lg-12">
                      <img class="img img-fluid mx-auto" 
                           src="https://picsum.photos/600/400" 
                           alt="" loading="lazy"/>
                    </div>
                    <div class="o_carousel_product_card_body pl-3 d-flex flex-column justify-content-between o_colored_level col-lg-12">
                      <div class="info-wrap">
                        <div class="card-title">
                          <h4><strong>Title</strong></h4>
                        </div>
                        <div class="mb-2">
                          <p>Description text...</p>
                        </div>
                        <div class="btn-wrap">
                          <a href="#">more <i class="fa fa-angle-right"></i></a>
                        </div>
                      </div>
                      <div class="d-flex justify-content-between align-items-center flex-wrap icon-wrap">
                        <div class="o_dynamic_snippet_btn_wrapper">
                          <a href="#" class="cus-icon-btn">
                            <img class="img-fluid" src="/path/to/icon.svg" alt=""/>
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Background image layers -->
        <div class="bg-image bg1 active" style="background-image: url('https://picsum.photos/1920/1080');"></div>
        <div class="bg-image bg2" style="background-image: url('https://picsum.photos/1920/1080');"></div>
      </section>
      
      <!-- Optional: All Category Button -->
      <section class="s_text_block o_colored_level pt0 mt-4 mt-lg-0 text-center pb0 s_custom_allCatBtn" 
               data-snippet="s_text_block" 
               data-custom-name="allCatBtn">
        <div class="s_allow_columns container">
          <p>
            <a href="#" class="btn btn-primary">Application Overview</a>
          </p>
        </div>
      </section>
      
    </div>
  </div>
</section>
```

---

## 08. Worldwide Scroll

**Custom Class:** `s_custom_worldwide`  
**說明:** 上圖下文卡片水平捲軸

### XML Structure

```xml
<section class="s_faq_collapse pt32 pb32 o_colored_level s_custom_worldwide" 
         data-snippet="s_faq_collapse" 
         data-name="Accordion"
         data-custom-name="worldwide">
  <div class="container">
    <div class="accordion" role="tablist">
      
      <!-- Repeat .card for each item -->
      <div class="card" data-name="Item">
        <a href="#" role="tab" data-toggle="collapse" aria-expanded="true" 
           class="card-header o_default_snippet_text s_faq_collapse_right_icon" 
           data-target="#myCollapseTab1">Card Title</a>
        <div class="collapse show" role="tabpanel" id="myCollapseTab1">
          <div class="card-body">
            <ul class="card-text">
              <li>Item 1</li>
              <li>Item 2</li>
              <li>Item 3</li>
            </ul>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</section>
```

### SCSS

```scss
//  ---------- Worldwide Scroll ---------- //
:root {
    --scroll-distance2: 380px;
    --list-row: 2;
}

.s_custom_worldwide {
    >.container:hover {
        .carousel-arrow:not(.disabled) {
            opacity: 1;
        }
    }
    .accordion {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        padding: 25px 0;
    }
    .card {
        width: 380px !important;
        max-width: 380px !important;
        flex: 0 0 380px !important;
        margin: 0 10px;
        border: 1px solid rgba(0, 0, 0, 0.125);
        background-color: rgba(255, 255, 255, 0.8) !important;
        box-shadow: 0px 0px 6px 3px rgba(0, 0, 0, 0.09);
        overflow: hidden;
        
        .collapse {
            display: block !important;
        }
        .card-header {
            background-color: transparent;
            font-weight: 700;
            &::before {
                display: none !important;
            }
        }
        ul.card-text {
            padding-left: 20px;
            margin: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 3px 28px;
            li {
                width: calc((100% / var(--list-row)) - (28px * (var(--list-row) - 1)) / var(--list-row));
            }
        }
    }
}
```

---

## 09. Worldwide RWD Collapse

**Custom Class:** `s_custom_worldwideRWDcollapse`  
**說明:** 桌機為捲軸模式，RWD 時改為收合模式

與 [08. Worldwide Scroll](#08-worldwide-scroll) 結構相同，只是在 RWD 時行為不同。

---

## Usage Guidelines

> [!IMPORTANT]
> **AI 生成規則:**
> 1. 只複製 XML 結構和 SCSS，不需要 `<style>` 標籤
> 2. JavaScript 必須放在 `s_custom_jqCode` 區塊內
> 3. 圖片使用 `https://picsum.photos/` 作為 placeholder
> 4. 確保 `data-custom-name` 屬性與 class 中 `s_custom_` 後的名稱對應

### Common Patterns

1. **Custom Class Naming:** `s_custom_[componentName]`
2. **Data Attribute:** `data-custom-name="[componentName]"`
3. **JS Code Container:** `s_custom_jqCode`
4. **Hidden Elements:** `s_custom_hidden`

### Dependencies

確保專案 SCSS 中有以下 mixins:
- `@include transition;`
- `@include media-breakpoint-down(md);`
- `@include media-breakpoint-up(lg);`
- `@include clamp-2;`
- `$wrap-size` 變數
- `$primary`, `$secondary`, `$default` 顏色變數
