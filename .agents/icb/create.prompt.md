---
name: create
description: 以 templates/ 為靈感庫，創作全新 ICB 頁面（禁止直接複製任何 template 結構）
---

# /create

以 ICB 元件為靈感，**重新設計**全新頁面結構。與 `/page`（套版模式）不同，此指令要求 AI 自行創作排版。

## 用法範例

```
/create 機械產業首頁
/create 科技感的關於我們頁面
/create 溫暖風格的產品展示頁，需要產品輪播和公司沿革
```

## 執行步驟

### Phase A：規劃骨架（先輸出，等待確認）

#### 1. 讀取 Skill
讀取 `.agents/skills/icb_page_generator/SKILL.md`

#### 2. 讀取專案配色
讀取 `docs/PROJECT_THEME.css`

#### 3. 詢問 / 確認需求
若使用者未明確說明，需先確認：
- 產業類型（科技 / 製造 / 服務 / 零售...）
- 視覺風格（科技感 / 溫暖 / 專業簡約 / 大膽...）
- 重點訴求（產品展示 / 品牌形象 / 服務介紹...）
- 是否需要動態區塊（產品輪播 / 部落格新聞）

#### 4. 盤點可用積木
讀取 `resources/custom_blocks.md` 了解 templates/ 有哪些積木類型，但**僅作為語法參考**。

#### 5. 輸出文字骨架
產出每個 section 的規劃：
```
Section 1: [類型] — [設計概念與訴求]
  → 參考積木：[Banner-XX / Content-XX / 全新創作]
  → 與既有模板差異點：[說明]
Section 2: ...
```

> ⛔ **Phase A 嚴禁輸出任何 XML 或 SCSS 程式碼**

### 🚦 Gate：等待使用者確認或調整

### Phase B：生成 XML + SCSS（確認後才執行）

#### 6. 依確認的骨架生成程式碼
- 靜態區塊：自由創作 XML 結構
- 輪播 Banner：外框用系統輪播結構，slide 內容自由設計
- 動態產品/消息：使用 `s_dynamic_snippet` 系統結構，只寫 SCSS 樣式
- SCSS 來源：參考 templates/ 同名 .scss 的**寫法**，但不整包複製

#### 7. 輸出
1. **XML** — QWeb 模板（圖片用 `https://picsum.photos/`）
2. **SCSS** — 只包含此頁面實際使用的樣式

輸出到 `outputs/` 目錄，檔名含日期時間。

## 禁止事項

- ❌ 直接複製 templates/ 任一檔案的完整結構
- ❌ 照搬 page_templates.md 的配方順序
- ❌ Phase A 階段輸出程式碼
- ❌ 動態區塊自創 HTML 結構
