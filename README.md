# 圖片轉PNG工具 (Image to PNG Converter)
![version](https://img.shields.io/badge/version-1.0.0-green)
![license](https://img.shields.io/badge/license-MIT-blue)
![python](https://img.shields.io/badge/Python-3.7%2B-orange)
![tkinter](https://img.shields.io/badge/tkinter-built--in-lightgrey)
![pillow](https://img.shields.io/badge/Pillow-9.0%2B-red)
![platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen)
![icon](icon.png)

一個基於 Python + Tkinter 開發的圖形介面工具，可將常見格式的圖片（JPG、BMP、GIF、WebP 等）快速轉換為 PNG 格式，操作簡單、無需命令列操作。

## 🌟 功能特點
- 支援多種輸入格式：JPG/JPEG、PNG、BMP、GIF、TIFF、WebP
- 圖形化操作介面（GUI），無需編程基礎即可使用
- 自動處理 GIF 動畫圖片（保留第一幀並轉換為 PNG）
- 繁體中文介面，適配台灣/香港等地區使用習慣
- 錯誤提示友好，檔案不存在/未選擇檔案時給出明確提示

## 📋 環境需求
### 1. 依賴套件
```bash
# 安裝必要套件
pip install pillow
```
> 備註：tkinter 通常隨 Python 預裝，若缺失可透過以下方式補裝：
> - Windows：重新安裝 Python 並勾選「Tcl/Tk and IDLE」
> - macOS：`brew install python-tk`
> - Linux (Ubuntu/Debian)：`sudo apt-get install python3-tk`

### 2. 系統相容性
- Windows 7/10/11
- macOS 10.14+
- Linux (Ubuntu 18.04+)
- Python 版本：3.7 及以上

## 🚀 使用方法
### 1. 執行程式
將程式程式碼儲存為 `image_to_png.py`，透過以下命令執行：
```bash
python image_to_png.py
```

### 2. 操作步驟
1. 點擊「選擇圖片」按鈕，在彈出的檔案選擇框中選取要轉換的圖片檔案；
2. 確認輸入框顯示正確的檔案路徑後，點擊「轉換為 PNG」按鈕；
3. 在彈出的儲存對話框中選擇儲存位置並確認檔名（預設為原檔名 + .png）；
4. 轉換成功後會彈出提示視窗，此時可在指定位置找到轉換後的 PNG 檔案。

## 📁 專案結構
```
.
├── image_to_png.py  # 主程式檔案
└── README.md        # 使用說明文件
```

## ⚠️ 注意事項
1. GIF 動畫圖片轉換後僅保留第一幀，無法保留動畫效果；
2. 轉換大尺寸圖片時，程式可能短暫無回應，屬正常現象；
3. 確保選擇的輸入檔案路徑不含特殊字元（如全形符號、空格），避免轉換失敗；
4. 若出現「檔案不存在」提示，請檢查原圖片檔案是否被移動/刪除。

## 🐞 常見問題
| 問題現象 | 可能原因 | 解決方案 |
|----------|----------|----------|
| 程式開啟後介面亂碼 | 系統缺少繁體中文字體 | 安裝「微軟正黑體 (Microsoft JhengHei)」 |
| 轉換 GIF 圖片失敗 | GIF 檔案損壞或格式異常 | 更換正常的 GIF 檔案，或先透過其他工具修復檔案 |
| 點擊按鈕無反應 | 缺少 Pillow 套件 | 重新執行 `pip install pillow` 安裝依賴 |

## 📄免責聲明

> 本專案僅供教學參考，開發者不承擔任何損失責任。

---

### 總結
1. 頂部新增了版本、授權、Python版本、依賴庫、支援平台等徽章，符合標準開源專案 README 規範；
2. 核心依賴僅需安裝 `Pillow`（tkinter 為 Python 內建），執行命令簡化且明確；
3. 操作流程為「選取圖片 → 點擊轉換 → 儲存PNG」，無需複雜設定，同時標註了 GIF 轉換的限制。
