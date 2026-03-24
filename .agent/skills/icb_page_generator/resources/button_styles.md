# Odoo Button Styles Guide

> [!IMPORTANT]
> **一個網站只使用一種按鈕風格！** 選擇後全站統一套用。
> 按鈕 SCSS 直接寫入全域樣式的 `// 按鈕區 開始` ~ `// 按鈕區 結束` 區間，**不需要任何包裹 class**。

> [!WARNING]
> **`templates/btn-style.scss` 中的區塊僅用於模板預覽頁面的樣式隔離！**
> 在實際網站中，選定一種風格後，SCSS 直接作用於 `#wrapwrap .btn`、`header .btn`、`section .btn` 等全域選擇器。
> 若某個特定按鈕需要脫離全站風格，才需要額外撰寫覆蓋 SCSS（例如某區塊不要箭頭效果）。

---

## 0. Odoo 按鈕系統的設計師控制原則（AI 必讀）

Odoo 編輯器右側的屬性面板可以讓設計師在不改 HTML 的情況下調整按鈕外觀。
按鈕的 HTML class 是由三個維度組合而成：

```
btn  +  [樣式 class]  +  [尺寸 class]  +  [形狀 class]
```

| 維度 | 選項 | 對應 Class | 說明 |
|------|------|-----------|------|
| **樣式** | 首要的 | `btn-primary` | 實心主色 |
| | 次要的 | `btn-secondary` | 實心次色 |
| | 填充主要 | `btn-fill-primary` | 實心，hover 顏色變化 |
| | 填充次要 | `btn-fill-secondary` | 實心，hover 顏色變化 |
| | 輪廓主要 | `btn-outline-primary` | 空心外框 |
| | 輪廓次要 | `btn-outline-secondary` | 空心外框 |
| | 平滑 | `btn-primary flat` 或 `btn-secondary flat` | 無圓角 |
| **尺寸** | 小 | `btn-sm` | - |
| | 中 | _(無 class)_ | 預設 |
| | 大 | `btn-lg` | - |
| **形狀** | 預設 | _(無 class)_ | 圓角矩形 |
| | 圓形 | `rounded-circle` | 完全圓角 |

### ✅ AI 生成按鈕的規則

1. **永遠用有效的組合 class** — 讓設計師可以在編輯器中繼續用下拉式修改
2. **不要寫死 style=""** — 使用 class 組合，讓顏色走 o_cc1~o_cc5 變數
3. **只用 `btn-primary` 和 `btn-secondary`** 兩種顏色 — 其他色（success、danger）保留給系統用途
4. **常見組合範例：**

```html
<!-- 推薦：標準 CTA 按鈕 -->
<a href="#" class="btn btn-primary">立即聯繫</a>
<a href="#" class="btn btn-outline-secondary">了解更多</a>

<!-- 推薦：大尺寸 Hero 按鈕 -->
<a href="#" class="btn btn-primary btn-lg">立即了解</a>

<!-- 特殊：填充按鈕（hover 效果更明顯） -->
<a href="#" class="btn btn-fill-primary">Join Us</a>
```

---

## 1. 基礎選擇器系統

AI 生成按鈕樣式時，必須理解以下組合：

### Type（類型）
| Class | 說明 |
|-------|------|
| `btn-primary` | 主要按鈕 |
| `btn-secondary` | 次要按鈕 |
| `btn-fill-primary` | 實心主要按鈕 |
| `btn-fill-secondary` | 實心次要按鈕 |
| `btn-outline-primary` | 外框主要按鈕 |
| `btn-outline-secondary` | 外框次要按鈕 |

### Shape（形狀）
| Class | 說明 |
|-------|------|
| *(default)* | 預設圓角 |
| `rounded-circle` | 完全圓角 |
| `flat` | 直角無圓角 |

### Size（尺寸）
| Class | 說明 |
|-------|------|
| `btn-sm` | 小 |
| *(default)* | 中 |
| `btn-lg` | 大 |

### 組合範例
```html
<a class="btn btn-fill-primary rounded-circle btn-lg">Large Round Button</a>
<a class="btn btn-outline-secondary flat btn-sm">Small Flat Button</a>
```

---

## 2. AI 生成自訂風格的必要條件

當使用者需要 **非預設風格** 時，AI 生成的 SCSS 必須符合以下規則：

### A. 選擇器規範
```scss
// ✅ 必須涵蓋這些選擇器
.btn-primary, .btn-fill-primary
.btn-secondary, .btn-fill-secondary

// ✅ 必須排除系統按鈕
.btn:not(.dropdown-toggle):not(.oe_search_button):not(.o_add_compare_dyn):not(.o_add_compare):not(.o_add_quote):not(.js_add_cart_json)
```

### B. 色彩變數系統（每個 o_cc 區塊）
```scss
// o_cc1 ~ o_cc5 都有對應變數
.btn-fill-primary { background-color: var(--o-cc1-btn-primary); }
.btn-fill-primary:hover { background-color: var(--o-cc1-btn-primary-border); }

.o_cc2 {
    .btn-fill-primary { background-color: var(--o-cc2-btn-primary); }
    // ...
}
// 依此類推到 o_cc5
```

### C. 尺寸適配
```scss
.btn::after {
    // 預設尺寸
}
.btn.btn-sm::after {
    // 小尺寸調整
}
.btn.btn-lg::after {
    // 大尺寸調整
}
```

### D. 編輯器模式處理
```scss
// ✅ 必須禁用編輯模式下的動畫
#wrapwrap.odoo-editor-editable {
    .btn:hover::after {
        animation: none;
    }
}
```

