
import os
import shutil

def getParentDir(path):
    return os.path.dirname(path)

def file_error(e, func):
    """
    파일 열람 시 발생할 수 있는 에러에 관한 메세지를 송출

    Parameters - 
    e (Exception): 발생한 예외 상황(오류)
    func (str): 현재 실행하고 있는 기능의 이름
    """
    if isinstance(e, FileNotFoundError):
        print(f"Error: 파일이 존재하지 않거나 파일의 경로가 잘못되었습니다.")
    elif isinstance(e, PermissionError):
        print(f"Error: {func} 기능을 수행할 수 있는 권한이 없습니다.")
    elif isinstance(e, IsADirectoryError):
        print(f"Error: 입력된 파일이 경로입니다.")
    elif isinstance(e, OSError):
        print(f"Error: 운영체제 관련 오류입니다. 파일 시스템이 가득 찼거나, 파일 이름이 유효하지 않거나, 디스크 오류가 있지는 않은지 확인하시길 바랍니다.")
    else:
        print(f"{func} 기능을 수행하는 중 기타 오류가 발생하였습니다. : {e}")

def copyFile(src, dest):
    """
    특정 파일(src)을 dest의 위치로 복사.

    parameters -
    src : 복사할 파일의 경로.
    dest : 복사시킬 위치의 경로.
    -- 두 경로 모두 상대경로와 절대경로 모두 설정 가능하다.
    """
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        file_error(e, "복사")

def moveFile(src, dest):
    """
    특정 파일(src)를 dest의 위치로 이동.

    parameters -
    src : 이동할 파일의 경로.
    dest : 이동시킬 위치의 경로.
    -- 두 경로 모두 상대경로와 절대경로 모두 설정 가능하다.
    """
    try:
        shutil.move(src,dest)
        print(f"파일이 {dest}로 이동되었습니다.")
    except Exception as e:
        file_error(e, "이동")

def rename_file(old_name, new_name):
    """
    파일의 이름을 old_name에서 new_name으로 변경.

    Parameters -
    old_name (str): 이름을 변경할 파일의 경로
    new_name (str): 변경시킬 이름으로 수정한 파일의 경로
    --동일한 위치 내에서 작성해야 제대로 동작함.
        ex) old_name : C:\a.txt
            new_name : C:\b.txt
    """
    try:
        shutil.move(old_name, new_name)
        print(f"{old_name}이 {new_name}으로 변경되었습니다.")
    except Exception as e:
        file_error(e, "복사")

        
## 새 기능을 추가할 때마다 리스트에 등록합니다.
## 도움말을 불러올 경우 기능 리스트가 출력됩니다.
func_list = ["복사", "이동", "이름변경"]

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("기능 1 실행.")
        # Add functionality for option 1 here

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

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")