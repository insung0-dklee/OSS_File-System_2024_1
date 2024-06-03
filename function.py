# flake8: noqa
import os, re, shutil
import winreg

"""
파일 이름 일괄 변경 코드
작성자 : 권혁준
학번 : 22311905
일자 : 2024-05-30
기능 : 여러 개의 파일을 선택해, 해당 파일의 이름을 번호 순으로 바꾸는 코드
      (000, 001, 002 ...)
"""

def fileNamer():
    # 현재 작업 디렉토리의 파일 목록 출력
    files = os.listdir('.')
    print("현재 폴더의 파일 목록:\n")
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")

    # 이름을 변경할 파일의 번호 저장
    indexList = []
    for x in input("""변경할 파일들의 번호를 변경하고 싶은 순서대로, 공백 문자 혹은 -로 구분해 입력 
                      (ex: 1 3-20 21 22): """).split():
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

"""
디렉토리 경로를 반환, 디렉토리 경로를 입력받아 이동하는 함수
작성자 : 권혁준
학번 : 22311905
일자 : 2024-05-31
기능 : 디렉토리 경로를 입력받아 이동을 시도하고, 실패하면 오류 출력
       현재 디렉토리 경로를 반환
"""


# 디렉토리 경로를 이동하는 함수
def moveDir(path):
    try:
        os.chdir(path)
        return os.listdir('.'), path
    except:
        print(f"경로가 존재하지 않거나, 폴더가 아니거나, 권한이 없습니다.")

# 현재 디렉토리의 경로를 반환하는 함수
def currentDir():
    return os.getcwd()

"""
디렉토리 경로가 이동 가능한지 확인하는 함수
작성자 : 권혁준
학번 : 22311905
일자 : 2024-05-31
기능 : 선택된 파일의 경로가 이동 가능한 경로인지 확인하고, 
       이동 가능하면 경로를, 아니라면 False를 반환
"""

# 리스트 위젯을 더블클릭했을 때 호출
# 선택한 경로로 이동을 시도하고, 이동이 되지 않는 경우 False를 반환
def moveSelected(selected):
    selected_path = os.path.join(os.getcwd(), selected)
    try:
        if os.path.isdir(selected_path):
            return selected_path
        else:
            return False
    except:
        return False
    
"""
확장자의 기본 응용 프로그램이 설정되어 있는지 확인하는 함수
작성자 : 권혁준
학번 : 22311905
일자 : 2024-06-01
기능 : 기본 응용 프로그램이 설정되어 있으면 해당 프로그램을 반환하고,
       아니면 None을 반환한다.
"""

def get_default_program(extension):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\." + extension + r"\OpenWithList") as key:
            value, _ = winreg.QueryValueEx(key, "MRUList")
            return winreg.QueryValueEx(key, value[0])[0]
    except FileNotFoundError:
        return None
    
"""
예외처리가 이루어진 복사, 삭제하는 함수
작성자 : 권혁준
학번 : 22311905
일자 : 2024-06-03
기능 : 예외처리를 해당 함수에서 수행해서 복사, 삭제한다.
"""

def copyFile(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"소스 파일이 존재하지 않습니다: {src_path}")

    if not os.path.exists(os.path.dirname(dest_path)):
        print(f"대상 디렉토리가 존재하지 않습니다: {os.path.dirname(dest_path)}")

    try:
        shutil.copy(src_path, dest_path)
        print(f"파일이 복사되었습니다")
    except:
        print(f"예상치 못한 오류가 발생했습니다.")

def delFile(src_path):
    if not os.path.exists(src_path):
        print(f"소스 파일이 존재하지 않습니다: {src_path}")

    try:
        os.remove(src_path)
        print(f"파일이 삭제되었습니다")
    except:
        print(f"예상치 못한 오류가 발생했습니다.")