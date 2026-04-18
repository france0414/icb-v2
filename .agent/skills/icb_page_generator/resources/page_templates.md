# 頁面樣板配方 (Page Templates)

> [!IMPORTANT]
> Home 頁面配方已改為輕量索引格式。
> 詳細區塊組裝資訊（data-snippet、s_custom_* class、data-* 屬性）請讀：
> `.agent/skills/icb_page_generator/resources/home_recipes.md`

---

## 使用方式

讀取 `home_recipes.md` 取得目標配方的完整區塊清單，直接照此組裝 XML。
不需要讀取任何外部 XML 範本檔。

| 配方 | 特色 |
|------|------|
| home-1 | 三角遮罩 Banner + 橫式 icon 卡 + 動態產品 + HoverBg 輪播 + 新聞 |
| home-2 | 原生輪播 + 三段穿插 + 四欄輪播 + counter + 部落格 |
| home-3 | 影片 Banner + 滿版產品 + 視差 × 2 + 部落格輪播 |
| home-4 | 純影片 Banner + 固定側欄新聞 + 互動地圖 + 交錯輪播 |

---

## 注意事項

1. **不生成說明區塊** — 網站上的「複製 SCSS / 不要變更」區塊是維運用，生成頁面時跳過
2. **SCSS 來源** — 每個區塊的 SCSS 來源已列在 `home_recipes.md` 各區塊說明中
3. **圖片** — 使用 `https://picsum.photos/[width]/[height]` 作為佔位圖
