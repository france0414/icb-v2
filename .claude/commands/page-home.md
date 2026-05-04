# page-home (首頁套版模式)

專為首頁設計的快速生成指令。讀取配方索引後直接組裝 XML + SCSS。

## Steps

1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. 讀 `docs/design/PROJECT_THEME.css` 與 `docs/design/user_custom_rules.scss`
3. 讀 `.agent/skills/icb_page_generator/resources/home_recipes.md` 取得目標配方
4. 依需求讀 `.agent/skills/icb_page_generator/resources/snippet_rules.md`
5. 需要動態區塊時依 `resources/dynamic_rules.md`，遵守 `templates/base/base-dynamic-*.xml` locked 結構
6. **可點卡片**：產品分類/應用卡保留原 <a>，父層加 position-relative s_custom_clickableCard、既有 <a> 加 s_custom_cardLink；SCSS 用 #wrapwrap:not(.odoo-editor-editable) .s_custom_cardLink::before { inset:0; position:absolute; } overlay；禁用 stretched-link
7. **Footer 獨立輸出**：另產 `outputs/<時間>_footer.xml` + `.scss`，用 `<data inherit_id="website.layout"><xpath expr="//div[@id='footer']" position="replace">` 包覆，依專案客製
8. 每個 section 明確 pt-*/pb-* 間距（含斷點變體），標題字級用 var(--h1)~var(--h6)，禁止硬編 clamp/rem
9. 輸出到 `outputs/`（XML + SCSS，檔名含日期時間）

## 使用方式

```
/page-home [版型編號 1-4] [需求描述]
```

## 首頁專屬

`<t t-call="website.layout">` 內必加 `<t t-set="pageName" t-value="'homepage'"/>`，切勿遺漏。
