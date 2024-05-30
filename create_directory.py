
# create_directory.py

import os

def create_directory(path):
    try:
        os.mkdir(path)
        print(f"디렉토리 '{path}'가 생성되었습니다.")
    except FileExistsError:
        print(f"이미 존재하는 디렉토리입니다.")
    except Exception as e:
        print(f"디렉토리를 생성하는 중 오류가 발생했습니다: {e}")