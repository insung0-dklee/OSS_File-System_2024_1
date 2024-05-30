from glob import glob
import os
#경로를 통해 파일을 찾아내는 glob 사용
path = "file/path/"  # 변경하고싶은 파일이 들어있는 경로를 복사해서 붙여넣기
files = glob(os.path.join(path, '*'))

for i, f in enumerate(files):
    #인덱스와 요소를 차례로 반복하게 해주는 함수인 enumerate()를 이용해 파일에 접근

    new_f = os.path.join(path,
                         f'img_{i}{os.path.splitext(f)[1]}')  #파일 이름을 한번에 바꿈

    if not os.path.exists(new_f):  # 새 파일명이 이미 존재하지 않는 경우에만 변경
        try:
            os.rename(f, new_f)
            print("{f} -> {new_f}")
        except Exception:
            print("에러가 존재합니다. 파일명을 고치세요.")
    else:
        print("File {new_f}이 이미 존재합니다.")

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