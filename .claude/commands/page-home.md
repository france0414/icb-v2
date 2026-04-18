# page-home (首頁套版模式)

專為首頁設計的快速生成指令。讀取配方索引後直接組裝 XML + SCSS。

## Steps

1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. 讀 `docs/design/PROJECT_THEME.css`
3. 讀 `.agent/skills/icb_page_generator/resources/home_recipes.md` 取得目標配方的區塊清單
4. 依需求讀 `.agent/skills/icb_page_generator/resources/snippet_rules.md`
5. 需要動態區塊時，依 `.agent/skills/icb_page_generator/resources/dynamic_rules.md`，並遵守 `templates/base/base-dynamic-*.xml` 的 locked 結構
6. 輸出到 `outputs/`（XML + SCSS，檔名含日期時間）

## 使用方式

```
/page-home [版型編號 1-4] [需求描述]
```

- 指定版型編號（1–4）→ 以 `home_recipes.md` 對應配方為區塊骨架，替換內容與色彩
- 不指定版型 → 根據需求描述從 4 個配方中選最適合的

## 首頁必備區塊順序（預設）

1. Hero / Banner（Carousel 或靜態大圖）
2. 服務亮點 / 特色介紹
3. 產品 / 案例展示
4. CTA 行動呼籲
5. 頁腳前置區（品牌資訊、聯絡方式）

## 首頁專屬 XML 結構注意事項

首頁的 `t-call="website.layout"` 內**必須**加入：

```xml
<t t-call="website.layout">
  <t t-set="pageName" t-value="'homepage'"/>
  ...
</t>
```

`pageName` 設為 `'homepage'` 是首頁特有的識別標記，其他頁面類型不需要此行，**切勿遺漏**。
