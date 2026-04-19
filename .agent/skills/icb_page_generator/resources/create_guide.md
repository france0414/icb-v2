# /create 設計組合引導手冊

> 此文件從所有 content-sections 模板中提煉設計規律，專供 `/create` 指令在 Phase A 骨架規劃與 Phase B 程式碼生成時參考。  
> 讀此文件前請先確認已讀 `snippet_rules.md`（Snippet 嵌套規則）與 `layout_patterns.md`（基礎佈局模式）。

---

## 一、設計意圖 → 分類快速對照表

當使用者描述需求時，依關鍵詞對應分類，再查 `templates_index.json` 取得對應 XML：

| 使用者說... | 對應分類 | 模板 key |
|------------|---------|---------|
| icon 清單、服務特色、功能卡片、水平排列帶 icon | `feature-highlight` | `content-section-feature-highlight` |
| 品牌故事、文字+圖、關於我們、介紹區、左圖右字 | `intro-content` | `content-section-intro-content` |
| 成就數字、累積統計、計數器、業績展示 | `achievement` | `content-section-achievement` |
| 視差效果、固定背景圖、滾動色塊切換、全螢幕區塊 | `visual-parallax` | `content-section-visual-parallax` |
| 相片牆、多圖展示、相簿、輪播、水平捲動 | `gallery-showcase` | `content-section-gallery-showcase` |
| 分頁Tab、FAQ、地圖、滑鼠互動特效、產業應用、解決方案 | `solution-industry` | `content-section-solution-industry` |

---

## 二、跨類別通用修飾器 (Utility Modifiers)

這些 `s_custom_*` class 可以疊加在任何標準 Snippet 上，不限分類使用：

### `s_custom_titleUnderLine` ⚠️ 選用，依設計需求決定
- **加在**：`s_text_block` section
- **效果**：標題文字下方加底線裝飾
- **使用條件**：**只在設計稿/需求明確要求底線標題裝飾時才加**；一般標題不預設套用
- **不該用的情況**：深色背景 section、標題本身已有其他視覺強調、極簡風格頁面
- **範例**：
  ```xml
  <section class="s_text_block o_colored_level pt0 pb0 s_custom_titleUnderLine"
           data-snippet="s_text_block" data-name="Text"
           data-custom-name="titleUnderLine" style="background-image: none;">
  ```

### `s_custom_fullContainer`
- **加在**：`s_vertical_layout` 或 `s_column_layout` 的 section
- **效果**：讓內部容器突破標準 padding 限制，視覺延伸至邊緣
- **慣用場景**：需要全版色塊、出血圖片、邊緣切齊效果的 section
- **常與** `s_custom_insertBelow`、`s_custom_textUnderFeature`、`s_custom_textmultiCarousel` 搭配

### `s_custom_backgroundColor`
- **加在**：`s_text_block` section（通常在 `s_column_layout` 的子 section）
- **效果**：為特定欄加上客製背景色塊
- **慣用場景**：左右欄中，讓某一欄有實心色塊背景（不同於父層 `o_cc`）
- **必須搭配** `s_custom_fullContainer` 使用，才能讓色塊延伸至邊緣

### `s_custom_reverse`
- **加在**：`s_text_block` section（含 2 欄 row 結構時）
- **效果**：在手機版讓左右欄順序對調（避免圖片下移跑到文字後面）
- **慣用場景**：所有左圖右文或左文右圖的 2-col 排版，幾乎必加

### `s_custom_noRemove`
- **加在**：`s_embed_code` section
- **效果**：SCSS 會在編輯模式顯示「重要 Code，請勿刪除」警示
- **規則**：⚠️ **所有 JS 互動區塊的 s_embed_code 必須加此 class + `data-custom-name="noRemove"`**

### `s_custom_scaleL`
- **加在**：`s_static_snippet` 或 `s_static_carousel` section
- **效果**：卡片懸停時放大縮放特效
- **慣用場景**：gallery 相簿卡片、產品卡片展示，提升互動感

### `s_custom_default`
- **加在**：`s_static_snippet` section
- **效果**：還原 static_snippet 的預設卡片樣式（清除客製化覆蓋）
- **常與** `s_custom_brickAlbum`、`s_custom_scaleL` 同時出現

---

## 三、s_vertical_layout 作為組合容器的結構規則

> ⚠️ 這是所有以 `s_vertical_layout` 包裹多個子 section 的核心規則，違反會造成左右 padding 不一致。

