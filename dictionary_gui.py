import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup

def get_definition():
    word = entry.get().strip().lower()
    if not word:
        messagebox.showwarning("提示", "請輸入單字！")
        return

    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        definition = soup.find('div', class_='def ddef_d db')
        example = soup.find('span', class_='eg deg')

        # 清除舊內容並顯示新內容
        result_area.config(state=tk.NORMAL)
        result_area.delete(1.0, tk.END)
        
        if definition:
            result_area.insert(tk.END, f"【Definition】\n{definition.get_text().strip()}\n\n")
            if example:
                result_area.insert(tk.END, f"【Example】\n{example.get_text().strip()}")
        else:
            result_area.insert(tk.END, "抱歉，找不到該單字的定義。")
        
        result_area.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("錯誤", f"發生問題：{e}")

# --- 建立視窗介面 ---
root = tk.Tk()
root.title("My English Dictionary Tool")
root.geometry("500x400")

# 輸入區域
tk.Label(root, text="輸入英文單字:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)
entry.bind('<Return>', lambda event: get_definition()) # 按 Enter 也能查詢

# 查詢按鈕
search_btn = tk.Button(root, text="查詢 (Search)", command=get_definition, bg="#4CAF50", fg="white", font=("Arial", 10))
search_btn.pack(pady=10)

# 結果顯示區域 (加上捲軸)
result_area = scrolledtext.ScrolledText(root, font=("Arial", 11), width=55, height=12, state=tk.DISABLED)
result_area.pack(pady=10, padx=10)

root.mainloop()