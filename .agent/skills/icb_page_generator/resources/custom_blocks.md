# 客製化區塊索引 (Custom Blocks Index)

> [!IMPORTANT]
> 此檔為**索引**，不包含程式碼。AI 需要某個元件時，請到 `templates/improved/` 讀取對應子目錄的檔案指定行數範圍，並讀取同名 `.scss` 取得樣式。

---

## A. Banner (橫幅輪播)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 | SCSS 來源 |
|------|---------|---------------------|---------|----------|
| Banner-01 | 三角形遮罩輪播 | `bannerGeometricTriangle` | `templates/improved/banners/banner.xml` L11~L83 | `templates/improved/banners/banner.scss` |
| Banner-02 | Ken Burns 縮放 | `banner2` | `templates/improved/banners/banner.xml` L89~L185 | `templates/improved/banners/banner.scss` |
| Banner-03 | 左文影片背景 | `textleftmiddle` | `templates/improved/banners/banner.xml` L191~L230 | `templates/improved/banners/banner.scss` |
| Banner-04 | 純影片滿版 | `pureVideoBanner` | `templates/improved/banners/banner.xml` L236~L263 | `templates/improved/banners/banner.scss` |

## B. Content - 靜態圖文

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 | SCSS 來源 |
|------|---------|---------------------|---------|----------|
| Content-01 | 橫式 icon 卡片 4 欄 | `iconCardHorizontal 1x1` | `templates/improved/content-sections/content-sections.xml` 排版區塊-01 | `templates/improved/content-sections/content-sections.scss` |
| Content-02 | 上標題+底部圓形 icon 列 | `iconCardHorizontal 1x1` | `templates/improved/content-sections/content-sections.xml` 排版區塊-02 | `templates/improved/content-sections/content-sections.scss` |
| Content-03 | 出血頁籤切換 | `tabEffect` | `templates/improved/content-sections/content-sections.xml` 排版區塊-03 | `templates/improved/content-sections/content-sections.scss` |
| Content-04 | Hover 背景放大描述 | `hoverBgTextEfect` | `templates/improved/content-sections/content-sections.xml` L483+ | `templates/improved/content-sections/content-sections.scss` |
| Content-05 | 視差錯位滾動 | `scrollItemBgFix` | `templates/improved/content-sections/content-sections.xml` L587+ | `templates/improved/content-sections/content-sections.scss` |
| Content-06 | 數字計數器 (主色) | `counterPrimary` | `templates/improved/content-sections/content-sections.xml` L655+ | `templates/improved/content-sections/content-sections.scss` |
| Content-07 | 左文右手風琴 FAQ | `simpleFAQ` | `templates/improved/content-sections/content-sections.xml` L717+ | `templates/improved/content-sections/content-sections.scss` |
| Content-08 | 滿版描述+背景圖 | `descriptUpperBanner fullContainer` | `templates/improved/content-sections/content-sections.xml` L782+ | `templates/improved/content-sections/content-sections.scss` |
| Content-09 | 左文右圓角圖卡 | (標準佈局) | `templates/improved/content-sections/content-sections.xml` L850+ | `templates/improved/content-sections/content-sections.scss` |
| Content-10 | 單側圖片滿版 | `imgFillContent` | `templates/improved/content-sections/content-sections.xml` L910+ | `templates/improved/content-sections/content-sections.scss` |
| Content-11 | 傾斜溢出背景 | `leaningOverflow` | `templates/improved/content-sections/content-sections-2.xml` L13~L71 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-12 | 左 Sticky 右滾動 | `pageIntro` | `templates/improved/content-sections/content-sections-2.xml` L86~L136 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-13 | 圖文多段描述 | `moreDescription` | `templates/improved/content-sections/content-sections-2.xml` L144~L206 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-14 | 兩欄 Sticky 靜態輪播 | (標準佈局) | `templates/improved/content-sections/content-sections-2.xml` L215~L325 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-15 | 左文右多輪播 | `textmultiCarousel` | `templates/improved/content-sections/content-sections-2.xml` L334~L450 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-16 | 左圖右文+底計數器 | `textUnderFeature` | `templates/improved/content-sections/content-sections-2.xml` L459~L579 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-17 | 左小標右大段文 | (標準 `s_text_block`) | `templates/improved/content-sections/content-sections-2.xml` L588~L607 | 無 |
| Content-18 | 左右反轉文字區 | `reverse` | `templates/improved/content-sections/content-sections-2.xml` L617~L636 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-19 | 左圖+右計數器+底文 | `insertBelow` | `templates/improved/content-sections/content-sections-2.xml` L646~L721 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-20 | 全螢幕視差 | `fullScreenParallax` | `templates/improved/content-sections/content-sections-2.xml` L730~L757 | `templates/improved/content-sections/content-sections-2.scss` |
| Content-21 | 計數器+色彩後綴 | `counterAfterColor` | `templates/improved/content-sections/content-sections-3.xml` L13~L86 | `templates/improved/content-sections/content-sections-3.scss` |
| Content-22 | 固定背景+右半卡片 | `fixBGList` | `templates/improved/content-sections/content-sections-3.xml` L96~L140 | `templates/improved/content-sections/content-sections-3.scss` |
| Content-23 | 磚牆相簿+彈窗輪播 | `brickAlbum` | `templates/improved/content-sections/content-sections-3.xml` L154~L268 | `templates/improved/content-sections/content-sections-3.scss` |

