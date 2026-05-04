# page-home (首頁套版模式)

專為首頁設計的快速生成指令。讀取配方索引後直接組裝 XML + SCSS。

## Steps

0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. 讀 `docs/design/PROJECT_THEME.css` 與 `docs/design/user_custom_rules.scss`
3. 讀 `.agent/skills/icb_page_generator/resources/home_recipes.md` 取得目標配方
4. 依需求讀 `.agent/skills/icb_page_generator/resources/snippet_rules.md`
5. 需要動態區塊時依 `resources/dynamic_rules.md`，遵守 `templates/base/base-dynamic-*.xml` locked 結構
6. 若使用者想先看版型而非直接產正式碼，可先提供 layout-only HTML 骨架確認
7. **可點卡片**：產品分類/應用卡保留原 <a>，父層加 position-relative s_custom_clickableCard、既有 <a> 加 s_custom_cardLink；SCSS 用 #wrapwrap:not(.odoo-editor-editable) .s_custom_cardLink::before { inset:0; position:absolute; } overlay；禁用 stretched-link
8. **Footer 獨立輸出**：另產 `outputs/<時間>_footer.xml` + `.scss`，用 `<data inherit_id="website.layout"><xpath expr="//div[@id='footer']" position="replace">` 包覆，依專案客製
9. 每個 section 明確 pt-*/pb-* 間距（含斷點變體），標題字級用 var(--h1)~var(--h6)，禁止硬編 clamp/rem
10. 輸出到 `outputs/`（XML + SCSS，檔名含日期時間）

## 使用方式

```
/page-home [版型編號 1-4] [需求描述]
```

## 首頁專屬

`<t t-call="website.layout">` 內必加 `<t t-set="pageName" t-value="'homepage'"/>`，切勿遺漏。
