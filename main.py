
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("기능 1 실행.")
        # Add functionality for option 1 here

    elif func == "2":
        print("기능 2 실행.")
        # Add functionality for option 2 here

    elif func == "3":
        print("기능 3 실행.")
        # Add functionality for option 3 here

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
       
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Selected file: {file_path}")
        selected_file.set(file_path)

def compress_file():
    file_path = selected_file.get()
    if file_path:
        zip_path = file_path + ".zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        messagebox.showinfo("Success", f"File compressed to: {zip_path}")
    else:
        messagebox.showwarning("Warning", "No file selected")

root = tk.Tk()
root.title("파일 압축기")

selected_file = tk.StringVar()

select_button = tk.Button(root, text="파일 선택", command=select_file)
select_button.pack(pady=10)

file_label = tk.Label(root, text="파일을 선택하세요")
file_label.pack(pady=10)

compress_button = tk.Button(root, text="파일 압축", command=compress_file)
compress_button.pack(pady=10)

root.mainloop()