
import os
import shutil
import random
import string

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")
def rename_files_in_directory(directory, base_name): #directory: 파일 이름을 변경할 디렉토리 경로,base_name: 새로운 파일 이름의 기본 문자열
    
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))] #주어진 디렉토리 내의 파일 목록을 가져오고 파일목록을 순회하면서 파일 이름 변
        for i, filename in enumerate(files):
            old_path = os.path.join(directory, filename) #기존파일 경
            ext = os.path.splitext(filename)[1]  # 파일 확장자 추출
            new_filename = f"{base_name}_{i+1}{ext}"  # 새로운 파일 이름 생성
            new_path = os.path.join(directory, new_filename) #새로운 파일 경로
            os.rename(old_path, new_path) #파일 이름 변
            print(f"파일 이름이 변경되었습니다: {old_path} -> {new_path}")
    except Exception as e:
        print(f"파일 이름 변경 중 오류가 발생했습니다: {e}") #오류메시지 춢력
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
        
    elif func == "이름바꾸기":
        directory = input("파일 이름을 변경할 디렉토리 경로를 입력하세요: ")
        base_name = input("새로운 파일 이름의 기본 문자열을 입력하세요: ")
        rename_files_in_directory(directory, base_name)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
