
"""
현재 경로에 특정 파일이나 디렉토리가 존재하는지를 확인하기 위해 import os를 사용
파일을 이동이나 복사하기 위해 shutil 모듈을 사용하였음
파일 탐색기에서의 잘라내기 기능을 구현함
cut_file 함수는 잘라낼 파일의 경로와 붙여넣을 경로를 매개변수로 함
이때 붙여넣을 경로에 입력이 잘못됐을 경우 에러를 발생시킴
b_is_exit 변수를 0으로 초기화하고
1을 입력하였을때 잘라내기 기능이 구현되도록 함수를 작성하였음
favorites : 즐겨찾기 목록
addFavorite() : 원하는 파일을 즐겨찾기에 추가하는 함수
showFavorites() : 즐겨찾기 안의 파일 목록을 순서대로 출력하는 함수
"""

import os
import shutil
import hashlib
import time
import function
import zipfile

def search_files(directory, extension=None, min_size=None, max_size=None):
    """
    지정된 디렉토리에서 조건에 맞는 파일들을 검색합니다.

    :param directory: 검색을 시작할 디렉토리의 경로
    :param extension: 검색할 파일의 확장자 (예: '.txt')
    :param min_size: 검색할 파일의 최소 크기 (바이트 단위)
    :param max_size: 검색할 파일의 최대 크기 (바이트 단위)
    :return: 조건에 맞는 파일 경로의 리스트
    """
    matched_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if extension and not filename.endswith(extension):
                continue
            filepath = os.path.join(dirpath, filename)
            file_size = os.path.getsize(filepath)
            if min_size and file_size < min_size:
                continue
            if max_size and file_size > max_size:
                continue
            matched_files.append(filepath)
    return matched_files

"""
주어진 file_paths 리스트의 파일들을 output_zip 파일로 압축.

zipfile.ZipFile을 사용하여 파일을 순회하며 압축 파일에 추가
"""
def compress_files(file_paths, output_zip):
    try:
        with zipfile.ZipFile(output_zip, 'w') as zipf:
            for file in file_paths:
                zipf.write(file, os.path.basename(file))
        print(f"파일들이 {output_zip}으로 압축되었습니다.")
    except Exception as e:
        print(f"파일 압축 중 오류가 발생했습니다: {e}")
"""
주어진 zip_path 파일을 extract_to 디렉토리로 압축 해제

zipfile.ZipFile을 사용하여 압축 파일을 열고, extractall 메서드를 통해 모든 파일을 지정된 디렉토리로 해제
"""
def decompress_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_to)
        print(f"{zip_path} 파일이 {extract_to}으로 압축 해제되었습니다.")
    except Exception as e:
        print(f"파일 압축 해제 중 오류가 발생했습니다: {e}")

# 파일 관리 시스템
# - 중복 파일 탐지 및 삭제: 주어진 디렉토리에서 중복 파일을 찾아내고, 중복된 파일을 삭제합니다.
# - 파일 이름 변경: 사용자가 지정한 파일의 이름을 변경합니다.
# - 파일 메타데이터 관리: 파일의 생성 시간, 수정 시간, 파일 크기를 출력합니다.

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

# 지정한 파일을 삭제하는 함수
def delete_file(path):
    """
    파일의 경로를 받아 해당 파일을 삭제
    
    Args:
        path (str): 삭제할 파일의 경로
    
    Returns:
        None
    """
    if os.path.exists(path):
        os.remove(path)
        print(f"{path} 파일이 삭제되었습니다.")
    else:
        print(f"{path} 파일이 존재하지 않습니다.")

def search_file(root_directory, target_filename):
    """
    특정 파일을 파일 시스템에서 검색하는 함수입니다.
    :param root_directory: 검색을 시작할 루트 디렉토리
    :param target_filename: 검색할 파일의 이름
    :return: 파일의 경로 리스트 (파일이 여러 개일 경우)
    """
    matched_files = []

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename == target_filename:
                matched_files.append(os.path.join(dirpath, filename))

    return matched_files

"""
    입력한 경로의 디렉토리 내 파일 크기를 KB, MB처럼 사람이 읽기쉽게 변환하여 보여주는 함수
    매개변수 size_in_bytes: 바이트 단위의 파일 크기
    리턴값 str: 사람이 읽기 쉬운 형식으로 변환된 파일 크기
"""
def get_human_readable_size(size_in_bytes):

    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

"""
    주어진 디렉토리의 파일 크기를 사람이 읽기 쉬운 형식으로 출력
    매개변수 directory: 디렉토리 경로
    파일 사이즈 출력
"""
def display_file_sizes(directory):
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                size_in_bytes = os.path.getsize(file_path)
                human_readable_size = get_human_readable_size(size_in_bytes)
                print(f"{filename}: {human_readable_size}")
    except Exception as e:
        print(f"Error: {e}")

"""
Moves a file from the source path to the destination path.
@Param
    source : The source file path.
    destination : The destination file path.
@Return
    None
@Raises
    Prints an error message if the operation fails.
"""
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved file from {source} to {destination}")
    except Exception as e:
        print(f"Error moving file: {e}")

"""
Creates a directory at the specified path.
@Param
    directory_path : The path where the new directory should be created.
@Return
    None
@Raises
    Prints an error message if the operation fails.
"""
def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Created directory {directory_path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

"""
Lists all files in the specified directory.
@Param
    directory : The directory path to list files from.
@Return
    A list of filenames in the directory.
@Raises
    Prints an error message if the operation fails and returns an empty list.
"""
def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in {directory}: {files}")
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

"""
Gets the parent directory of the specified path.
@Param
    path : The file or directory path.
@Return
    The parent directory path.
"""
def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

def cut_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"{source} 파일이 {destination}으로 잘라내기 되었습니다.")
    except Exception as e:
        print(f"파일을 이동하는 중 오류가 발생했습니다: {e}")

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def create_and_write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

favorites = []
def addFavorite():
    path = input("즐겨찾기에 추가할 파일 경로를 입력하세요: ")
    favorites.append(path)
    print("즐겨찾기에 추가되었습니다.")

def showFavorites():
    if not favorites:
        print("현재 즐겨찾기 목록이 비어있습니다.")
    else:
        print("즐겨찾기 목록:")
        for i, favorite in enumerate(favorites, 1):
            print(f"{i}. {favorite}")


b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        source = input("잘라낼 파일의 경로를 입력하세요: ")
        destination = input("붙여넣을 경로를 입력하세요: ")
        cut_file(source, destination)
        print("잘라내기 완료")

    elif func == "2":
        print("기능 2 실행.")
        # Add functionality for option 2 here

    elif func == "3":
        print("기능 3 실행.")
        # Add functionality for option 3 here

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1을 입력하여 잘라내기(이동)하거나 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
