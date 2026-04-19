# Timeline Rules（歷史沿革 /create 模式指南）

> 此文件供 `/create` 模式使用，讓 AI 能從零生成歷史沿革區塊，不依賴 `/page`。
> 範本參考：`templates/improved/timelines/time-line.xml`、`templates/base/base-time-line.xml`
> SCSS 來源：`templates/improved/timelines/time-line.scss`

---

## 三種結構家族

| 家族 | data-snippet | 適合場景 | 行動裝置行為 |
|------|-------------|---------|------------|
| A. s_timeline | `s_timeline` | 有時間軸線、左右或單側卡片 | date 在上，content 堆疊在下 |
| B. s_vertical_layout 列表 | `s_vertical_layout` | 無軸線、每行獨立 row | Bootstrap 欄位自動堆疊 |
| C. s_text_image 交錯 | `s_vertical_layout` + 內嵌 `s_text_image` | 大圖 + 文字左右交錯 | 文字在上、圖片在下 |

---

## 家族 A：s_timeline Snippet（帶軸線）

### 核心結構

```xml
<section class="s_timeline pt24 pb48 o_colored_level [parallax_classes] s_custom_[NAME]"
         data-snippet="s_timeline" data-name="Timeline"
         style="background-image: none;" data-custom-name="[NAME]">

  <!-- 視差背景（選用） -->
  <span class="s_parallax_bg oe_img_bg o_bg_img_center"
        style="background-image: url('https://picsum.photos/1920/600');"/>
  <!-- 暗色遮罩（選用） -->
  <div class="o_we_bg_filter bg-black-25"/>

  <div class="s_timeline_line o_container_small" [style="border-color: rgb(R,G,B)!important;"]>

    <!-- Row：每個時間點 -->
    <div class="s_timeline_row d-block d-md-flex flex-row" data-name="Row">
      <div class="s_timeline_date">
        <span class="bg-white"><b class="o_default_snippet_text">2019</b></span>
      </div>
      <!-- 第一個 s_timeline_content = 左側 -->
      <div class="s_timeline_content d-flex">
        <div class="s_timeline_card s_card card w-100" data-name="Card" data-snippet="s_card">
          <div class="card-body"><p>內容文字</p></div>
        </div>
      </div>
      <!-- 第二個 s_timeline_content = 右側（空 = 佔位） -->
      <div class="s_timeline_content"/>
    </div>

  </div>
</section>
```

### 左右布局邏輯（關鍵規則）

| 布局模式 | 第一個 s_timeline_content | 第二個 s_timeline_content |
|---------|--------------------------|--------------------------|
| **左側單邊**（timeLine03/05） | `d-flex` + 有卡片內容 | 空 `<div class="s_timeline_content"/>` |
| **右側單邊** | 空 `<div class="s_timeline_content"/>` | `d-flex` + 有卡片內容 |
| **交錯（奇左偶右）** | 奇數行：填內容；偶數行：空 | 奇數行：空；偶數行：填內容 |

> 行動裝置（`d-block d-md-flex`）：所有排列都變成垂直堆疊，左右區分消失。
> date 永遠顯示在 content 上方。

### 視差背景用法

加入視差時，在 `<section>` 加上：
```
parallax s_parallax_is_fixed s_parallax_no_overflow_hidden
data-scroll-background-ratio="1"
```
並在 section 第一個子元素放：
```xml
<span class="s_parallax_bg oe_img_bg o_bg_img_center"
      style="background-image: url('https://picsum.photos/1920/600');"/>
```

### 動畫用法

在 `s_timeline_row` 加入：`o_animate o_anim_fade_in_up o_visible`

### 自訂 class 對照

| 變體 | s_custom_* class | 特色 |
|-----|-----------------|------|
| timeLine03 | `s_custom_timeLine03` | 視差 bg + Wavy 形狀 + 左側單邊卡片 |
| timeLine05 | `s_custom_timeLine05` | 視差 bg + 橘色軸線 + 左側單邊 + 動畫 |
| base-alternate | `s_custom_timeLineBase s_custom_timelineLineCenter s_custom_timelineModeAlternate` | 無 bg，交錯模式 |
| base-left | `s_custom_timeLineBase s_custom_timelineLineLeft s_custom_timelineModeLeft` | 左側單邊 |
| base-right | `s_custom_timeLineBase s_custom_timelineLineRight s_custom_timelineModeRight` | 右側單邊 |

---

## 家族 B：s_vertical_layout 列表（無軸線）

### 核心結構

```xml
<section data-snippet="s_vertical_layout"
         class="s_vertical_layout o_colored_level pt0 pb0 s_custom_[NAME]"
         data-name="Vertical Layout" style="background-image: none;"
         data-custom-name="[NAME]">
  <div class="container">
    <div class="oe_structure oe_structure_not_nest oe_empty">

      <!-- 每個時間點 = 一個 s_text_block section -->
      <section class="s_text_block o_colored_level pb24 pt24"
               data-snippet="s_text_block" data-name="Text" style="background-image: none;">
        <div class="s_allow_columns container">
          <div class="row [no-gutters]">
            <!-- 年份 + 文字欄 -->
            <div class="o_colored_level col-lg-8">
              <h3><strong>2019</strong></h3>
              <p><strong>標題</strong>內文說明</p>
            </div>
            <!-- 圖片欄 -->
            <div class="o_colored_level col-lg-4">
              <p><img class="img-fluid" src="https://picsum.photos/600/400" alt="" loading="lazy"/></p>
            </div>
          </div>
        </div>
      </section>

    </div>
  </div>
</section>
```

