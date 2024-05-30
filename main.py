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

# 파일 속성 변경 함수 추가
def changeFilePermission(path, mode):
    try:
        os.chmod(path, mode)
        print(f"파일 권한이 성공적으로 변경되었습니다: {path}")
    except Exception as e:
        print(f"파일 권한 변경 중 오류가 발생했습니다: {e}")

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

    elif func == "속성 변경":
        path = input("속성을 변경할 파일의 경로를 입력하세요: ")
        print("예) 읽기 전용으로 변경: 0o444, 쓰기 가능으로 변경: 0o666")
        mode = int(input("변경할 권한 모드를 입력하세요 (예: 0o666): "), 8)  # 8진수로 입력받기
        changeFilePermission(path, mode)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사', '속성 변경'을 입력하여 파일을 복사하거나 속성을 변경하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
