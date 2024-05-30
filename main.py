
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

def delete_old_files(directory, days_threshold=30):
    # 현재 시간 가져오기
    current_time = time.time()
    # 기준 시간 계산 (한 달 전의 시간)
    threshold_time = current_time - (days_threshold * 24 * 60 * 60)

    # 주어진 디렉토리 안의 모든 파일 확인
    for filename in os.listdir(directory):
        # 파일의 절대 경로 가져오기
        filepath = os.path.join(directory, filename)
        # 파일인 경우에만 처리
        if os.path.isfile(filepath):
            # 파일의 마지막으로 수정된 시간 가져오기
            last_modified_time = os.path.getmtime(filepath)
            # 만약 파일이 threshold_time 이전에 수정되었다면 삭제
            if last_modified_time < threshold_time:
                os.remove(filepath)

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("기능 1 실행.")
        directory_to_check = input("삭제할 파일이 있는 디렉토리 경로를 입력하세요: ")
        delete_old_files(directory_to_check)
        print("삭제 완료.")

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