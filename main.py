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

def moveFile(src, dest):
    try:
        shutil.move(src, dest)
        print(f"파일이 성공적으로 이동되었습니다: {dest}")
    except Exception as e:
        print(f"파일 이동 중 오류가 발생했습니다: {e}")

def deleteFile(path):
    try:
        os.remove(path)
        print(f"파일이 성공적으로 삭제되었습니다: {path}")
    except Exception as e:
        print(f"파일 삭제 중 오류가 발생했습니다: {e}")

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

    elif func == "이동":
        src = input("이동할 파일의 경로를 입력하세요: ")
        dest = input("이동할 위치를 입력하세요: ")
        moveFile(src, dest)

    elif func == "삭제":
        path = input("삭제할 파일의 경로를 입력하세요: ")
        deleteFile(path)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사', '이동', '삭제'를 입력하여 파일을 관리하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
