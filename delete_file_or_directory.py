# delete_file_or_directory.py

import os

def delete_file_or_directory(path):
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
                print(f"파일 '{path}'이(가) 삭제되었습니다.")
            elif os.path.isdir(path):
                os.rmdir(path)
                print(f"디렉토리 '{path}'가 삭제되었습니다.")
        else:
            print(f"'{path}' 경로가 존재하지 않습니다.")
    except Exception as e:
        print(f"파일 또는 디렉토리를 삭제하는 중 오류가 발생했습니다: {e}")