`s_vertical_layout` 的直接子層**必須是 `container-fluid`**（左右 padding = 0），而不是 `container`。
這樣裡面每個子 section 才能各自用 `.container` 套用全域統一的 `--container-pd-x`。

```xml
<!-- ✅ 正確：外層 container-fluid，內層各 section 自帶 container -->
<section data-snippet="s_vertical_layout" class="s_vertical_layout o_colored_level pt80 pb72"
         data-name="Vertical Layout" style="background-image: none;">
  <div class="container-fluid">                        ← 外層滿版，左右 padding 為 0
    <div class="oe_structure oe_structure_not_nest oe_empty">

      <section class="s_text_block o_colored_level pt0 pb0" data-snippet="s_text_block">
        <div class="container s_allow_columns">        ← 子 section 各自 container，統一左右距離
          ...
        </div>
      </section>

      <section class="s_static_snippet o_colored_level pt0 pb0" data-snippet="s_static_snippet">
        <div class="container">                        ← 同上，各自 container
          ...
        </div>
      </section>

    </div>
  </div>
</section>
```

```xml
<!-- ❌ 錯誤：外層就用 container，子 section 再套 container → 雙層 padding，內縮過多 -->
<section data-snippet="s_vertical_layout" class="s_vertical_layout o_colored_level ...">
  <div class="container">        ← 不可在這裡用 container
    <div class="oe_structure">
      <section class="s_text_block ...">
        <div class="container">  ← 造成雙重 padding，內容被過度擠壓
```

**子 section 的容器寬度選擇**：

| 子 section 用途 | 容器 class | 說明 |
|---------------|-----------|------|
| 一般文字、標題、icon 清單 | `container s_allow_columns` | 標準寬度，跟頁面其他區塊對齊 |
| 文章、說明型窄版文字 | `o_container_small` | 最大寬度 1200px，適合閱讀型內容 |
| 需要突破左右限制（出血） | 搭配 `s_custom_fullContainer` SCSS | 由 SCSS 控制取消 container padding |

---

## 四、已驗證的黃金組合配方

### 配方 A：標準 Section 標題區（所有分類通用）

每個主要 section 的頂端都應套用這個三段式標題骨架：

```
s_vertical_layout  ← 直接子層必須是 container-fluid（見第三節）
  └─ s_text_block (container)   ← 大標題
  └─ s_text_block (container)   ← 副標題或說明文字
  └─ [主要內容 Snippet (container)]
```

> **s_custom_titleUnderLine** 是選用裝飾，只在設計需要底線強調時才加到標題 s_text_block；不要預設套用。

**pt/pb 建議**：外層 `pt88 pb72`，標題 section 均設 `pt0 pb0`。

---

### 配方 B：Sticky 左標題 + 右捲動內容

適用：品牌故事、FAQ、功能說明清單、左側固定說明、右側多段落

```xml
<section class="s_column_layout o_colored_level o_auto_screen_height pt48 pb40"
         data-sticky="used" data-snippet="s_column_layout">
  <div class="col-wrapper container">
    <div class="row d-flex align-items-stretch">
      <!-- 左欄：黏著標題 (col-lg-4 ~ col-lg-5) -->
      <div class="col-lg-4 s_col_no_bgcolor col-left">
        <div class="s_column_layout_content oe_structure col-sticky">
          <!-- s_title / s_text_block / s_text -->
        </div>
      </div>
      <!-- 右欄：捲動內容 (col-lg-7 ~ col-lg-8) -->
      <div class="col-lg-8 col-right o_colored_level">
        <div class="s_column_layout_content oe_structure">
          <!-- s_faq_collapse / s_text_image / s_static_snippet / 等 -->
        </div>
      </div>
    </div>
  </div>
</section>
```

**實際案例**：排版7 (sticky + simpleFAQ)、排版12 (pageIntro + textUnderLeft)、排版14 (text + carousel)、排版22 (fixBGList)

---

### 配方 C：s_counting 計數器區塊

`s_counting` 必須以 `s_text_block` 為容器，再加客製 class 控制外觀。

```xml
<!-- 容器 section -->
<section class="s_text_block o_colored_level pt0 pb0 s_custom_counterPrimary"
         data-snippet="s_text_block" data-name="Text"
         data-custom-name="counterPrimary" style="background-image: none;">
  <div class="container">
    <div class="row">
      <div class="col-lg-4 text-center">
        <div class="s_counting c_counting o_not_editable"
             data-count-from="0"
             data-count-to="300"
             data-count-timer="1"
             data-delay-timer="0"
             data-count-before-text=""
             data-count-after-text="+"
             data-snippet="s_counting" data-name="Counting">
        </div>
        <div class="s_text" data-snippet="s_text" data-name="Text">標籤文字</div>
      </div>
      <!-- 重複欄位... -->
    </div>
  </div>
</section>
```

