'''
파일 자체를 컨트롤 하는 기능들의 패키지 입니다.
'''

import os
import shutil
import time
import zipfile
from collections import defaultdict
import datetime
import hashlib
import platform
from typing import List
from functools import lru_cache
from Control.FileControl import search_file


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

def get_file_system_statistics():
    """
    주어진 디렉토리의 파일 시스템 통계를 계산합니다.
    
    @param
        directory: 통계를 계산할 디렉토리 경로
    
    @Returns
        파일 시스템 통계를 담은 딕셔너리
    """
    directory = input("통계를 계산할 디렉토리 경로 : ")

    statistics = {
        'total_files': 0,
        'total_directories': 0,
        'total_size': 0,
        'file_type_counts': defaultdict(int)
    }

    for dirpath, dirnames, filenames in os.walk(directory):
        # 디렉토리 수 증가
        statistics['total_directories'] += len(dirnames)

        # 파일 수 및 파일 크기 증가
        for filename in filenames:
            statistics['total_files'] += 1
            file_path = os.path.join(dirpath, filename)
            statistics['total_size'] += os.path.getsize(file_path)

            # 파일 유형별 통계 증가
            _, file_extension = os.path.splitext(filename)
            statistics['file_type_counts'][file_extension] += 1

    return statistics


def print_file_system_statistics():
    """
    주어진 디렉토리의 파일 시스템 통계를 출력합니다.
    
    @param
        directory: 통계를 출력할 디렉토리 경로
    """
    directory = input('통계를 출력할 디렉토리 경로 : ')

    stats = get_file_system_statistics(directory)

    print(f"디렉토리: {directory}")
    print(f"총 파일 수: {stats['total_files']}")
    print(f"총 디렉토리 수: {stats['total_directories']}")
    print(f"총 용량: {stats['total_size']} bytes")
    print("파일 유형별 통계:")
    for file_type, count in stats['file_type_counts'].items():
        print(f"  {file_type if file_type else 'No Extension'}: {count} files")


def print_directory_tree():
    """
    주어진 디렉토리의 트리 구조를 출력합니다.
    @param
        root_directory: 트리를 출력할 루트 디렉토리
        indent: 들여쓰기 문자열
    """
    root_directory = input('트리를 출력할 루트 디렉토리 : ')
    indent=input('들여쓰기 문자열 : ')

    items = os.listdir(root_directory)
    for index, item in enumerate(items):
        item_path = os.path.join(root_directory, item)
        if index == len(items) - 1:
            print(indent + "└── " + item)
            new_indent = indent + "    "
        else:
            print(indent + "├── " + item)
            new_indent = indent + "│   "
        if os.path.isdir(item_path):
            print_directory_tree(item_path, new_indent)

def print_system_info():
    """
    현재 시스템의 운영체제 및 컴퓨터 정보를 출력한다.
    매개변수 없음
    """
    try:
        # 운영체제 및 기본 시스템 정보
        print(f"운영체제: {platform.system()}") 
        print(f"운영체제 상세 버전: {platform.version()}")  
        arch_info = platform.architecture()
        print(f"시스템 아키텍처: {arch_info[0]}") 
        print(f"컴퓨터 이름: {platform.node()}")
        print(f"프로세서: {platform.processor()}")  
        print(f"Python 버전: {platform.python_version()}")

    except Exception as e:
        print(f"시스템 정보 출력 중 오류가 발생했습니다: {e}")


def print_files_by_mtime():
    """
    사용자가 입력한 디렉토리 내에서 파일을 수정 시간 순으로 정렬하여 출력한다.
    매개변수 directory: 디렉토리 경로
    """
    directory = input('디렉토리 경로 : ')
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        for file in files:
            mtime = os.path.getmtime(file)
            mtime_readable = time.ctime(mtime)
            print(f"{file}: 수정 시간 - {mtime_readable}")

    except Exception as e:
        print(f"파일 목록 출력 중 오류 발생: {e}")


def classify_files_by_extension():
    """
    파일 형식에 따라 파일을 분류하여 이동하는 함수
    :param source_directory: 파일들이 있는 소스 디렉토리
    :param destination_directory: 분류된 파일들을 저장할 목적지 디렉토리
    """
    source_directory = input('파일들이 있는 소스 디렉토리 : ')
    destination_directory = input('분류된 파일들을 저장할 목적지 디렉토리 : ')
    # 소스 디렉토리에서 모든 파일과 디렉토리 가져오기
    for item in os.listdir(source_directory):
        item_path = os.path.join(source_directory, item)

        # 파일인 경우에만 처리
        if os.path.isfile(item_path):
            # 파일 확장자 가져오기
            file_extension = os.path.splitext(item)[1][1:].lower()  # 확장자에서 점(.) 제거하고 소문자로 변환
            if file_extension:  # 확장자가 있는 경우
                # 목적지 디렉토리 경로 만들기
                extension_dir = os.path.join(destination_directory, file_extension)
                os.makedirs(extension_dir, exist_ok=True)  # 확장자 디렉토리 생성 (이미 있으면 무시)

                # 파일을 목적지 디렉토리로 이동
                shutil.move(item_path, os.path.join(extension_dir, item))
                print(f"Moved: {item} -> {extension_dir}")

