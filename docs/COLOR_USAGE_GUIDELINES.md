# 色彩使用規範 (Color Usage Guidelines)

> **版本**：1.0  
> **最後更新**：2026-03-13  
> **依據**：`docs/PROJECT_THEME.css`

---

## 1. 核心原則

### 1.1 絕不寫死顏色
**原則**：除非有特殊需求，否則所有文字、背景、邊框顏色都應依賴 Odoo 系統主題變數。

**為什麼？**
- 讓使用者能在後台直接修改配色
- 維持全站視覺一致性
- 避免與未來主題更新衝突

### 1.2 色彩由背景決定
**原則**：文字顏色由所在的背景色塊 (`o_ccN`) 自動決定。

| 背景色塊 | 背景色 | 文字顏色 | 標題顏色 |
|---------|--------|---------|---------|
| `o_cc1` | 白色 | 深灰 (`#212529`) | 深灰 (`#212529`) |
| `o_cc2` | 淺灰 | 深灰 (`#212529`) | 主色 (`#35979c`) |
| `o_cc3` | 主色 | 白色 | 白色 |
| `o_cc4` | 自訂 | 依設定 | 依設定 |
| `o_cc5` | 深色 | 白色 | 白色 |

---

## 2. 色彩系統架構

### 2.1 Odoo 色塊主題 (Color Combinations)

在 XML 中直接套用 class：

```xml
<!-- 白底 (最常用) -->
<section class="o_cc1">...</section>

<!-- 淺灰底 (區隔用) -->
<section class="o_cc2">...</section>

<!-- 主色底 (強調用) -->
<section class="o_cc3">...</section>

<!-- 深色底 (Footer/Hero) -->
<section class="o_cc5">...</section>
```

### 2.2 CSS 變數系統

在 SCSS 中使用 CSS 變數，**不要寫死色碼**：

```scss
// ✅ 正確：使用變數
.my-element {
  background-color: var(--o-cc1-bg);
  color: var(--o-cc1-text);
  border-color: var(--o-cc1-btn-primary);
}

// ❌ 錯誤：寫死色碼
.my-element {
  background-color: #FFFFFF;  // 不應該這樣寫
  color: #212529;             // 不應該這樣寫
}
```

---

## 3. 使用情境與範例

### 3.1 情境一：一般內容區塊 (最常見)

**需求**：顯示文章、產品介紹等一般內容

**做法**：使用 `o_cc1` (白底)，不寫任何顏色

```xml
<!-- XML -->
<section class="o_cc1">
  <div class="container">
    <h2>產品特色</h2>
    <p>這是產品的詳細描述...</p>
    <a href="#" class="btn btn-primary">了解更多</a>
  </div>
</section>
```

```scss
// SCSS
.product-features {
  padding: 60px 0;
  
  h2 {
    font-size: 2rem;
    margin-bottom: 20px;
    // ❌ 不寫 color，讓 o_cc1 自動決定為深色
  }
  
  p {
    font-size: 1.1rem;
    line-height: 1.6;
    // ❌ 不寫 color，讓 o_cc1 自動決定為深色
  }
}
```

### 3.2 情境二：深色背景區塊 (Footer/Hero)

**需求**：全版 Banner 或 Footer

**做法**：使用 `o_cc5` (深底)，文字自動變白色

```xml
<!-- XML -->
<section class="o_cc5 oe_img_bg" style="background-image: url('...');">
  <div class="container">
    <h1>全版標題</h1>
    <p class="lead">副標題描述</p>
    <button class="btn btn-light">行動按鈕</button>
  </div>
</section>
```

```scss
// SCSS
.hero-banner {
  padding: 100px 0;
  
  h1 {
    font-size: 3rem;
    font-weight: bold;
    // ❌ 不寫 color，o_cc5 會自動設為白色
  }
  
  .lead {
    font-size: 1.5rem;
    // ❌ 不寫 color，o_cc5 會自動設為白色
  }
}
```

### 3.3 情境三：特殊突顯 (需要手動變色)

**需求**：某段文字需要特別紅色或品牌色

**做法 A**：使用 `style=""` (讓使用者可在後台修改)

```xml
<h3 style="color: #FF5500;">緊急公告：活動即將結束！</h3>
```

**做法 B**：使用客製化 Class (固定樣式)

```scss
// SCSS
.s_custom_urgent {
  color: #FF5500 !important;
  font-weight: bold;
}
```

```xml
<!-- XML -->
<h3 class="s_custom_urgent">緊急公告：活動即將結束！</h3>
```

### 3.4 情境四：按鈕與連結

**原則**：頁面主要使用 `<a>` 作為按鈕，除非是系統生成的表單按鈕才用 `<button>`

#### 3.4.1 連結按鈕 (`<a>`)

**做法**：使用 `<a>` 標籤 + Bootstrap class

```xml
<!-- 主要連結按鈕 -->
<a href="#" class="btn btn-primary">主要按鈕</a>

<!-- 次要連結按鈕 -->
<a href="#" class="btn btn-secondary">次要按鈕</a>

<!-- 淺色連結按鈕 (深色背景用) -->
<a href="#" class="btn btn-light">淺色按鈕</a>

<!-- 外框樣式 -->
<a href="#" class="btn btn-outline-primary">外框按鈕</a>
```

**SCSS 範例**：
```scss
// 一般情況不寫顏色，依賴系統主題
.my-button {
  padding: 10px 20px;
  border-radius: 5px;
  // ❌ 不寫 background-color，讓 btn-primary 自動決定
}

// 特殊樣式才寫死顏色
.s_custom_btnOrange {
  background-color: #FF5500 !important;
  border-color: #FF5500 !important;
  
  &:hover {
    background-color: #E04D00 !important;
  }
}
```

