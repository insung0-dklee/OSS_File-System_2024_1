
import os
import shutil

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

# 현재 디렉토리의 파일 및 폴더 목록을 출력하는 함수, 예외 발생시 에러 메세지 출력
def listFilesFolders(path="."):
    try:
        files_folders = os.listdir(path)  
        print(f"{path} 디렉토리의 파일/폴더 목록:")
        for item in files_folders: 
            print(item)
    except Exception as e:  
        print(f"목록을 가져오는 중 오류가 발생했습니다: {e}")

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

# 도움말 리스트 함수 추가 및 간략화
    elif func == "?":
        print("도움말: 1, 2, 3 - 각각의 기능 선택, '복사' - 파일 복사, '리스트' - 파일 및 폴더 목록 출력, '종료' - 프로그램 종료")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")