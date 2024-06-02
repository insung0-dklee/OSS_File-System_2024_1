'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
3. 파일 비교
'''

import os
from pathlib import Path

def file_edit():
    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print("""   
    '읽기'      입력시 해당 파일의 내용을 출력")
    '파일생성'  입력시 파일을 생성하고 원하는 내용을 작성")
    '종료'      입력시 프로그램을 종료할 수 있습니다.
                """)

        elif select == "읽기":
            read_file()
        elif select == "파일생성":
            create_and_write_file()
        elif select == "파일비교":
            compare_files()
        elif select == '종료':
            print('파일 편집 기능을 종료합니다.')
            finish = True
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


def read_file():
    while True:
        file_path = input("읽고 싶은 파일의 경로를 입력하세요. : ")
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다. 올바른 경로를 입력하세요.")
        except IOError:
            print("파일을 열 수 없습니다. 다시 시도하세요.")
        except UnicodeDecodeError:  # 인코딩 관련 오류 처리
            print("파일을 읽을 수 없습니다. 다시 입력해주세요.")

def create_and_write_file():
    file_path = input("파일을 생성하고 싶은 디렉토리의 경로를 입력하세요. : ")
    content = input("쓰고 싶은 문장을 입력하세요. : ")
    with open(file_path, 'w') as file:
        file.write(content)

def compare_files():
    """
    두 텍스트 파일을 비교하여 차이점을 출력합니다.
    
    @param
        file1_path: 첫 번째 파일 경로
        file2_path: 두 번째 파일 경로
    """
    file1_path = input('첫 번째 파일 경로 : ')
    file2_path = input('두 번째 파일 경로 : ')

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

def create_symlink(target, link_name):
    '''
    심볼릭 링크를 만드는 함수
    target : 심볼릭 링크를 만들 파일 경로
    link_name : 링크 이름
    '''
    os.symlink(target, link_name)

def is_symlink(path):
    '''
    해당 파일이 심볼릭 링크인지 확인하는 함수
    path : 확인할 파일의 경로
    '''
    return os.path.islink(path)

def create_hardlink(target, link_name):
    '''
    하드 링크를 만드는 함수
    target : 하드 링크를 만들 파일 경로
    link_name : 링크 이름
    '''
    os.link(target, link_name)

def is_hardlink(path):
    """
    입력한 파일이 하드 링크인지 확인하는 함수
    하드 링크 여부는 직접적으로 확인하기 어렵지만, os.stat()으로 inode 번호를 통해 확인 가능하다.
    path : 확인할 파일의 경로
    """
    try:
        stat_info = os.stat(path)
        return stat_info.st_nlink > 1
    except FileNotFoundError:
        return False
    
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