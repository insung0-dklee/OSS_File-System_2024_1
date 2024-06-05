
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
import time
import function
import zipfile
import tarfile
import getpass
import hashlib
from Control import Bookmark
from Control import FileEdit
from Control import FileControl
from Control import Duplicates
from Control import Readable
from Control.FileControl import search_file
import datetime
from collections import defaultdict
import platform
from Control import AutoFileManage
import subprocess
import ctypes
import stat

import paramiko
import socket

def move_to_trash(file_path):
    """
    파일을 휴지통으로 이동합니다.
    :param file_path: 삭제할 파일의 경로
    """
    trash_dir = os.path.join(os.path.expanduser("~"), ".trash")
    if not os.path.exists(trash_dir):
        os.makedirs(trash_dir)

    try:
        shutil.move(file_path, trash_dir)
        print(f"{file_path}가 휴지통으로 이동되었습니다.")
    except Exception as e:
        print(f"파일을 휴지통으로 이동하는 중 오류가 발생했습니다: {e}")

### 휴지통에서 파일을 복구하는 함수
def restore_from_trash(file_name):
    """
    휴지통에서 파일을 복구합니다.
    :param file_name: 복구할 파일의 이름
    """
    trash_dir = os.path.join(os.path.expanduser("~"), ".trash")
    if not os.path.exists(trash_dir):
        print("휴지통이 비어 있습니다.")
        return

    file_path = os.path.join(trash_dir, file_name)
    if not os.path.exists(file_path):
        print(f"{file_name}이(가) 휴지통에 없습니다.")
        return

    try:
        restored_path = os.path.join(os.path.expanduser("~"), "Desktop", file_name)  # 복구할 경로 지정
        shutil.move(file_path, restored_path)
        print(f"{file_name}이(가) {restored_path}로 복구되었습니다.")
    except Exception as e:
        print(f"파일을 복구하는 중 오류가 발생했습니다: {e}")

### 휴지통 내 파일 목록을 출력하는 함수
def list_trash():
    """
    휴지통 내의 파일 목록을 출력합니다.
    """
    trash_dir = os.path.join(os.path.expanduser("~"), ".trash")
    if not os.path.exists(trash_dir):
        print("휴지통이 비어 있습니다.")
        return

    files = os.listdir(trash_dir)
    if not files:
        print("휴지통이 비어 있습니다.")
        return

    print("휴지통 내 파일 목록:")
    for file in files:
        print(f"  - {file}")

def defragment_file_system(path):
    """주어진 경로에 대해 파일 시스템 조각 모음을 수행합니다."""
    try:
        result = subprocess.run(["e4defrag", path], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"조각 모음 중 오류 발생: {e.stderr}")

def run_file_or_open_folder(path):
    if os.path.isfile(path):
        # 파일인 경우 바로 실행
        if os.name == 'nt':  # Windows인 경우
            os.startfile(path)
        elif os.name == 'posix':  # Linux, macOS인 경우
            subprocess.run(['xdg-open', path])
    elif os.path.isdir(path):
        # 폴더인 경우 열기
        if os.name == 'nt':  # Windows인 경우
            os.startfile(path)
        elif os.name == 'posix':  # Linux, macOS인 경우
            subprocess.run(['xdg-open', path])

def compare_files(file1_path, file2_path):
    """
    두 텍스트 파일을 비교하여 차이점을 출력합니다.
    
    @param
        file1_path: 첫 번째 파일 경로
        file2_path: 두 번째 파일 경로
    """
    supported_extensions = ['.txt', '.md', '.py', '.json']

    def check_extension(file_path):
        _, ext = os.path.splitext(file_path)
        if ext not in supported_extensions:
            raise ValueError(f"지원하지 않는 파일 형식입니다: {ext}")

    try:
        check_extension(file1_path)
        check_extension(file2_path)

        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

        differences = []
        max_lines = max(len(file1_lines), len(file2_lines))

        for i in range(max_lines):
            line1 = file1_lines[i] if i < len(file1_lines) else ""
            line2 = file2_lines[i] if i < len(file2_lines) else ""
            if line1 != line2:
                differences.append((i + 1, line1, line2))

        if differences:
            print("파일의 내용 차이점:")
            for line_num, line1, line2 in differences:
                print(f"Line {line_num}:")
                print(f"  파일1: {line1.strip()}")
                print(f"  파일2: {line2.strip()}")
        else:
            print("두 파일의 내용은 동일합니다.")

    except FileNotFoundError as e:
        print(f"파일을 찾을 수 없습니다: {e}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"파일 비교 중 오류가 발생했습니다: {e}")

def search_files_with_keyword(directory, keyword):
    """
    디렉토리 내에서 특정 키워드를 포함한 파일을 검색합니다.
    :param directory: 검색할 디렉토리 경로
    :param keyword: 검색할 키워드
    """
    result_files = []  # 키워드를 포함한 파일 경로를 저장할 리스트
    for dirpath, _, filenames in os.walk(directory):  # 디렉토리 내 모든 파일을 순회
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)  # 파일의 절대 경로 생성
            try:
                with open(file_path, 'r', encoding='utf-8') as file:  # 파일을 읽기 모드로 열기
                    content = file.read()  # 파일 내용 읽기
                    if keyword in content:  # 키워드가 파일 내용에 포함되어 있는지 확인
                        result_files.append(file_path)  # 키워드를 포함한 파일 경로를 리스트에 추가
            except (UnicodeDecodeError, IOError):  # 인코딩 오류 또는 입출력 오류 처리
                continue
    return result_files  # 키워드를 포함한 파일 경로 리스트 반환

