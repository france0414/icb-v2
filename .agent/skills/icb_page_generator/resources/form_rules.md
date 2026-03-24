# Odoo 14 表單 (Form) 佈局與樣式規範

在 Odoo 中，表單 (`s_website_form`) 是一個與後端系統 (例如 `mail.mail` 或 CRM) 深度綁定的動態元件。如果直接在模板中 hardcode `<form>` HTML，會失去 Odoo 的防偽造 (CSRF)、欄位驗證與自動路由功能。

預設策略是 **「佈局容器 (Layout) + 原生表單投放 (Dropzone)」** 的完全解耦。
但當使用者提供 **真實的 `s_website_form` 結構** (例如 `templates/form-contact.xml`) 時，AI 可以直接輸出完整表單結構，並維持原生欄位與屬性。

---

## 1. 核心開發策略：外殼與核心分離

### 1-1. 佈局外殼 (Layout Container)
在撰寫聯絡我們 (`Contact Us`) 或任何包含表單的區塊時，若**沒有**提供真實 `s_website_form` 結構，**XML 內不可包含 `<form>`**。我們只負責建立左右分欄、背景、聯絡資訊與提示文字，並留下一個名為 `.icb-form` (或其他自訂 class) 的空白區域，指示使用者將表單拖入。

**結構範例 (`contact.xml`)**：
```xml
<section class="s_text_block icb-contact-layout">
    <div class="container">
        <div class="row">
            <!-- 左側：聯絡資訊與文字 -->
            <div class="col-lg-6 icb-info">
                <h2>Contact Us</h2>
                <p>Welcome to our contact form!</p>
            </div>
            
            <!-- 右側：表單投放區 (Dropzone) -->
            <div class="col-lg-6 icb-form">
                <h3>Get in Touch</h3>
                <!-- 指示設計師/使用者將原生表單拖入此處 -->
                <div class="s_text"><p>請於此區拉入表單 (s_website_form)</p></div>
            </div>
        </div>
    </div>
</section>
```

### 1-2. 表單核心 (The Form)
使用者在 Odoo 網頁編輯器中，從左側區塊選單拖出原生的「Form (表單)」Snippet，並放進剛剛準備好的 `.icb-form` 區塊內。
- 這樣表單就能繼承 Odoo 預設的 `action="/website/form/"`、隱藏的預設欄位 (`email_to`) 等所有後端功能。

### 1-3. 真實表單結構 (可直接輸出)
若使用者已提供真實 `s_website_form` 結構，允許直接輸出完整 `<form>` HTML。必須維持原生欄位屬性與 class，並以提供的結構為準，不得自行改寫。

**來源：** `templates/form-contact.xml`

**結構範例 (精簡版，實際輸出請完整保留欄位)：**
```xml
<section class="s_website_form pt16 pb16" data-vcss="001" data-snippet="s_website_form" data-name="Form">
    <div class="container">
        <form action="/website/form/" method="post" enctype="multipart/form-data" class="o_mark_required" data-mark="*" data-pre-fill="true" data-privacy-checkbox="use" data-success-mode="redirect" data-success-page="/contactus-thank-you" data-model_name="mail.mail">
            <div class="s_website_form_rows row s_col_no_bgcolor">
                <div class="form-group s_website_form_field col-12 s_website_form_dnone" data-name="Field">
                    <div class="row s_col_no_resize s_col_no_bgcolor">
                        <label class="col-form-label col-sm-auto s_website_form_label" style="width: 200px">
                            <span class="s_website_form_label_content"/>
                        </label>
                        <div class="col-sm">
                            <input type="hidden" class="form-control s_website_form_input" name="email_to" value="info@yourcompany.example.com"/>
                        </div>
                    </div>
                </div>
                <div class="form-group s_website_form_field col-12 s_website_form_custom s_website_form_required" data-type="char" data-name="Field">
                    <div class="row s_col_no_resize s_col_no_bgcolor">
                        <label class="col-form-label col-sm-auto s_website_form_label" style="width: 200px" for="field_name">
                            <span class="s_website_form_label_content">Your Name</span>
                            <span class="s_website_form_mark"> *</span>
                        </label>
                        <div class="col-sm">
                            <input type="text" class="form-control s_website_form_input" name="name" required="1" data-fill-with="name" id="field_name"/>
                        </div>
                    </div>
                </div>
                <div class="form-group col-12 s_website_form_submit" data-name="Submit Button">
                    <div style="width: 200px;" class="s_website_form_label"/>
                    <a href="#" role="button" class="btn btn-primary btn-lg s_website_form_send o_default_snippet_text">Submit</a>
                    <span id="s_website_form_result"/>
                </div>
            </div>
        </form>
    </div>
</section>
```