**三種計數器容器樣式選擇**：
| class | 外觀特徵 | 來源排版 |
|-------|---------|---------|
| `s_custom_counterPrimary` | 主色大數字、簡潔 | 排版6 |
| `s_custom_insertBelow` | 數字插入下方圖片，需 `fullContainer` | 排版19 |
| `s_custom_counterAfterColor` | 數字右側接彩色色塊說明文字 | 排版21 |

**搭配 parallax 的黃金組合**：
```xml
<section class="s_column_layout parallax s_parallax_is_fixed s_parallax_no_overflow_hidden
                o_auto_screen_height o_colored_level pt64 pb80"
         data-scroll-background-ratio="1" data-sticky="none"
         data-snippet="s_column_layout">
```
→ 左欄放標題+說明，右欄放計數器 `s_text_block (counterPrimary)`

---

### 配方 D：視差背景 (Parallax) 必要 class 組合

在 Odoo 15，parallax 效果靠以下 class **全部到位** 才能運作：

```
parallax  s_parallax_is_fixed  s_parallax_no_overflow_hidden
```

同時 section 必須加 `data-scroll-background-ratio="1"`（或其他數值）。

**三種視差使用模式**：

| 模式 | 結構 | class 加在哪 |
|------|------|------------|
| **段落固定背景** | `s_column_layout` 或 `s_text_block` | 直接在 section 上 |
| **全螢幕視差圖** | `s_parallax` snippet | `s_parallax parallax s_parallax_is_fixed` |
| **滾動切換背景** | 多個 `s_text_block (scrollItemBgFix)` | 每個 text block 分別加 |

**全螢幕視差配方（排版20）**：
```xml
<section class="s_vertical_layout s_parallax_no_overflow_hidden s_custom_fullScreenParallax"
         data-scroll-background-ratio="0" ...>
  <!-- 視差佔位圖層 -->
  <section class="s_parallax parallax s_parallax_is_fixed o_colored_level o_auto_screen_height"
           data-scroll-background-ratio="1" data-fade-method="none"
           data-snippet="s_parallax" ...>
  </section>
  <!-- 文字內容層 (疊在視差上方) -->
  <section class="s_text_block parallax s_parallax_is_fixed s_parallax_no_overflow_hidden
                  o_auto_screen_height o_colored_level o_cc o_cc3"
           data-scroll-background-ratio="1" ...>
  </section>
</section>
```

---

### 配方 E：Tab 導航區（產業/應用分頁）

結構層次：`s_vertical_layout (tabEffectContent)` → 標題區 → `s_tabs (tabEffect)`

每個 Tab 面板內的固定結構：
```
s_text (簡介文字)
s_media_list (pt0 pb0 + oe_img_bg o_bg_img_center → 全寬背景圖)
  └─ s_media_list_item
       └─ s_media_list_item_body → 覆蓋文字
```

關鍵：`s_media_list` 上加 `oe_img_bg o_bg_img_center` 讓清單背景圖全版，再用 SCSS 控制高度。

---

### 配方 F：JS 互動區塊的標準三段結構

每個 JS 互動區塊（fullImgHoevr1/2、productRightScroll、mapEffect 等）都遵循：

```
[1] 標題 section (s_text_block, 給客戶識別用途)
    └─ data-name="標題" or "描述"
[2] 主視覺 section (s_vertical_layout 或 s_text_block + s_custom_XXX)
    └─ 放 HTML 結構
[3] s_embed_code (s_custom_noRemove, 放對應 JS)
    └─ data-custom-name="noRemove"  ← 必填
    └─ <script>...</script>          ← JS 邏輯
```

⚠️ JS 的 querySelector 必須用特定 class 精準鎖定，不可使用通用 id。

---

### 配方 G：相簿 + 點擊放大燈箱

```
s_vertical_layout
  ├─ s_click_popup (style="display:none" aria-hidden="true")  ← 燈箱容器
  │   └─ s_image_gallery (o_slideshow)                        ← 燈箱內的輪播
  └─ s_static_snippet (s_custom_brickAlbum s_custom_scaleL)  ← 縮圖展示格
```

`s_click_popup` 的 `id` 與縮圖上的 `data-bs-target` 需一對一對應。

