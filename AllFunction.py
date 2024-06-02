import os
import re
import zipfile
import time
import zipfile
import getpass
import matplotlib.pyplot as plt
from PIL import Image
from Control.FileControl import search_file

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


def compress_file(file_path):
    """
    사용자가 파일경로를 입력하면 해당파일을 zip으로 압축합니다.
    
    매개변수 file_path (str): 압축할 파일의 경로
    """
    try:
        file_dir = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
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

def preview_image(file_path):
    """
    이미지 파일을 미리보기합니다.
    
    매개변수 file_path (str): 미리보기할 이미지 파일의 경로
    """
    try:
        with Image.open(file_path) as img:
            plt.imshow(img)
            plt.axis('off')
            plt.show()
    except Exception as e:
        print(f"이미지 미리보기 중 오류가 발생했습니다: {e}")

def preview_text(file_path, num_lines=5):
    """
    텍스트 파일의 처음 몇 줄을 미리보기합니다.
    
    매개변수 file_path (str): 미리보기할 텍스트 파일의 경로
    매개변수 num_lines (int): 미리볼 줄 수, 기본값은 5줄
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [next(file) for _ in range(num_lines)]
        for line in lines:
            print(line, end='')
    except Exception as e:
        print(f"텍스트 미리보기 중 오류가 발생했습니다: {e}")


def search_files(directory, name_pattern, use_regex=False):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if use_regex:
                if re.match(name_pattern, file):
                    found_files.append(os.path.join(root, file))
            else:
                if file == name_pattern:
                    found_files.append(os.path.join(root, file))
    return found_files
"""
파일 이름 일괄 변경 코드
작성자 : 권혁준
학번 : 22311905
일자 : 2024-05-30
기능 : 여러 개의 파일을 선택해, 해당 파일의 이름을 번호 순으로 바꾸는 코드 (000, 001, 002 ...)
"""

def fileNamer():
    # 현재 작업 디렉토리의 파일 목록 출력
    files = os.listdir('.')
    print("현재 폴더의 파일 목록:\n")
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")

    # 이름을 변경할 파일의 번호 저장
    indexList = []
    for x in input("""변경할 파일들의 번호를 변경하고 싶은 순서대로, 공백 문자 혹은 -로 구분해 입력 (ex: 1 3-20 21 22): """).split():
        if re.match(r'^\d+$|^\d+-\d+$', x):  # 숫자 또는 숫자-숫자 형식의 입력 검증
            if '-' in x:
                start, end = x.split('-')
                indexList.extend([x for x in range(int(start), int(end)+1)])
            else:
                indexList.append(int(x))
        else:
            print("입력된 파일 번호가 문자이거나 정상적이지 않습니다.")
            return

    # 인덱스 중복 검증
    if len(indexList) != len(set(indexList)):
        print("입력된 파일 목록이 중복되었습니다.")
        return

    # 파일 목록 저장 후 사용자에게 목록 출력
    renameList = [files[index-1] for index in indexList]
    print("변경할 파일들은 아래와 같습니다.")
    for x in renameList:
        print(x)

    # 변경할 파일의 새로운 이름을 입력
    # -1을 입력하여 중단할 수 있음
    print("""파일 이름을 입력하면 (입력한 파일명)_001 부터 차례대로 이름이 변경됩니다.
            실행 취소하려면 \"-1\"를 입력해주세요.
            파일이 변경 도중 중복되거나 존재하지 않을 경우 중단됩니다.""")
    new_filename = input("설정할 파일 이름을 입력: ")
    if new_filename == "-1":
        print("실행 취소되었습니다.")
        return

    # 파일명 변경
    try:
        for rename in range(len(renameList)):
            _, file_extension = os.path.splitext(renameList[rename])  # 파일 확장자 분리
            new_name = f"{new_filename}_{str(rename+1).rjust(3, '0')}{file_extension}"
            os.rename(renameList[rename], new_name)
        print("파일이 성공적으로 변경되었습니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없거나 실행 도중 파일이 변경되었습니다.")
    except FileExistsError:
        print("동일한 이름의 파일이 이미 존재합니다.")