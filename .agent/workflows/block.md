---
description: 呼叫歷史開發過的優良區塊與版面配置
---

# /block

從客製化區塊知識庫中提取設計師常用的版面與特效結構，例如 Global Footer CTA、客製化時間軸等。

## 1. 讀取區塊知識庫
// turbo-all
**MUST** 讀取 `.agent/skills/icb_page_generator/resources/layout_patterns.md`
**MUST** 讀取 `.agent/skills/icb_page_generator/resources/custom_blocks.md`

## 2. 11 款客製化區塊菜單 (Block Menu)
當使用者詢問或未指定時，請直接向使用者展示此菜單，讓他們選擇：

| # | 行銷分類 | 區塊名稱 | 版面與效果說明 |
|---|----------|----------|----------------|
| 1 | 全域導購 | `Global Pre-Footer CTA` | 視差滾動背景 + 半透明濾鏡的行動呼叫區塊 |
| 2 | 敘事時間 | `History Time Line` | 企業歷史沿革時間軸 (原生結構加強) |
| 3 | 敘事流程 | `Flowchart` | Icon 步驟引導與弓型連線流程圖 |
| 4 | 內容排版 | `Content Sections` | 非對稱圖文，透過 SCSS 重疊上下區塊創造破格層次 |
| 5 | 內容排版 | `Three Chains` | 三段式連續區塊，中間帶有滿版穿插背景 |
| 6 | 靜態卡片 | `Static Snippet Cards` | 包含「字壓圖 (`titleUpperBg`)」與「水平滑動 (`RWDscroll`)」排版 |
| 7 | 進階互動 | `Bleeding Tabs` | 左側圓點清單頁籤，右側滿版圖片淡入淡出切換 |
| 8 | 內容排版 | `Icon Card Horizontal` | 左側 Icon (1:1對齊) + 右側文字的水平卡片清單 |
| 9 | 內容排版 | `Leaning Overflow` | 左右分鏡，帶有傾斜有色背景塊的視覺排版 |
| 10 | 視覺清單 | `Fix BG List` | 視差滾動背景搭配固定重疊的文字區塊 |
| 11 | 數據呈現 | `Counter After Color` | 動態數字跑馬燈，後綴符號與品牌主題色自動連動 |

## 3. 選擇與輸出規範
根據使用者輸入的關鍵字或描述，選擇適合的區塊結構輸出。
請依照 Odoo 原生 XML, SCSS 結構獨立產出，並確保所有 tag 都具備正確的 `data-snippet` 與 `data-custom-name` 屬性。