# 사용 예시
directory = input("검색할 디렉토리 경로를 입력하세요: ")  # 사용자로부터 검색할 디렉토리 경로 입력 받기
keyword = input("검색할 키워드를 입력하세요: ")  # 사용자로부터 검색할 키워드 입력 받기
matching_files = search_files_with_keyword(directory, keyword)  # 함수 호출하여 결과 저장
print(f"키워드를 포함한 파일 목록: {matching_files}")  # 결과 출력


def get_file_system_statistics(directory):
    """
    주어진 디렉토리의 파일 시스템 통계를 계산합니다.
    
    @param
        directory: 통계를 계산할 디렉토리 경로
    
    @Returns
        파일 시스템 통계를 담은 딕셔너리
    """
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

def print_file_system_statistics(directory):
    """
    주어진 디렉토리의 파일 시스템 통계를 출력합니다.
    
    @param
        directory: 통계를 출력할 디렉토리 경로
    """
    stats = get_file_system_statistics(directory)

    print(f"디렉토리: {directory}")
    print(f"총 파일 수: {stats['total_files']}")
    print(f"총 디렉토리 수: {stats['total_directories']}")
    print(f"총 용량: {stats['total_size']} bytes")
    print("파일 유형별 통계:")
    for file_type, count in stats['file_type_counts'].items():
        print(f"  {file_type if file_type else 'No Extension'}: {count} files")

def print_directory_tree(root_directory, indent=""):
    """
    주어진 디렉토리의 트리 구조를 출력합니다.
    @param
        root_directory: 트리를 출력할 루트 디렉토리
        indent: 들여쓰기 문자열
    """
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

def print_files_by_mtime(directory):
    """
    사용자가 입력한 디렉토리 내에서 파일을 수정 시간 순으로 정렬하여 출력한다.
    매개변수 directory: 디렉토리 경로
    """
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        for file in files:
            mtime = os.path.getmtime(file)
            mtime_readable = time.ctime(mtime)
            print(f"{file}: 수정 시간 - {mtime_readable}")

    except Exception as e:
        print(f"파일 목록 출력 중 오류 발생: {e}")

def classify_files_by_extension(source_directory, destination_directory):
    """
    파일 형식에 따라 파일을 분류하여 이동하는 함수
    :param source_directory: 파일들이 있는 소스 디렉토리
    :param destination_directory: 분류된 파일들을 저장할 목적지 디렉토리
    """
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

def get_last_modified_time(file_path):
    """
    파일의 최종 수정시간을 출력하는 함수
    매개변수
    file_path : 최종 수정시간을 확인하고 싶은 파일의 경로
    출력 : "최종 수정 시간 :", last_modified_time)
    """
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

def is_symlink(path):
    return os.path.islink(path)

def create_hardlink(target, link_name):
    os.link(target, link_name)

def is_hardlink(path):
    """하드 링크 여부는 직접적으로 확인하기 어렵지만, os.stat()으로 inode 번호를 통해 확인 가능하다."""
    try:
        stat_info = os.stat(path)
        return stat_info.st_nlink > 1
    except FileNotFoundError:
        return False


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