### E. Hover 過渡效果
```scss
// ✅ 必須有平滑過渡
@mixin transition {
    transition: all 0.5s ease-in-out;
}
```

---

## 3. 預設風格庫（6 種）

以下為可直接套用的預設風格，選擇一種後全站統一使用。
完整的 SCSS 與預覽展示在 `templates/btn-style.scss` 中。

> [!NOTE]
> 下方 SCSS 範例為**精簡版核心邏輯**，實際部署時請從 `templates/btn-style.scss` 中複製完整版（含 o_cc1~o_cc5 色彩變數、尺寸適配、編輯器模式處理）。

---

### 3.1 右下角斜切 (Skew)

**Class:** `s_custom_btn01`  
**效果:** 按鈕右下角呈現斜切遮罩

```scss
#wrapwrap .btn:not(.dropdown-toggle):not(.oe_search_button):not([class*=outline]):not(.o_add_compare_dyn):not(.o_add_compare):not(.o_add_quote):not(.js_add_cart_json) {
    padding-right: 30px;
    mask: linear-gradient(314deg, rgba(167, 11, 11, 0) 16px, black 0%);
    border: none;
}
```

---

### 3.2 一般箭頭 (Arrow)

**Class:** `s_custom_btn021`  
**效果:** FontAwesome 箭頭 + Hover 晃動動畫

```scss
header, section {
    .btn:not(.dropdown-toggle):not(.oe_search_button):not(.o_add_compare_dyn):not(.o_add_compare):not(.o_add_quote) {
        display: inline-flex !important;
        gap: 6px;
        align-items: center;
        &::after {
            content: "\f105";
            font-family: "FontAwesome" !important;
        }
        &:hover::after {
            animation: btn-bounce-left2 .8s ease;
        }
    }
}
@keyframes btn-bounce-left2 {
    50% { transform: translateX(4px); }
}
```

---

### 3.3 細箭頭 (Thin Arrow)

**Class:** `s_custom_btn02`  
**效果:** CSS 繪製細長箭頭 + Hover 拉伸

```scss
header, section {
    .btn:not(.dropdown-toggle):not(.oe_search_button):not(.o_add_compare_dyn):not(.o_add_compare):not(.o_add_quote) {
        display: inline-flex !important;
        gap: 6px;
        &::after {
            content: "";
            width: 22px;
            height: 8px;
            border-right: 1px solid currentColor;
            border-bottom: 1px solid currentColor;
            transform: skewX(45deg);
        }
        &:hover::after {
            animation: btn-bounce-left 1s ease;
        }
    }
}
@keyframes btn-bounce-left {
    80% { transform: translateX(6px) skewX(45deg); }
}
```

---

### 3.4 圓點放大 (Dot Zoom)

**Class:** `s_custom_btn03`  
**效果:** 左側圓點 Hover 時放大填滿背景  
**注意:** padding-left 至少 36px

```scss
#wrapwrap .btn[class*='primary'], 
#wrapwrap .btn[class*='secondary'] {
    &:not(.dropdown-toggle):not(.oe_search_button) {
        position: relative;
        overflow: hidden;
        &::before {
            content: "";
            width: 6px;
            height: 6px;
            border-radius: 50%;
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            z-index: -1;
        }
        &:hover::before {
            transform: scale(100);
        }
    }
}
```

---

### 3.5 閃光效果 (Flash)

**Class:** `s_custom_btn04`  
**效果:** Hover 時光影快速掃過

```scss
#wrapwrap:not(.odoo-editor-editable) {
    header, section {
        .btn:not(.dropdown-toggle) {
            position: relative;
            overflow: hidden;
            &::before {
                content: '';
                position: absolute;
                left: -75%;
                width: 50%;
                height: 100%;
                background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,.3) 100%);
                transform: skewX(-25deg);
            }
            &:hover::before {
                animation: shine .75s;
            }
        }
    }
}
@keyframes shine {
    100% { left: 125%; }
}
```

---

### 3.6 傾斜填滿 (Hover Skew Fill)

**Class:** `s_custom_btn06`  
**效果:** Hover 時背景色斜切填滿

```scss
#wrapwrap .btn[class*='primary'], 
#wrapwrap .btn[class*='secondary'] {
    &:not(.dropdown-toggle):not(.oe_search_button) {
        position: relative;
        overflow: hidden;
        &::after {
            content: '';
            width: 100%;
            height: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-30deg);
            z-index: -1;
            transition: all 0.5s ease-in-out;
        }
        &:hover::after {
            height: 350%;
            width: 130%;
        }
    }
}
```

---

## 4. 色彩變數參考表

每個風格都需要支援 `o_cc1` ~ `o_cc5` 的色彩變數：

| 區塊 | Primary 變數 | Secondary 變數 |
|------|-------------|----------------|
| o_cc1 | `--o-cc1-btn-primary` | `--o-cc1-btn-secondary` |
| o_cc2 | `--o-cc2-btn-primary` | `--o-cc2-btn-secondary` |
| o_cc3 | `--o-cc3-btn-primary` | `--o-cc3-btn-secondary` |
| o_cc4 | `--o-cc4-btn-primary` | `--o-cc4-btn-secondary` |
| o_cc5 | `--o-cc5-btn-primary` | `--o-cc5-btn-secondary` |

Hover 狀態使用 `*-border` 後綴或 `color-mix()` 函式：
```scss
&:hover {
    background-color: var(--o-cc1-btn-primary-border);
    // 或
    background-color: color-mix(in srgb, var(--o-cc1-btn-primary) 90%, #222 35%);
}
```
