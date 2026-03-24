# 客製化區塊索引 (Custom Blocks Index)

> [!IMPORTANT]
> 此檔為**索引**，不包含程式碼。AI 需要某個元件時，請到 `templates/` 讀取對應檔案的指定行數範圍，並讀取同名 `.scss` 取得樣式。

---

## A. Banner (橫幅輪播)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 | SCSS 來源 |
|------|---------|---------------------|---------|----------|
| Banner-01 | 三角形遮罩輪播 | `bannerGeometricTriangle` | `banner.xml` L11~L83 | `banner.scss` |
| Banner-02 | Ken Burns 縮放 | `banner2` | `banner.xml` L89~L185 | `banner.scss` |
| Banner-03 | 左文影片背景 | `textleftmiddle` | `banner.xml` L191~L230 | `banner.scss` |
| Banner-04 | 純影片滿版 | `pureVideoBanner` | `banner.xml` L236~L263 | `banner.scss` |

## B. Content - 靜態圖文

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 | SCSS 來源 |
|------|---------|---------------------|---------|----------|
| Content-01 | 橫式 icon 卡片 4 欄 | `iconCardHorizontal 1x1` | `content-sections.xml` 排版區塊-01 | `content-sections.scss` |
| Content-02 | 上標題+底部圓形 icon 列 | `iconCardHorizontal 1x1` | `content-sections.xml` 排版區塊-02 | `content-sections.scss` |
| Content-03 | 出血頁籤切換 | `tabEffect` | `content-sections.xml` 排版區塊-03 | `content-sections.scss` |
| Content-04 | Hover 背景放大描述 | `hoverBgTextEfect` | `content-sections.xml` L483+ | `content-sections.scss` |
| Content-05 | 視差錯位滾動 | `scrollItemBgFix` | `content-sections.xml` L587+ | `content-sections.scss` |
| Content-06 | 數字計數器 (主色) | `counterPrimary` | `content-sections.xml` L655+ | `content-sections.scss` |
| Content-07 | 左文右手風琴 FAQ | `simpleFAQ` | `content-sections.xml` L717+ | `content-sections.scss` |
| Content-08 | 滿版描述+背景圖 | `descriptUpperBanner fullContainer` | `content-sections.xml` L782+ | `content-sections.scss` |
| Content-09 | 左文右圓角圖卡 | (標準佈局) | `content-sections.xml` L850+ | `content-sections.scss` |
| Content-10 | 單側圖片滿版 | `imgFillContent` | `content-sections.xml` L910+ | `content-sections.scss` |
| Content-11 | 傾斜溢出背景 | `leaningOverflow` | `content-sections-2.xml` L13~L71 | `content-sections-2.scss` |
| Content-12 | 左 Sticky 右滾動 | `pageIntro` | `content-sections-2.xml` L86~L136 | `content-sections-2.scss` |
| Content-13 | 圖文多段描述 | `moreDescription` | `content-sections-2.xml` L144~L206 | `content-sections-2.scss` |
| Content-14 | 兩欄 Sticky 靜態輪播 | (標準佈局) | `content-sections-2.xml` L215~L325 | `content-sections-2.scss` |
| Content-15 | 左文右多輪播 | `textmultiCarousel` | `content-sections-2.xml` L334~L450 | `content-sections-2.scss` |
| Content-16 | 左圖右文+底計數器 | `textUnderFeature` | `content-sections-2.xml` L459~L579 | `content-sections-2.scss` |
| Content-17 | 左小標右大段文 | (標準 `s_text_block`) | `content-sections-2.xml` L588~L607 | 無 |
| Content-18 | 左右反轉文字區 | `reverse` | `content-sections-2.xml` L617~L636 | `content-sections-2.scss` |
| Content-19 | 左圖+右計數器+底文 | `insertBelow` | `content-sections-2.xml` L646~L721 | `content-sections-2.scss` |
| Content-20 | 全螢幕視差 | `fullScreenParallax` | `content-sections-2.xml` L730~L757 | `content-sections-2.scss` |
| Content-21 | 計數器+色彩後綴 | `counterAfterColor` | `content-sections-3.xml` L13~L86 | `content-sections-3.scss` |
| Content-22 | 固定背景+右半卡片 | `fixBGList` | `content-sections-3.xml` L96~L140 | `content-sections-3.scss` |
| Content-23 | 磚牆相簿+彈窗輪播 | `brickAlbum` | `content-sections-3.xml` L154~L268 | `content-sections-3.scss` |