def calculate_directory_size(directory): # 폴더크기 측정 기능 함수
    """
    주어진 디렉토리의 총 크기를 계산합니다.
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

directory_path = input("크기를 측정할 디렉토리 경로를 입력하세요: ")
print(f"디렉토리의 총 크기: {calculate_directory_size(directory_path)} bytes")


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

def touch(file_path):
    """
    사용자로부터 파일의 경로를 입력받아서 타임스탬프를 업데이트
    파일이 존재하면 마지막 수정 시간을 갱신한다.
    파일이 존재하지 않으면 에러 출력
    매개변수 file_path: 사용자로부터 입력받은 타임스탬프를 업데이트할 파일의 경로
    """
    try:
        if os.path.exists(file_path):
            os.utime(file_path, None)
            print(f"'{file_path}' 파일의 타임스탬프가 업데이트 되었습니다.")
        else:
            raise FileNotFoundError(f"'{file_path}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일 수정 중 오류가 발생했습니다: {e}")

def hideFile(path):
    try:
        subprocess.call(['attrib', '+H', path])
        print(f"파일이 성공적으로 숨겨졌습니다: {path}")
    except Exception as e:
        print(f"파일 숨기기 중 오류가 발생했습니다: {e}")

def backup_directory_files(file_path, backup_directory):
    """
    지정된 디렉토리의 파일들을 백업 디렉토리로 복사합니다.
    :param file_path: 백업할 소스 디렉토리의 경로
    :param backup_directory: 백업 파일을 저장할 디렉토리의 경로
    """

    # 백업 디렉토리 생성
    os.makedirs(backup_directory, exist_ok=True)

    # 디렉토리 내 파일들의 리스트 가져오기
    file_list = os.listdir(file_path)

    # 디렉토리 내 파일들을 백업 디렉토리로 복사
    for file_name in file_list:
        file_path = os.path.join(file_path, file_name)
        backup_path = os.path.join(backup_directory, file_name)
        shutil.copy2(file_path, backup_path)

    print("파일 백업 완료!")

def list_zip_contents(zip_path):
    """
    ZIP 파일의 내용을 나열합니다.
    :param zip_path: ZIP 파일의 경로
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            print(f"{zip_path} 내용:")
            for file in file_list:
                print(f"  - {file}")
    except Exception as e:
        print(f"ZIP 파일 내용을 나열하는 중 오류가 발생했습니다: {e}")

