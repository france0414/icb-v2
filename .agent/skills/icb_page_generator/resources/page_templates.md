# 頁面樣板配方 (Page Templates)

> [!IMPORTANT]
> Home 頁面配方已改為輕量索引格式。
> 詳細區塊組裝資訊（data-snippet、s_custom_* class、data-* 屬性）請讀：
> `.agent/skills/icb_page_generator/resources/home_recipes.md`

---

## 首頁配方（快速索引）

| 配方 | 特色 |
|------|------|
| home-1 | 三角遮罩 Banner + 橫式 icon 卡 + 動態產品 + HoverBg 輪播 + 新聞 |
| home-2 | 原生輪播 + 三段穿插 + 四欄輪播 + counter + 部落格 |
| home-3 | 影片 Banner + 滿版產品 + 視差 × 2 + 部落格輪播 |
| home-4 | 純影片 Banner + 固定側欄新聞 + 互動地圖 + 交錯輪播 |

→ 詳細配方讀 `home_recipes.md`，不需另讀 XML 範本檔。

---

## 內頁配方

> 配方代號格式：`SP` = 服務/產品、`AB` = 關於我們、`CT` = 聯絡、`NL` = 新聞列表。
> 每個配方列出：區塊順序 → 建議 Snippet → 建議色塊 → pt/pb 建議。

---

### SP-01：服務 / 產品介紹頁（標準版）

**適用場景：** 單一服務說明、產品介紹、解決方案頁面

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **Hero Banner** | `s_cover` 或 `s_banner` | `o_cc5` 深色底 | pt128 pb128 |
| 2 | **服務摘要 / 核心主張** | `s_text_block`（左文右圖）或 `s_text_image` | `o_cc1` 白 | pt80 pb80 |
| 3 | **特色亮點**（3~4 欄圖標） | `s_features` 或 `s_three_columns` + `s_custom_scaleL` | `o_cc2` 淺灰 | pt80 pb80 |
| 4 | **流程 / 步驟說明**（選用） | `s_process_steps` 或 `s_timeline` | `o_cc1` 白 | pt64 pb64 |
| 5 | **案例 / 客戶見證**（選用） | `s_quotes_carousel` 或 `s_references` | `o_cc2` 淺灰 | pt64 pb64 |
| 6 | **行動呼籲（CTA）** | `s_call_to_action` | `o_cc4` 主色藍 | pt80 pb80 |

**色彩節奏：**
```
o_cc5（Hero）→ o_cc1 → o_cc2 → o_cc1 → o_cc2 → o_cc4（CTA）
```

**注意事項：**
- Hero 建議加 `oe_img_bg o_bg_img_center` 背景圖；文字覆蓋 `o_we_bg_filter bg-black-50`
- `s_features` 每欄：icon（`fa fa-*`）+ 標題（`<h4>`）+ 說明（`<p>`）
- CTA section 文字用 `o_cc4` 白字系統，按鈕用 `btn btn-secondary`（灰白）或自訂

---

### SP-02：服務 / 產品介紹頁（左右交錯版）

**適用場景：** 多個服務項目並列、圖文交錯介紹

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **Hero Banner** | `s_cover` 或 `s_banner` | `o_cc4` 主色藍 | pt128 pb128 |
| 2 | **服務項目 A**（左圖右文） | `s_text_image` | `o_cc1` 白 | pt80 pb80 |
| 3 | **服務項目 B**（左文右圖） | `s_image_text` | `o_cc2` 淺灰 | pt80 pb80 |
| 4 | **服務項目 C**（左圖右文） | `s_text_image` | `o_cc1` 白 | pt80 pb80 |
| 5 | **數字成就**（選用） | `s_numbers` | `o_cc3` 金 | pt64 pb64 |
| 6 | **行動呼籲（CTA）** | `s_call_to_action` | `o_cc4` 主色藍 | pt80 pb80 |