## C. Content-JS (含 JS 互動)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| ContentJS-01 | Hover 按鈕切換 (暗底) | `fullImgHoevr1` | `templates/improved/content-sections/content-sections-js.xml` L21~L170 |
| ContentJS-02 | Hover 卡片展開 | `fullImgHoevr2` | `templates/improved/content-sections/content-sections-js.xml` L189~L395 |
| ContentJS-03 | 固定側欄最新消息 | `exhibitionUpdates fixed` | `templates/improved/content-sections/content-sections-js.xml` L409~L474 |
| ContentJS-04 | 水平滑動產品列表 | `productRightScroll` | `templates/improved/content-sections/content-sections-js.xml` L489~L776 |
| ContentJS-05 | 互動地圖效果 | `mapEffect` | `templates/improved/content-sections/content-sections-js.xml` L792+ |
| ContentJS-06 | 內文固定 + 背景圖 fix | `stickyBG` | `templates/improved/content-sections/content-sections-js.xml` L1118~L1290 |
| ContentJS-07 | icon 背景圖互動 | `fullHoverBackground` | `templates/improved/content-sections/content-sections-js.xml` L1579~L2113 |
| ContentJS-08 | 上圖下文：下方文字 x 卷軸 | `worldwide` | `templates/improved/content-sections/content-sections-js.xml` L2297~L2483 |
| ContentJS-09 | 上圖下文：下方文字 x 卷軸 (RWD 收合) | `worldwideRWDcollapse simpleFAQ` | `templates/improved/content-sections/content-sections-js.xml` L2665~L2736 |

## D. Static Snippet (靜態卡片)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| Static-01 | 字壓圖卡片 | `titleUpperBg` | `templates/improved/carousels/customized-Static-Snippet.xml` L23~L67 |
| Static-02 | 三段式背景穿插 | `threeChains` | `templates/improved/carousels/customized-Static-Snippet.xml` L71~L273 |
| Static-03 | RWD 水平滑動 (圓角) | `RWDscroll` | `templates/improved/carousels/customized-Static-Snippet.xml` L274~L387 |
| Static-04 | 橫式特色圖標卡片 | `textBlock` | `templates/improved/carousels/customized-Static-Snippet.xml` L388~L527 |
| Static-05 | 滿版分類卡片 | `fullWrapProduct` | `templates/improved/carousels/customized-Static-Snippet.xml` L528~L680 |
| Static-06 | 交錯磚牆卡片 | `staggerBricks` | `templates/improved/carousels/customized-Static-Snippet.xml` L681+ |

## E. Static Carousel (靜態輪播)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| Carousel-01 | Hover 背景漸變放大 | `carouselHoverBgEffect` | `templates/improved/carousels/customized-static-carousel.xml` |
| Carousel-02 | 四欄滿版相簿輪播 | `staticCarousel2` | `templates/improved/carousels/customized-static-carousel.xml` |

## F. Dynamic Products (動態產品)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| Products-01 | 左文右滿版輪播 | `upperNext products01` | `templates/improved/dynamic/products/customized-dynamic-products.xml` |
| Products-02 | 視差背景產品 | `upperNext products02` | `templates/improved/dynamic/products/customized-dynamic-products.xml` |
| Products-03 | 全寬產品展示 | `products03` | `templates/improved/dynamic/products/customized-dynamic-products.xml` |

## G. Dynamic News (動態消息)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| News-01 | 左大圖+右日期列表 | `newsSummary dateLeft` | `templates/improved/dynamic/news/customized-dynamic-news.xml` |

## H. 按鈕風格 (全站擇一)

| 編號 | 中文名稱 | SCSS 標記 |
|------|---------|---------|
| Btn-01 | 右下角斜切 | `按鈕，右下角斜切` |
| Btn-02 | 普通箭頭 | `按鈕，普通箭頭` |
| Btn-03 | 細箭頭 | `按鈕，細箭頭` |
| Btn-04 | 圓點放大 | `按鈕，實心圓點放大` |
| Btn-05 | 閃光效果 | `按鈕，閃光效果` |
| Btn-06 | 傾斜填滿 | `按鈕，hover 傾斜填滿` |

## I. 通用小元件

- **Pre-Footer CTA** (行動呼叫區塊)
- **s_counting** (數字計數器)
- **titleUnderLine** (標題底線裝飾)

## J. Timeline (歷史沿革)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 | SCSS 來源 |
|------|---------|---------------------|---------|----------|
| Timeline-01 | 中線交錯圖文 | `timeLine01` | `templates/improved/timelines/time-line.xml` time line-01 | `templates/improved/timelines/time-line.scss` time line 01 |
| Timeline-02 | 中線卡片交錯 | `timeLine02` | `templates/improved/timelines/time-line.xml` time line-02 | `templates/improved/timelines/time-line.scss` time line 02 |
| Timeline-03 | 波浪背景時間軸 | `timeLine03` | `templates/improved/timelines/time-line.xml` time line-03 | `templates/improved/timelines/time-line.scss` time line 03 |
| Timeline-04 | 左線卡片列 | `timeLine04` | `templates/improved/timelines/time-line.xml` time line-04 | `templates/improved/timelines/time-line.scss` time line 04 |
| Timeline-05 | 日期浮框卡片 | `timeLine05` | `templates/improved/timelines/time-line.xml` time line-05 | `templates/improved/timelines/time-line.scss` time line 05 |
| Timeline-06 | 雙色背景交錯 | `timeLine06` | `templates/improved/timelines/time-line.xml` time line-06 | `templates/improved/timelines/time-line.scss` time line 06 |
| Timeline-07 | 圖文左右流程 | `time-line-07` | `templates/improved/timelines/time-line.xml` time line-07 | `templates/improved/timelines/time-line.scss` time line 07 |
| Timeline-08 | 中線左右交錯 | `time-line-08` | `templates/improved/timelines/time-line.xml` time line-08 | `templates/improved/timelines/time-line.scss` time line 08 |
