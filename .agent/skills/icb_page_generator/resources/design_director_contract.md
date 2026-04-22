# design-director 分工契約（Experimental）

## 目的

在 `/create` 與 `/create-home` 的輸入過短或過度抽象時，避免直接落入安全版型，先補齊可執行的 `brief.json` 決策。

## 觸發條件

- 指令為 `/create` 或 `/create-home`
- 使用者輸入少於 20 字，或只有抽象形容詞而缺少具體版面指示

## 不觸發條件

- `/page`、`/page-home`（套版模式）
- 已提供具體佈局策略（例如 Hero 結構、產品呈現法、視覺語彙）

## 角色邊界

### design-director 負責

- 先做網站類型分流題（B2B / 牙醫 / 其他自填）
- 先完成 Hero 問卷（媒體型態、Slogan、按鈕導流、點擊互動）
- 再補 2 個關鍵問題（內容結構與視覺語彙）
- 收到回答後產出 `outputs/<YYYY-MM-DD_HHMM>_brief.json`
- 提供 3 個決策摘要與 Phase A 建議方向

### 主流程 agent 負責

- Phase A：文字骨架
- Phase B：分段 XML + SCSS
- Phase C：Footer 獨立輸出（僅 `/create-home`）

## 禁止事項（design-director）

- 不產 XML/SCSS
- 不產 Phase A 文字骨架
- 不讀 `templates/`
- 不跳過反問直接產 brief

## I/O 契約

- **Input**：原始 prompt + 專案規範上下文
- **Output**：
  - `brief.json` 檔案路徑
  - 三個決策摘要
  - 建議下一步（進入 Phase A）

## Fallback（跨平台同步規則）

若執行環境不支援 subagent：

- 由主流程直接提出同一組「分流題 + Hero 問卷 + 2 題」（與 design-director 同規格）
- 等使用者回答後，主流程產出 `brief.json`
- 後續流程與有 subagent 時相同

## 狀態標記

- 目前狀態：`experimental`
- 需先通過 `design_director_validation.md` 的 4 筆最小案例，才可升級為 stable
