import os

def getParentDir(path):
    return os.path.dirname(path)

import os
import subprocess

def edit_desktop_file():
    # 바탕화면 경로 가져오기
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # 바탕화면의 파일 목록 가져오기
    files = os.listdir(desktop_path)
    
    # 파일 선택 받기
    print("바탕화면의 파일 목록:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    
    file_index = int(input("편집할 파일 번호를 입력하세요: "))
    selected_file = os.path.join(desktop_path, files[file_index-1])
    
    # 메모장으로 파일 열기
    subprocess.call(["notepad.exe", selected_file])
    
    print("파일 편집이 완료되었습니다.")

if __name__ == "__main__":
    edit_desktop_file()

