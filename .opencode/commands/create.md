# create

以 ICB 元件為靈感，重新設計全新頁面結構。與 /page（套版模式）不同，此指令要求 AI 自行創作排版。

## Steps

### Phase A：規劃骨架（先輸出，等待確認）
1. 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`
2. 讀取專案配色：`docs/PROJECT_THEME.css`
3. 若使用者未明確說明，需先確認：產業類型、視覺風格、重點訴求、是否需動態區塊
4. 讀取 `resources/custom_blocks.md` 了解 templates/ 可用積木類型（僅作語法參考）
5. 輸出文字骨架：每個 section 的類型、設計概念、參考積木、與既有差異
6. ⛔ Phase A 嚴禁輸出 XML 或 SCSS 程式碼

### 🚦 Gate：等待使用者確認或調整

### Phase B：生成 XML + SCSS（確認後才執行）
7. 靜態區塊自由創作 XML；輪播外框用系統結構、slide 內容自由；動態用 s_dynamic_snippet 只寫 SCSS
8. SCSS 只包含實際使用的樣式，禁止整包複製
9. 輸出 XML + SCSS 到 outputs/（檔名含日期時間，圖片用 picsum.photos）

## 禁止事項
- ❌ 直接複製 templates/ 完整結構
- ❌ 照搬 page_templates.md 配方順序
- ❌ Phase A 輸出程式碼
- ❌ 動態區塊自創 HTML
