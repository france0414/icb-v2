# 主題色更新指南

> **適用情境**：當你在 Odoo 後台更改了網站主題色之後，  
> 請按照以下步驟把最新的色碼同步給開發團隊。

---

## 什麼時候需要執行？

- 在 Odoo 後台 **網站 → 主題 → 色彩** 修改了任何顏色之後
- 開發人員告訴你「請更新配色」的時候

---

## 步驟（約 2 分鐘）

### 第 1 步：開啟你的網站

用 Chrome 或 Edge 開啟你的 Odoo 網站首頁。

---

### 第 2 步：打開開發者工具

按下鍵盤 **`F12`**，畫面右側或下方會出現一個工具面板。

點上方分頁列找到 **`Console`**（主控台）。

---

### 第 3 步：解鎖貼上功能（只需做一次）

在 Console 下方的輸入框裡，**手動輸入**以下文字，然後按 `Enter`：

```
allow pasting
```

> 這是 Chrome 的安全機制，輸入一次後就解鎖了。

---

### 第 4 步：貼入指令

把以下整段指令**複製**後**貼入** Console 輸入框，按 `Enter`：

```javascript
const s = getComputedStyle(document.documentElement);
['--o-color-1','--o-color-2','--o-color-3','--o-color-4','--o-color-5','--primary','--secondary','--o-cc1-bg','--o-cc2-bg','--o-cc3-bg','--o-cc4-bg','--o-cc5-bg','--o-cc1-text','--o-cc2-text','--o-cc3-text','--o-cc4-text','--o-cc5-text','--o-cc1-headings','--o-cc2-headings','--o-cc3-headings','--o-cc4-headings','--o-cc5-headings'].map(v=>`${v}: ${s.getPropertyValue(v).trim()}`).join('\n')
```

---

### 第 5 步：複製輸出結果

按 `Enter` 後，Console 會顯示一段文字，內容像這樣：

```
--o-color-1: #E60012
--o-color-2: #7A7A7A
--o-color-3: #EFEFEF
...
```

**把這段文字全部複製起來**（點一下輸出區域，全選後複製）。

---

### 第 6 步：傳給開發人員

把複製的內容貼給開發人員即可，例如：
- 貼到 Line / Email
- 或直接告訴 AI：「請用這些色碼更新 PROJECT_THEME.css」

---

## 完成！

開發人員收到後會更新 `docs/design/PROJECT_THEME.css`，  
之後 AI 生成的所有頁面就會自動套用你最新的品牌配色。

---

## 常見問題

**Q：Console 在哪裡找不到？**  
A：按 F12 後，在上方找 `Console`、`主控台` 或 `콘솔` 分頁（依瀏覽器語言不同）。

**Q：貼上後顯示錯誤？**  
A：確認有先輸入 `allow pasting` 並按 Enter，再貼入指令。

**Q：我用 Safari / Firefox 可以嗎？**  
A：可以，但建議使用 Chrome 或 Edge，步驟一致。Safari 可能不需要輸入 `allow pasting`。
