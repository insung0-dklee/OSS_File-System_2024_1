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


"""
    입력한 경로의 디렉토리 내 파일 크기를 KB, MB처럼 사람이 읽기쉽게 변환하여 보여주는 함수
    매개변수 size_in_bytes: 바이트 단위의 파일 크기
    리턴값 str: 사람이 읽기 쉬운 형식으로 변환된 파일 크기
"""
def get_human_readable_size(size_in_bytes):
   
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

"""
    주어진 디렉토리의 파일 크기를 사람이 읽기 쉬운 형식으로 출력
    매개변수 directory: 디렉토리 경로
    파일 사이즈 출력
"""
def display_file_sizes(directory):
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                size_in_bytes = os.path.getsize(file_path)
                human_readable_size = get_human_readable_size(size_in_bytes)
                print(f"{filename}: {human_readable_size}")
    except Exception as e:
        print(f"Error: {e}")

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("기능 1 실행.")
        # Add functionality for option 1 here

    elif func == "2":
        print("기능 2 실행.")
        # Add functionality for option 2 here

    # 기능 3번에 디렉토리 내 파일 크기 확인 기능 추가
    elif func == "3": 
        print("디렉토리내 파일 크기확인 실행")
        directory_path = input("파일 크기를 확인할 디렉토리 경로를 입력하세요: ")
        display_file_sizes(directory_path)

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1, 2, 3(디렉토리 내 파일 사이즈 보기)을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
