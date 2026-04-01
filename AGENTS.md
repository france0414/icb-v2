Rules:

> **繼續工作前請先讀 `TODO.md`，了解目前尚未完成的知識庫補充工作。**

- 你正在做 Odoo 15 WebBuilder 的頁面開發

- 本專案**不使用** git worktree，請直接在專案根目錄工作，不要建立 `.worktrees/` 或其他 worktree 目錄

- 所有 XML 必須由以下母節點包覆:
```xml
<t t-name="website.xxxxxx">
    <t t-call="website.layout">
        <div id="wrap" class="oe_structure oe_empty"/>
    </t>
</t>
```

- 首頁結構多加 pageName：
```xml
<t t-name="website.xxxxxx">
    <t t-call="website.layout">
        <t t-set="pageName" t-value="'homepage'"/>
        <div id="wrap" class="oe_structure oe_empty"/>
    </t>
</t>
```

- 輸出目錄在 `outputs/`，檔名必須含日期與時間
- 規劃呈現：除 `/create` Phase A 文字骨架外，禁止輸出 `plan.md` 或任何規劃檔；規劃僅在對話中簡短說明，使用者確認後直接執行
- 🚨 **AI 雙模式任務與 `templates/` 定位：**
  `templates/` 是「靈感庫 + 積木庫」，不是「直接成品庫」。嚴禁直接複製 templates/ 任一檔案完整結構作為最終輸出。
  1. **【套版模式 `/page`】** 允許從 `templates/` 和 `.agent/skills/icb_page_generator/resources/page_templates.md` 配方直接組裝，替換文案圖片即可。
  2. **【創作模式 `/create`】** 不論使用者是提供「純文字描述」還是「參考範例網址/截圖」，皆為創作模式。AI 必須重新設計 section 順序與視覺重心，以設計靈感為首，但骨架必須符合 Odoo 的「承重牆規則」（Bootstrap Grid QWeb 外框、對位 class、動態鎖定區塊）。先出文字骨架確認後，才生成 XML+SCSS。
  3. **【元件晉升保守策略】** 創作或抓站轉化出來的新畫面，預設只產出「當下專案可用草稿 (放在 outputs/)」，不自動拆成公版元件、不自動寫入 `templates/`；只有在使用者明確要求「晉升公版/元件化」時才執行。
  4. **SCSS 提取絕對原則**：為組件補給 SCSS 時，主來源**絕對是** `templates/` 內該組件同檔名的 `.scss` 檔案。嚴禁憑空通靈發明 CSS！
- `clientInfo/` 為客戶提供的素材區（文字、圖片、PPT 等）
- Icon 規範：主要使用 **Font Awesome v4**（例如 `fa fa-star`）
- 圖片使用 `https://picsum.photos/` 作為來源
- 佈局容器：每個 `<section>` 內的核心框架必須明確選擇使用 `.container` (寬度置中) 或 `.container-fluid` (滿版)，不可遺漏或隨意自創網格外殼。
- 樣式原則：新寫的樣式一律放 SCSS，禁止在 XML 內寫 `<style>`；`style=""` 僅在 Odoo 系統元件本身必須或既有結構已依賴時可保留/最小使用
- 🚨 **極度重要：若 `docs/design/user_custom_rules.scss` 已有客製樣式（如 `.s_custom_titleUnderLine`, `.s_custom_scaleL`, 輪播箭頭定位等），AI 只需要在 XML 套用對應的 class（並設定 `data-custom-name`）即可，禁止重寫；若沒有對應樣式，則必須在輸出 SCSS 補上。** (詳見 `.agent/skills/icb_page_generator/resources/scss_reference.md`)
- 🚨 **重疊與絕對定位保護：所有會導致元素重疊的 SCSS (如負邊距 `mt-n5`、絕對定位覆蓋圖文) 頂層必須加上 `#wrapwrap:not(.odoo-editor-editable)` 前綴，確保在 Odoo 編輯模式下元素會自動解開重疊，讓使用者能正常點選並替換文字與圖片！**
- 🚨 **斷點規範：符合 Bootstrap 4.5 的斷點，請使用 Bootstrap 4.5 的斷點寫法（含 `media-breakpoint-up/down` mixin）。若需額外斷點，請使用 `docs/design/user_custom_rules.scss` 內的自訂 RWD 斷點變數與 mixin（`//--自訂RWD 斷點變數 開始--//` 區塊）。**

## 可用 Commands

| 指令 | 說明 |
|------|------|
| `/page` | 生成完整頁面（🏷️ 套版模式） |
| `/create` | 創作全新頁面（無論輸入是網址/截圖或文字，皆先骨架分析後生成） |
| `/dynamic` | 快速加入動態產品/消息區塊 |
| `/btn` | 套用按鈕風格 |
| `/js` | 加入互動 JS 元件 |

## 深度知識

完整的 Snippet 規則和代碼參考在 Skill 中：
→ `.agent/skills/icb_page_generator/SKILL.md`

補充：
- 若使用者有參考資料要提供給 AI，放在 `clientInfo/`；公版結構參考放在 `templates/`
- 若 AI 要輸出新生成的 XML、SCSS 或其他交付檔，統一放在 `outputs/`

## Skill 同步流程

- ICB skill 的單一來源是 `sources/skill/icb_skill.source.json`
- 不要直接手改 `.agent/skills/icb_page_generator/SKILL.md`、`.agents/skills/icb_page_generator/SKILL.md`、`opencode.json`
- 修改共用 skill 規則後，執行：
```bash
# macOS/Linux
python3 scripts/sync_icb_skill.py

# Windows
py -3 scripts/sync_icb_skill.py
```
- 上述指令會自動同步更新 Gemini、Copilot 與 OpenCode 的 skill 入口
