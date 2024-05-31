
import os
import shutil
import time

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

def clean_up_directory(directory, days_threshold):
    """
    지정된 디렉토리에서 지정된 기간 이상 사용되지 않은 파일 자동 삭제
    
        directory (str): 정리할 디렉토리 경로
        days_threshold (int): 삭제 기준 일수 (예: 30일)
    """
    # 현재 시간을 가져옴
    current_time = time.time()
    
    # 지정된 경로의 파일 목록을 가져옴
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 파일의 최종 수정 시간을 가져옴
            file_modified_time = os.path.getmtime(file_path)
            
            # 파일의 최종 수정 시간과 현재 시간의 차이를 일(day) 단위로 계산
            time_difference_days = (current_time - file_modified_time) / (60 * 60 * 24)
            
            # 지정된 기간 이상 미사용된 파일을 삭제
            if time_difference_days > days_threshold:
                os.remove(file_path)
                print(f"Deleted: {file_path}") 

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