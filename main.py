import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# 주어진 경로의 부모 디렉토리를 반환하는 함수
def getParentDir(path):
    return os.path.dirname(path)

# 파일을 복사하는 함수
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        messagebox.showinfo("성공", f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        messagebox.showerror("오류", f"파일 복사 중 오류가 발생했습니다: {e}")

# 파일을 이동하는 함수
def moveFile(src, dest):
    try:
        shutil.move(src, dest)
        messagebox.showinfo("성공", f"파일이 성공적으로 이동되었습니다: {dest}")
    except Exception as e:
        messagebox.showerror("오류", f"파일 이동 중 오류가 발생했습니다: {e}")

# 파일 이름을 변경하는 함수
def renameFile(src, new_name):
    try:
        parent_dir = getParentDir(src)
        new_path = os.path.join(parent_dir, new_name)
        os.rename(src, new_path)
        messagebox.showinfo("성공", f"파일이 성공적으로 이름이 변경되었습니다: {new_path}")
    except Exception as e:
        messagebox.showerror("오류", f"파일 이름 변경 중 오류가 발생했습니다: {e}")

# 파일을 삭제하는 함수
def deleteFile(path):
    try:
        os.remove(path)
        messagebox.showinfo("성공", f"파일이 성공적으로 삭제되었습니다: {path}")
    except Exception as e:
        messagebox.showerror("오류", f"파일 삭제 중 오류가 발생했습니다: {e}")

# 파일 선택 다이얼로그를 여는 함수
def selectFile():
    return filedialog.askopenfilename()

# 폴더 선택 다이얼로그를 여는 함수
def selectFolder():
    return filedialog.askdirectory()

# 파일 이동 GUI 기능
def moveFileGUI():
    src = selectFile()
    if not src:
        return
    dest = selectFolder()
    if not dest:
        return
    moveFile(src, dest)

# 파일 이름 변경 GUI 기능
def renameFileGUI():
    src = selectFile()
    if not src:
        return
    new_name = simpledialog.askstring("새 파일 이름", "새 파일 이름을 입력하세요:")
    if not new_name:
        return
    renameFile(src, new_name)

# 파일 삭제 GUI 기능
def deleteFileGUI():
    path = selectFile()
    if not path:
        return
    deleteFile(path)

# 파일 복사 GUI 기능
def copyFileGUI():
    src = selectFile()
    if not src:
        return
    dest = selectFolder()
    if not dest:
        return
    copyFile(src, dest)

# 메인 윈도우 생성
root = tk.Tk()
root.title("파일 관리 GUI")

# 각 기능에 대한 버튼 추가
btn_move = tk.Button(root, text="파일 이동", command=moveFileGUI)
btn_move.pack(pady=5)

btn_rename = tk.Button(root, text="파일 이름 바꾸기", command=renameFileGUI)
btn_rename.pack(pady=5)

btn_delete = tk.Button(root, text="파일 삭제", command=deleteFileGUI)
btn_delete.pack(pady=5)

btn_copy = tk.Button(root, text="파일 복사", command=copyFileGUI)
btn_copy.pack(pady=5)

btn_exit = tk.Button(root, text="종료", command=root.destroy)
btn_exit.pack(pady=5)

# 메인 루프 실행
root.mainloop()
