# HANDOVER.md — 進度報告專案交接文件

## 專案定位

此專案是公司的**核心商品採購資料庫**，包含所有商品的分類、名稱、重量、價格和供應商連結。  
它同時為 `site-generator-prototype`（自動建站系統）提供商品數據。

---

## 當前狀態

| 指標 | 數值 |
|---|---|
| 版本 | v2.7 |
| 商品分類數 | 20 |
| 商品總數 | 412 |
| 主檔案大小 | 618 KB（index.html） |
| 部署平台 | Vercel |
| 數據同步 | ✅ 已與 site-generator-prototype 建立自動同步 |

---

## 已完成功能

- [x] 商品資料庫（SOURCING_RAW）— 20 類 412 項
- [x] 儀表板 UI（TailwindCSS + 漸層設計）
- [x] 多幣種支持（人民幣/台幣/美元）
- [x] 分類篩選與搜尋功能
- [x] 響應式設計（含手機 PWA 優化）
- [x] Python 數據提取腳本（extract_data.py）
- [x] Vercel 部署（含 cache-control 配置）
- [x] 與 site-generator-prototype 自動同步機制

---

## 已知問題

### 🔴 高優先級

1. **單檔案過大** — `index.html` 達 618KB / 4668 行，修改效率低且容易衝突
2. **Service Worker 已停用** — 因快取問題被禁用（第 17-33 行），PWA 離線功能不可用

### 🟡 中優先級

3. **硬編碼路徑** — `extract_data.py` 和 `generate_report.py` 使用絕對路徑，換機器需手動修改
4. **無版本控制歷史** — 首次上傳 git，之前的變更紀錄已丟失

---

## 技術債

| 項目 | 說明 | 建議優先級 |
|---|---|---|
| 拆分 HTML | 將 CSS/JS/數據從 index.html 分離 | 高 |
| 相對路徑 | Python 腳本改用相對路徑或 CLI 參數 | 中 |
| 數據外移 | 將 SOURCING_RAW 移至獨立 JSON 檔案 | 中 |
| 測試覆蓋 | 目前無任何自動化測試 | 低 |
| SW 修復 | 修復 Service Worker 的快取策略 | 低 |

---

## 下一步建議

### 1. 短期（本週可做）
- 修復 Python 腳本的硬編碼路徑
- 新增 `.gitignore` 排除 `.vercel/` 和 `.env.local`

### 2. 中期（1-2 週）
- 將 `SOURCING_RAW` 數據外移至 `products.json`
- 建立 CI/CD：git push → Vercel 自動部署 → 觸發 site-generator 同步

### 3. 長期（1 個月+）
- 重構為模組化前端（React/Vue）
- 建立後端 API 管理商品數據
- 加入用戶權限管理
