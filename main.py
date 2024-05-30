
import os
import shutil

def getParentDir(path):
    return os.path.dirname(path)

"""

    주어진 경로에 폴더를 생성합니다. 상위 디렉토리가 없으면 생성합니다.

    @param path 생성할 폴더의 경로
    @return None
    @exception FileNotFoundError 상위 디렉토리가 존재하지 않을 때 발생합니다. 이 경우 상위 디렉토리를 생성하려 시도합니다.
    @exception PermissionError 폴더를 생성할 권한이 없을 때 발생합니다.
    @exception FileExistsError 폴더가 이미 존재할 때 발생합니다.
    @exception Exception 기타 모든 예외 상황에 대해 발생합니다.

"""
def MakeDir(path):
    try:
        os.mkdir(path)
        print(f"폴더 '{path}'가 성공적으로 생성되었습니다.")
    except FileNotFoundError:
	try:
            os.makedirs(path)
            print(f"상위 디렉토리와 폴더 '{path}'가 성공적으로 생성되었습니다.")
        except PermissionError:
            print(f"폴더 '{path}'를 생성할 권한이 없습니다.")
        except Exception as e:
            print(f"폴더를 생성하는 동안 오류가 발생했습니다: {e}")    
    except PermissionError:
        print(f"폴더 '{path}'를 생성할 권한이 없습니다.")
    except FileExistsError:
        print(f"폴더 '{path}'가 이미 존재합니다.")
    except Exception as e:
        print(f"폴더를 생성하는 동안 오류가 발생했습니다: {e}")

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

    elif func == "폴더생성":
        print("폴더 생성.")
        path = input("폴더를 생성할 경로를 입력하세요: ")
        MakeDir(path)

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