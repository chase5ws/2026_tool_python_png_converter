import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# ===================== 仅保留窗口尺寸可配置 =====================
WINDOW_WIDTH = 600   # 窗口宽度（可随意调整）
WINDOW_HEIGHT = 300  # 窗口高度（可随意调整）

# ===================== 功能函数 =====================
def select_image():
    """選擇圖片檔案"""
    # 開啟檔案選擇對話框，支援常見圖片格式
    file_path = filedialog.askopenfilename(
        title="選擇圖片檔案",
        filetypes=[
            ("所有圖片檔案", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp *.ico"),
            ("JPG檔案", "*.jpg *.jpeg"),
            ("PNG檔案", "*.png"),
            ("BMP檔案", "*.bmp"),
            ("GIF檔案", "*.gif"),
            ("ICO檔案", "*.ico"),
            ("所有檔案", "*.*")
        ]
    )
    
    if file_path:
        # 將選擇的檔案路徑顯示在輸入框中
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def convert_image():
    """將選取的圖片轉換為指定格式"""
    input_path = entry_path.get().strip()
    # 獲取選擇的目標格式（從单选按钮的变量中获取）
    try:
        target_format = format_var.get().upper()
    except:
        messagebox.showwarning("警告", "請選擇要轉換的目標格式！")
        return
    
    # 檢查是否選擇了檔案
    if not input_path:
        messagebox.showwarning("警告", "請先選擇要轉換的圖片檔案！")
        return
    
    # 檢查檔案是否存在
    if not os.path.exists(input_path):
        messagebox.showerror("錯誤", "選取的檔案不存在！")
        return
    
    # 檢查是否選擇了目標格式
    if not target_format or target_format == "":
        messagebox.showwarning("警告", "請選擇要轉換的目標格式！")
        return
    
    try:
        # 開啟圖片
        with Image.open(input_path) as img:
            # 處理GIF等動畫圖片（只保留第一幀）
            if img.is_animated:
                img = img.convert('RGBA')
            
            # 根據目標格式做處理
            if target_format == "ICO":
                # ICO格式需要指定尺寸，這裡使用常用的64x64
                img = img.resize((64, 64), Image.Resampling.LANCZOS)
                # 轉換為RGBA確保透明度支援
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
            elif target_format == "JPG" or target_format == "JPEG":
                # JPG不支援透明通道，需要轉換為RGB並填充白色背景
                if img.mode in ('RGBA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[3])
                    else:
                        background.paste(img)
                    img = background
            
            # 準備保存參數
            file_name = os.path.splitext(os.path.basename(input_path))[0]
            ext = f".{target_format.lower()}"
            
            # 選擇儲存位置和檔名
            save_path = filedialog.asksaveasfilename(
                title=f"儲存{target_format}檔案",
                defaultextension=ext,
                initialfile=file_name,
                filetypes=[(f"{target_format}檔案", f"*{ext}")],
                initialdir=os.path.dirname(input_path)
            )
            
            if save_path:
                # 根據格式設定保存參數
                save_kwargs = {}
                if target_format in ["JPG", "JPEG"]:
                    # JPG品質設定（0-100）
                    save_kwargs['quality'] = 95
                    save_kwargs['format'] = 'JPEG'
                else:
                    save_kwargs['format'] = target_format
                
                # 儲存圖片
                img.save(save_path, **save_kwargs)
                messagebox.showinfo("成功", f"圖片已成功轉換並儲存為：\n{save_path}")
                # 清空輸入框
                entry_path.delete(0, tk.END)
    
    except Exception as e:
        messagebox.showerror("轉換失敗", f"發生錯誤：{str(e)}")

# ===================== 界面创建 =====================
# 建立主視窗
root = tk.Tk()
root.title("多功能圖片格式轉換工具")

# 設置窗口尺寸（使用可配置参数）
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  
root.resizable(False, False)  

# 設置視窗ICON
try:
    root.iconbitmap("my_icon.ico")
except Exception as e:
    # 如果ICON加載失敗，給出提示但不影響程式運行
    print(f"提示：無法加載自定義圖標 - {e}")

# 設定字體
font_style = ("Microsoft JhengHei", 10)

# 建立介面元件
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# 檔案路徑輸入框區域
label_path = tk.Label(frame, text="選取的圖片：", font=font_style)
label_path.grid(row=0, column=0, sticky=tk.W, pady=15)

entry_path = tk.Entry(frame, width=35, font=font_style)
entry_path.grid(row=0, column=1, padx=10, pady=15)

btn_select = tk.Button(frame, text="選擇圖片", command=select_image, 
                       font=font_style, width=10)
btn_select.grid(row=0, column=2, padx=5, pady=15)

# ========== 核心修改：缩小单选按钮间距，紧凑排列 ==========
# 目標格式標籤
label_format = tk.Label(frame, text="目標格式：", font=font_style)
label_format.grid(row=1, column=0, sticky=tk.W, pady=15)

# 建立单选按钮的变量
format_var = tk.StringVar()
# 默认不选中任何选项
format_var.set("")

# 建立格式选项的单选按钮（紧凑横向排列）
formats = ["PNG", "JPG", "ICO", "BMP", "GIF"]
# 创建一个子框架来容纳所有单选按钮，避免列错位
radio_frame = tk.Frame(frame)
radio_frame.grid(row=1, column=1, columnspan=5, sticky=tk.W, padx=0, pady=15)

# 紧凑排列单选按钮，间距从8px改为2px
for idx, fmt in enumerate(formats):
    rb = tk.Radiobutton(radio_frame, text=fmt, variable=format_var, value=fmt, font=font_style)
    rb.grid(row=0, column=idx, padx=2, pady=0)  # 关键：padx改为2，大幅缩小间距

# 轉換按鈕（调整列跨度，适配紧凑布局）
btn_convert = tk.Button(frame, text="開始轉換", command=convert_image, font=font_style, 
                        bg="#4CAF50", fg="white", 
                        width=25, height=3)
btn_convert.grid(row=2, column=0, columnspan=6, pady=30)

# 啟動主迴圈
root.mainloop()