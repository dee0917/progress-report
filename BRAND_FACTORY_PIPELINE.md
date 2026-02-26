# 🏭 自動化建站工廠：標準化生成流程 (Site Factory Pipeline)

本文件定義了從 `progress-report` 單一資料庫，自動衍生出無數個**完整、獨立、可直接上線（如 `C:\Users\Dee\MyApp\A`）的實體電商網站**的標準化流程。

生成出來的網站並非只是空殼預覽，而是**具備所有電商該有功能的完整專案**（包含商品頁、購物車、多步驟結帳、狀態保留與響應式佈局）。

---

## 🏗️ 核心架構：The Base Template (基底模板)

自動化建站的第一準則：**「不要每次從頭寫程式碼」**。
在執行建站工廠前，系統必須維持一個高度模組化且乾淨的基底模板（例如存在 `C:\Users\Dee\MyApp\BaseTemplate` 中）。

**基底模板必須已經內建以下完整功能：**
1. **基礎框架**：React + Vite + TypeScript + TailwindCSS
2. **核心頁面**：Home（首頁）、Catalog（商品列表）、Product Detail（商品詳情與畫廊）、Checkout（結帳與表單驗證）、Order Success（結帳成功頁）、AboutUs / ContactUs（靜態介紹）。
3. **電商邏輯**：基於 Context 的全域購物車（`CartContext`）、localStorage 持久化儲存、多幣種計算邏輯。
4. **設計系統槽（Slots）**：所有顏色、字體、圓角皆由 CSS 變數控制，等待 AI 注入參數。

---

## ⚙️ 自動化建站工廠 5 步驟標準流程

當系統開始執行「建站任務」時（例如產生代號為 `A` 的專案），將嚴格遵循以下流水線：

### Step 1: 抽選資料與特徵提取 (Data Extraction)

1. **讀取源頭**：從 `C:\Users\Dee\MyApp\work\projects\progress-report\extracted_products.json` 讀取商品資料庫。
2. **隨機/指定選定**：由系統隨機（或由您手動指定）抽選一個分類。例如抽出 `【傳統風水護身類】`。
3. **資料打包**：將該分類下的所有實體商品（名稱、價格、重量、1688 照片 URL 等）打包成一份輕量級的 JSON，準備帶入下一步。

### Step 2: AI 大腦塑形與文案生成 (AI Agent Generation)

啟動內部 AI Agent（如 Claude/Gemini 工作流），輸入 Step 1 的商品資料，要求 AI 輸出**專屬品牌設定檔 (Brand Config)**。

* **Agent: 品牌策略師**
  * 命名：【福運閣】（Fortune Pavilion）
  * Slogan：傳承經典，護佑安康。
  * 品牌故事：為首頁和 About Us 頁面生成專屬的背景故事與願景。
* **Agent: 視覺設計師**
  * 選定設計 Preset（例如：`minimal-luxury`）。
  * 決定配色：主色 `#D4AF37`（金色），輔助色 `#8B0000`（暗紅）。
  * 決定字體：襯線字體（Serif）以顯傳統高雅。

**[產出物]**：`theme.json` 與 `content.json`。

### Step 3: 磁碟上的實體克隆 (Physical Cloning)

這是將「代碼」變成「實體專案」的關鍵步驟：
1. **建立資料夾**：腳本在硬碟上建立全新目錄 `C:\Users\Dee\MyApp\A`（或依品牌名 `C:\Users\Dee\MyApp\FortunePavilion`）。
2. **複製架構**：將 `BaseTemplate` 裡的所有原始程式碼（包括 `src/`, `package.json`, `index.html` 等）**完整複製**進 `C:\Users\Dee\MyApp\A`。
3. 此刻，資料夾 `A` 已經是一個可以獨立跑 `npm install` 與 `npm run dev` 的 React 專案，但它還是一個缺乏靈魂的空殼。

### Step 4: 靈魂注入與配置覆寫 (Data & Theme Injection)

將 Step 1 和 Step 2 準備好的資料，精準覆寫進剛剛建立的 `C:\Users\Dee\MyApp\A` 中：

1. **注入商品**：將 Step 1 包好的該分類商品 JSON，單獨寫入 `A/src/data/raw_products.json` 中。（此專案未來只會賣風水護身物，不會包含露營或咖啡用品，做到真正的獨立分離）。
2. **注入品牌配置**：將 Step 2 AI 生成的 `theme.json` 與 `content.json` 寫入 `A` 專案中，覆蓋基底預設值。
3. **注入全域變數**：修改 `A` 專案的 `index.html` 的 Title，以及可能涉及 SEO 的 Meta 標籤。

### Step 5: 自動化依賴安裝與測試驗證 (Build & Verify)

腳本在背景針對 `C:\Users\Dee\MyApp\A` 執行終端機命令：

1. `npm install`：安裝所有前端依賴套件。
2. `npx tsc --noEmit`：進行 TypeScript 靜態檢查，確保注入的 JSON 與 TypeScript 介面完美吻合。
3. （可選）`npm run build`：確保此獨立網站可正常打包成生產環境 (Production Build)。
4. 測試通過後，回報建立成功。

---

## 🚀 成果：100% 獨立的【福運閣】網站誕生

經過這 5 個步驟，`C:\Users\Dee\MyApp\A` 已經不再是原型（Prototype），而是一個**馬上就能推上 Vercel 或 Netlify 上線賺錢的獨立電商網站**。

它擁有：
✅ 清晰的品牌定位與首頁文案（福運閣）
✅ 該分類專屬的商品列表與詳情圖片（護身符、轉運珠）
✅ 屬於該風格的 UI 視覺（金色/暗紅的黑底燙金風格）
✅ 完整的全域購物車面板
✅ 擁有驗證機制的 Checkout 流程與成功頁面

**未來的無限擴展：**
只要有了這套標準化流程，您只需在終端機輸入：
`npm run generate-site --count 10`
系統就能以極快的速度，從 `progress-report` 中抽出 10 個不同分類，在您的 `MyApp` 資料夾底下自動生成 `C:\Users\Dee\MyApp\Site1` 到 `Site10`，10 個完全不同領域、不同設計的完整品牌網站！
