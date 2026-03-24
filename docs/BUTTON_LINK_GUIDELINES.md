# 按鈕與連結使用規範 (Button & Link Guidelines)

> **版本**：1.0  
> **最後更新**：2026-03-13  
> **說明**：規範頁面中按鈕與連結的使用方式

---

## 1. 核心原則

### 1.1 主要使用 `<a>` 標籤

**原則**：頁面中的互動元素（按鈕）主要使用 `<a>` 標籤，而非 `<button>`

**為什麼？**
- `<a>` 標籤具有語義上的「連結」意義
- 使用者習慣點擊連結跳轉頁面
- 更容易被搜尋引擎索引
- 在 Odoo 編輯器中更容易編輯

### 1.2 `<button>` 的使用時機

**原則**：只有在表單提交或系統元件中使用 `<button>`

**適用場景**：
- 表單提交按鈕 (`<form>`)
- 彈出視窗按鈕 (`<modal>`)
- 系統內建元件按鈕

---

## 2. 連結按鈕 (`<a>`)

### 2.1 基本用法

```xml
<!-- 主要按鈕 -->
<a href="/page" class="btn btn-primary">主要按鈕</a>

<!-- 次要按鈕 -->
<a href="/page" class="btn btn-secondary">次要按鈕</a>

<!-- 外框樣式 -->
<a href="/page" class="btn btn-outline-primary">外框按鈕</a>

<!-- 淺色按鈕 (深色背景用) -->
<a href="/page" class="btn btn-light">淺色按鈕</a>
```

### 2.2 按鈕尺寸

```xml
<!-- 小按鈕 -->
<a href="#" class="btn btn-primary btn-sm">小按鈕</a>

<!-- 預設尺寸 -->
<a href="#" class="btn btn-primary">預設按鈕</a>

<!-- 大按鈕 -->
<a href="#" class="btn btn-primary btn-lg">大按鈕</a>
```

### 2.3 按鈕狀態

```xml
<!-- 啟用狀態 -->
<a href="#" class="btn btn-primary">啟用按鈕</a>

<!-- 停用狀態 -->
<a href="#" class="btn btn-primary disabled" aria-disabled="true">停用按鈕</a>
```

---

## 3. 一般連結 (`<a>`)

### 3.1 文字連結

```xml
<!-- 基本連結 -->
<p>請參考 <a href="/page">詳細說明</a></p>

<!-- 開新分頁 -->
<p>相關文件 <a href="/page" target="_blank" rel="noopener">外部連結</a></p>
```

### 3.2 連結樣式

**原則**：依賴系統主題色，不寫死顏色

```scss
// SCSS：一般連結樣式
a {
  color: var(--o-cc1-link); // 依賴系統主題
  text-decoration: underline;
  transition: color 0.2s;
  
  &:hover {
    text-decoration: none;
    color: var(--o-cc1-text); // 懸停時顏色
  }
}
```

---

## 4. 系統按鈕 (`<button>`)

### 4.1 表單按鈕

```xml
<form action="/submit" method="post">
  <input type="text" name="name" placeholder="姓名">
  <button type="submit" class="btn btn-primary">送出表單</button>
</form>
```

### 4.2 系統元件按鈕

```xml
<!-- 彈出視窗 -->
<div class="modal-footer">
  <button type="button" class="btn btn-secondary" data-dismiss="modal">關閉</button>
  <button type="button" class="btn btn-primary">確定</button>
</div>
```

---

## 5. SCSS 範例

### 5.1 一般按鈕樣式

```scss
// ✅ 正確：依賴系統主題
.my-button {
  padding: 10px 20px;
  border-radius: 5px;
  transition: all 0.2s;
  
  // ❌ 不寫 background-color，讓 btn-primary 自動決定
}

// ✅ 正確：特殊樣式才寫死顏色
.s_custom_btnOrange {
  background-color: #FF5500 !important;
  border-color: #FF5500 !important;
  
  &:hover {
    background-color: #E04D00 !important;
  }
}
```

### 5.2 連結樣式

```scss
// ✅ 正確：依賴系統主題
a {
  color: var(--o-cc1-link);
  text-decoration: underline;
  
  &:hover {
    text-decoration: none;
  }
}

// ✅ 正確：特殊連結樣式
.s_custom_link {
  color: #FF5500 !important; // 品牌色
  font-weight: bold;
  
  &:hover {
    color: #E04D00 !important;
  }
}
```

---

## 6. 開發檢查清單

### 6.1 XML 檢查
- [ ] 按鈕使用 `<a>` 標籤（除非是表單或系統元件）
- [ ] 正確使用 Bootstrap class（`btn-primary`, `btn-secondary` 等）
- [ ] 連結有正確的 `href` 屬性
- [ ] 外部連結有 `target="_blank"` 和 `rel="noopener"`

### 6.2 SCSS 檢查
- [ ] 一般按鈕不寫死顏色
- [ ] 特殊樣式才寫死顏色，並加上註解
- [ ] 連結顏色依賴系統主題 (`var(--o-cc1-link)`)
- [ ] 有 hover 狀態樣式

### 6.3 功能檢查
- [ ] 點擊按鈕/連結能正確跳轉
- [ ] 懸停時有視覺回饋
- [ ] 在 Odoo 編輯器中可編輯

---

## 7. 常見錯誤與修正

### 錯誤 1：用 `<button>` 做連結

```xml
<!-- ❌ 錯誤：button 不適合做連結 -->
<button onclick="location.href='/page'">前往頁面</button>

<!-- ✅ 修正：使用 a 標籤 -->
<a href="/page" class="btn btn-primary">前往頁面</a>
```

### 錯誤 2：寫死按鈕顏色

```scss
// ❌ 錯誤
.my-button {
  background-color: #35979c; // 寫死顏色
}

// ✅ 修正：使用系統主題
.my-button {
  // 不寫 background-color，依賴 btn-primary
}
```

### 錯誤 3：連結沒有 hover 狀態

```scss
// ❌ 錯誤
a {
  color: var(--o-cc1-link);
}

// ✅ 修正：加上 hover 狀態
a {
  color: var(--o-cc1-link);
  
  &:hover {
    text-decoration: none;
  }
}
```

---

## 8. 參考資源

- `docs/COLOR_USAGE_GUIDELINES.md` - 色彩使用規範
- `docs/PROJECT_THEME.css` - 專案色彩定義
- Bootstrap 4 按鈕文件 - https://getbootstrap.com/docs/4.6/components/buttons/

---

## 9. 範例檔案

以下是一些符合規範的範例檔案：

- `templates/home-1.xml` - 首頁連結按鈕範例
- `templates/customized-Static-Snippet.xml` - 靜態元件按鈕範例

---

**總結**：  
頁面互動主要使用 `<a>` 標籤，依賴系統主題色，特殊樣式才寫死顏色並登記例外。
