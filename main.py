import os
import datetime

def getParentDir(path):
    return os.path.dirname(path)

# 파일 경로
file_path = r'./image/file_menu.png'

# 부모 디렉토리 가져오기
parent_dir = getParentDir(file_path)
print("부모 디렉토리:", parent_dir)

# 파일의 생성 시간 가져오기
ctime = os.path.getctime(file_path)
print("생성 시간 (원본):", ctime)

# 생성 시간을 datetime 객체로 변환
creation_datetime = datetime.datetime.fromtimestamp(ctime)
print("생성 시간 (datetime 객체):", creation_datetime)

# datetime 객체를 형식화
formatted_time = creation_datetime.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
print("생성 시간 (형식화):", formatted_time)
def getParentDir(path):
    return os.path.dirname(path)

