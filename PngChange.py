import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def select_image():
    """選擇圖片檔案"""
    # 開啟檔案選擇對話框，支援常見圖片格式
    file_path = filedialog.askopenfilename(
        title="選擇圖片檔案",
        filetypes=[
            ("所有圖片檔案", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp"),
            ("JPG檔案", "*.jpg *.jpeg"),
            ("PNG檔案", "*.png"),
            ("BMP檔案", "*.bmp"),
            ("GIF檔案", "*.gif"),
            ("所有檔案", "*.*")
        ]
    )
    
    if file_path:
        # 將選擇的檔案路徑顯示在輸入框中
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def convert_to_png():
    """將選取的圖片轉換為PNG格式"""
    input_path = entry_path.get().strip()
    
    # 檢查是否選擇了檔案
    if not input_path:
        messagebox.showwarning("警告", "請先選擇要轉換的圖片檔案！")
        return
    
    # 檢查檔案是否存在
    if not os.path.exists(input_path):
        messagebox.showerror("錯誤", "選取的檔案不存在！")
        return
    
    try:
        # 開啟圖片
        with Image.open(input_path) as img:
            # 處理GIF等動畫圖片（只保留第一幀）
            if img.is_animated:
                img = img.convert('RGBA')
            
            # 選擇儲存位置和檔名
            file_name = os.path.splitext(os.path.basename(input_path))[0]
            save_path = filedialog.asksaveasfilename(
                title="儲存PNG檔案",
                defaultextension=".png",
                initialfile=file_name,
                filetypes=[("PNG檔案", "*.png")]
            )
            
            if save_path:
                # 儲存為PNG格式
                img.save(save_path, format='PNG')
                messagebox.showinfo("成功", f"圖片已成功轉換並儲存為：\n{save_path}")
                # 清空輸入框
                entry_path.delete(0, tk.END)
    
    except Exception as e:
        messagebox.showerror("轉換失敗", f"發生錯誤：{str(e)}")

# 建立主視窗
root = tk.Tk()
root.title("圖片轉PNG工具")
root.geometry("500x150")  # 設定視窗大小
root.resizable(False, False)  # 禁止調整視窗大小

# 設定字體（確保繁體中文顯示正常）
font_style = ("Microsoft JhengHei", 10)

# 建立介面元件
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# 檔案路徑輸入框
label_path = tk.Label(frame, text="選取的圖片：", font=font_style)
label_path.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_path = tk.Entry(frame, width=40, font=font_style)
entry_path.grid(row=0, column=1, padx=10, pady=5)

# 選擇檔案按鈕
btn_select = tk.Button(frame, text="選擇圖片", command=select_image, font=font_style, width=10)
btn_select.grid(row=0, column=2, padx=5, pady=5)

# 轉換按鈕
btn_convert = tk.Button(frame, text="轉換為PNG", command=convert_to_png, font=font_style, 
                        bg="#4CAF50", fg="white", width=20, height=2)
btn_convert.grid(row=1, column=1, pady=15)

# 啟動主迴圈
root.mainloop()