**色彩節奏：**
```
o_cc4（Hero）→ o_cc1 → o_cc2 → o_cc1 → o_cc3 → o_cc4（CTA）
```

**注意事項：**
- `s_text_image` / `s_image_text` 圖片欄用 picsum 占位，比例建議 4:6 或 5:7
- 交錯排列製造節奏感，避免連續同方向
- `s_numbers` 搭配金底（o_cc3）作為視覺停頓點

---

### AB-01：關於我們頁（完整版）

**適用場景：** 公司介紹、企業文化、品牌故事頁

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **Hero Banner（含標題）** | `s_cover` 或 `s_banner` | `o_cc5` 深色 | pt128 pb128 |
| 2 | **公司核心主張 / 使命** | `s_text_block` 或 `s_column_layout` 左標題右說明 | `o_cc1` 白 | pt80 pb80 |
| 3 | **數字成就 / 里程碑** | `s_numbers` | `o_cc2` 淺灰 | pt64 pb64 |
| 4 | **品牌故事 / 發展歷程**（選用） | `s_timeline` 或 `s_text_image` | `o_cc1` 白 | pt80 pb80 |
| 5 | **核心價值 / 特色**（3 欄） | `s_three_columns` 或 `s_features` | `o_cc2` 淺灰 | pt80 pb80 |
| 6 | **團隊介紹**（選用） | `s_company_team` | `o_cc1` 白 | pt64 pb64 |
| 7 | **合作客戶 / 認證** | `s_references` | `o_cc2` 淺灰 | pt48 pb48 |
| 8 | **行動呼籲（CTA）** | `s_call_to_action` | `o_cc4` 主色藍 | pt80 pb80 |

**色彩節奏：**
```
o_cc5（Hero）→ o_cc1 → o_cc2 → o_cc1 → o_cc2 → o_cc1 → o_cc2 → o_cc4（CTA）
```

**注意事項：**
- `s_numbers` 數字欄位建議 3~4 個，如「成立年數、服務客戶、完成案例、合作國家」
- `s_column_layout` 左右比例建議 4:8（左窄標題，右寬說明）
- `s_references` 只需放 Logo 圖，不需文字

---

### AB-02：關於我們頁（精簡版）

**適用場景：** 小型企業、文字優先的品牌介紹

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **頁首標題** | `s_title` 或短版 `s_cover` | `o_cc4` 主色藍 | pt96 pb96 |
| 2 | **公司介紹（左圖右文）** | `s_text_image` | `o_cc1` 白 | pt80 pb80 |
| 3 | **核心價值（3 欄）** | `s_features` | `o_cc2` 淺灰 | pt64 pb64 |
| 4 | **數字成就** | `s_numbers` | `o_cc3` 金 | pt64 pb64 |
| 5 | **行動呼籲（CTA）** | `s_call_to_action` | `o_cc4` 主色藍 | pt80 pb80 |

---

### CT-01：聯絡我們頁（含表單）

**適用場景：** 客服聯絡、詢價、預約諮詢

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **頁首標題** | `s_title` 或短版 `s_cover` | `o_cc4` 主色藍 | pt96 pb96 |
| 2 | **聯絡資訊（左）+ 表單（右）** | `s_text_block`（row 6:6 手工切欄） | `o_cc1` 白 | pt80 pb80 |
| 3 | **地圖** | `s_map` 或 `s_google_map` | `o_cc2` 淺灰 | pt0 pb0 |

**欄位切法（區塊 2 的 row 結構）：**
```
左 col-lg-5：地址、電話、Email、社群連結（用 fa icon）
右 col-lg-7：s_website_form 聯絡表單
```

**注意事項：**
- 聯絡資訊 icon 使用 `fa fa-map-marker`、`fa fa-phone`、`fa fa-envelope`
- `s_website_form` 保持原生結構，只需用 SCSS 調整外觀，不修改 form DOM
- 地圖建議全寬（container-fluid），高度 450px
- 詳細表單 SCSS 規則讀 `resources/form_rules.md`

