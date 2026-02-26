# 🏭 UI/UX Pro Max 自動化建站工廠：標準化生成流程

本文件定義了從 `progress-report` 單一資料庫，自動衍生出無數個**完整、高質感、絕不重複的實體電商網站（如 `C:\Users\Dee\MyApp\A`）**的標準化流程。

**核心目標**：生成的網站不能看起來像是廉價的模板站，必須達到 **UI/UX Pro Max** 級別。每一個產出的網站都要像 [Melanie Casey](https://www.melaniecasey.com/) 那樣：具備經營 5 年以上的品牌底蘊、極致的視覺美學、獨一無二的設計系統，以及無懈可擊的電商基礎建設。

---

## 💎 第一支柱：Pro Max 級 Base Template (基底模板)

自動化建站不能依賴簡陋的空殼。系統在複製專案前，依賴的 `BaseTemplate` 必須具備頂級電商的所有模組：

1. **頂級技術棧**：`React` (或 Next.js) + `TailwindCSS` + `shadcn/ui` + `Framer Motion` (流暢微動畫)。
2. **全功能專業佈局**：
   * **沉浸式首頁**：動態 Hero Banner、熱銷推薦、品牌理念區塊、質感圖文交錯排版。
   * **進階導覽 (Mega Menu)**：支援多層次分類展開、懸停特效。
   * **Pro 級網頁底圖 (Footer)**：依照頂級品牌標準配置（Logo/簡介、商品分類、顧客服務、聯絡資訊及社交媒體圖示）。
   * **信任信號 (Trust Signals)**：SSL 安全認證圖示、退換貨保證、真實質感的空殼評論評分系統。
3. **完整的後勤頁面**：不僅有首頁和商品頁，還內建 **隱私權政策、退換貨政策、服務條款、常見問題 (FAQ)、配送說明** 等經營 5 年以上老店必備的完整靜態頁面。
4. **設計變量槽 (Design Variables)**：抽離所有硬編碼的樣式，讓顏色、字體、圓角、間距全權交由動態注入。

---

## ⚙️ 自動化建站工廠 5 步驟標準流程

### Step 1: 抽選資料與深度特徵提取 (Data Sourcing)
1. 從 `progress-report/extracted_products.json` 讀取商品資料庫。
2. 隨機或指定抽選一個分類（例如：`【傳統風水護身類】`）。
3. 將該分類下所有實體商品（名稱、價格）打包，並轉換為視覺設計的參考依據。

### Step 2: AI 大腦深度品牌塑形 (AI Deep Branding - 不重複保證)
這是達成「獨一無二」的關鍵步驟。AI 接收分類資料後，不使用任何預設版型 (No Presets)，而是**無中生有生成一套完整的 Design System**：

* **品牌文案工程**：
  * 生成品牌名（【福運閣】）、Slogan、以及一段充滿底蘊的 5 年品牌故事。
  * 自動擴寫各項政策文案（配送說明、退換貨等），確保內容符合福運閣的語氣。
* **獨家色彩學 (Dynamic Color Palette)**：
  * AI 精準計算一套全新的 HSL 色票（主色、輔助色、背景色、強調色）。例如：主色黯金色 `#D4AF37` 配搭深木色 `#2C1E16`。
* **排版與字體 (Typography Pairing)**：
  * AI 負責從 Google Fonts 中挑選一對獨一無二的字體組合（如 `Noto Serif TC` 搭配 `Inter`），並計算字階 (Type Scale)。
* **微型互動風格**：
  * 決定按鈕是銳利直角（現代前衛）還是大圓角（親和自然），決定動畫是柔和淡入還是俐落滑動。

**[產出物]**：一份極度龐大且細緻的 `brand_config.json`（包含文案、Footer 結構、動態 Tailwind 變數）。

### Step 3: 磁碟上的實體克隆與隔離 (Physical Cloning)
1. 腳本在硬碟上建立全新目錄 `C:\Users\Dee\MyApp\A`（或依品牌名 `C:\Users\Dee\MyApp\FortunePavilion`）。
2. 將 `BaseTemplate` 裡的所有原始程式碼完整複製進 `A`。確保每一個網站都是實體的獨立專案。

### Step 4: 靈魂注入與全域覆寫 (Data & Theme Injection)
將 Step 2 的 AI 成果注入實體專案：
1. **覆寫 Tailwind 配置**：腳本自動修改 `A/tailwind.config.js` 與 `A/src/index.css`，將 AI 生成的專屬色環與字體寫入 CSS 變數。
2. **建構 Pro Footer 與導覽列**：將 AI 規劃的 Footer 連結（顧客服務、聯絡電話、營業時間）精準寫入元件配置檔，確保網站底部看起來專業且資訊豐富。
3. **注入商品資料庫**：將護身符商品寫入 `A/src/data/raw_products.json`。
4. **注入法律與服務頁面**：將 AI 自動生成的退換貨、隱私權政策內容，生成對應的 markdown 或 TSX 檔。

### Step 5: 自動化依賴安裝與生產環境測試 (Build & Verify)
1. 在 `A` 目錄下自動執行 `npm install`。
2. 下載 AI 選定的 Google Fonts 到本地以加速載入。
3. 執行 `npx tsc --noEmit` 及 `npm run build`。
4. 驗證無誤後，這就是一個可以直接部署上網的全新頂級品牌。

---

## 🎯 最終產出：超越樣板的工匠級網站

透過這套流程，每次在終端機執行 `npm run factory:generate` 時：
- 您**不會**得到換湯不換藥的樣板站。
- 您**會得到**一個擁有獨特色調、獨家高質感字體、擁有完整 Footer（含聯絡方式、政策條款）、並且運作流暢的現代化電商。
- 無論產生 10 個還是 100 個網站，每一個的視覺與使用者體驗（UI/UX）都將像 Melanie Casey 一樣，具備強烈的品牌識別度與無死角的專業感。
