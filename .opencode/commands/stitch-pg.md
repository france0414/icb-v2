# stitch-pg

一鍵執行：Stitch/HTML → ICB/Odoo 一般頁轉換 + preview。

## 用法

```
/stitch-pg clientinfo/<專案資料夾>
```

或：

```
/stitch-pg clientinfo/<專案資料夾>/code.html
```

## 補充

- 共用腳本：`scripts/auto_convert_preview.py`
- 一般 page 預設不注入 homepage 結構
- 若有案件前台網址，正式 preview 前應先更新 live asset bundles；未提供網址時可先用 fallback preview 對稿

## 動作

1. 執行 `scripts/auto_convert_preview.py --input <path>`
2. 轉換出：`outputs/<name>.xml` + `outputs/<name>.scss`
3. 輸出 normalize 報告：`outputs/<name>.normalize.report.md`
4. 輸出轉換備註：`outputs/<name>.mapping.scss`
5. 輸出 strict final baseline：`outputs/<timestamp>_<name>_strict_final.xml/.scss`
6. 建立預覽：`preview/<時間>_<名稱>.html`（同時更新 `preview/index.html` 作為最新預覽捷徑）
