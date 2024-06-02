'''
파일 자체를 컨트롤 하는 기능들의 패키지 입니다.
'''

import os
import shutil
import time
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
            print(" '파일색상 변경'      입력시 파일이름의 색상을 변경합니다")
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
            copyFile()

        elif select == '잘라내기':
            cut_file()

        elif select == '파일색상 변경':
            directory = input("파일을 나열할 디렉토리 경로를 입력하세요: ")
            print("색상 선택: 1 - 빨간색, 2 - 파란색")
            color_choice = int(input("파일 이름의 색을 선택하세요 (1 또는 2): "))
            list_files(directory, color_choice)

            
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

# 파일 이름 색상을 바꾸는 기능
def display_files_with_color(files: List[str], color_choice: int):
    if color_choice == 1:
        color_code = RED  # 빨간색 텍스트
    elif color_choice == 2:
        color_code = BLUE  # 파란색 텍스트
    else:
        print("잘못된 색상 선택입니다.")
        return

    for file in files:
        print(f"{color_code}{file}{ENDC}")

def list_files(directory: str, color_choice: int = None) -> List[str]:
    """
    Lists all files in the specified directory.
    @Param
        directory : The directory path to list files from.
    @Return
        A list of filenames in the directory.
    @Raises
        Prints an error message if the operation fails and returns an empty list.
    """
    try:
        files = os.listdir(directory)
        if color_choice is not None:
            display_files_with_color(files, color_choice)
        else:
            print(f"Files in {directory}: {files}")
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []
