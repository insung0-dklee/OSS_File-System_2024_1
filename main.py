import ctypes
import os
import shutil

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")




"""
toggle_hidden(file_path)

파일을 숨김상태로 설정하거나, 숨김상태를 해제 합니다.

@Param

    file_path : 숨김 상태를 바꾸고 싶은 경로 
                 
    state : | 0 => 숨김 해제 | 1 => 숨김 |

@exception

    숨김 속성을 변경하는 중 오류 발생시 ctypes.WinError() 예외를 발생시킴.

@Return

    none

"""
# SetFileAttributesW 함수의 인자 값 설정
FILE_ATTRIBUTE_HIDDEN = 0x02

def toggle_hidden(file_path):

    if not os.path.exists(file_path):
        print(f"{file_path}가 경로에 없습니다.")
        return

    state = input("숨김 상태를 입력하세요(0=숨김 해제 | 1=숨김) : ")
    
    if state == '1': # hide true
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN)
        if ret:
            print(f"{file_path} 상태 : Hidden")
        else:
            raise ctypes.WinError()
    elif state == '0':  # hide false
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN ^ FILE_ATTRIBUTE_HIDDEN)
        if ret:
            print(f"{file_path} : Dissable Hidden")
        else:
            raise ctypes.WinError()

        

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

    elif func == "숨김설정":
        file_fath=input("경로를 입력하세요 : ")
        toggle_hidden(file_fath)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
