# 頁面樣板配方 (Page Templates)

> [!IMPORTANT]
> 每個 Home 頁面都有**完整的 XML + SCSS 範本檔**，可直接讀取使用。
> 元件配方用於了解頁面組成，方便局部替換時查找對應元件。

---

## 使用方式

### 模式一：整頁範本（最快）
直接讀取對應的 XML + SCSS 檔案，替換文案、圖片即可。

| 頁面 | XML 範本 | SCSS 範本 |
|------|---------|----------|
| Home-1 | `templates/home-1.xml` (613 行) | `templates/home-1.scss` |
| Home-2 | `templates/home-2.xml` (609 行) | `templates/home-2.scss` |
| Home-3 | `templates/home-3.xml` (599 行) | `templates/home-3.scss` |
| Home-4 | `templates/home-4.xml` (582 行) | `templates/home-4.scss` |

### 模式二：混搭組合
用配方了解區塊組成，再到 `custom_blocks.md` 查找個別元件的 XML 來源進行替換。

---

## 頁面配方

### Home-1
```
Banner-01 (bannerGeometricTriangle 三角形遮罩輪播)
→ Content-01 (iconCardHorizontal 1x1，col-lg-6 橫式 4 欄 icon 卡片)
→ Products-01 (upperNext 動態產品輪播)
→ Carousel-01 (carouselHoverBgEffect Hover 背景漸變放大)
→ 圖文區 (s_text_image + titleUnderLine)
→ News-01 (newsSummary dateLeft 左大圖+右日期列表)
```

### Home-2
```
Odoo 原生輪播 (s_carousel_default，非自訂 Banner)
→ Content-02 (iconCardHorizontal 上標題+中描述+底部圓形 icon 列表)
→ Static-02 (threeChains 三段式背景穿插，內含：圖文 + 文字 + scaleL 產品卡 + 雙按鈕)
→ Carousel-02 (staticCarousel2 四欄滿版相簿輪播)
→ 視差背景品牌區 + Content-06 (counterPrimary 數字計數器)
→ 動態部落格 News (s_blog_post_card)
```

### Home-3
```
Banner-03 (textleftmiddle 左文影片背景)
→ 文字介紹區塊
→ Content-19 (insertBelow 左圖+右計數器＋底文)
→ Content-18 (reverse 左右反轉文字區)
→ Static-05 (fullWrapProduct 滿版分類卡片 - 靜態)
→ 動態產品 (fullWrapProduct 動態版)
→ Static-06 (staggerBricks 交錯磚牆卡片)
→ Content-18 (reverse 第二組)
→ Content-20 (fullScreenParallax 全螢幕視差 ×2)
→ 動態部落格 News (s_dynamic_snippet_carousel)
```

### Home-4
```
Banner-04 (純影片滿版)
→ ContentJS-03 (exhibitionUpdates 固定側欄最新消息)
→ ContentJS-04 (productRightScroll 靜態卡片 + 動態產品輪播)
→ Content-21 (counterAfterColor 計數器+色彩後綴)
→ ContentJS-05 (mapEffect 互動地圖)
→ interlaceCarousel (交錯輪播)
→ 動態部落格 News (s_blog_post_card)
→ Static-01 (titleUpperBg 字壓圖 CTA)
```

---

## 注意事項

1. **不生成說明區塊** — 網站上的「複製 SCSS / 不要變更」區塊是維運用，生成頁面時跳過
2. **SCSS 提取** — 若需要元件 SCSS，讀取與 XML 同名的 `.scss` 檔案
3. **圖片** — 使用 `https://picsum.photos/[width]/[height]` 作為佔位圖
