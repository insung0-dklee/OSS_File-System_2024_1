import os

def getParentDir(path):
    return os.path.dirname(path)


"""

@Param    
    origin : 원본 파일 경로
    target : 이동을 원하는 파일 경로

파일을 origin에서 target으로 이동시킴.

# 사용 예시
origin_path = '/path/to/source/file.txt'
target_path = '/path/to/destination/'
FileMove(origin_path, target_path)

"""
def FileMove(origin,target):

    try:
        shutil.move(origin, target)
        print(f"파일 이동 {origin} => {target}")
    except FileNotFoundError:
        print(f"파일을 찾을 수 없음 => {origin}")
    except Exception as e:
        print(f"파일 이동 오류 발생 => {e}")