---

### 配方 H：圖文交錯清單 (moreDescription 模式)

多組圖文交錯排版，使用 `s_text_image` 重複疊加：

```
s_vertical_layout (s_custom_moreDescription)
  └─ s_text_image (pt32 pb32)  ← 圖片在右
  └─ s_text_image (pt32 pb32)  ← 圖片在右（內容在左）
     - 加 s_custom_reverse 讓手機版不破版
  └─ s_text_image (pt32 pb32)
```

每個 `s_text_image` 內：描述段 `.description.pb32.pt8` + 延伸段 `.description.pt32.pb0`。

---

## 四、s_column_layout 左右欄比例慣例

根據不同用途選擇欄寬比例：

| 用途 | 左欄 | 右欄 | 備注 |
|------|------|------|------|
| 標題+說明 / 主內容 | `col-lg-4` | `col-lg-8` | 最常見，右側內容較豐富 |
| 均等分欄 | `col-lg-6` | `col-lg-6` | 對等比較、雙特色說明 |
| 窄標題+寬主體 | `col-lg-3` | `col-lg-9` | 右側為圖片牆或卡片網格時 |
| 寬文字+窄圖 | `col-lg-7` | `col-lg-5` | 文字重的設計，圖作輔助 |

無論何種比例，左欄 sticky 時加 `class="col-sticky"` 在 `.s_column_layout_content` 上。

---

## 五、設計節奏：Section 順序建議

一個完整頁面的 section 順序規律（非強制，但符合閱讀習慣）：

```
1. Banner / Hero         → 首屏吸引注意（banner 模板）
2. intro-content         → 品牌/產品簡介（配方 B sticky 或排版17/18）
3. feature-highlight     → 核心特色列表（配方 A + iconCardHorizontal）
4. solution-industry     → 深度應用說明（Tab 或 FAQ）
5. achievement           → 數字佐證（計數器 + parallax）
6. visual-parallax       → 視覺分隔/強調引語（hoverBgTextEfect 或 fullScreenParallax）
7. gallery-showcase      → 案例/相簿（brickAlbum 或 textmultiCarousel）
8. CTA / Form            → 行動呼籲（footer 或 form-contact）
```

**色彩節奏**（配合 `o_cc1`~`o_cc5`）：
```
o_cc1(白) → o_cc2(淺灰) → o_cc1(白) → o_cc4(主深色) → o_cc1(白) → o_cc3(主色) → o_cc5(深)
```

---

## 六、常見錯誤對照表

| ❌ 錯誤 | ✅ 正確 |
|--------|--------|
| `s_vertical_layout` 直接子層用 `container`（非 `container-fluid`） | 外層必須 `container-fluid`，讓子 section 各自接 `container` |
| 把 `s_counting` 直接放在 section 內不包 text_block | 必須包在 `s_text_block` 裡 |
| parallax section 少了 `s_parallax_no_overflow_hidden` | 三個 parallax class 必須同時在場 |
| `s_embed_code` 沒有加 `s_custom_noRemove` | 所有 JS block 必加 noRemove |
| `s_column_layout` 用 `data-sticky="used"` 但子欄沒有 `col-sticky` | sticky 必須在 `.s_column_layout_content` 加 `.col-sticky` |
| 多圖交錯沒加 `s_custom_reverse` | 確保手機版圖片不會移到文字後面 |
| 自行寫 `s_static_snippet` 骨架 | 必須從 `templates_index.json` 找 XML 參考，再讀取骨架 |
| `s_custom_fullContainer` 搭配 `s_custom_backgroundColor` 少了一個 | 兩者要同時加才能正確出血 |

---

## 七、/create Phase A 骨架規劃對照口訣

收到需求後，Phase A 骨架描述時用這個框架驗證每個 section：

```
[section 編號] [設計意圖] 
  → Snippet: [從 snippet_rules.md 選]
  → 修飾器: [s_custom_* 清單]
  → 配方: [參照本文件哪個配方]
  → 欄寬比: [如有 column_layout]
  → 視差/互動: [parallax/JS/tab/counting 等特效]
```

**範例**：
```
[S3] 累積數字展示 (公司成就)
  → Snippet: s_column_layout
  → 修飾器: parallax, s_parallax_is_fixed, s_parallax_no_overflow_hidden, s_custom_fullContainer
  → 配方: 配方C (計數器) + parallax 背景
  → 欄寬比: col-lg-5 / col-lg-7
  → 互動: s_counting × 3 (data-count-to 依客戶數字)
```
