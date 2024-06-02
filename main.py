import os
import subprocess
from functools import lru_cache


def getParentDir(path):
    return os.path.dirname(path)

@lru_cache(maxsize=128)
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def defragment_file_system(path):
    """주어진 경로에 대해 파일 시스템 조각 모음을 수행합니다."""
    try:
        result = subprocess.run(["e4defrag", path], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"조각 모음 중 오류 발생: {e.stderr}")

def main():
    # 예제 파일 경로
    file_path = 'example.txt'
    
    # 파일이 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("This is a sample file for caching example.")
    
    # 파일 읽기 (캐시 사용)
    content = read_file(file_path)
    print(content)
    
    # 캐시된 데이터를 사용하여 다시 파일 읽기
    content = read_file(file_path)
    print(content)

    path = "/path/to/defragment"  # 조각 모음을 수행할 경로로 변경하세요
    defragment_file_system(path)


if __name__ == "__main__":
    main()


