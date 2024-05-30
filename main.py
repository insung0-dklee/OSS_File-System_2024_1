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

if __name__ == "__main__":
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