---

## 2. 表單樣式 (SCSS) 覆寫規則

既然表單是動態拖入的，我們必須在對應佈局的 SCSS 中，針對該區塊底下的 `.s_website_form` 及其子元素進行樣式攔截與美化。

### 2-1. 輸入框 (Input / Textarea) 扁平化
Odoo 預設表單採用 Bootstrap 標準的帶邊框輸入框。高品質的版面通常會改用「僅有底線」或「圓角無邊框加陰影」的設計。

```scss
.icb-contact-layout { // 確保樣式只影響這個特定版面
    .s_website_form {
        // 隱藏不必要的間距
        .s_website_form_rows > .form-group {
            padding-top: 0; 
        }

        // 修改 Input 和 Textarea 外觀
        .form-control {
            border: 0;
            border-bottom: 1px solid #ddd; // 改為僅顯示底線
            height: auto;
            min-height: 40px;
            padding: 8px 10px;
            border-radius: 0; // 取除 Bootstrap 預設圓角
            background-color: transparent; // 融入背景
            box-shadow: none;
            
            &:focus {
                border-bottom-color: var(--o-cc3-text); // 點擊時的底線顏色變化
            }
        }
    }
}
```

### 2-2. 標籤 (Label) 控制
有時設計上不需要顯示欄位名稱 (Label)，或者希望將其移至上方。這其實可以透過 Odoo 編輯器的 UI 設定「隱藏 Label 並使用 Placeholder」，但 SCSS 仍需負責文字樣式：
```scss
.icb-contact-layout {
    .s_website_form {
        label.s_website_form_label {
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 5px;
            // 如果 Odoo 原生強制 label 與 input 同列 (橫向排列)，可透過 SCSS 強制垂直排列
            width: 100% !important;
            text-align: left;
        }
    }
}
```

### 2-3. 送出按鈕 (Submit Button) 美化
Odoo 表單最難看的就是預設的 Submit 按鈕，它會包含一個冗餘的 `div.s_website_form_label` 佔據空間。我們可以透過 Flex 排版將按鈕推向右方，並加入自訂的圖標動畫。

```scss
.icb-contact-layout {
    .s_website_form_submit {
        display: flex;
        justify-content: flex-end; // 將按鈕對齊右側
        align-items: center;

        // 隱藏不必要的佔位 label
        .s_website_form_label {
            display: none !important;
        }

        .s_website_form_send {
            display: flex;
            align-items: center;
            border-radius: 30px; // 將按鈕改為圓角藥丸狀
            
            // 可以搭配我們先前設定好的 btn-arrow 或其他動態效果
            &::after {
                content: "\f003"; // FontAwesome Mail Icon
                font-family: "fontawesome";
                font-size: 20px;
                width: 50px;
                height: 50px;
                border-radius: 50px;
                margin-left: 15px;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: var(--o-cc5-bg);
                color: #fff;
                transition: background-color 0.3s ease;
            }

            &:hover::after {
                background-color: var(--o-cc3-bg); // Hover 變色
            }
        }
    }
}
```

---

## 3. 總結流程
1. **若無真實結構**：建立 HTML Layout，留下 `.icb-form` 讓使用者拖入表單。
2. **若有真實結構**：直接輸出完整 `s_website_form` 結構，欄位與屬性保持原生。
3. **準備 SCSS**：在對應的 `.scss` 檔內寫好針對 `.s_website_form` 的所有覆寫樣式 (如 Input 扁平化、送出按鈕對齊)。
4. **前端操作**：在 Odoo 網頁編輯器中確認表單可正常送出與驗證。