### 欄位比例變體

| 變體 | 欄位組合 | 說明 |
|-----|---------|-----|
| **timeLine01**（基本） | `col-lg-8` 文字 + `col-lg-4` 圖片 | 無外框，簡潔 |
| **timeLine02**（卡片） | 同上，外層加 `border` 或 `shadow` class | 有邊框 / 陰影卡片效果 |
| **timeLine04**（三欄） | `col-lg-2` 年份 + `col-lg-6` 文字 + `col-lg-4` 圖片 | 年份獨立欄 |
| **timeLine06**（split bg） | `col-lg-8` 文字 + `col-lg-4` 圖片，交替 `o_cc4` | 左灰右品牌色背景 |

### timeLine06 split bg 技巧

wrapper section 加 `style="background-image: linear-gradient(90deg, rgb(245,245,245) 0%, rgb(245,245,245) 50%, rgb(BrandR,BrandG,BrandB) 50%, rgb(BrandR,BrandG,BrandB) 100%);"`

奇數 row 的 section：`style="background-color: rgb(245,245,245) !important; background-image: none;"`
偶數 row 的 section：加 class `o_cc o_cc4`（使用品牌色 4）

### timeLine02 卡片外框

在 `<div class="row no-gutters">` 的直接子 `col-lg-12` 加：
- 邊框版：`class="col-lg-12 o_colored_level border" style="border-width: 1px !important;"`
- 陰影版：`class="col-lg-12 o_colored_level shadow"`

---

## 家族 C：s_text_image 交錯（大圖模式）

### 核心結構

```xml
<section data-snippet="s_vertical_layout"
         class="s_vertical_layout pt32 pb32 o_colored_level s_custom_[NAME]"
         data-name="Vertical Layout" style="background-image: none;"
         data-custom-name="[NAME]">
  <div class="container-fluid">
    <div class="oe_structure oe_structure_not_nest oe_empty">

      <!-- 每個時間點 = 一個 s_text_image section -->
      <section class="s_text_image o_colored_level pt64 pb64"
               data-snippet="s_text_image" data-name="Text - Image"
               style="background-image: none;">
        <div class="container">
          <div class="row align-items-stretch">

            <!-- 左：文字 + 年份 -->
            <div class="col-lg-6 o_colored_level text-content pt16 pb16">
              <div class="s_text time-year" data-snippet="s_text" data-name="Text">
                <p class="h2"><strong>1990</strong></p>
              </div>
              <p>說明文字</p>
            </div>

            <!-- 右：圖片（單圖版） -->
            <div class="col-lg-6 o_colored_level img-content pt16 pb16">
              <div class="s_text" data-snippet="s_text" data-name="Text">
                <div class="row">
                  <div class="o_colored_level col-lg-12">
                    <img src="https://picsum.photos/800/500" class="img img-fluid mx-auto" alt="" loading="lazy"/>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

    </div>
  </div>
</section>
```

### 圖片欄版本

| 版本 | 圖片欄 HTML | 說明 |
|-----|------------|-----|
| **單圖** | `col-lg-12` × 1 | 全寬大圖 |
| **三圖網格** | `col-lg-4` × 3 | 橫排三張圖 |

### 交替背景規則

奇數 row（1st、3rd…）：`style="background-image: none;"` （預設白）
偶數 row（2nd、4th…）：`style="background-color: rgb(245,245,245) !important; background-image: none;"`

> 行動裝置：文字在上（左 col 先渲染），圖片在下。文字永遠在圖片之前顯示。

---

## 如何選擇家族

```
需要視覺軸線（中軸線）？
  ├─ YES → 家族 A（s_timeline）
  │        ├─ 左右交錯 → alternate 模式
  │        ├─ 全部左側 → left 模式
  │        └─ 全部右側 → right 模式
  └─ NO
      ├─ 每列有大圖（佔 50% 寬）？
      │   └─ YES → 家族 C（s_text_image）
      └─ 每列是文字+小圖、或只有文字？
          └─ YES → 家族 B（s_vertical_layout 列表）
                   ├─ 需要年份獨立欄 → timeLine04 3欄
                   ├─ 需要卡片邊框/陰影 → timeLine02
                   ├─ 需要雙色 split bg → timeLine06
                   └─ 基本款 → timeLine01
```

---

## 行動裝置（RWD）行為總結

| 家族 | 機制 | Mobile 效果 |
|-----|-----|------------|
| A | `d-block d-md-flex flex-row` 在 `s_timeline_row` | date 上方，content 堆疊 |
| B | Bootstrap grid 自動 | 欄位由上到下堆疊 |
| C | Bootstrap grid 自動 | 文字上方（col-lg-6 先），圖片在下 |

> 家族 A 的左右交錯在手機上會全部變成垂直列表，左右語義消失。
> 若要手機也保留視覺差異，建議改用家族 B 搭配交替 bg（timeLine06）。

---

## 必填 / 禁止事項

- 每個 `s_timeline_row` 必須有 **兩個** `s_timeline_content`（即使一個是空的）
- 家族 A wrapper `<section>` 必須有 `data-snippet="s_timeline"`
- 家族 B/C wrapper `<section>` 必須有 `data-snippet="s_vertical_layout"`
- 圖片使用佔位圖：`https://picsum.photos/[width]/[height]`
- 不可使用 `/web/image/...` 格式（那是 Odoo 資源 ID，不能直接貼）
- 每個 section 必須有 `data-custom-name` 屬性，命名格式：`timeLine[NN]` 或 `timeLineBase`
