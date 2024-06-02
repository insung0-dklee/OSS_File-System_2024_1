'''
파일 자체를 컨트롤 하는 기능들의 패키지 입니다.
'''

import os
import shutil
import time
import hashlib
from typing import List

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
            print(" '해시저장'           입력시 파일의 해시값을 지정경로의 txt파일에 저장")
            print(" '무결성 검사'        입력시 파일의 원본해시값과 현재해시값을 비교해 무결성 검사")
            print(" '종료'               입력시 프로그램을 종료할 수 있습니다.")
        elif select == '메타데이터 출력':
            manage_metadata()
        
        elif select == '파일삭제':
            delete_file()
        
        elif select == '파일검색':
            search_file()

        elif select == '파일이동':
            move_file()
        
        elif select == '디렉토리 생성':
            create_directory()

        elif select == '파일목록':
            list_files()

        elif select == '부모 디렉토리 확인':
            getParentDir()

        elif select == '파일복사':
            copy_file()

        elif select == '잘라내기':
            cut_file()

        elif select == '해시저장':
            file_path = input("해시값을 계산할 원본파일 경로 : ")
            hash_file_path = input("해시값을 저장할 경로 : ")
            save_hash(file_path,hash_file_path)

        elif select == '무결성 검사':
            file_path = input("무결성을 검사할 파일의 경로 : ")
            hash_path = input("대상파일의 원본 해시값이 저장된 경로 : ")
            check_integrity(hash_path, file_path)
            

        elif select == "종료":
            print("중복 관리를 종료합니다.")
            finish = True

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요. : ")


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
    """
    if os.path.exists(path):
        os.remove(path)
        print(f"{path} 파일이 삭제되었습니다.")
    else:
        print(f"{path} 파일이 존재하지 않습니다.")





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

    shutil.copy(src_path, dest_path)
    print(f"파일이 복사되었습니다: {src_path} -> {dest_path}")

# cut-file 함수 추
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










        
