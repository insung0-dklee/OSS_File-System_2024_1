'''
중복 파일 관리  패키지
'''
import os
import hashlib

def duplicates():

    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print(" '탐색' 입력을 통해 중복이 있는지 확인할 수 있습니다. ")
            print(" '중복 제거' 입력을 통해 중복되는 파일을 제거할 수 있습니다. ")

        elif select == "탐색":
            find_duplicates()

        elif select == "중복 제거":
            remove_duplicates()

        elif select == "나가기":
            print("중복 관리를 종료합니다.")
            finish = True

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")


def find_duplicates():
    """
    입력한 경로의 디렉토리에서 중복 파일을 찾아내고 중복된 파일의 경로를 반환합니다.
    """
    directory = input('탐색을 원하는 디렉토리의 경로를 입력하세요. : ')
    duplicates = {}
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            # 파일 경로 생성
            filepath = os.path.join(dirpath, filename)
            # 파일 내용의 해시 값 계산
            with open(filepath, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            # 해시 값을 이용하여 중복 파일 확인
            if file_hash in duplicates:
                duplicates[file_hash].append(filepath)
            else:
                duplicates[file_hash] = [filepath]
    # 중복된 파일만 반환
    return {hash: paths for hash, paths in duplicates.items() if len(paths) > 1}



def remove_duplicates():
    """
    입력한 경로의 디렉토이의 중복된 파일을 삭제합니다.
    """
    duplicates = input("중복 파일 삭제를 원하는 디렉토리의 경로를 입력하세요. : ")
    for _, duplicate_paths in duplicates.items():
        for path in duplicate_paths[1:]:
            # 중복된 파일 삭제
            os.remove(path)
            print(f"Deleted: {path}")