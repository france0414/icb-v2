# Templates 目錄 — AI 導航指南

> [!IMPORTANT]
> **AI 必讀：** 本目錄是「靈感庫 + 積木庫」，不是「直接成品庫」。
> **嚴禁直接複製任一檔案的完整結構作為最終輸出。**
> 需要整頁範本時，請參考 `.agent/skills/icb_page_generator/resources/page_templates.md`。

---

## 🗂 目錄結構

```
templates/
├── base/           ← 🔒 鎖定結構（禁止修改內部 DOM）
└── improved/       ← 📦 元件積木庫（按類型分組）
    ├── banners/        橫幅 / 輪播 Banner
    ├── buttons/        按鈕風格 SCSS
    ├── carousels/      靜態卡片輪播
    ├── content-sections/  靜態圖文區塊（含 JS 互動版）
    ├── dynamic/        動態產品 / 新聞客製化版本
    │   ├── news/
    │   └── products/
    ├── footers/        Footer XML
    ├── forms/          聯絡表單
    ├── headers/        Header 選單 SCSS
    ├── home-recipes/   完整首頁配方 (Home 1–4)
    └── timelines/      時間軸
```

---

## 🔒 `base/` — 鎖定結構基底

這三份是 **結構絕對鎖定** 的基底模板，AI **只能** 在 section 外層加 class 或 `data-custom-name`，**禁止** 修改內部 XML 結構：

| 檔案 | 用途 | 鎖定原因 |
|------|------|---------|
| `base-dynamic-products.xml` + `.html` | 動態產品 Snippet 基底 | Odoo `s_dynamic_snippet_products` 內部結構由後端渲染決定 |
| `base-dynamic-news.xml` + `.html` | 動態新聞/部落格 Snippet 基底 | 同上，`s_dynamic_snippet` 結構 |
| `basd-Static-Snippet.xml` | 靜態卡片模板完整範例 | 含多種 Odoo 官方 static template class 變體 |

**如何使用 base 鎖定結構：**
```xml
<!-- ✅ 正確：只在 section 加 class 和 data 屬性 -->
<section class="s_dynamic_snippet_products o_cc2 s_custom_MyProducts"
         data-custom-name="MyProducts"
         ...以下直接複製 base-dynamic-products.xml 的其他屬性...>
```

---

## 📦 `improved/` — 元件積木庫

每個子目錄對應一種元件類型。**每個 XML 對應同名 SCSS**（若存在）。

### Token 節省原則

AI 查詢元件時，**優先**用以下順序，避免讀整份 XML 檔：

1. **先查 `custom_blocks.md`** → 知道元件位置（XML 檔名 + 行號範圍）
2. **再用 `view_range` 讀指定行** → 只讀需要的區塊
3. **同名 `.scss` 讀全文** → SCSS 通常比 XML 小很多

```
# 不好：直接讀整份大 XML
view templates/improved/content-sections/content-sections.xml

# 好：先查 custom_blocks.md 得到行號，再精準讀取
view templates/improved/content-sections/content-sections.xml [L655, L720]
```

### 各子目錄快速說明

| 目錄 | 包含元件 | 索引來源 |
|------|---------|---------|
| `banners/` | Banner-01~04 (三角形遮罩/Ken Burns/影片) | `custom_blocks.md` A節 |
| `buttons/` | 所有按鈕 SCSS 風格 | `button_styles.md` |
| `carousels/` | Static Snippet 輪播、客製化輪播 | `custom_blocks.md` D節 |
| `content-sections/` | Content-01~23（靜態圖文） + ContentJS-01~09（JS互動） | `custom_blocks.md` B+C節 |
| `dynamic/news/` | 動態部落格客製化版本（帶 SCSS） | `custom_blocks.md` G節 |
| `dynamic/products/` | 動態產品客製化版本（含 JS 版） | `custom_blocks.md` F節 |
| `footers/` | Footer-1、Footer-2（需 XPath XML 輸出） | `header_footer_rules.md` |
| `forms/` | 聯絡表單佈局 | `form_rules.md` |
| `headers/` | Menu-01~04 SCSS（純 SCSS，無 XML） | `header_footer_rules.md` |
| `home-recipes/` | Home-1~4 完整首頁（整頁 XML+SCSS） | `page_templates.md` |
| `timelines/` | 時間軸元件 | `custom_blocks.md` E節 |

---

## 🔗 使用流程

### 我要生成整頁首頁
→ 讀 `.agent/skills/icb_page_generator/resources/page_templates.md`，選 Home-1~4 配方

### 我要找某個具體元件（如 Banner、FAQ）
→ 讀 `.agent/skills/icb_page_generator/resources/custom_blocks.md`，找到 XML 行號，精準讀取

### 我要選擇哪個 Snippet
→ 讀 `.agent/skills/icb_page_generator/resources/snippet_catalog.md`

### 我要查某個 SCSS 變數或 mixin
→ 讀 `.agent/skills/icb_page_generator/resources/scss_reference.md`

### 我要加入動態產品或部落格
→ 讀 `.agent/skills/icb_page_generator/resources/dynamic_rules.md`

---

## ⚠️ 常見錯誤

| ❌ 錯誤 | ✅ 正確 |
|--------|--------|
| 讀整份 `content-sections.xml`（數千行） | 查 `custom_blocks.md` 找行號後 `view_range` 讀 |
| 自己猜測 XML 結構 | 從 templates 讀取原始碼 |
| 直接輸出 templates 檔案 | 先骨架確認，再輸出到 `outputs/` |
| 修改 `base/` 的內部結構 | 只加 section-level class 和 data 屬性 |
