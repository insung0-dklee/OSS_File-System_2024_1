import os
import shutil
import zipfile

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")


"""
1번 기능: 압축해제 기능 구현 (ZipOff 함수)
WhereIsZip == 압축해제할 .zip파일의 위치경로
WherePutIt == 압축해제 완료된 파일을 어디에 저장할지 정하는 경로
압축해제 하기를 원하는 .zip 파일의 위치경로를 입력받습니다.(WhereIsZip)
압축해제 완료된 파일을 어디 경로에 저장할 것인지 사용자가 입력할 수 있습니다.(WherePutIt)
만약 WhereIsZip을 통해 지정한 파일이 .zip 파일이 아닌 경우에는 오류가 발생할 수 있습니다.
"""
def ZipOff(WhereIsZip, WherePutIt):
    try:
        with zipfile.ZipFile(WhereIsZip, 'r') as zip_ref:
            zip_ref.extractall(WherePutIt)
            print(f"압축 해제 완료.")
    except Exception as e:
        print(f"압축 해제 중 오류가 발생.")


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

    elif func == "압축해제":
        WhereIsIt = input("압축해제할 압축파일의 경로 입력 (.zip까지 붙여주세요): ")
        WherePutIt = input("압축해제된 파일을 둘 경로를 입력: ")
        ZipOff(WhereIsIt, WherePutIt)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")