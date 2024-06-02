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
    """주어진 경로에 대해 ext4 파일 시스템 조각 모음을 수행합니다."""
    if not os.path.exists(path):
        print(f"오류: 경로 '{path}'가 존재하지 않습니다.")
        return
    
    # 관리자 권한 확인 (리눅스 시스템에서만 가능)
    if os.geteuid() != 0:
        print("오류: 관리자 권한이 필요합니다. 'sudo'를 사용하여 스크립트를 실행하세요.")
        return
    
    try:
        # 파일 시스템 타입 확인
        result = subprocess.run(["df", "-T", path], capture_output=True, text=True)
        if 'ext4' not in result.stdout:
            print(f"오류: 경로 '{path}'는 ext4 파일 시스템이 아닙니다.")
            return
        
        # 조각 모음 실행
        result = subprocess.run(["e4defrag", path], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"조각 모음 중 오류 발생: {e.stderr}")
    except Exception as e:
        print(f"예상치 못한 오류 발생: {str(e)}")

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


