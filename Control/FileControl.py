'''
파일 자체를 컨트롤 하는 기능들의 패키지 입니다.
'''

import os
import shutil
import time
from typing import List
import hashlib
from functools import lru_cache
from pathlib import Path

def file_control():
    finish = False

    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print("도움말")
            print(" '메타데이터 출력'    입력시 해당 파일 메타 데이터 확인")
            print(" '파일삭제'           입력시 해당 파일 삭제")
            print(" '파일검색'           입력시 원하는 파일의 위치 검색")
            print(" '파일이동'           입력시 파일을 원하는 디렉토리로 이동")
            print(" '디렉토리 생성'      입력시 원하는 경로에 디렉토리 생성")
            print(" '파일목록'           입력시 해당 디렉토리의 파일의 목록 출력")
            print(" '부모 디렉토리 확인' 입력시 선택한 디렉토리의 부모 디렉토리 출력")
            print(" '파일복사'           입력시 파일 복사 및 붙여넣기")
            print(" '잘라내기'           입력시 파일 잘라내기 및 붙여넣기")
            print(" '종료'               입력시 프로그램을 종료할 수 있습니다.")
        elif select == '메타데이터 출력':
            manage_metadata(input("속성을 출력할 경로를 입력하세요 : "))
        
        elif select == '파일삭제':
            delete_file(input("삭제할 파일의 경로를 입력하세요 : "))
        
        elif select == '파일검색':
            search_file(input("파일을 검색할 디렉토리 경로를 입력하세요 : "), input("파일의 이름을 입력하세요 : "))

        elif select == '파일이동':
            file = input("이동할 파일의 이름을 입력하세요 : ")
            path = input("파일을 이동할 디렉토리 경로를 입력하세요 : ")
            move_file(file, path)
        
        elif select == '디렉토리 생성':
            create_directory(input("폴더를 생성할 디렉토리 경로를 입력하세요 : "))

        elif select == '파일목록':
            list_files(input("파일 목록을 출력할 디렉토리 경로를 입력하세요 : "))

        elif select == '부모 디렉토리 확인':
            getParentDir(input("부모 디렉토리를 확인할 디렉토리의 경로를 입력하세요 : "))

        elif select == '파일복사':
            copy_file(input("복사할 파일의 경로를 입력하세요 : "), input("파일을 붙여넣을 디렉토리를 입력하세요 : "))

        elif select == '잘라내기':
            cut_file(input("잘라낼 파일의 경로를 입력하세요 : "), input("파일을 붙여넣을 디렉토리를 입력하세요 : "))

        elif select == "종료":
            print("중복 관리를 종료합니다.")
            finish = True

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요. : ")

@lru_cache(maxsize=128)
def read_file(file_path):
    """
    기존 read_file 함수는 존재하지 않은 file path일 경우에 대해 버그 야기
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise Exception("존재하지 않은 파일입니다.")
    except PermissionError:
        raise Exception("파일 권한이 없습니다.")
    except IsADirectoryError:
        raise Exception("파일이 아닌 디렉토리 입니다.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

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

def search_content_in_file(file_path, content):
    """
    file path와 검색할 문자열을 입력받아 해당 파일에
    검색 문자열이 존재하면 해당 라인과 줄 수를 반환하고 없으면
    empty stirng을 반환하는 메소드
    :param file_path: 내용을 찾을 파일
    :param cotent: 찾고 싶은 내용
    :return: 1. 파일 경로 o, 내용 o -> 줄 번호, 해당 줄
             2. 파일 경로 o, 내용 x -> empty string
             3. 파일 경로 x -> error 메세지
    """

    try:
        file = read_file(file_path)
        content_lines = file.split('\n')

        for i, line in enumerate(content_lines):
            if line.find(content) != -1:
                return f"{i + 1}: {line}"
        return ""
    except Exception as e:
        return e

def create_and_write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


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




# 지정한 파일을 삭제하는 함수
def delete_file(path):
    """
    파일의 경로를 받아 해당 파일을 삭제
    
    Args:
        path (str): 삭제할 파일의 경로
    
    Returns:
        None

    6/3 파일의 권한이 없거나 다른 이유로 오류가 발생하는 문제 해결
    """
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"{path} 파일이 삭제되었습니다.")
        else:
            print(f"{path} 파일이 존재하지 않습니다.")
    except PermissionError:
        print(f"{path}에 접근할 권한이 없습니다.")
    except Exception as e:
        return f"예상치 못한 오류가 발생했습니다: {str(e)}"


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


def copy_file(src_path, dest_path):
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"소스 파일이 존재하지 않습니다: {src_path}")

    if not os.path.exists(os.path.dirname(dest_path)):
        raise FileNotFoundError(f"대상 디렉토리가 존재하지 않습니다: {os.path.dirname(dest_path)}")

    try:
        shutil.copy(src_path, dest_path)
        print(f"파일이 복사되었습니다: {src_path} -> {dest_path}")
    except PermissionError:
        print(f"파일을 복사할 권한이 없습니다.")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {str(e)}")

# cut-file 함수 추가
def cut_file(src_path, dest_path):
    """
    파일을 잘라내어 다른 위치로 이동합니다.
    :param src_path: 잘라낼 파일의 경로
    :param dest_path: 붙여넣을 위치의 경로
    """
    try:
        if not os.path.exists(src_path):
            print("잘라낼 파일이 존재하지 않습니다.")
            return

        if not os.path.exists(dest_path):
            print("붙여넣을 경로가 잘못되었습니다.")
            return

        shutil.move(src_path, dest_path)
        print(f"파일이 {dest_path}로 이동되었습니다.")
    except Exception as e:
        print(f"파일 이동 중 오류가 발생했습니다: {e}")

def create_symLink(file_path,link_path):
    """
    파일 또는 폴더에 대한 심볼릭 링크(symbolic link)를 생성하는 함수
    @Param
        file_path: 심볼릭 링크의 대상이 되는 파일 또는 폴더의 절대경로
        link_path: 생성될 심볼릭 링크의 절대경로
        
    @Return
        None
        
    @Raises
        Exception : If an error occurs while creating the link, an exception is output.
    """

    target = Path(file_path)
    link = Path(link_path)

    # link 파일이 이미 경로에 존재할 경우 처리
    if link.exists():
        print(f"{link} is already exists.")
        return

    try:
        link.symlink_to(target, target.is_dir())
        print(f"{link} | SymLink is created.")
    except Exception as e:
        print(f"Error is occured during creating SymLink : {e}")

# 파일 분할
"""
지정한 파일을 지정된 크기로 분할.
@Param
    file_path : 분할할 원본 파일의 경로.
    setSize : 분할될 파일 한개의 크기 (바이트 단위).
        
