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

def renameFile(old_path, new_name):
    """
    이 함수는 주어진 파일의 이름을 새로운 이름으로 변경합니다.

    :param old_path: 기존 파일의 전체 경로
    :param new_name: 새 파일 이름
    :return: 새 파일의 전체 경로
    """
    parent_dir = getParentDir(old_path)
    new_path = os.path.join(parent_dir, new_name)
    
    try:
        os.rename(old_path, new_path)
        print(f"파일 이름이 {old_path}에서 {new_path}(으)로 변경되었습니다.")
        return new_path
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {old_path}")
    except PermissionError:
        print(f"파일 이름을 변경할 권한이 없습니다: {old_path}")
    except Exception as e:
        print(f"파일 이름 변경 중 오류가 발생했습니다: {e}")

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
        old_path = input("이름을 변경할 파일의 경로를 입력하세요: ")
        new_name = input("새 파일 이름을 입력하세요: ")
        renameFile(old_path, new_name)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사' 또는 '이름 변경'을 입력하여 파일을 관리하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
