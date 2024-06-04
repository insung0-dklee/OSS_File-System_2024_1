import os

# 실제 디렉토리 경로 입력
directory = "C:/Users/minja/Desktop" # 원하는 경로로 수정 필요

# 디렉토리 내의 파일 목록 가져오기
try:
    files = os.listdir(directory)
    # 파일 이름을 기준으로 정렬
    sorted_files = sorted(files)
    # 정렬된 파일 목록 출력
    for file in sorted_files:
        print(file)
except FileNotFoundError:
    print("지정된 경로를 찾을 수 없습니다.")