@Return
    None
"""

def Partition_file(file_path, setSize):
    file_num = 0
    with open(file_path, 'rb') as infile:
        while True:
            size = infile.read(setSize)
            if not size:
                break
            with open(f"{file_path}_part{file_num}", 'wb') as chunk_file:
                chunk_file.write(size)
            file_num += 1
    print(f"File is partitioned to {file_num} parts.")

    # delete original file
    os.remove(file_path)


# 파일 병합
"""
분할된 파일들을 하나의 파일로 병합합니다.
@Param
    output_path : 병합된 파일을 저장할 위치
    input_paths : 병합할 분할된 파일들의 경로.
    
@Return
    None
"""

def Merge_files(output_path, input_paths):
    with open(output_path, 'wb') as outfile:
        for file_path in input_paths:
            with open(file_path, 'rb') as infile:
                outfile.write(infile.read())
    print("Files are Merged to =>", output_path)

    # delete partitioned files
    for file_path in input_paths:
        os.remove(file_path)
        print(f"Delete Complete {file_path}.")


"""
Using example
분할
Partition_file('test.txt', 2048)
병합
input_files = [f'test.txt_part{i}' for i in range(분할 파일개수)]
Merge_files('test.txt', input_files)
"""

def save_hash(file_path,hash_file_path):
    """
    파일의 해시 값을 계산하여 지정된 경로의 텍스트 파일에 저장합니다.
    @Param
        file_path: 해시 값을 계산할 파일의 경로
        hash_file_path: 해시 값을 저장할 텍스트 파일의 경로
    @Return
        없음
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(4096)
        while buf:
            hasher.update(buf)
            buf = f.read(4096)
    # 해시 값을 텍스트 파일에 저장
    with open(hash_file_path, 'w') as hash_file:
        hash_file.write(hasher.hexdigest())
    print("해시값이 저장되었습니다.")


def load_hash(hash_file_path):
    """
    지정된 텍스트 파일로부터 해시 값을 불러옵니다.
    @Param
        hash_file_path: 해시 값을 저장하고 있는 텍스트 파일의 경로
    @Return
        파일로부터 읽은 해시 값
    """
    with open(hash_file_path, 'r') as hash_file:
        return hash_file.read()



def calculate_hash(file_path):
    """
    파일의 해시 값을 계산하여 반환합니다.
    @Param
        file_path: 해시 값을 계산할 파일의 경로
    @Return
        계산된 해시 값
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(4096)
        while buf:
            hasher.update(buf)
            buf = f.read(4096)
    return hasher.hexdigest()

def check_integrity(hash_path, file_path):
    """
    경로상 파일의 저장된 원본 해시값과 현재 해시값을 비교해 무결성을 검사하는 함수
    
    @Param
        hash_path: 비교할 해시값이 저장된 텍스트 파일의 경로
        file_path: 무결성을 확인할 파일의 경로
        
    @Return
        없음
        
    @Raises
        FileNotFoundError : 파일 경로가 존재 하지 않을때 발생
        IOError : 파일 읽기에 실패시 발생
    """
    origin_hash = load_hash(hash_path)  # 해시 파일로부터 해시값을 불러옴
    current_hash = calculate_hash(file_path)  # 현재 파일의 해시값을 계산
    if current_hash == origin_hash:
        print(f"{file_path}의 무결성 : 정상")
    else:
        print(f"{file_path}의 무결성 : 손상\nCurrent Hash: {current_hash}\nOrigin Hash: {origin_hash}")

"""
Deletes a directory at the specified path.
@Param
    directory_path : The path where the directory should be deleted.
@Return
    None
@Raises
    Prints an error message if the operation fails.
"""
def delete_directory(directory_path):
    try:
        os.rmdir(directory_path)
        print(f"Directory {directory_path} deleted successfully")
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
    except OSError as e:
        print(f"Error deleting directory: {e}")