---

### CT-02：聯絡我們頁（多據點）

**適用場景：** 有多個辦公室、門市或工廠地點

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **頁首標題** | `s_cover` 短版 | `o_cc5` 深色 | pt96 pb96 |
| 2 | **據點列表**（左右交錯或三欄） | `s_text_block` 手工 row/col | `o_cc1` 白 | pt80 pb80 |
| 3 | **地圖** | `s_map` | `o_cc2` 淺灰 | pt0 pb0 |
| 4 | **聯絡表單** | `s_text_block`（row 包 `s_website_form`） | `o_cc1` 白 | pt80 pb80 |

---

### NL-01：新聞 / 部落格列表頁

**適用場景：** 公司新聞、產業文章、媒體報導

> ⚠️ Blog 系統頁（`/blog`）只能輸出 SCSS，不可輸出 XML。此配方用於**自訂靜態新聞列表頁**。

**區塊順序與組合：**

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **頁首標題** | `s_title` | `o_cc2` 淺灰 | pt64 pb64 |
| 2 | **文章列表**（靜態，3 欄卡片） | `s_static_snippet` + `s_blog_post_card` + `s_custom_scaleL` | `o_cc1` 白 | pt80 pb80 |
| 3 | **行動呼籲（可選）** | `s_call_to_action` | `o_cc4` 主色藍 | pt64 pb64 |

**注意事項：**
- 若明確要求動態部落格，改用 `s_dynamic_snippet`（讀 `dynamic_rules.md`）
- 靜態卡片建議 3 欄，每張：上圖 + 分類標籤 + 標題 + 日期 + 摘要
- `s_blog_post_card` 骨架查 `resources/indexes/templates_index.json`

---

### NL-02：產品列表頁（靜態展示）

**適用場景：** 產品型錄、解決方案總覽

| # | 區塊名稱 | Snippet | 色塊 | pt / pb |
|---|---------|---------|------|---------|
| 1 | **頁首標題** | `s_cover` 或 `s_title` | `o_cc4` 主色藍 | pt96 pb96 |
| 2 | **產品篩選說明（選用）** | `s_text_block` | `o_cc1` 白 | pt48 pb48 |
| 3 | **產品卡片列表** | `s_static_snippet` + `s_product_product_borderless_1` + `s_custom_scaleL` | `o_cc2` 淺灰 | pt80 pb80 |
| 4 | **行動呼籲** | `s_call_to_action` | `o_cc4` 主色藍 | pt64 pb64 |

---

## 配方選擇決策樹

```
使用者說「做一個 X 頁面」

├── Hero 類型？
│   ├── 全版大圖主視覺    → s_cover 或 s_banner
│   ├── 純文字頁首        → s_title（較矮）
│   └── 短版帶色底標題    → s_cover + pt96 pb96

├── 主體結構？
│   ├── 單一服務說明      → SP-01
│   ├── 多服務左右交錯    → SP-02
│   ├── 公司介紹完整版    → AB-01
│   ├── 公司介紹精簡版    → AB-02
│   ├── 聯絡含表單        → CT-01
│   ├── 多據點聯絡        → CT-02
│   ├── 新聞/文章列表     → NL-01
│   └── 產品展示列表      → NL-02

└── CTA 區塊？
    ├── 有明確行動         → s_call_to_action + o_cc4（主色藍）
    └── 無 CTA            → 省略最後區塊
```

---

## 注意事項

1. **不生成說明區塊** — 維運用的區塊（如「複製 SCSS / 不要變更」）生成頁面時跳過
2. **SCSS 來源** — 對應區塊的 SCSS 若 templates/improved/ 有同名 .scss 則優先讀取
3. **圖片** — 使用 `https://picsum.photos/[width]/[height]` 作為佔位圖
4. **色彩** — 所有 o_ccX 對應色碼詳見 `docs/design/PROJECT_THEME.css`
