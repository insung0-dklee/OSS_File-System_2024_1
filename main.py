import os
import hashlib

def getParentDir(path):
    return os.path.dirname(path)

def find_duplicates(directory):
    """
    주어진 디렉토리에서 중복 파일을 찾아내고 중복된 파일의 경로를 반환합니다.
    """
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

def remove_duplicates(duplicates):
    """
    중복된 파일을 삭제합니다.
    """
    for _, duplicate_paths in duplicates.items():
        for path in duplicate_paths[1:]:
            # 중복된 파일 삭제
            os.remove(path)
            print(f"Deleted: {path}")

def renameFile():
    """
    파일 이름 변경 함수
    """
    try:
        srcPath = input("이름을 변경할 파일의 경로 입력: ")
        newName = input("새로운 파일이름 입력: ")
        parentDir = getParentDir(srcPath)
        newPath = os.path.join(parentDir, newName)
        os.rename(srcPath, newPath)
        print("기존경로: ", srcPath, " 바뀐경로: ", newPath, " 변경완료!")
    except Exception as e:
        print("파일이름 변경 중 에러발생", e)

if __name__ == "__main__":
    while True:
        print("--------------------------------")
        print("기능 선택")
        print("--------------------------------")
        print("1. 파일이름 변경")
        print("2. 중복 파일 탐지 및 삭제")
        print("0. 종료")

        select = input("입력 (0번 입력시, 종료): ")
        print("\n")

        if select == '1':
            renameFile()
        elif select == '2':
            directory_to_check = input("중복 파일을 찾을 디렉토리 경로를 입력하세요: ")
            duplicate_files = find_duplicates(directory_to_check)
            if duplicate_files:
                print("중복된 파일이 발견되었습니다:")
                for hash_value, files in duplicate_files.items():
                    print(f"해시 값 {hash_value}:")
                    for file in files:
                        print(f"\t{file}")
                remove_duplicates(duplicate_files)
                print("중복 파일이 성공적으로 삭제되었습니다.")
            else:
                print("중복된 파일이 없습니다.")
        elif select == '0':
            print("종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")

