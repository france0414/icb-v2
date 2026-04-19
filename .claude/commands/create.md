# create (創作模式)

設計新版面。三階段流程：Phase 0 內容解析 → Phase A 文字骨架 → Phase B 分段生成。輸入可為純文字或外部網址。

## Steps

0. **Terse prompt 偵測**：輸入少於 20 字或僅有抽象形容詞（「歐美簡約」「工業風」）而無具體指示時，先 Agent 呼叫 `design-director` 子代理反問 3 題並擴寫 brief。具體輸入則跳過此步。
1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. **Phase 0 — 內容解析（中介層）**：若 Step 0 已產 brief 則跳過；否則解析輸入抽出 business/keyAssets/mustHaves/excluded/visualDirection，輸出 `outputs/<日期時間>_brief.json`，停下等使用者確認
3. **Phase A — 文字骨架**：從 brief 推導版面（不再套 home_recipes），每個區塊選擇必須引用 brief 欄位理由；列出 Bootstrap Grid 對應與 Snippet 類型，停下等確認
4. **Phase B — 分段生成 XML + SCSS**：拆 2–3 段，每段寫完立即 preview 確認再下一段；骨架先行、文案後填
5. 動態內容（產品/新聞）必須對接 `s_dynamic_snippet*`，不可手刻假卡片
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
