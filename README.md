# ⚔️ NCA2-Tools — AION2 玩家便利工具集

<p align="center">
  <strong>專為《AION2 永恆紀元2》玩家打造的開源靜態網頁工具集合</strong><br>
  由社群玩家自主開發維護，致力於提供實用、好看、免安裝的遊戲輔助計算器。
</p>

> **線上使用：** [https://nca2.enoscloud.com](https://nca2.enoscloud.com)

---

## 📦 工具一覽

| 工具名稱 | 說明 | 連結 |
|---------|------|------|
| 🛡️ **裝備製作成本計算器** | 以「系列」為單位挑選多件裝備，自動合併所需材料並試算總基納成本 | [nca2-craft-tool](nca2-craft-tool/) |
| 💰 **幣值換算最佳化工具** | 精算台幣轉換基納的最大效益，支援官方寶石、兌換所寶箱與第三方幣商的四方案比較 | [nca2-coin-tool](nca2-coin-tool/) |

每個工具都是獨立的子目錄，內含各自的 `README.md` 說明文件，歡迎點進去查看詳細的功能介紹與開發指南。

---

## 🏗️ 專案架構
```text
nca2-tools/
├── index.html            # 首頁導覽入口
├── .nojekyll             # 禁用 GitHub Pages 的 Jekyll 編譯
│
├── nca2-craft-tool/      # 裝備製作成本計算器
│   ├── index.html        # [自動產物] 單頁式應用 (由 build_all.py 生成)
│   ├── css/style.css     # 原始樣式表
│   ├── js/items.js       # 道具辭典 (圖片、品階對應)
│   ├── js/recipes.js     # 配方資料庫 (材料需求)
│   ├── images/           # 道具圖片 (全英文檔名)
│   └── README.md         # 該工具的詳細說明
│
├── nca2-coin-tool/       # 幣值換算最佳化工具
│   ├── index.html        # 單頁式幣值計算器
│   └── README.md         # 該工具的詳細說明
│
├── build_all.py          # 裝備計算器的 Python 編譯腳本
├── app_series_cart.js    # 裝備計算器的購物車邏輯原始碼
└── rename.py             # 圖片中英文檔名轉換工具
```

---

## 🚀 部署方式

本專案為**純前端靜態網頁**，無需任何後端。

1. Fork 或 Clone 此倉庫。
2. 在 GitHub 設定中開啟 **GitHub Pages** (Source: `main` branch)。
3. 如需自訂網域，設定 CNAME 即可 (本專案已設定為 `nca2.enoscloud.com`)。

---

## 👨‍💻 作者

* **Enos.Lo**

## 📄 授權

本專案採用 [MIT License](LICENSE) 授權，歡迎自由 Fork、修改與分享。
