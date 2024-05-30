
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

def get_directory_storage(dir_path = "C:\\"):
    """
    dir_path 매개변수를 이용하여 해당하는 디렉토리의 사용량 확인
    dir_path에 디폴트 매개변수로 c드라이브를 설정하여
    아무 입력이 없을 시 c드라이브의 사용량을 확인하도록 함

    """
    directory = dir_path
    if shutil.disk_usage(directory):
        total_space, used_space, free_space= shutil.disk_usage(directory)
        """
        shutil.disk_usage 함수가 리턴값으로 total, used, free 세 가지의 정보를 가진 tuple을 리턴하므로
        리턴값을 받아주는 각각의 변수 선언

        """
        print(f"총 용량: {total_space / (1024**3):.2f}GB")
        print(f"사용 중: {used_space / (1024**3):.2f}GB")
        print(f"남은 공간: {free_space / (1024**3):.2f}GB")
        """
        위에서 받은 세 가지 값을 출력

        """
    else:
        print("디렉토리를 찾을 수 없습니다.")    
    """
    디렉토리를 찾지 못할 때 출력
    """



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

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")

