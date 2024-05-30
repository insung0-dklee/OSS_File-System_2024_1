import os

file_path = 'file_to_delete.txt'

# 파일 존재 여부 확인
if os.path.exists(file_path):
    # 파일이 존재할 경우 os.remove() 함수를 사용하여 파일 삭제
    os.remove(file_path)
    print(f"{file_path} 파일이 삭제되었습니다.")
else:
    print(f"{file_path} 파일이 존재하지 않습니다.")

def getParentDir(path):
    return os.path.dirname(path)

