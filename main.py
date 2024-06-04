import os
import ctypes
import tkinter as tk
from tkinter import ttk, filedialog
from pathlib import Path

def pin_to_taskbar(file_path):
    """
    파일을 작업 표시줄에 고정하는 함수
    """
    try:
        # 작업 표시줄에 파일 고정
        shell = ctypes.CreateObject("WScript.Shell")
        shortcut = shell.CreateShortcut(os.path.join(os.path.expanduser("~"), "Desktop", os.path.basename(file_path) + ".lnk"))
        shortcut.TargetPath = file_path
        shortcut.Save()

        # 작업 표시줄에 아이콘 추가
        APPID = "MyApp"
        ctypes.windll.shell32.SetAppUserModelId(APPID)
        ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)

        return f"{os.path.basename(file_path)}이(가) 작업 표시줄에 고정되었습니다."
    except Exception as e:
        return f"오류 발생: {e}"

def select_and_pin_file():
    """
    바탕화면에 있는 파일을 선택하고 작업 표시줄에 고정하는 함수
    """
    desktop_path = str(Path.home() / "Desktop")
    file_path = filedialog.askopenfilename(initialdir=desktop_path)
    if file_path:
        result = pin_to_taskbar(file_path)
        text_box.insert(tk.END, result + "\n")

# GUI 생성
root = tk.Tk()
root.title("파일 작업 표시줄 고정")

button = ttk.Button(root, text="작업 표시줄에 고정", command=select_and_pin_file)
button.pack(pady=10)

text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

root.mainloop()