def extract_file_from_zip(zip_path, file_name, dest_dir):
    """
    ZIP 파일에서 특정 파일을 추출합니다.
    :param zip_path: ZIP 파일의 경로
    :param file_name: 추출할 파일의 이름
    :param dest_dir: 추출할 목적지 디렉토리
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if file_name in zip_ref.namelist():
                zip_ref.extract(file_name, dest_dir)
                print(f"{file_name}이(가) {dest_dir}로 추출되었습니다.")
            else:
                print(f"{file_name}이(가) ZIP 파일에 존재하지 않습니다.")
    except Exception as e:
        print(f"ZIP 파일에서 파일을 추출하는 중 오류가 발생했습니다: {e}")

def set_desktop_background(image_path):
    """
    바탕화면 배경을 지정된 이미지 파일로 설정합니다.
    
    @param
        image_path: 바탕화면 배경으로 설정할 이미지 파일의 경로
    """
    try:
        # SPI_SETDESKWALLPAPER 상수를 사용하여 바탕화면 배경 이미지 설정
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        print("바탕화면 배경이 설정되었습니다.")
    except Exception as e:
        print(f"바탕화면 배경 설정 중 오류가 발생했습니다: {e}")

def get_desktop_files():
    """
    바탕화면의 파일 목록을 반환합니다.
    """
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.listdir(desktop_path)



def compress_file(file_path, method='zip'):
    """
    사용자가 파일경로를 입력하면 해당파일을 zip으로 압축합니다.
    
    매개변수 file_path (str): 압축할 파일의 경로
    """
    try:
        # 압축할 파일의 디렉토리와 파일 이름 추출
        file_dir = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        if method == 'zip':
            output_zip = os.path.join(file_dir, f"{file_name}.zip")
            with zipfile.ZipFile(output_zip, 'w') as zipf:
                zipf.write(file_path, file_name)
            print(f"파일이 성공적으로 압축되었습니다: {output_zip}")

        elif method == 'tar.gz':
            output_tar_gz = os.path.join(file_dir, f"{file_name}.tar.gz")
            with tarfile.open(output_tar_gz, 'w:gz') as tarf:
                tarf.add(file_path, arcname=file_name)
            print(f"파일이 성공적으로 압축되었습니다: {output_tar_gz}")

        elif method == 'tar.bz2':
            output_tar_bz2 = os.path.join(file_dir, f"{file_name}.tar.bz2")
            with tarfile.open(output_tar_bz2, 'w:bz2') as tarf:
                tarf.add(file_path, arcname=file_name)
            print(f"파일이 성공적으로 압축되었습니다: {output_tar_bz2}")

        else:
            print(f"지원하지 않는 압축 방식입니다: {method}")
    except Exception as e:
        print(f"파일 압축 중 오류가 발생했습니다: {e}")

def print_file_permissions_rwx(file_path):
    """
    사용자가 입력한 파일 경로의 권한을 rwx 형식으로 출력합니다.
    매개변수 file_path: 권한을 출력할 파일 경로
    """
    def get_permission_string(mode):
        """
        파일 모드를 rwx 문자열로 변환합니다.
        매개변수 mode: 파일 모드
        """
        is_dir = 'd' if stat.S_ISDIR(mode) else '-'
        perms = [
            (stat.S_IRUSR, 'r'), (stat.S_IWUSR, 'w'), (stat.S_IXUSR, 'x'),
            (stat.S_IRGRP, 'r'), (stat.S_IWGRP, 'w'), (stat.S_IXGRP, 'x'),
            (stat.S_IROTH, 'r'), (stat.S_IWOTH, 'w'), (stat.S_IXOTH, 'x')
        ]
        permission_string = is_dir + ''.join([perm if mode & mask else '-' for mask, perm in perms])
        return permission_string

    try:
        mode = os.stat(file_path).st_mode
        permission_string = get_permission_string(mode)
        print(f"{file_path}의 권한: {permission_string}")
    except Exception as e:
        print(f"권한 확인 중 오류가 발생했습니다: {e}")

def check_extension_in_directory(directory, extension):
    """
    사용자가 입력한 디렉토리 내에 사용자가 입력한 확장자가 존재하는지 여부를 출력합니다.
    :param directory: 검색할 디렉토리 경로
    :param extension: 검색할 파일 확장자 (예: '.txt')
    """
    if not os.path.exists(directory):
        print(f"경로가 존재하지 않습니다: {directory}")
        return

    if not os.path.isdir(directory):
        print(f"유효한 디렉토리가 아닙니다: {directory}")
        return

    try:
        extension_found = False
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(extension):
                    extension_found = True
                    print(f"확장자가 {extension}인 파일 발견: {os.path.join(dirpath, filename)}")

        if not extension_found:
            print(f"디렉토리 내에 확장자가 {extension}인 파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"확장자 확인 중 오류가 발생했습니다: {e}")

def print_file_mode(file_path):
    """
    파일의 권한(모드)를 8진수 형식으로 출력합니다.
    매개변수 file_path: 권한(모드)를 출력할 파일 경로
    """
    try:
        mode = os.stat(file_path).st_mode
        print(f"{file_path}의 모드: {oct(mode)}")
    except Exception as e:
        print(f"모드 확인 중 오류가 발생했습니다: {e}")

def decompressFile(zip_path, dest):
    """
    압축 파일을 해제합니다.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dest)
        print(f"압축 해제가 성공적으로 완료되었습니다: {dest}")
    except Exception as e:
        print(f"압축 해제 중 오류가 발생했습니다: {e}")


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


# 메모 파일 저장 경로
MEMO_DIR = './memos'

# 메모 디렉토리가 존재하지 않으면 생성
if not os.path.exists(MEMO_DIR):
    os.makedirs(MEMO_DIR)

def read_memo(file_path):
    """
    파일에 대한 메모를 읽어옵니다.
    :param file_path: 파일의 경로
    :return: 메모 내용 반환, 메모가 없을 경우 None 반환
    """
    # 메모 파일 경로 생성
    memo_path = os.path.join(MEMO_DIR, os.path.basename(file_path) + '.txt')
    # 메모 파일이 존재하면 내용을 읽어서 반환
    if os.path.exists(memo_path):
        with open(memo_path, 'r', encoding='utf-8') as f:
            return f.read()
    # 메모 파일이 없으면 None 반환
    return None

def write_memo(file_path, memo):
    """
    파일에 대한 메모를 작성합니다.
    :param file_path: 파일의 경로
    :param memo: 작성할 메모 내용
    """
    # 메모 파일 경로 생성
    memo_path = os.path.join(MEMO_DIR, os.path.basename(file_path) + '.txt')
    # 메모 파일에 내용을 작성
    with open(memo_path, 'w', encoding='utf-8') as f:
        f.write(memo)