def get_last_modified_time():
    """
    파일의 최종 수정시간을 출력하는 함수
    매개변수
    file_path : 최종 수정시간을 확인하고 싶은 파일의 경로
    출력 : "최종 수정 시간 :", last_modified_time)
    """
    file_path = input('최종 수정시간을 확인하고 싶은 파일의 경로')

    try:
        # 파일의 최종 수정 시간을 가져옴 (os.path.getmtime)
        # 타임스탬프를 datetime 객체로 변환
        last_modified_datetime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        # 문자열로 반환
        last_modified_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Last modified time:", last_modified_datetime)
    except OSError as e:
        print("Error:", e)
        return None
    


def save_hash(file_path):
    """
    경로의 파일의 해시 값을 계산하는 함수
    
    @Param
        file_path : 해시 값을 계산할 파일의 경로
        
    @Return
        생성된 해시 값
        
    @Raises
        FileNotFoundError : 파일 경로가 존재 하지 않을때 발생
        IOError : 파일 읽기에 실패시 발생
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(4096)
        while buf:
            hasher.update(buf)
            buf = f.read(4096)
    return hasher.hexdigest()


origin_hash = "" #해시값 저장을 위한 변수

def check_integrity(origin_hash, file_path):
    """
    경로상 파일의 저장된 원본 해시값과 현재 해시값을 비교해 무결성을 검사하는 함수
    
    @Param
        origin_hash: 비교할 원본 해시 값
        file_path: 무결성을 확인할 파일의 경로
        
    @Return
        없음
        
    @Raises
        FileNotFoundError : 파일 경로가 존재 하지 않을때 발생
        IOError : 파일 읽기에 실패시 발생
    """
    current_hash = save_hash(file_path)
    if current_hash == origin_hash:
        print(f"{file_path}의 무결성 : 정상")
    else:
        print(f"{file_path}의 무결성 : 손상\nCurrent Hash: {current_hash}\nOrigin Hash: {origin_hash}")

def encrypt_file(file_path): 
    """
    파일을 sha256 암호화하는 기능
    """
    try: #파일 내용을 읽어, sha256으로 변환.
        with open(file_path, 'rb') as file: 
            file_content = file.read()
            sha256_hash = hashlib.sha256(file_content).hexdigest()

        #그 후, 변환된 값을 다시 저장
        with open(file_path, 'w') as file:
            file.write(sha256_hash)

        #성공적으로 저장
        return "File content has been hashed and saved."
    except FileNotFoundError:
        return "File not found. Please check the file path." # 파일을 찾을 수 없을때 나타나는 error
    except Exception as e: #외의 에러 제어
        return f"An error occurred: {e}"
    


def search_in_file(file_path, keyword):
    with open(file_path, 'r') as file:
        return [line for line in file if keyword in line]
    
def get_directory_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_file_size(file_path):
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    return None


# 파일 분할


def Partition_file(file_path, setSize):
    """
    지정한 파일을 지정된 크기로 분할.
    @Param
        file_path : 분할할 원본 파일의 경로.
        setSize : 분할될 파일 한개의 크기 (바이트 단위).
            
    @Return
        None
    """
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


def Merge_files(output_path, input_paths):
    """
    분할된 파일들을 하나의 파일로 병합합니다.
    @Param
        output_path : 병합된 파일을 저장할 위치
        input_paths : 병합할 분할된 파일들의 경로.
        
    @Return
        None
    """
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
        return "존재하지 않은 파일입니다."
    except PermissionError:
        return "파일 권한이 없습니다."
    except IsADirectoryError:
        return "파일이 아닌 디렉토리 입니다."
    except Exception as e:
        return f"An error occurred: {e}"

def compress_file(file_path):
    """
    사용자가 파일경로를 입력하면 해당파일을 zip으로 압축합니다.
    
    매개변수 file_path (str): 압축할 파일의 경로
    """
    try:
        # 압축할 파일의 디렉토리와 파일 이름 추출
        file_dir = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        # 출력 zip 파일 경로 설정
        output_zip = os.path.join(file_dir, f"{file_name}.zip")

        with zipfile.ZipFile(output_zip, 'w') as zipf:
            zipf.write(file_path, file_name)
        print(f"파일이 성공적으로 압축되었습니다: {output_zip}")
    except Exception as e:
        print(f"파일 압축 중 오류가 발생했습니다: {e}")


def list_file_creation_times(directory):
    """
    사용자가 입력한 디렉토리 내부의 모든 파일들의 생성 시간을 출력합니다.
    
    매개변수 directory: 파일 생성 시간을 출력할 디렉토리의 경로
    """
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                created_time = os.path.getctime(file_path)
                created_time_readable = time.ctime(created_time)
                print(f"{filename}: 생성 시간 - {created_time_readable}")
    except Exception as e:
        print(f"파일 생성 시간 출력 중 오류가 발생했습니다: {e}")