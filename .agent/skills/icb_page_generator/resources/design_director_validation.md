# design-director 最小驗證清單（4 Cases）

目的：釐清觸發邏輯與分工是否正確，避免誤觸發或漏觸發。

## 驗證規則

- 2 筆應觸發（terse/抽象）
- 2 筆不應觸發（具體）
- 每筆都要記錄：是否觸發、是否只做 brief、是否正確交棒

## Case 1（應觸發）

- Input：`/create-home B2B 軸承歐美風`
- Expected：
  - 觸發 design-director（或 fallback 三問）
  - 先問 3 題，不直接出 brief
  - 回答後產出 `brief.json`
  - 不產 XML/SCSS

## Case 2（應觸發）

- Input：`/create 關於我們 要高級感`
- Expected：
  - 觸發 design-director（或 fallback 三問）
  - 先問 3 題
  - 產出具名 `designMoves`（3-5 個）
  - 不越權到 Phase A/B

## Case 3（不觸發）

- Input：`/create-home Hero 用 asymmetric split，產品用規格表，案例用 index list，色系黑白紅`
- Expected：
  - 不觸發 design-director
  - 直接進 Phase 0（產 brief）
  - 不重複反問同一組 3 題

## Case 4（不觸發）

- Input：`/page-home 1`
- Expected：
  - 不觸發 design-director
  - 走套版流程

## 驗證紀錄格式（建議）

```text
[日期時間]
Case: <1|2|3|4>
Env: <claude|opencode|other>
Trigger: <yes|no>
FallbackUsed: <yes|no>
OnlyBriefStage: <yes|no>
HandoffCorrect: <yes|no>
Notes: <補充>
```

## 驗收門檻

- 4/4 符合 Expected
- 任一案例失敗即維持 `experimental`

## 最新驗證結果

### 2026-04-20（Rule E2E Dry-run）

```text
[2026-04-20]
Case: 1
Env: claude+opencode (rule check)
Trigger: yes
FallbackUsed: yes (entrypoint rule exists)
OnlyBriefStage: yes
HandoffCorrect: yes
Notes: /create-home terse 條件與 design-director 觸發規則一致。

[2026-04-20]
Case: 2
Env: claude+opencode (rule check)
Trigger: yes
FallbackUsed: yes (entrypoint rule exists)
OnlyBriefStage: yes
HandoffCorrect: yes
Notes: /create terse 條件與 design-director 觸發規則一致。

[2026-04-20]
Case: 3
Env: claude+opencode (rule check)
Trigger: no
FallbackUsed: no
OnlyBriefStage: yes
HandoffCorrect: yes
Notes: 具體 prompt 明確標示「具體輸入則跳過此步」。

[2026-04-20]
Case: 4
Env: claude+opencode (rule check)
Trigger: no

FallbackUsed: no
OnlyBriefStage: yes
HandoffCorrect: yes
Notes: design-director 明確排除 /page 與 /page-home。
```

- 結果：`4/4` 符合 Expected。
- 補充：跨入口 fallback 規則已對齊（原先 1 筆文案不一致已修正），E2E 規則檢查總計 `6/6 PASS`。