def manage_memo_for_files(root_directory, target_filename):
    """
    주어진 디렉토리에서 특정 파일을 검색하고 메모를 관리합니다.
    :param root_directory: 검색을 시작할 루트 디렉토리
    :param target_filename: 검색할 파일의 이름
    """
    # 파일 검색
    matched_files = search_file(root_directory, target_filename)

    if matched_files:
        for file_path in matched_files:
            print(f'파일을 찾았습니다: {file_path}')
            # 파일에 대한 메모 읽기
            memo = read_memo(file_path)
            if memo:
                print(f'기존 메모:\n{memo}')
                # 메모 수정 여부 확인
                if input('메모를 수정하시겠습니까? (y/n): ').lower() == 'y':
                    new_memo = input('새 메모 내용을 입력하세요: ')
                    write_memo(file_path, new_memo)
                    print('메모가 수정되었습니다.')
                else:
                    print('메모 수정이 취소되었습니다.')
            else:
                # 새 메모 작성
                new_memo = input('메모가 없습니다. 새 메모 내용을 입력하세요: ')
                write_memo(file_path, new_memo)
                print('메모가 추가되었습니다.')
    else:
        print('파일을 찾을 수 없습니다.')

# 디렉토리 모니터링 기능 추가
def get_files_snapshot(directory):
    """
    주어진 디렉토리의 파일 및 디렉토리 상태를 스냅샷으로 가져옵니다.
    
    Args:
        directory (str): 스냅샷을 가져올 디렉토리 경로
    Returns:
        dict: 파일 경로와 수정 시간을 담은 딕셔너리
    """
    snapshot = {}  # 스냅샷을 저장할 딕셔너리 초기화
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)  # 파일의 절대 경로 생성
            snapshot[file_path] = os.stat(file_path).st_mtime  # 파일의 마지막 수정 시간을 저장
    return snapshot

def compare_snapshots(old_snapshot, new_snapshot):
    """
    이전 스냅샷과 현재 스냅샷을 비교하여 파일 생성, 수정, 삭제를 감지합니다.
    
    Args:
        old_snapshot (dict): 이전 스냅샷
        new_snapshot (dict): 현재 스냅샷
    Returns:
        tuple: 추가된 파일 목록, 삭제된 파일 목록, 수정된 파일 목록
    """
    # new_snapshot에 있지만 old_snapshot에 없는 파일 (추가된 파일)
    added = [file for file in new_snapshot if file not in old_snapshot]

    # old_snapshot에 있지만 new_snapshot에 없는 파일 (삭제된 파일)
    removed = [file for file in old_snapshot if file not in new_snapshot]

    # 둘 다 있지만 수정 시간이 다른 파일 (수정된 파일)
    modified = [file for file in new_snapshot if file in old_snapshot and old_snapshot[file] != new_snapshot[file]]

    return added, removed, modified

def monitor_directory(directory, interval=5):
    """
    주어진 디렉토리를 모니터링하며, 변경 사항을 감지합니다.
    
    Args:
        directory (str): 모니터링할 디렉토리 경로
        interval (int): 스냅샷을 비교할 시간 간격 (초)
    """
    print(f"Monitoring directory: {directory}")
    previous_snapshot = get_files_snapshot(directory)  # 초기 스냅샷 생성
    try:
        while True:
            time.sleep(interval)  # 주어진 시간 간격(기본 5초)으로 대기
            current_snapshot = get_files_snapshot(directory)  # 현재 상태 스냅샷 생성
            added, removed, modified = compare_snapshots(previous_snapshot, current_snapshot)  # 스냅샷 비교

            # 추가된 파일 출력
            for file in added:
                print(f"File created: {file}")

            # 삭제된 파일 출력
            for file in removed:
                print(f"File deleted: {file}")

            # 수정된 파일 출력
            for file in modified:
                print(f"File modified: {file}")

            previous_snapshot = current_snapshot  # 현재 스냅샷을 이전 스냅샷으로 업데이트
    except KeyboardInterrupt:
        print("Directory monitoring stopped.")

