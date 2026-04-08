# Skill 編寫與自動化部署標準流程

> 本文件適用於 **france0414/icb-v2** 專案，定義 Skill 開發的角色分工、標準流程、以及自動化部署機制（CI/CD）。

---

## 1. 角色分工表

| 角色 | 職責範圍 | 輸入 | 產出 |
|------|---------|------|------|
| **內容規劃者** (Content Planner) | 定義 Skill 的使用情境、知識邊界與測試案例 | 使用者需求、設計稿、歷史對話 | `resources/*.md` 草稿、`knowledge_map` 條目草案 |
| **技術負責人** (Tech Lead) | 制定 Skill 格式規範、審閱 `icb_skill.source.json` 結構、核准合併 | 草稿文件、PR diff | 審查意見、合併核准 |
| **維運自動化工程師** (DevOps Engineer) | 維護 `scripts/sync_icb_skill.py` 同步腳本、管理 CI/CD Workflow | 同步腳本、`.github/workflows/` | 更新後的同步機制、自動 PR 觸發 |
| **驗收人員** (QA Reviewer) | 執行 Skill 功能測試（AI 對話驗收）、確認知識庫準確性 | 部署後的 SKILL.md | 驗收報告、回饋清單 |
| **發布協調者** (Release Coordinator) | 統籌版本 tag、整理 Release Notes | 驗收通過的 PR | Release tag、`TODO.md` 更新 |

---

## 2. Skill 開發標準流程（完整步驟）

### Phase A — 需求分析與草稿

```
1. [內容規劃者] 定義觸發情境
   - 明確描述「什麼問題要靠這份知識解決」
   - 列出 3~5 個測試 Prompt 範例

2. [內容規劃者] 撰寫知識文件草稿
   - 放置於 .agent/skills/icb_page_generator/resources/
   - 格式：Markdown，含表格/範例/規則/禁止事項

3. [技術負責人] 審閱草稿
   - 確認知識不重複既有資源
   - 確認新知識有對應到 icb_skill.source.json 的 knowledge_map
```

### Phase B — 整合至 SSOT

```
4. [技術負責人] 更新 sources/skill/icb_skill.source.json
   - 在 knowledge_map 新增條目（意圖描述 → 檔案路徑）
   - 在 resource_files 新增檔名
   - 如需新規則，加入 core_rules

5. [維運自動化工程師] 執行同步腳本
   $ python3 scripts/sync_icb_skill.py
   
   同步目標（自動更新）：
   ├── .agent/skills/icb_page_generator/SKILL.md  (Gemini/Copilot)
   ├── .agents/skills/icb_page_generator/SKILL.md (其他 Agent)
   ├── opencode.json                               (OpenCode)
   └── .claude/commands/*.md                       (Claude 指令)
```

### Phase C — 驗收與發布

```
6. [驗收人員] 功能驗收（AI 對話測試）
   - 用 3~5 個 Prompt 測試觸發與產出品質
   - 填寫驗收清單

7. [發布協調者] 合併 PR、打 tag、更新 TODO.md
   - PR title 格式：feat(skill): 新增 [知識名稱]
   - TODO.md 中標記 [x] 已完成
```

---

## 3. 自動化部署 DevOps 流程圖（純文字步驟）

```
┌─────────────────────────────────────────────────────────────┐
│                    SKILL 開發自動化流程                      │
└─────────────────────────────────────────────────────────────┘

[開發者] 修改 resources/*.md  OR  icb_skill.source.json
    │
    ▼
[本地端] 執行同步腳本（手動或 pre-commit hook）
    $ python3 scripts/sync_icb_skill.py
    │
    ├─→ .agent/skills/icb_page_generator/SKILL.md（Gemini/Copilot 入口）
    ├─→ .agents/skills/icb_page_generator/SKILL.md（其他 Agent）
    ├─→ opencode.json（OpenCode 設定）
    └─→ .claude/commands/*.md（Claude 快捷指令）
    │
    ▼
[Git] commit + push → 發起 Pull Request
    │
    ▼
[GitHub Actions] 自動觸發（建議實作）
    │
    ├─→ validate_dynamic_lock.py    ─→ 確認 locked 結構未被修改
    ├─→ 比對 SKILL.md 與 source.json 是否同步  ─→ 若不同步，CI 失敗並標記 PR
    └─→ 發送通知（Slack/Email）給驗收人員
    │
    ▼
[驗收人員] 執行 AI 對話測試 → 在 PR 留下驗收意見
    │
    ▼
[技術負責人] Code Review → Approve 或 Request Changes
    │
    ▼
[發布協調者] Merge → 自動 tag（如 skill/v1.2.0）→ 更新 TODO.md
    │
    ▼
[所有 AI 模型] 自動讀取最新 SKILL.md / opencode.json（下次對話即生效）
```

---

## 4. 專案檔案/腳本組織建議

