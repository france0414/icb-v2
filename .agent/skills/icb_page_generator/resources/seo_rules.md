# SEO 規則 — H 標籤層級

> 適用所有指令：`/create`、`/page`、`/page-home`  
> AI 生成 XML 時，**每個頁面**都必須遵守此層級規則。

---

## 核心規則

### H1 — 每頁只能有一個

| 情境 | H1 放哪裡 |
|------|----------|
| 有全版 Banner / Hero | Banner 的主標題 → H1 |
| 無 Banner，第一個 section 是介紹區 | 介紹區的頁面大標題 → H1 |
| 首頁 | 通常在 Banner 或第一個視覺焦點區 |

> Odoo 後台「網站 → 頁面屬性 → SEO 標題」是 `<title>` tag，**不是頁面上的 H1**，兩者不衝突，都需要設定。

---

### H2 — 每個主要 Section 的標題

每個獨立 section 的大標題用 H2，代表「這個區塊在說什麼」。

```
頁面
  ├─ Banner → H1（唯一）
  ├─ Section：關於我們 → H2
  ├─ Section：服務特色 → H2
  ├─ Section：成就數字 → H2
  └─ Section：聯絡我們 → H2
```

---

### H3 — Section 內的子項目標題

Section 內的卡片標題、FAQ 問題、列表項目標題 → H3

```
Section：服務特色（H2）
  ├─ 卡片1：品質保證 → H3
  ├─ 卡片2：快速交貨 → H3
  └─ 卡片3：客製服務 → H3
```

---

### H4 以下 — 改用 `p.h4` / `p.h5`

H4、H5、H6 會增加語意層級，一般頁面應避免。  
若設計上需要「視覺像標題但不增加 H 層級」，改用 Bootstrap 的 heading class 套在 `<p>` 上：

```xml
<!-- ✅ 視覺像 H4，但不佔語意層級 -->
<p class="h4">小標題文字</p>
<p class="h5">更小的標題文字</p>

<!-- ❌ 不必要地增加語意層級 -->
<h4>小標題文字</h4>
```

**判斷口訣**：這個標題「需要被搜尋引擎重視」→ 用真正的 H 標籤；只是「視覺上大一點」→ 用 `p.h4` / `p.h5`。

---

## 在 Odoo XML 中的寫法

### s_title snippet（AI 常用）

`s_title` 預設輸出 H2，若要改成 H1 或 H3 需明確指定：

```xml
<!-- H1：Banner 主標題 -->
<h1 class="o_default_snippet_text">頁面主標題</h1>

<!-- H2：Section 標題（預設） -->
<h2 class="o_default_snippet_text">服務特色</h2>

<!-- H3：卡片或子項目標題 -->
<h3 class="o_default_snippet_text">品質保證</h3>
```

### s_text_block 內的標題

```xml
<section class="s_text_block o_colored_level pt0 pb0" data-snippet="s_text_block">
  <div class="container s_allow_columns">
    <h2>關於我們</h2>          ← Section 標題
    <p>品牌介紹文字...</p>
  </div>
</section>
```

### Static Snippet 卡片標題

```xml
<!-- o_carousel_product_card 內的標題用 H3 -->
<div class="card-title">
  <h3>服務項目名稱</h3>
</div>
```

---

## Phase A 骨架規劃時的標記方式

在 `/create` Phase A 輸出骨架時，每個 section 必須標明使用的標題層級：

```
[S1] Hero Banner
  → 主標題：H1「品牌核心標語」
  → 副標：p 標籤（不用 H）

[S2] 品牌介紹
  → Section 標題：H2「關於 XXX」
  → 說明文字：p

[S3] 服務特色（4張卡片）
  → Section 標題：H2「我們的服務」
  → 每張卡片標題：H3

[S4] 常見問題 FAQ
  → Section 標題：H2「常見問題」
  → 每個問題：H3（s_faq_collapse 的 accordion 標題）
```

---

## 常見錯誤

| ❌ 錯誤 | ✅ 正確 |
|--------|--------|
| 每個 section 都用 H1 | 全頁只有一個 H1 |
| Section 標題用 H1，卡片也用 H1 | Section → H2，卡片 → H3 |
| 跳過層級：H1 直接接 H3 | 層級必須連續：H1 → H2 → H3 |
| 視覺小標題用 `<h4>`、`<h5>` | 改用 `<p class="h4">` / `<p class="h5">` |
| s_title 全部不改，預設都是 H2 | Banner 主標題記得改成 H1 |