"""
파일에 비밀번호를 부여하고 그 파일의 경로를 만들기 위해선 비밀번호를 입력해야하는 코드입니다.
import os
import getpass                                -> getpass 라이브러리는 비밀번호와 같은 입력을 받기위해 사용했습니다.
def check_password(input_password):            -> 입력한 비밀번호가 맞는지 확인하기 위해 만든 함수입니다.
    correct_password = "1234"                  -> correct_password는 사용자가 지정한 비밀번호를 담기 위해 만들었습니다.
    return input_password == correct_password  -> 함수의 매개변수에 사용자가 지정해준 비밀번호를 리턴해줍니다.
def create_file(filename):                            -> 파일을 만드는 함수입니다.
    password = getpass.getpass("비밀번호를 입력하세요: ")  -> getpass.getpass()는 사용자에게 비밀번호를 입력받는 getpass 라이브러리에
                                                          등록되어있는 함수입니다.
    if check_password(password):                       -> 만약 입력받은 password가 지정해둔 password와 같다면,
        print(f"'{filename}' 파일이 생성되었습니다.")      -> 파일을 생성시키는 함수를 나타내었습니다. f"string"을 사용하여 중괄호 안에
                                                          넣고자하는 변수를 사용하여 변수에 해당한 값을 나타내줍니다.
    else:
        print("비밀번호가 틀렸습니다.")                     -> 비밀번호가 틀렸다는 것을 알려주기 위해 작성하였습니다.
if __name__ == "__main__":
    filename = input("만들고자 하는 파일 명을 입력하시오: ")   -> 만들고자 하는 파일명을 입력받습니다.
    file_path = os.path.join(os.getcwd(), filename)      -> 파일명을 현재 작업하고 있는 파일의 경로와 합쳐 파일 경로 형식으로 만듭니다.
    create_file(file_path)                               -> create_file함수를 통과하면서 코드가 마무리됩니다.
"""

def change_permissions(path, mode):
    """
    파일 또는 디렉토리의 권한을 변경합니다.
    :param path: 파일 또는 디렉토리 경로
    :param mode: 권한 모드 (8진수 형태로 입력, 예: 0o755)
    """
    try:
        os.chmod(path, mode)
        print(f"{path}의 권한이 {oct(mode)}로 변경되었습니다.")
    except Exception as e:
        print(f"권한 변경 중 오류가 발생했습니다: {e}")


def check_password(input_password):
    correct_password = "1234"
    return input_password == correct_password

def create_file(filename):
    password = getpass.getpass("비밀번호를 입력하세요: ")
    if check_password(password):
        print(f"'{filename}' 파일이 생성되었습니다.")
    else:
        print("비밀번호가 틀렸습니다.")

def calculate_hash(file_path):
    """
    파일의 SHA-256 해시 값을 계산하여 반환합니다.
    @param
        file_path: 해시 값을 계산할 파일의 경로
    """
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            buffer = file.read(65536)  # 64KB씩 읽기
            while buffer:
                hasher.update(buffer)
                buffer = file.read(65536)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return None
    except Exception as e:
        print(f"해시 계산 중 오류가 발생했습니다: {e}")
        return None

def save_hash(file_path, hash_file_path):
    """
    파일의 해시 값을 계산하여 지정된 경로에 저장합니다.
    @param
        file_path: 해시 값을 계산할 파일의 경로
        hash_file_path: 해시 값을 저장할 파일의 경로
    """
    hash_value = calculate_hash(file_path)
    if hash_value:
        try:
            with open(hash_file_path, 'w') as hash_file:
                hash_file.write(hash_value)
            print(f"해시 값이 {hash_file_path}에 저장되었습니다.")
        except Exception as e:
            print(f"해시 값을 저장하는 중 오류가 발생했습니다: {e}")

def verify_file_integrity(file_path, hash_file_path):
    """
    파일의 무결성을 검증합니다.
    @param
        file_path: 무결성을 검증할 파일의 경로
        hash_file_path: 저장된 해시 값이 있는 파일의 경로
    """
    try:
        with open(hash_file_path, 'r') as hash_file:
            stored_hash = hash_file.read().strip()
        current_hash = calculate_hash(file_path)
        if current_hash == stored_hash:
            print(f"{file_path}의 무결성이 확인되었습니다.")
        else:
            print(f"{file_path}의 무결성이 손상되었습니다.")
            print(f"현재 해시 값: {current_hash}")
            print(f"저장된 해시 값: {stored_hash}")
    except FileNotFoundError:
        print(f"해시 파일을 찾을 수 없습니다: {hash_file_path}")
    except Exception as e:
        print(f"무결성 검증 중 오류가 발생했습니다: {e}")

