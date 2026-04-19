# create-home (首頁創作模式)

設計全新首頁。結合 /create 三階段流程 + /page-home 首頁專屬規範。

## Steps

0. **Terse prompt 偵測**：若使用者輸入少於 20 字或只有抽象形容詞（「歐美簡約」「高級感」「現代」）而無具體版面指示，**必須先 Agent 呼叫 `design-director` 子代理**反問 3 個關鍵決策，取得擴寫過的 brief.json 後才繼續。具體輸入則跳過此步。
1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. 讀 `docs/design/PROJECT_THEME.css` 與 `docs/design/user_custom_rules.scss`（字體大小變數、客製 class）
3. `home_recipes.md` 僅作靈感參考，非強制套用
4. **Phase 0 — 內容解析**：若 Step 0 已由 design-director 產 brief，則跳過；否則輸出 `outputs/<日期時間>_brief.json`，停下等確認
5. **Phase A — 文字骨架**：從 brief 推導版面；每個區塊選擇必須引用 brief 欄位理由；首頁必備 Hero → 服務亮點 → 產品/案例 → 關於我們 → 最新消息；列出 Bootstrap Grid 對應與 Snippet；停下等確認
6. **Phase B — 分段生成頁面內容 XML + SCSS**（只處理 `<div id='wrap'>` 內 sections，不含 Footer；依 section 數量拆 1~3 段：≤4 一次到位、5–7 拆 B1/B2、≥8 拆 B1/B2/B3）：
   - 首頁專屬：`<t t-call="website.layout">` 內必加 `<t t-set="pageName" t-value="'homepage'"/>`
   - 每個 section 明確使用 pt-*/pb-* 間距 utility（含斷點變體），8 的倍數
   - 標題字級一律 var(--h1)~var(--h6)，禁止硬編 clamp/rem
   - 可點卡片：父層 position-relative s_custom_clickableCard、既有 <a> 加 s_custom_cardLink，SCSS 用 ::before overlay 並加 `#wrapwrap:not(.odoo-editor-editable)` 守護
   - 動態區塊對接 s_dynamic_snippet*，遵守 templates/base/base-dynamic-*.xml locked 結構
   - 每段 preview 確認後再下一段
7. **Footer 獨立輸出**（首頁必做）：另產 `outputs/<時間>_footer.xml` + `.scss`，使用 `<data inherit_id="website.layout"><xpath expr="//div[@id='footer']" position="replace">` 包覆，依專案內容客製欄位
8. 產出後執行預覽：`PYTHONIOENCODING=utf-8 python scripts/build_preview.py outputs/<產出檔>.xml`

## 使用方式

```
/create-home [需求描述 或 參考網址]
```

## 與其他指令的差異

| 指令 | 是否 Phase 0 brief | 是否文字骨架 | pageName |
|---|---|---|---|
| `/page` | 否 | 否 | 否 |
| `/page-home` | 否 | 否 | ✅ |
| `/create` | ✅ | ✅ | 否 |
| `/create-home` | ✅ | ✅ | ✅ |
