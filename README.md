# 多功能圖片格式轉換工具 (Multi-Format Image Converter)
![version](https://img.shields.io/badge/version-2.0.0-green)
![license](https://img.shields.io/badge/license-MIT-blue)
![python](https://img.shields.io/badge/Python-3.7%2B-orange)
![tkinter](https://img.shields.io/badge/tkinter-built--in-lightgrey)
![pillow](https://img.shields.io/badge/Pillow-9.0%2B-red)
![platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen)

一個基於 Python + Tkinter 開發的圖形介面工具，支援 PNG、JPG、ICO、BMP、GIF 等常見圖片格式之間的互相轉換，操作簡單直觀，無需命令列操作。

## 🌟 功能特點
- **多格式互轉**：支援輸入 JPG/JPEG、PNG、BMP、GIF、TIFF、WebP、ICO，輸出 PNG、JPG、ICO、BMP、GIF
- **直觀操作介面**：採用單選按鈕選擇目標格式，視窗尺寸可自定義調整
- **格式自適配處理**：
  - ICO 格式自動調整為 64x64 標準尺寸，支援透明度
  - JPG 格式自動處理透明通道（填充白色背景），可設定 95% 壓縮品質
  - GIF 動畫圖片自動保留第一幀進行轉換
- **繁體中文介面**：適配台灣/香港等地區使用習慣，支援微軟正黑體顯示
- **友好錯誤提示**：檔案不存在/未選擇檔案/未選擇格式時給出明確提示
- **自定義視窗圖標**：支援加載自定義 ICO 圖標（my_icon.ico）

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
### 1. 自定義配置（可選）
編輯程式頂部的參數，調整視窗尺寸：
```python
WINDOW_WIDTH = 600   # 自定義窗口宽度
WINDOW_HEIGHT = 300  # 自定義窗口高度
```
> 若需使用自定義視窗圖標，請將 `my_icon.ico` 放在程式同一目錄下

### 2. 執行程式
將程式程式碼儲存為 `image_converter.py`，透過以下命令執行：
```bash
python image_converter.py
```

### 3. 操作步驟
1. 點擊「選擇圖片」按鈕，在彈出的檔案選擇框中選取要轉換的圖片檔案；
2. 在「目標格式」區域點擊對應的單選按鈕，選擇要轉換的格式（PNG/JPG/ICO/BMP/GIF）；
3. 點擊「開始轉換」按鈕，在彈出的儲存對話框中選擇儲存位置（預設為原檔名 + 目標格式副檔名）；
4. 轉換成功後會彈出提示視窗，此時可在指定位置找到轉換後的圖片檔案。

## 📁 專案結構
```
.
├── image_converter.py  # 主程式檔案
├── my_icon.ico         # 自定義視窗圖標（可選）
└── README.md           # 使用說明文件
```

## ⚙️ 自定義擴展
### 1. 調整視窗尺寸
修改程式頂部的 `WINDOW_WIDTH` 和 `WINDOW_HEIGHT` 參數即可自定義視窗大小：
```python
WINDOW_WIDTH = 800   # 寬度改為800像素
WINDOW_HEIGHT = 400  # 高度改為400像素
```

### 2. 新增支援格式
若需新增轉換格式，只需修改 `formats` 列表並補充對應的格式處理邏輯：
```python
formats = ["PNG", "JPG", "ICO", "BMP", "GIF", "WEBP"]  # 新增WEBP格式
```

## ⚠️ 注意事項
1. GIF 動畫圖片轉換後僅保留第一幀，無法保留動畫效果；
2. ICO 格式轉換後固定為 64x64 尺寸，若需其他尺寸可修改程式中 `img.resize((64, 64))` 的數值；
3. JPG 格式不支援透明通道，轉換時會自動將透明區域替換為白色背景；
4. 確保選擇的輸入檔案路徑不含特殊字元（如全形符號、空格），避免轉換失敗；
5. 轉換大尺寸圖片時，程式可能短暫無回應，屬正常現象；
6. 若自定義圖標加載失敗，程式會在控制台輸出提示，但不影響核心功能使用。

## 🐞 常見問題
| 問題現象 | 可能原因 | 解決方案 |
|----------|----------|----------|
| 程式開啟後介面亂碼 | 系統缺少繁體中文字體 | 安裝「微軟正黑體 (Microsoft JhengHei)」 |
| 轉換 ICO 格式失敗 | 原圖片尺寸過小或格式異常 | 使用尺寸大於 64x64 的圖片進行轉換 |
| 轉換 JPG 後背景變黑 | 原圖片含透明通道未處理 | 程式已內建自動填充白色背景，確認使用最新版本 |
| 點擊按鈕無反應 | 缺少 Pillow 套件 | 重新執行 `pip install pillow` 安裝依賴 |
| 自定義圖標不顯示 | 圖標檔案不存在或路徑錯誤 | 確認 `my_icon.ico` 放在程式同一目錄，或修改 `iconbitmap()` 路徑 |

## 📄 免責聲明
> 本專案僅供教學與個人使用，開發者不承擔因使用本工具導致的任何數據丟失、檔案損壞等損失責任。

---

### 版本更新說明（v2.0.0）
1. 從單一 PNG 轉換升級為多格式互轉
2. 替換下拉框為單選按鈕，優化格式選擇體驗
3. 支援視窗尺寸自定義配置
4. 新增 ICO/JPG 格式專屬處理邏輯
5. 支援自定義視窗圖標加載