# SSH를 통해 원격 서버의 파일을 관리하는 함수들
def ssh_connect(hostname, port, username, password):
    """
    SSH 연결을 설정하고 반환합니다.
    @param
        hostname: 원격 서버의 호스트명 또는 IP 주소
        port: 원격 서버의 포트 번호
        username: SSH 사용자명
        password: SSH 비밀번호
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password, timeout=30)  # 30초 타임아웃 설정
        return client
    except (paramiko.ssh_exception.NoValidConnectionsError, socket.timeout):
        print("SSH 연결이 30초 내에 완료되지 않았습니다. 다시 시도하세요.")
    except paramiko.ssh_exception.AuthenticationException:
        print("SSH 인증 실패. 사용자명 또는 비밀번호를 확인하세요.")
    except Exception as e:
        print(f"SSH 연결 중 오류가 발생했습니다: {e}")
    return None

def list_remote_files(client, remote_path):
    """
    원격 서버의 파일 목록을 나열합니다.
    @param
        client: paramiko SSHClient 객체
        remote_path: 파일 목록을 나열할 원격 경로
    """
    try:
        sftp = client.open_sftp()
        files = sftp.listdir(remote_path)
        sftp.close()
        return files, None
    except FileNotFoundError:
        return None, f"원격 경로가 올바르지 않습니다: {remote_path}"
    except Exception as e:
        return None, f"원격 파일 목록을 나열하는 중 오류가 발생했습니다: {e}"

def upload_file_to_remote(client, local_path, remote_path, is_windows):
    """
    로컬 파일을 원격 서버에 업로드합니다.
    @param
        client: paramiko SSHClient 객체
        local_path: 업로드할 로컬 파일 경로
        remote_path: 업로드할 원격 파일 경로
        is_windows: 원격 서버가 윈도우 운영체제인지 여부
    """
    if not os.path.exists(local_path):
        print(f"잘못된 로컬 파일 경로: {local_path}")
        return

    try:
        sftp = client.open_sftp()
        # 원격 경로가 절대 경로가 아니면 홈 디렉토리로 설정
        if not (remote_path.startswith('/') or (is_windows and remote_path[1:3] == ':\\')):
            home_dir = sftp.normalize(".")
            remote_path = os.path.join(home_dir, remote_path).replace('\\', '/')
        
        # 원격 경로에 동일한 파일명이 존재하는지 확인
        try:
            sftp.stat(remote_path)
            overwrite = input(f"{remote_path}에 동일한 이름의 파일이 있습니다. 덮어쓰시겠습니까? (y/n): ").strip().lower()
            if overwrite != 'y':
                print("업로드가 중단되었습니다.")
                return
        except FileNotFoundError:
            pass  # 파일이 존재하지 않으면 계속 진행

        sftp.put(local_path, remote_path)
        sftp.close()
        print(f"{local_path}가 {remote_path}로 업로드되었습니다.")
    except Exception as e:
        print(f"파일을 업로드하는 중 오류가 발생했습니다: {e}")

def download_file_from_remote(client, remote_path, local_path):
    """
    원격 서버에서 로컬로 파일을 다운로드합니다.
    @param
        client: paramiko SSHClient 객체
        remote_path: 다운로드할 원격 파일 경로
        local_path: 다운로드할 로컬 파일 경로
    """
    try:
        sftp = client.open_sftp()
        sftp.stat(remote_path)  # 원격 파일 존재 여부 확인

        # 로컬 경로가 절대 경로가 아니면 현재 작업 디렉토리로 설정
        if not os.path.isabs(local_path):
            local_path = os.path.join(os.getcwd(), local_path)

        if os.path.exists(local_path):
            overwrite = input(f"{local_path}에 동일한 이름의 파일이 있습니다. 덮어쓰시겠습니까? (y/n): ").strip().lower()
            if overwrite != 'y':
                print("다운로드가 중단되었습니다.")
                return

        sftp.get(remote_path, local_path)
        sftp.close()
        print(f"{remote_path}가 {local_path}로 다운로드되었습니다.")
    except FileNotFoundError:
        print(f"잘못된 원격 파일 경로: {remote_path}")
    except Exception as e:
        print(f"파일을 다운로드하는 중 오류가 발생했습니다: {e}")

def close_ssh_connection(client):
    """
    SSH 연결을 종료합니다.
    @param
        client: paramiko SSHClient 객체
    """
    client.close()
    print("SSH 연결이 종료되었습니다.")

def detect_remote_os(client):
    """
    원격 서버의 운영체제를 감지합니다.
    @param
        client: paramiko SSHClient 객체
    """
    try:
        stdin, stdout, stderr = client.exec_command('uname')
        if stdout.read().strip():
            return "unix"
        return "windows"
    except Exception as e:
        print(f"원격 OS 감지 중 오류가 발생했습니다: {e}")
        return None

# 원격 파일 관리를 위한 인터페이스 추가
def remote_file_management():
    """
    원격 파일 관리 인터페이스를 제공하는 함수입니다.
    """
    hostname = input("원격 서버 호스트명(IP)을 입력하세요: ")
    
    while True:
        port_input = input("원격 서버 포트를 입력하세요 (기본값: 22): ").strip()
        if not port_input:
            port = 22
            break
        elif port_input.isdigit():
            port = int(port_input)
            break
        else:
            print("잘못된 포트 번호입니다. 숫자로 입력하세요.")
            continue 
    
    username = input("사용자명을 입력하세요: ")
    password = getpass.getpass("비밀번호를 입력하세요: ")

    client = ssh_connect(hostname, port, username, password)
    if not client:
        return

    os_type = detect_remote_os(client)
    is_windows = os_type == "windows"

    while True:
        command = input("원격 파일 관리 작업을 선택하세요 (목록, 업로드, 다운로드, 종료): ").strip().lower()
        if command == "목록":
            remote_path = input("목록을 볼 원격 경로를 입력하세요: ")
            files, error = list_remote_files(client, remote_path)
            if error:
                print(error)
            else:
                print(f"{remote_path}의 파일 목록")
                print(f"{files}")
        elif command == "업로드":
            local_path = input("업로드할 로컬 파일 경로를 입력하세요: ")
            remote_path = input("업로드할 원격 파일 경로를 입력하세요: ")
            upload_file_to_remote(client, local_path, remote_path, is_windows)
        elif command == "다운로드":
            remote_path = input("다운로드할 원격 파일 경로를 입력하세요: ")
            local_path = input("다운로드할 로컬 파일 경로를 입력하세요: ")
            download_file_from_remote(client, remote_path, local_path)
        elif command == "종료":
            break
        else:
            print("잘못된 명령어입니다. 다시 시도하세요.")

    close_ssh_connection(client)

b_is_exit = False
version = "1.0.0"
print(f"프로그램 버전: {version}")

bookmark_list = []

while not b_is_exit:

    func = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
    

    if func == "파일편집":
        print("파일 편집 기능 실행")
        FileEdit.file_edit()

    elif func == "즐겨찾기":
        print("즐겨찾기 기능 실행.")
        Bookmark.bookmark(bookmark_list)

    elif func == "파일관리":
        print("파일 관리 기능 실행")
        FileControl.file_control()

    elif func == "가독성":
        print("가독성 기능 실행")
        Readable.readable()

    elif func == "중복관리":
        print("중복 관리 기능 실행")
        Duplicates.duplicates()

    elif func == "Check":
        print("파일 무결성 검사 기능 실행")
        sub_func = input("원하는 무결성 검사 기능을 입력하세요 ('저장', '검증'): ")

        if sub_func == "저장":
            file_path = input("해시 값을 저장할 파일의 경로를 입력하세요: ")
            hash_file_path = file_path + '.hash'
            save_hash(file_path, hash_file_path)

        elif sub_func == "검증":
            verify_file_path = input("무결성을 검증할 파일의 경로를 입력하세요: ")
            verify_hash_file_path = verify_file_path + '.hash'
            verify_file_integrity(verify_file_path, verify_hash_file_path)
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

    elif func == "Remote":
        print("원격 파일 관리 기능 실행")
        remote_file_management()

    elif func == "?":
        print("""
                [도움말]
                '파일편집' 입력시 파일을 편집할 수 있습니다.
                '즐겨찾기' 입력시 즐겨찾기 기능을 사용할 수 있습니다.
                '파일관리' 입력시 파일을 관리할 수 있습니다.
                '가독성'   입력시 파일의 단위를 읽기 좋게 볼 수 있습니다.
                '중복관리' 입력시 중복 파일을 관리할 수 있습니다.
                'Check'   입력시 파일의 무결성을 검사할 수 있습니다.
                'Remote'  입력시 원격 서버의 파일을 관리할 수 있습니다.
                '종료'     입력시 프로그램을 종료합니다.
            """)

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요. : ")