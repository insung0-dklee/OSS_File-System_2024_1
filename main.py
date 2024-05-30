import os
import hashlib
import time

# 파일 관리 시스템
# - 중복 파일 탐지 및 삭제: 주어진 디렉토리에서 중복 파일을 찾아내고, 중복된 파일을 삭제합니다.
# - 파일 이름 변경: 사용자가 지정한 파일의 이름을 변경합니다.
# - 파일 메타데이터 관리: 파일의 생성 시간, 수정 시간, 파일 크기를 출력합니다.

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

def manage_metadata(file_path):
    """
    주어진 파일의 메타데이터를 관리합니다.
    """
    # 파일 생성 및 수정 시간 가져오기
    created_time = os.path.getctime(file_path)
    modified_time = os.path.getmtime(file_path)
    
    # 생성 및 수정 시간을 사람이 읽기 쉬운 형식으로 변환
    created_time_readable = time.ctime(created_time)
    modified_time_readable = time.ctime(modified_time)
    
    # 파일 크기 가져오기
    file_size = os.path.getsize(file_path)
    
    # 파일 메타데이터 출력
    print(f"File: {file_path}")
    print(f"Created Time: {created_time_readable}")
    print(f"Modified Time: {modified_time_readable}")
    print(f"Size: {file_size} bytes")

if __name__ == "__main__":
    while True:
        print("--------------------------------")
        print("기능 선택")
        print("--------------------------------")
        print("1. 파일이름 변경")
        print("2. 중복 파일 탐지 및 삭제")
        print("3. 파일 메타데이터 관리")
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
        elif select == '3':
            file_path = input("메타데이터를 확인할 파일의 경로를 입력하세요: ")
            manage_metadata(file_path)
        elif select == '0':
            print("종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
