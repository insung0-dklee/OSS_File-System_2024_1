# list_directory_contents.py

import os

def list_directory_contents(path="."):
    try:
        contents = os.listdir(path)
        print(f"'{path}' 디렉토리의 내용물:")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"'{path}' 디렉토리를 찾을 수 없습니다.")
    except Exception as e:
        print(f"디렉토리 내용물을 가져오는 중 오류가 발생했습니다: {e}")