## C. Content-JS (含 JS 互動)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| ContentJS-01 | Hover 按鈕切換 (暗底) | `fullImgHoevr1` | `content-sections-js.xml` L21~L170 |
| ContentJS-02 | Hover 卡片展開 | `fullImgHoevr2` | `content-sections-js.xml` L189~L395 |
| ContentJS-03 | 固定側欄最新消息 | `exhibitionUpdates fixed` | `content-sections-js.xml` L409~L474 |
| ContentJS-04 | 水平滑動產品列表 | `productRightScroll` | `content-sections-js.xml` L489~L776 |
| ContentJS-05 | 互動地圖效果 | `mapEffect` | `content-sections-js.xml` L792+ |
| ContentJS-06 | 內文固定 + 背景圖 fix | `stickyBG` | `content-sections-js.xml` L1118~L1290 |
| ContentJS-07 | icon 背景圖互動 | `fullHoverBackground` | `content-sections-js.xml` L1579~L2113 |
| ContentJS-08 | 上圖下文：下方文字 x 卷軸 | `worldwide` | `content-sections-js.xml` L2297~L2483 |
| ContentJS-09 | 上圖下文：下方文字 x 卷軸 (RWD 收合) | `worldwideRWDcollapse simpleFAQ` | `content-sections-js.xml` L2665~L2736 |

## D. Static Snippet (靜態卡片)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| Static-01 | 字壓圖卡片 | `titleUpperBg` | `customized-Static-Snippet.xml` L23~L67 |
| Static-02 | 三段式背景穿插 | `threeChains` | `customized-Static-Snippet.xml` L71~L273 |
| Static-03 | RWD 水平滑動 (圓角) | `RWDscroll` | `customized-Static-Snippet.xml` L274~L387 |
| Static-04 | 橫式特色圖標卡片 | `textBlock` | `customized-Static-Snippet.xml` L388~L527 |
| Static-05 | 滿版分類卡片 | `fullWrapProduct` | `customized-Static-Snippet.xml` L528~L680 |
| Static-06 | 交錯磚牆卡片 | `staggerBricks` | `customized-Static-Snippet.xml` L681+ |

## E. Static Carousel (靜態輪播)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| Carousel-01 | Hover 背景漸變放大 | `carouselHoverBgEffect` | `customized-static-carousel.xml` |
| Carousel-02 | 四欄滿版相簿輪播 | `staticCarousel2` | `customized-static-carousel.xml` |

## F. Dynamic Products (動態產品)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| Products-01 | 左文右滿版輪播 | `upperNext products01` | `customized-dynamic-products.xml` |
| Products-02 | 視差背景產品 | `upperNext products02` | `customized-dynamic-products.xml` |
| Products-03 | 全寬產品展示 | `products03` | `customized-dynamic-products.xml` |

## G. Dynamic News (動態消息)

| 編號 | 中文名稱 | `data-custom-name` | XML 來源 |
|------|---------|---------------------|---------|
| News-01 | 左大圖+右日期列表 | `newsSummary dateLeft` | `customized-dynamic-news.xml` |

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
| Timeline-01 | 中線交錯圖文 | `timeLine01` | `time-line.xml` time line-01 | `time-line.scss` time line 01 |
| Timeline-02 | 中線卡片交錯 | `timeLine02` | `time-line.xml` time line-02 | `time-line.scss` time line 02 |
| Timeline-03 | 波浪背景時間軸 | `timeLine03` | `time-line.xml` time line-03 | `time-line.scss` time line 03 |
| Timeline-04 | 左線卡片列 | `timeLine04` | `time-line.xml` time line-04 | `time-line.scss` time line 04 |
| Timeline-05 | 日期浮框卡片 | `timeLine05` | `time-line.xml` time line-05 | `time-line.scss` time line 05 |
| Timeline-06 | 雙色背景交錯 | `timeLine06` | `time-line.xml` time line-06 | `time-line.scss` time line 06 |
| Timeline-07 | 圖文左右流程 | `time-line-07` | `time-line.xml` time line-07 | `time-line.scss` time line 07 |
| Timeline-08 | 中線左右交錯 | `time-line-08` | `time-line.xml` time line-08 | `time-line.scss` time line 08 |
