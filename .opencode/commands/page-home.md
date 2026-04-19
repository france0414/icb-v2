# page-home（首頁套版模式）

專為首頁設計的快速生成指令。讀取 home_recipes.md 配方後直接組裝 XML + SCSS。

## Hard Rules

- 首頁 XML 必須在 `website.layout` 內加入 `<t t-set="pageName" t-value="'homepage'"/>`，**切勿遺漏**。
- 本專案禁止使用 git worktree；不得建立 `.worktrees/` 或任何 worktree 目錄。
- home_recipes.md 為 AI 配方參考，不得直接複製輸出，須替換內容與配色。

## Steps

1. 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`
2. 讀取專案配色：`docs/design/PROJECT_COLORS.json`（主色、各 o_cc 背景/文字色、usage 說明、note 特殊規則）
3. 讀取配方：`.agent/skills/icb_page_generator/resources/home_recipes.md`
   - 指定版型編號（1–4）→ 以對應配方為區塊骨架
   - 不指定 → 根據需求自動選擇
4. 依需求讀取 `resources/snippet_rules.md`
5. 需要動態區塊時，依 `resources/dynamic_rules.md`，並遵守 `templates/base/base-dynamic-*.xml` 的 locked 結構
6. 輸出 XML + SCSS 到 `outputs/`（檔名含日期時間）