```
icb-v2/
├── sources/
│   └── skill/
│       └── icb_skill.source.json    ← 唯一知識來源（SSOT）：修改從這裡開始
│
├── scripts/
│   ├── sync_icb_skill.py            ← 同步腳本（Python）
│   ├── sync_icb_skill.sh            ← Bash 封裝（macOS/Linux）
│   ├── sync_icb_skill.bat           ← BAT 封裝（Windows）
│   └── validate_dynamic_lock.py     ← 驗證 locked 結構完整性
│
├── .agent/skills/icb_page_generator/
│   ├── SKILL.md                     ← 自動生成（Gemini/Copilot 入口，勿手改）
│   └── resources/                   ← 知識文件目錄（手動維護）
│       ├── snippet_rules.md         ← Snippet 分類/嵌套/o_colored_level 規則
│       ├── layout_patterns.md       ← 版面設計模式
│       ├── button_styles.md         ← 按鈕規範（<a> + 組合 class）
│       ├── dynamic_rules.md         ← 動態區塊規則
│       ├── component_library.md     ← JS 互動元件
│       ├── page_templates.md        ← 首頁配方
│       ├── custom_blocks.md         ← 歷史客製區塊
│       ├── scss_reference.md        ← SCSS 變數/mixin 參考
│       ├── header_footer_rules.md   ← Header/Footer 規則
│       ├── form_rules.md            ← 表單規則
│       ├── system_pages_scss.md     ← 系統頁面 SCSS 覆寫
│       ├── skill_devops_process.md  ← 本文件：Skill 開發流程
│       └── indexes/
│           └── templates_index.json ← 模板快速定位索引
│
├── .agents/skills/icb_page_generator/
│   └── SKILL.md                     ← 自動生成（其他 Agent 入口，勿手改）
│
├── .claude/commands/                ← 自動生成（Claude 指令，勿手改）
│   ├── icb.md
│   ├── page.md
│   ├── create.md
│   ├── dynamic.md
│   ├── btn.md
│   ├── js.md
│   └── block.md
│
├── opencode.json                    ← 自動生成（OpenCode 設定，勿手改）
├── AGENTS.md                        ← 全域規則（手動維護）
└── TODO.md                          ← 知識庫工作清單（手動維護）
```

### 修改流程原則

| 要修改什麼 | 應該編輯哪個檔案 | 之後執行 |
|-----------|----------------|---------|
| 共用規則 / 描述 / 核心指令 | `sources/skill/icb_skill.source.json` | `python3 scripts/sync_icb_skill.py` |
| 新增知識文件 | `resources/新知識.md` + 更新 `source.json` | `python3 scripts/sync_icb_skill.py` |
| 全域硬規則 | `AGENTS.md` | 無需同步（直接生效） |
| 待辦工作 | `TODO.md` | 無需同步（直接生效） |
| 模板文件 | `templates/` 目錄 | 無需同步 |

---

## 5. GitHub Actions 建議配置（供 DevOps 工程師實作）

以下為建議的 CI 驗證步驟，可加入 `.github/workflows/skill-sync-check.yml`：

```yaml
# .github/workflows/skill-sync-check.yml
name: Skill Sync Validation

on:
  pull_request:
    paths:
      - 'sources/skill/**'
      - '.agent/skills/**'
      - '.agents/skills/**'
      - 'scripts/**'

jobs:
  validate-sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Run sync script and verify output is up-to-date
        run: |
          python3 scripts/sync_icb_skill.py
          if ! git diff --exit-code .agent/skills/ .agents/skills/ opencode.json .claude/; then
            echo "❌ SKILL.md or related files are out of sync with icb_skill.source.json."
            echo "   Please run: python3 scripts/sync_icb_skill.py and commit the result."
            exit 1
          fi
          echo "✅ All skill entry points are in sync."
          
      - name: Validate dynamic lock structures
        run: python3 scripts/validate_dynamic_lock.py

  notify-reviewer:
    needs: validate-sync
    runs-on: ubuntu-latest
    if: success()
    steps:
      - name: Comment on PR (remind QA review)
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '✅ Skill 同步驗證通過。\n請驗收人員使用 AI 對話測試以下情境，並在此 PR 回饋：\n- [ ] 觸發 Skill 正確\n- [ ] 知識輸出準確\n- [ ] 無重複/衝突規則'
            })
```

---

## 6. 知識文件品質核查清單（每次新增資源前確認）

- [ ] 知識文件放置於 `resources/` 目錄
- [ ] 已在 `icb_skill.source.json` 的 `knowledge_map` 新增對應意圖描述
- [ ] 已在 `icb_skill.source.json` 的 `resource_files` 加入檔名
- [ ] 確認與現有文件無重複知識（先搜尋）
- [ ] 新知識有具體範例（XML/SCSS/表格）
- [ ] 若有硬規則，已加入 `core_rules`
- [ ] 執行 `python3 scripts/sync_icb_skill.py` 同步完成
- [ ] 至少用 2 個 AI Prompt 測試觸發與輸出
