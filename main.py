
import os
import shutil
import difflib # Diff 함수를 위한 모듈

"""
printFileDiff : 두 파일을 비교하고 그 결과를 출력하는 기능
fromfile, tofile : diff 출력에 사용될 파일 이름
"""
def printFileDiff(file1, file2):
    if not os.path.exists(file1): #파일이 존재하는지 판별
        print(f"'{file1}' 파일이 존재하지 않습니다.")
        return
    if not os.path.exists(file2):
        print(f"'{file2}' 파일이 존재하지 않습니다.")
        return
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            diff = difflib.unified_diff(
                f1.readlines(), f2.readlines(),
                fromfile=file1, tofile=file2,
            ) #두 파일을 읽어 각각 변수 f1, f2에 저장하고 이를 비교
            for line in diff:
                print(line) #비교한 결과를 출력
    except Exception as e:
        print(f"파일을 읽는 중 오류가 발생했습니다: {e}")

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

    elif func == "문서비교":
        file1 = input("비교할 첫번째 파일의 경로를 입력하세요: ")
        file2 = input("비교할 두번째 파일의 경로를 입력하세요: ")
        printFileDiff(file1, file2)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")