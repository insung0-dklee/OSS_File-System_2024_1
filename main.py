import os

def getParentDir(path):
    return os.path.dirname(path)

import os
import winshell
import tkinter as tk
from tkinter import filedialog
import win32api
import win32con

def change_file_icon():
    """
    파일을 선택하고 아이콘 파일을 선택하면 
    해당 파일의 아이콘이 변경되는 함수
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if icon_path:
            try:
                # 파일 아이콘 변경
                win32api.SetFileAttributes(file_path, win32con.FILE_ATTRIBUTE_NORMAL)
                win32api.ExtractIcon(icon_path, file_path, 0)
                print(f"'{os.path.basename(file_path)}' 파일의 아이콘이 변경되었습니다.")
            except Exception as e:
                print(f"아이콘 변경에 실패했습니다: {e}")

# GUI 생성
root = tk.Tk()
root.title("파일 아이콘 변경")

# 버튼 생성 및 클릭 이벤트 연결
button = tk.Button(root, text="파일 아이콘 변경", command=change_file_icon)
button.pack(pady=20)

root.mainloop()

