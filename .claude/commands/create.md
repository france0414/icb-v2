# create (創作模式)

設計新版面。三階段流程：Phase 0 內容解析 → Phase A 文字骨架 → Phase B 生成與合併輸出。輸入可為純文字或外部網址。

## Steps

0. **Terse prompt 偵測（experimental）**：輸入少於 20 字或僅有抽象形容詞（「歐美簡約」「工業風」）而無具體指示時，優先呼叫 `design-director` 子代理反問 3 題並擴寫 brief；若環境不支援 subagent，改由主流程直接反問同一組 3 題後再產 brief。具體輸入則跳過此步。
1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. **Phase 0 — 內容解析（中介層）**：若 Step 0 已產 brief 則跳過；否則解析輸入抽出 business/keyAssets/mustHaves/excluded/visualDirection，輸出 `outputs/<日期時間>_brief.json`，停下等使用者確認
3. **Phase A — 文字骨架**：從 brief 推導版面（不再套 home_recipes），每個區塊選擇必須引用 brief 欄位理由；列出 Bootstrap Grid 對應與 Snippet 類型，停下等確認
4. **Phase B — 生成 XML + SCSS**：可分段思考與逐段 preview，但最終必須合併輸出為單一 `outputs/<時間>_full.xml` + `outputs/<時間>_full.scss`；骨架先行、文案後填
5. 產品/Blog 區塊預設可先用靜態 sheet + row/col；僅在明確要求動態資料時才對接 `s_dynamic_snippet*`
6. 每個 section 必須明確使用 pt-*/pb-* 間距 utility；標題字級用 var(--h1)~var(--h6)，禁止硬編 clamp/rem
7. 嚴禁覆蓋既有 `templates/`，產出統一存放 `outputs/`

## brief.json 格式

```json
{
  "business": { "type": "", "industry": "", "market": "", "tone": [] },
  "keyAssets": { "productCategories": [], "trustSignals": [], "applications": [] },
  "mustHaves": [],
  "excluded": [],
  "visualDirection": { "palette": "", "typography": "", "imagery": "" }
}
```
