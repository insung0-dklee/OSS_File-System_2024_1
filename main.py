
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
from functools import lru_cache
import getpass
from Control import Bookmark
from Control import FileEdit
from Control import FileControl
from Control import Duplicates
from Control import Readable
from Control.FileControl import search_file

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

b_is_exit = False

while not b_is_exit:

    func = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
    bookmark_list = []

    if func == "파일 편집":
        print("파일 편집 기능 실행")
        FileEdit.file_edit()

    elif func == "즐겨찾기":
        print("즐겨찾기 기능 실행.")
        Bookmark.bookmark(bookmark_list)

    elif func == "파일 관리":
        print("파일 관리 기능 실행")
        FileControl.file_control()

    elif func == "가독성":
        print("가독성 기능 실행")
        Readable.readable()

    elif func == "중복관리":
        print("중복 관리 기능 실행")
        Duplicates.duplicates()

    elif func == "트리출력":
        print("트리 출력 기능 실행")
        root_dir = input("트리를 출력할 루트 디렉토리 경로를 입력하세요: ")
        if os.path.exists(root_dir) and os.path.isdir(root_dir):
            print(root_dir)
            print_directory_tree(root_dir)
        else:
            print("유효한 디렉토리 경로가 아닙니다.")

    elif func == "?":
        print("""
                [도움말]
                '파일편집' 입력시 파일을 편집할 수 있습니다.
                '즐겨찾기' 입력시 즐겨찾기 기능을 사용할 수 있습니다.
                '파일관리' 입력시 파일을 관리할 수 있습니다.
                '가독성'   입력시 파일의 단위를 읽기 좋게 볼 수 있습니다.
                '중복관리' 입력시 중복 파일을 관리할 수 있습니다.
                '트리출력' 입력시 디렉토리 구조를 트리 형태로 출력합니다.
                '종료'     입력시 프로그램을 종료합니다.
            """)

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요. : ")