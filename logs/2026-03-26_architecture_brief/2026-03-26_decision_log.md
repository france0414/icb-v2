# 2026-03-26 Decision Log: ICB AI 架構 v1

## 背景

- 專案：`icb-v2`（Odoo WebBuilder）
- 目標：先建立可落地的 v1 架構，後續保留變化空間（可接 Figma / Pencil）
- 參考：本 repo 規則（`AGENTS.md`、`TODO.md`、`pipeline/`）、早上討論（LLM 在 AI 專案的應用）

## 共識（Decisions）

- 先做「穩定可運作」v1，不追求一次到位。
- LLM 分工先聚焦在「創意/內容」：文案濃縮、標題副標、icon 建議、描述文字。
- 版型結構、Odoo 規則、輸出格式由系統規則控制，不讓 LLM 自由發散。
- 不管來源是文字 / Figma / Pencil，都先轉成同一份中介規格，再進入 Odoo pipeline。

## v1 架構（Draft）

- Input Layer：先支援文字輸入（首頁標題 + 對應文案），格式用 JSON。
- Planning Layer：LLM 只負責把長文案整理成 3~5 個區塊，輸出統一 planning JSON。
- Composition Layer：依 ICB/Odoo 規則決定 section 順序與可用 snippet；`/page` 走套版規則。
- Render Layer：輸出 XML + SCSS（遵守 `AGENTS.md` 規範；動態區塊保持 locked 結構）。
- Validation Layer：驗證外框、container、`data-custom-name`、RWD、編輯模式可操作性。

## 規格（Planning JSON v1 構想）

- 欄位：`section`, `title`, `subtitle`, `description`
- 選填：`icon`, `cta`, `priority`, `source_ref`

## 未決事項（Open Questions）

- planning JSON 的 `section` 枚舉與對應的 snippet/模板映射表要怎麼定義（先少量、再擴充）。
- Figma / Pencil 的資料進來後，如何做最小資訊抽取（命名規範、frame 分段、元件識別）。

## 風險與缺資料（Risks/Assumptions）

- 尚未提供「真實 ICB 全部樣版」：v1 先以 repo 既有 `templates/` + `resources/` 規則推進。
- 若參考 Odoo 15 GitHub 資源：需先做 Odoo 14/15 相容性對照，避免直接套用造成不相容。

## 下一步（Next Actions）

- 定義 `homepage_planning.schema.json`（v1）。
- 做一個最小 PoC：文案 -> planning JSON -> 人工確認 -> XML/SCSS 產出。
- 第二階段再接 Figma/Pencil 匯入，不在 v1 一次做完。

## 狀態（Status）

- Copilot：正在搜集 Odoo 15 / ICB 相關參考資料（進行中）

## 等待項（Dependencies）

- Odoo 15 GitHub 資源整理結果（來源、可用片段、相容性風險）

## 暫停範圍（Hold）

- 在 Copilot 資料回來前，暫不定稿 planning schema、暫不進入實作階段（避免方向反覆）