#### 3.4.2 系統按鈕 (`<button>`)

**原則**：只有在表單、系統元件中使用 `<button>`

```xml
<!-- 表單提交按鈕 -->
<form>
  <input type="text" name="name">
  <button type="submit" class="btn btn-primary">送出</button>
</form>

<!-- 系統元件按鈕 -->
<div class="modal-footer">
  <button type="button" class="btn btn-secondary" data-dismiss="modal">關閉</button>
  <button type="button" class="btn btn-primary">確定</button>
</div>
```

#### 3.4.3 連結樣式

**原則**：一般連結使用系統主題色，不寫死顏色

```xml
<!-- 文字連結 -->
<p>請參考 <a href="#">詳細說明</a></p>

<!-- 按鈕式連結 -->
<a href="#" class="btn btn-link">了解更多</a>
```

**SCSS 範例**：
```scss
// 一般連結
a {
  color: var(--o-cc1-link); // 依賴系統主題
  text-decoration: underline;
  
  &:hover {
    text-decoration: none;
  }
}

// 特殊連結樣式
.s_custom_link {
  color: #FF5500 !important; // 品牌色
  font-weight: bold;
}
```

---

## 4. 開發檢查清單

在完成切版後，請檢查以下項目：

### 4.1 SCSS 檢查
- [ ] 是否有不必要的 `color: #xxx`？
- [ ] 是否有寫死的背景色 (`background-color: #xxx`)？
- [ ] 是否使用 CSS 變數 (`var(--o-ccN-xxx)`)？
- [ ] 是否有過度使用 `!important`？

### 4.2 XML 檔案檢查
- [ ] 每個 `<section>` 是否有套用 `o_ccN`？
- [ ] 標題和段落是否沒有寫 `style="color: ..."`（除非特殊需求）？
- [ ] 按鈕是否使用系統內建的 `btn-primary` / `btn-secondary`？

### 4.3 功能檢查
- [ ] 在 Odoo 編輯器中，文字是否可直接點擊編輯？
- [ ] 修改主題色後，頁面顏色是否同步更新？

---

## 5. 常見錯誤與修正

### 錯誤 1：在 SCSS 中寫死顏色
```scss
// ❌ 錯誤
.my-title {
  color: #333;
}

// ✅ 修正
.my-title {
  // 不寫 color，讓系統自動判斷
}
```

### 錯誤 2：在深色背景中寫深色文字
```xml
<!-- ❌ 錯誤 -->
<section class="o_cc5">
  <h1 style="color: #333;">標題</h1> <!-- 深底配深色字，看不見 -->
</section>

<!-- ✅ 修正 -->
<section class="o_cc5">
  <h1>標題</h1> <!-- 自動變白色 -->
</section>
```

### 錯誤 3：忽略 RWD 斷點
```scss
// ✅ 正確：使用斷點
.my-element {
  font-size: 1.2rem; // 手機版
  
  @include media-breakpoint-up(md) {
    font-size: 1.5rem; // 平板以上
  }
}
```

---

## 6. 參考資源

- `docs/PROJECT_THEME.css` - 專案色彩定義
- `docs/user_custom_rules.scss` - 自訂 RWD 斷點與 mixin
- Odoo 14 官方文件 - WebBuilder 規範

---

## 7. 範例檔案

以下是一些符合規範的範例檔案：

- `templates/home-1.xml` / `home-1.scss` - 首頁範例
- `templates/customized-Static-Snippet.xml` - 靜態元件範例

---

**總結**：  
色彩由系統控制，結構由 AI 生成。  
除非特殊需求，否則**不寫死顏色**。

---

## 8. 例外處理 (Exception Handling)

### 8.1 什麼情況下可以寫死顏色？

以下情況允許寫死顏色，但必須符合規範：

1.  **品牌識別色**：企業 LOGO、特定品牌色
2.  **特殊活動**：限時活動、節慶主題色
3.  **設計師明確要求**：設計稿中指定的特殊顏色
4.  **系統無法支援的漸層**：複雜的漸層效果

### 8.2 例外登記表

當你必須寫死顏色時，請在以下表格登記：

| 檔案路徑 | 位置 | 顏色值 | 原因 | 登記日期 | 負責人 |
|---------|------|--------|------|----------|--------|
| `templates/home-1.scss` | `.s_custom_urgent` | `#FF5500` | 緊急公告需醒目 | 2026-03-13 | AI |
| | | | | | |
| | | | | | |

### 8.3 例外顏色的寫法規範

**原則**：寫死顏色時，必須加上註解說明原因。

```scss
// ✅ 正確：加上註解說明
.s_custom_brandColor {
  color: #FF5500 !important; // 品牌識別色，不可更改
}

// ✅ 正確：使用變數管理
:root {
  --brand-orange: #FF5500; // 品牌橘色
}

.s_custom_brandColor {
  color: var(--brand-orange) !important;
}

// ❌ 錯誤：沒有註解
.s_custom_brandColor {
  color: #FF5500 !important;
}
```

### 8.4 例外顏色的 XML 規範

```xml
<!-- ✅ 正確：style 加上註解 -->
<h3 style="color: #FF5500;" title="品牌識別色，不可更改">緊急公告</h3>

<!-- ❌ 錯誤：沒有說明 -->
<h3 style="color: #FF5500;">緊急公告</h3>
```

### 8.5 定期審查例外顏色

建議每月審查一次例外登記表，確認是否需要：
1.  改為系統變數
2.  移除不必要的寫死顏色
3.  更新原因與負責人

---

## 9. 總結

**一般情況**：依賴系統主題，不寫死顏色  
**例外情況**：寫死顏色 + 註解說明 + 登記例外表

這樣既能保持系統的靈活性，又能確保例外情況有明確的記錄與管理。
