# dynamic

快速加入動態產品或動態消息區塊。

## Steps

1. 讀取 `.agent/skills/icb_page_generator/resources/dynamic_rules.md`
2. 確認使用者要生成的是 **動態產品 (Products)** 還是 **動態消息/部落格 (Blogs)**。

### 👉 動態產品 (Products) 參數表
| 模板名稱 (Template) | Template Key (部分) |
|---|---|
| Borderless Card 1 | `...borderless_1` |
| Centered Product | `...centered` |
| Classic Card | `...add_to_cart` |
| Horizontal Card | `...horizontal_card` |

*可選附掛類別 (Custom Classes)*: `scaleL`, `scaleS`, `nameHoverUnderLine`, `imgNoMargin`, `arrowRight`, `titleHoverFull`

### 👉 動態消息/部落格 (Blogs) 參數表
| 模板名稱 (Template) | Template Key (部分) |
|---|---|
| Card Layout | `...blog_post_card` |
| Big Picture | `...blog_post_big_picture` |
| Horizontal | `...blog_post_horizontal` |
| List Layout | `...blog_post_list` |

*可選附掛類別 (Custom Classes)*: `cardRadius`, `borderHover`, `hoverUnderLine`, `titleLine`, `picTop`, `picBottom`, `dateTop`

3. 根據上面挑選的參數，依照嚴格的 XML 結構指引輸出代碼。
