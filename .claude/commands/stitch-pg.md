# stitch-pg

一鍵執行：AI 生成頁面（Stitch/其他）轉換 + 產出 preview。

## 用法

```
/stitch-pg clientinfo/<專案資料夾>
```

或：

```
/stitch-pg clientinfo/<專案資料夾>/code.html
```

## 動作

1. 執行 `scripts/auto_convert_preview.py`
2. 自動轉換出：`outputs/<name>.xml`
3. 自動輸出報告：`outputs/<name>.report.md`
4. 自動輸出位移對應：`outputs/<name>.mapping.scss`
5. 自動產出 strict final baseline：`outputs/<timestamp>_<name>_strict_final.xml/.scss`
6. 建立預覽：`preview/index.html`
