import os

def getParentDir(path):
    return os.path.dirname(path)

import os
import tkinter as tk
from tkinter import filedialog, ttk

class FileEditor:
    def __init__(self, master):
        self.master = master
        master.title("File Editor")

        # 파일 선택 버튼
        self.select_button = ttk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack(pady=10)

        # 텍스트 편집 영역
        self.text_area = tk.Text(master, width=80, height=20)
        self.text_area.pack(pady=10)

        # 저장 버튼
        self.save_button = ttk.Button(master, text="Save", command=self.save_file)
        self.save_button.pack(pady=10)

        self.file_path = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename(initialdir=os.path.expanduser("~\\Desktop"))
        if self.file_path:
            with open(self.file_path, 'r') as file:
                content = file.read()
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert('1.0', content)

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        self.file_path = filedialog.asksaveasfilename(initialdir=os.path.expanduser("~\\Desktop"))
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))

root = tk.Tk()
app = FileEditor(root)
root.mainloop()

