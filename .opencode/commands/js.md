# js

從元件庫中選擇並插入互動 JS 元件。

## Steps

1. 讀取 `.agent/skills/icb_page_generator/resources/component_library.md`
2. 參考以下菜單選擇適合的互動元件：

| # | 元件名稱 | Custom Class | 效果描述 |
|---|----------|--------------|----------|
| 1 | Full Image Hover 1 | `fullImgHoevr1` | Hover 切換大圖，左側導航按鈕 |
| 2 | Full Image Hover 2 | `fullImgHoevr2` | Hover 滑入顯示背景大圖 |
| 3 | Exhibition Updates | `exhibitionUpdates` | 右側固定滑入新聞面板 |
| 4 | Product Right Scroll | `productRightScroll` | 水平滾動產品卡片列 |
| 5 | Interactive Map | `mapEffect` | 地圖互動標記點 |
| 6 | Sticky Background | `stickyBG` | 內文固定 + 背景圖 Fix |
| 7 | Full Hover Background | `fullHoverBackground` | Icon 觸發背景圖切換 |
| 8 | Worldwide Scroll | `worldwide` | 上圖下文卡片水平捲軸 |
| 9 | Worldwide RWD Collapse | `worldwideRWDcollapse` | 桌機捲軸 / RWD 收合 |

3. 輸出三個區塊：XML 結構 + JavaScript（包在 `s_embed_code` + `s_custom_noRemove`）+ SCSS
