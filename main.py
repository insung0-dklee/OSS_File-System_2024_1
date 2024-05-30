
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

def rename_file():
    files = os.listdir('.')
    print("현재 디렉토리의 파일 목록:")
    for idx, file in enumerate(files):
        print(f"{idx+1}. {file}")
    try:
        file_index = int(input("변경할 파일을 선택하세요 (번호 입력): ")) - 1
        if file_index < 0 or file_index >= len(files):
            print("올바르지 않은 파일 번호입니다.")
            return
        old_filename = files[file_index]
        new_filename = input("새로운 파일 이름을 입력하세요: ")
        if not new_filename:
            print("올바른 파일 이름을 입력하세요.")
            return
        if os.path.exists(new_filename):
            overwrite = input("동일한 이름의 파일이 이미 존재합니다. 덮어쓰시겠습니까? (y/n): ")
            if overwrite.lower() != 'y':
                print("파일 이름 변경이 취소되었습니다.")
                return
        os.rename(old_filename, new_filename)
        print(f"'{old_filename}' 파일이 '{new_filename}'로 변경되었습니다.")
    except ValueError:
        print("올바른 숫자를 입력하세요.")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

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

    elif func == "이름 변경":
        print("파일 이름 변경 기능 실행.")
        rename_file()

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '이름 변경'을 입력하여 파일 이름을 변경하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
