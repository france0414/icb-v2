# 標準生成模板（可直接貼給 AI）

這份是給設計師快速測試用的「可複製模板」，分成兩種：

- A. 直接生成網頁（Final）
- B. 先生成佈局文字（Layout-first 骨架）

---

## A) 直接生成網頁（Final）模板

### A1. 內頁 `/create`（Final）

```text
/create 請做【<頁面名稱>】。
請讀取素材：clientinfo/<專案資料夾>/README.md 與同資料夾圖片。

要求：
1) 直接做 Final（不要 Layout-first）
2) 產品/Blog 預設用靜態 sheet + row/col（除非我明確說 dynamic）
3) Hero 用 <3:9 / 4:8 / 5:7 / 6:6>，總和 12
4) 圖片先用我提供素材，沒有的才用占位
5) 產出 XML + SCSS 到 outputs/
```

### A2. 首頁 `/create-home`（Final）

```text
/create-home 請做【<首頁主題>】。
請讀取素材：clientinfo/<專案資料夾>/README.md 與同資料夾圖片。

要求：
1) 直接做 Final
2) Hero：<輪播 / 單圖 / 單影片 / 影片+第二張圖>
3) Hero 按鈕導流：<產品大類 / 主推產品 / 能力 / 解決方案 / ESG / 聯絡>
4) 區塊順序：Hero → 特色 → 產品/案例 → 解決方案/產業應用 → 關於我們 → Blog
5) Footer 需獨立輸出
6) 產出 XML + SCSS 到 outputs/
```

---

## B) 先生成佈局文字（Layout-first 骨架）模板

### B1. 內頁 `/create`（只出骨架）

```text
/create 請先做【Layout-first】版：<頁面名稱>。
請讀取：clientinfo/<專案資料夾>/README.md。

只要輸出「佈局文字骨架」，不要進入 Final。
規則：
1) 圖片位置全部灰色色塊占位（不放彩圖）
2) 明確列 section 順序
3) 每個 section 標註 container/container-fluid
4) 每個 section 標註 row/col 比例（總和 12）
5) 標註每段 pt/pb
6) 產品/Blog 用靜態 sheet + row/col
```

### B2. 佈局文字輸出格式（AI 應照此格式回覆）

```text
[Page]
- Name: <頁面名稱>
- Mode: Layout-first (gray blocks)

[Section 1] Hero
- Container: <container / container-fluid>
- Grid: <例 col-lg-4 + col-lg-8>
- Media: Gray block
- Copy: <主標占位 / 副標占位 / 按鈕占位>
- Spacing: ptXX pbXX

[Section 2] <區塊名稱>
- Container: ...
- Grid: ...
- Content: ...
- Spacing: ...

[Section N] Blog
- Type: Static sheet + row/col
- Card count: <3/4/...>
- Spacing: ptXX pbXX

[Footer]
- Note: Footer 另檔輸出（若為 create-home）
```

---

## C) 最小測試範例（你可直接貼）

```text
/create 李先生-解決方案內頁，先做 Layout-first。
素材在 clientinfo/li-mr/README.md。
Hero 用 4:8。
產品與 Blog 用靜態 sheet + row/col。
只輸出佈局文字骨架，不做 Final。
```

```text
/create 李先生-解決方案內頁，改做 Final。
沿用同一份素材，套入圖片與文案。
輸出 XML + SCSS 到 outputs/。
```
