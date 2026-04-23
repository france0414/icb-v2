# icb-v2 – AI 強制規則（Odoo XML + Page Generator）

> 適用範圍：本專案所有 AI 產生或修改的程式碼。
> 優先順序：本檔規則 > 專案既有程式碼風格 > 其他一般最佳實務。

---

## 1. Odoo XML / QWeb 結構規則（不得違反）

1. **禁止重寫既有 XML 結構**

   - 若檔案中已存在 Odoo view / template：
     - 只能做「最小修改」（新增區塊、微調內容）。
     - **禁止** 整段改寫、改動既有 `<xpath>`、`<t>` 結構或改變繼承方式。
   - 若要新增內容，優先在現有結構中插入，而不是重建整個 view。

2. **class 命名與 HTML 結構**

   - 所有 HTML / XML class 一律使用 **kebab-case**，例如：
     - `icb-hero-section`, `icb-feature-card`, `icb-page-header`
   - **禁止**：
     - `camelCase`, `PascalCase`, `snake_case`
     - 自行發明新命名風格
   - 若檔案內已有 class 命名慣例，**必須沿用**，不得改名或改風格。

3. **section + layout 結構（重要）**

   - 頁面主結構 layout 一律採用：

     ```xml
     <section class="s_vertical_layout icb-...">
       <div class="container"> 或 <div class="container-fluid">
         <div class="oe_structure">
           <!-- 這裡才可以插入多個 section/snippet -->
         </div>
       </div>
     </section>
     ```

   - **禁止**：
     - 直接輸出 `section` 裡面再巢狀 `section` 當一般內容。
     - 在非 `oe_structure` 區域任意插入新的 section。
   - 若需要多區塊，請在 `oe_structure` 內放入多個 snippet / section，而不是外層再包 section。

4. **xpath 使用規則**

   - 只能使用 **既有 / 已定義的 xpath 位置** 插入內容。
   - 不得：
     - 更改既有 xpath 的 `expr`。
     - 改變 xpath 的 `position`（除非明確要求）。
     - 移除既有 xpath 區塊。
   - 若需要新 xpath，優先請人類開發者定義；AI 不自行創造重要 xpath 插入點。

5. **snippet 命名規則**

   - snippet / section id 命名格式統一為：

     ```text
     <module>_<page>_<section>
     例如：icb_home_hero, icb_home_features, icb_pricing_section
     ```

   - 不可使用無意義 id，如：`section1`, `custom_block`, `my_snippet`。

---

## 2. HTML → Odoo XML 轉換規則

1. 若使用者提供 **HTML / JSX / Next.js 結構** 要轉成 Odoo XML：

   - **不得改變**：
     - DOM 階層結構（除了必要的 Odoo tag 包裝）。
     - class 名稱（除非明確要求重命名）。
   - 可以做的事：
     - 將 `<div>` / `<section>` 適度轉為 Odoo `<t>`、`<section>`、`<xpath>`、`<t t-foreach>` 等。
     - 加上必要的 `t-esc`、`t-out`、`t-if` 等 QWeb attribute。

2. 在轉換前，請先列出一段簡短說明（給人類看的）：

   - 「沿用的 class 命名」
   - 「套用的 layout 結構（包含 s_vertical_layout / container / oe_structure）」
   - 「使用到哪些 xpath（若有）」

---



## 3. Odoo Website 專案分工

1. 本專案為 Odoo Website / QWeb / XML 專案。
2. 所有頁面結構、snippet、section、layout、template inheritance 皆以 Odoo XML 為主。
3. AI 不得假設本專案存在 Next.js、React、Vue 或其他獨立前端框架，除非使用者明確要求。
4. 所有頁面修改必須優先沿用既有 Odoo view、template、xpath、class 命名與 snippet 結構。
5. 若需新增頁面版型，優先使用 Odoo 可編輯結構：
   - `section.s_vertical_layout`
   - `container` 或 `container-fluid`
   - `oe_structure`

---

## 4. AI 回覆格式要求

1. **在輸出 XML / 代碼前，先簡短說明：**

   - 「我遵守了哪些上面規則（列出 2–4 點）」。
   - 然後再給出程式碼區塊。

2. 每次修改既有檔案時，請標註：

   - 「新增區塊」vs「修改區塊」。
   - 避免混在一起看不出差異。

---

> 若無法同時滿足使用者需求與以上規則，請先說明「哪一條規則會被破壞」，並詢問使用者是否同意例外處理，而不是直接忽略本檔規則。