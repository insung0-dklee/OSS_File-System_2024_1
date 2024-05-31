
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
import json

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

def search_file_content(root_directory, keyword, extensions=None):
    """
    특정 키워드가 포함된 파일을 검색하는 함수입니다.
    @param
        root_directory: 검색을 시작할 루트 디렉토리
        keyword: 검색할 키워드
        extensions: 검색할 파일 확장자 리스트 (예: ['.txt', '.md'])
    @return
        키워드가 포함된 파일의 경로 리스트
    """
    if not keyword:
        print("검색할 키워드가 입력되지 않았습니다.")
        return []
    
    if extensions is None or not extensions:
        extensions = ['.txt', '.md', '.py', '.json']  # 기본 검색 파일 확장자 목록
    
    matched_files = []

    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_extension = os.path.splitext(filename)[1]
            if file_extension in extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if keyword in content:
                            matched_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")  # 파일을 읽을 수 없는 경우 예외 출력

    return matched_files

def preview_file(file_path, num_lines=3):
    """
    주어진 파일의 첫 num_lines 줄을 미리보기 합니다.
    
    @Args
        file_path(str): 미리보기 할 파일의 경로
        num_lines(int): 미리보기 할 줄 수 (기본값은 3줄)
    
    @Returns
        파일의 첫 num_lines줄
    """
    if not os.path.isfile(file_path):
        return f"{file_path} 파일이 존재하지 않습니다."
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [file.readline() for _ in range(num_lines)]
        return ''.join(lines)
    except Exception as e:
        return f"파일을 읽는 중 오류가 발생했습니다: {e}"

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

TAG_FILE = 'tags.json' # 설정한 태그가 저장될 파일

def load_tags():
    """
    태그 파일(tags.json)을 로드하여 태그 데이터를 반환
    파일이 존재하지 않거나 JSONDecodeError가 발생하면 빈 딕셔너리를 반환

    @Returns
        파일 경로를 키로 하고 태그 리스트를 값으로 하는 딕셔너리
    """
    if os.path.exists(TAG_FILE):
        try:
            with open(TAG_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

def save_tags(tags):
    """
    태그 데이터를 태그 파일(tags.json)에 저장

    @Args
        tags: 파일 경로를 키로 하고 태그 리스트를 값으로 하는 딕셔너리
    """
    with open(TAG_FILE, 'w') as file:
        json.dump(tags, file, indent=4)

def add_tag(file_path, tag):
    """
    주어진 파일 경로에 태그를 추가하고한다. 태그 파일에 해당 경로가 없으면 새로 추가

    @Args
        file_path: 태그를 추가할 파일 경로
        tag: 추가할 태그
    """
    tags = load_tags()
    if file_path in tags:
        if tag not in tags[file_path]:
            tags[file_path].append(tag)
    else:
        tags[file_path] = [tag]
    save_tags(tags)
    print(f"Tag '{tag}' added to file '{file_path}'.")

def remove_tag(file_path, tag):
    """
    주어진 파일 경로에서 태그를 제거한다. 태그가 제거된 후 파일에 더 이상 태그가 없으면 경로를 삭제

    @Args
        file_path: 태그를 제거할 파일 경로
        tag: 제거할 태그
    """
    tags = load_tags()
    if file_path in tags and tag in tags[file_path]:
        tags[file_path].remove(tag)
        if not tags[file_path]:
            del tags[file_path]
        save_tags(tags)
        print(f"Tag '{tag}' removed from file '{file_path}'.")
    else:
        print(f"Tag '{tag}' not found in file '{file_path}'.")

def search_by_tag(tag):
    """
    주어진 태그를 가진 파일 경로를 검색하여 반환

    @Args
        tag: 검색할 태그

    @Returns
        list: 태그를 가진 파일 경로 리스트
    """
    tags = load_tags()
    matched_files = [file for file, tags in tags.items() if tag in tags]
    return matched_files

def list_tags(file_path):
    """
    주어진 파일 경로에 부여된 태그 리스트를 반환

    @Args
        file_path: 태그를 확인할 파일 경로

    @Returns
        list: 파일 경로에 부여된 태그 리스트(태그가 없으면 빈 리스트 반환)
    """
    tags = load_tags()
    return tags.get(file_path, [])

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

    elif func == "검색":
        try:
            print("지원하는 파일 확장자는 .txt, .md, .py, .json 입니다.")
            root_directory = input("검색을 시작할 루트 디렉토리를 입력하세요: ")
            keyword = input("검색할 키워드를 입력하세요: ").strip()
            extensions_input = input("전체를 검색하고 싶다면 공백을 입력하고, 검색할 파일 확장자를 쉼표로 구분하여 입력하세요(예: .txt,.md,.py,.json): ").strip()
            extensions = [ext.strip() for ext in extensions_input.split(',')] if extensions_input else ['.txt', '.md', '.py', '.json']
            
            # 지원되는 확장자인지 확인
            supported_extensions = ['.txt', '.md', '.py', '.json']
            if any(ext not in supported_extensions for ext in extensions):
                print(f"지원되지 않는 파일 확장자가 포함되어 있습니다. 지원되는 확장자는 {', '.join(supported_extensions)} 입니다.")
                continue
            
            matched_files = search_file_content(root_directory, keyword, extensions)
            if matched_files:
                print("키워드가 포함된 파일 목록:")
                for file in matched_files:
                    print(file)
            else:
                print("키워드가 포함된 파일을 찾을 수 없습니다.")
        except Exception as e:
            print(f"검색 중 오류가 발생했습니다: {e}")

    elif func == "미리보기":
        print("미리보기는 .txt, .md, .py, .json 파일만 지원 가능합니다.")
        file_path = input("미리보기할 파일의 경로를 입력하세요: ")
        num_lines = int(input("미리보기할 줄 수를 입력하세요(기본값은 3줄): ") or 3)
        preview = preview_file(file_path, num_lines)
        print(f"파일 미리보기:\n{preview}")

    elif func == "태그 추가":
        file_path = input("태그를 추가할 파일 경로를 입력하세요: ")
        tag = input("추가할 태그를 입력하세요: ")
        add_tag(file_path, tag)

    elif func == "태그 제거":
        file_path = input("태그를 제거할 파일 경로를 입력하세요: ")
        tag = input("제거할 태그를 입력하세요: ")
        remove_tag(file_path, tag)

    elif func == "태그 검색":
        tag = input("검색할 태그를 입력하세요: ")
        matched_files = search_by_tag(tag)
        if matched_files:
            print("태그가 포함된 파일 목록:")
            for file in matched_files:
                print(file)
        else:
            print("해당 태그가 포함된 파일을 찾을 수 없습니다.")

    elif func == "태그 목록":
        file_path = input("태그 목록을 볼 파일 경로를 입력하세요: ")
        tags = list_tags(file_path)
        if tags:
            print(f"파일 '{file_path}'의 태그 목록:")
            for tag in tags:
                print(tag)
        else:
            print("파일에 태그가 없습니다.")

    elif func == "?":
        print("도움말: 1을 입력하여 잘라내기(이동)하거나 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")