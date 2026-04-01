# page (套版模式)

依照現有樣板配方或 Snippet 規則，快速生成頁面（XML + SCSS）。若需全新設計改用 `create`。

## Steps

1. 讀 ` .agent/skills/icb_page_generator/SKILL.md`
2. 讀 `docs/design/PROJECT_THEME.css`
3. 依需求讀 `resources/page_templates.md` / `resources/snippet_catalog.md`
4. 需要動態區塊時，依 `resources/dynamic_rules.md`，並遵守 `templates/base/base-dynamic-*.xml` 的 locked 結構
5. 輸出到 `outputs/`（XML + SCSS）
