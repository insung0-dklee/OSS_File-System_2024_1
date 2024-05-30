
import os
import shutil

def getParentDir(path):
    """
    주어진 경로의 부모 디렉토리를 반환합니다.
    """
    return os.path.dirname(path)

def copyFile(src, dest):
    """
    src 경로의 파일을 dest 경로로 복사합니다.
    """
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

def listFilesSortedByName(dir_path):
    """
    주어진 디렉토리의 파일 목록을 이름의 오름차순으로 정렬하여 반환합니다.
    """
    try:
        files = os.listdir(dir_path)
        files.sort()  # 이름의 오름차순으로 정렬
        return files
    except Exception as e:
        print(f"디렉토리 목록을 가져오는 중 오류가 발생했습니다: {e}")
        return []

def listFilesSortedBySize(dir_path):
    """
    주어진 디렉토리의 파일 목록을 파일 크기 순으로 정렬하여 반환합니다.
    """
    try:
        files = os.listdir(dir_path)
        files = [os.path.join(dir_path, f) for f in files if os.path.isfile(os.path.join(dir_path, f))]
        files.sort(key=os.path.getsize, reverse=True)  # 파일 크기로 정렬 (내림차순)
        return files
    except Exception as e:
        print(f"디렉토리 목록을 가져오는 중 오류가 발생했습니다: {e}")
        return []

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

    elif func == "4":
        print("기능 4 실행.")
        dir_path = input("파일 목록을 정렬할 디렉토리 경로를 입력하세요: ")
        if os.path.isdir(dir_path):
            files = listFilesSortedByName(dir_path)
            print(f"{dir_path}의 파일 목록 (이름의 오름차순):")
            for filename in files:
                print(filename)
        else:
            print("유효한 디렉토리 경로를 입력하세요.")

    elif func == "5":
        print("기능 5 실행.")
        dir_path = input("파일 목록을 정렬할 디렉토리 경로를 입력하세요: ")
        if os.path.isdir(dir_path):
            files = listFilesSortedBySize(dir_path)
            print(f"{dir_path}의 파일 목록 (크기 순, 내림차순):")
            for filename in files:
                print(f"{filename} ({os.path.getsize(filename)} bytes)")
        else:
            print("유효한 디렉토리 경로를 입력하세요.")

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '4'를 입력하여 파일 목록을 이름 순으로 정렬하거나 '5'를 입력하여 파일 목록을 크기 순으로 정렬하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
