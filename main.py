
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

b_is_exit = False

def list_files(directory, show_extensions=True):
    """
    디렉토리와 확장자 표시 여부를 입력 받은 후 해당 경로의 파일을 나열

    :매개변수 directory: 파일을 나열할 디렉토리
    :매개변수 show_extensions: True일 때 파일 확장자 표시
    """
    try:
        files = os.listdir(directory)
        for file in files:
            if not show_extensions:
                file = os.path.splitext(file)[0]
            print(file)
    except Exception as e:
        print(f"파일 목록을 가져오는 중 오류가 발생했습니다: {e}")

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

    elif func == "확장자 확인":
        directory = input("파일을 나열할 디렉토리 경로를 입력하세요: ")
        show_extensions = input("파일 확장자를 표시하시겠습니까? (y/n): ").lower() == 'y'
        list_files(directory, show_extensions)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '확장자 확인'을 입력하여 선택한 디렉토리에 있는 파일들의 확장자를 확인하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")