# Home Page (Menu-03) 設計說明

## 目標
- 以 `/page` 套版模式產出首頁 XML + SCSS
- 頁面主體使用既有 templates 片段組裝，不改動 Odoo 原生結構
- Header 使用 `menu-03` 的 SCSS 覆寫，不輸出 header XML

## 區塊順序 (由上到下)
1. Banner-03：左文背景影片輪播 (textleftmiddle)
2. Content-01：iconCardHorizontal 1x1 (四欄 icon 卡片)
3. Content-03：tabEffect (左側分頁 + 右側滿版媒體)
4. ContentJS-02：fullImgHoevr2 (hover 展開卡片，含 JS)
5. 最新消息：Dynamic Blog (預設 `s_blog_post_card`)

## 元件來源
- Banner-03：`templates/banner.xml` + `templates/banner.scss`
- Content-01、Content-03：`templates/content-sections.xml` + `templates/content-sections.scss`
- ContentJS-02：`templates/content-sections-js.xml` + `templates/content-sections-js.scss`
- Header menu-03：`templates/header-menus.scss` 的 MENU-3 區塊

## 動態最新消息規則
- 使用 `s_dynamic_snippet` (Blog)
- Template key：`website_blog.dynamic_filter_template_blog_post_card`
- class 包含 `s_blog_post_card`，不新增未定義的自訂 class

## 影像與佔位
- 所有圖片統一使用 `https://picsum.photos/` 作為佔位
- 背景圖與 img src 均替換為 picsum URL

## Odoo 結構與規範
- 首頁需包含 `t-set="pageName"`
- 每個 `section` 皆保留 `.container` 或 `.container-fluid`
- JS 互動只放在 `s_embed_code` 區塊，避免污染編輯模式

## 輸出
- XML 與 SCSS 皆輸出至 `outputs/`
- 檔名必須包含日期與時間
