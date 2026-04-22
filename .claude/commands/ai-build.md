# ai-build（AI 網站轉 Odoo）

將任意 AI 生成網站（HTML）整理為 Odoo 可用輸出，並套用專案固定規則。

## 用法

```
/ai-build <xml-path> <scss-path>
```

範例：

```
/ai-build outputs/20260421_131309_wellstand_content_convert.xml outputs/20260421_131309_wellstand_content_convert.scss
```

## Steps

1. 執行標準化腳本：
   - `python3 scripts/normalize_ai_build.py <xml-path> <scss-path>`
2. 產生規則報告：
   - `<xml-path>` 同名 `.normalize.report.md`
3. 重建預覽：
   - `python3 scripts/build_preview.py <xml-path> <scss-path>`

## 內建規則（摘要）

- `section` 層禁止 `px-*`
- 內層 `s_custom_*` 轉為一般 class（section 層保留 `s_custom_*`）
- `w-full/h-full` -> `w-100/h-100`
- `sm:/md:/lg:/xl:order-*` -> Bootstrap `order-*`
- SEO 標題跳級時改 `p.h*`
- `text-xs` 轉 `<small>`
- 輪播控制移除 `display:none`
