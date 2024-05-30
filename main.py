import os

def getParentDir(path):
    return os.path.dirname(path)

def existDir(path): #파일 또는 디렉토리의 존재를 확인하는 함수
    return os.path.exists(path)