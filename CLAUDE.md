# CLAUDE.md — 進度報告專案開發指南

## 專案概述

「進度報告」是一個**單頁 HTML 應用程式**，作為公司的商品採購資料庫與進度管理儀表板。  
此專案同時是 `site-generator-prototype` 的**唯一商品數據來源 (Single Source of Truth)**。

---

## 快速啟動

```bash
# 本地開發 — 直接用瀏覽器打開
start index.html

# 或使用任意靜態伺服器
npx serve .

# 提取商品數據（Python）
python extract_data.py

# 生成分析報告（Python）
python generate_report.py

# 同步商品到 site-generator-prototype
cd ../site-generator-prototype && npm run sync
```

---

## 技術棧

| 層級 | 技術 |
|---|---|
| 結構 | 單一 `index.html`（4668 行） |
| 樣式 | TailwindCSS CDN + 內聯 `<style>` |
| 字體 | Google Fonts: Noto Sans TC + Inter |
| 部署 | Vercel（靜態託管） |
| PWA | `manifest.json` + Service Worker（已停用） |
| 數據提取 | Python 3 (`extract_data.py`, `generate_report.py`) |

---

## 核心數據結構

### SOURCING_RAW 陣列

位於 `index.html` 約第 833 行，是所有商品的主數據：

```javascript
const SOURCING_RAW = [
  {
    "id": "## 1. 傳統風水護身類",
    "title": "## 1. 傳統風水護身類 (Traditional Feng Shui Talismans)",
    "items": [
      {
        "id": "1001",
        "name": "太歲金卡",
        "weight": "20g",
        "price": 5.0,
        "url": "https://s.1688.com/..."
      }
    ]
  }
];
```

### 欄位說明

| 欄位 | 類型 | 說明 |
|---|---|---|
| `id` | string | 分類 ID（含 markdown 標記） |
| `title` | string | 分類標題（中英文，英文在括號內） |
| `items[].id` | string | 商品唯一 ID |
| `items[].name` | string | 商品中文名稱 |
| `items[].weight` | string | 商品重量 |
| `items[].price` | number | 採購價格（人民幣） |
| `items[].url` | string | 1688 搜尋連結 |

---

## 編碼規範

- **語言**：HTML/CSS/JS 全在 `index.html` 內
- **新增商品**：直接編輯 `SOURCING_RAW` 陣列
- **新增分類**：在陣列中新增物件，`title` 必須包含英文括號名
- **禁止**刪除 `SOURCING_RAW` 的變數名——同步腳本依賴此名稱做正則提取
- **部署**：推送到 `main` 分支即自動觸發 Vercel 部署

---

## 與 site-generator-prototype 的連動

本專案的 `SOURCING_RAW` 數據通過同步腳本自動流向 `site-generator-prototype`：

```
index.html (SOURCING_RAW) → sync-products.ts → raw_products.json → 前端建站系統
```

修改商品數據後，需在 `site-generator-prototype` 目錄執行 `npm run sync` 或 `npm run dev`（自動觸發 predev hook）。
