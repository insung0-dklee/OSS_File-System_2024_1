"""
현재 경로에 특정 파일이나 디렉토리가 존재하는지를 확인하기 위해 import os를 사용
파일을 이동이나 복사하기 위해 shutil 모듈을 사용하였음
파일 탐색기에서의 잘라내기 기능을 구현함
cut_file 함수는 잘라낼 파일의 경로와 붙여넣을 경로를 매개변수로 함
이때 붙여넣을 경로에 입력이 잘못됐을 경우 에러를 발생시킴

b_is_exit 변수를 0으로 초기화하고
1을 입력하였을때 잘라내기 기능이 구현되도록 함수를 작성하였음

"""
import os
import shutil
def cut_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"{source} 파일이 {destination}으로 잘라내기 되었습니다.")
    except Exception as e:
        print(f"파일을 이동하는 중 오류가 발생했습니다: {e}")

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력: ")

    if func == "1":
        source = input("잘라낼 파일의 경로를 입력하세요: ")
        destination = input("붙여넣을 경로를 입력하세요: ")
        cut_file(source, destination)
        print("잘라내기 완료")
        break
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        b_is_exit = not b_is_exit



"""
파일이름 변경 함수 renameFile 설명

매개변수는 없음.

이름을 변경할 파일의 경로와 새로운 파일이름을 입력받음.

입력받은 파일경로의 부모 디렉토리를 getParentDir함수로 구해서 새로운 파일 경로를 생성함.
os.rename함수로 파일 이름을 변경함.

성공 시, 기존경로, 바뀐경로를 출력함.
실패 시, 에러 메시지 출력함.
"""
def renameFile():
    try:
        srcPath = input("이름을 변경할 파일의 경로 입력: ")
        newName = input("새로운 파일이름 입력: ")
        parentDir = getParentDir(srcPath)
        newPath = os.path.join(parentDir, newName)
        os.rename(srcPath, newPath)
        print("기존경로: ", srcPath, " 바뀐경로: ", newPath, " 변경완료!")
    except Exception as e:
        print("파일이름 변경 중 에러발생", e)


"""
기능을 선택할 수 있음

1 입력 시, 파일 이름 변경
0 입력 시, 프로그램 종료

잘못된 입력은 다시 입력하도록 함

추가기능 구현 시, 조건문 추가
"""
if __name__ == "__main__":
    while True:
        print("--------------------------------")
        print("기능 선택")
        print("--------------------------------")
        print("1. 파일이름 변경")
        print("0. 종료")

        select = input("입력 (0번 입력시, 종료): ")
        print("\n")


        if select == '1':
            renameFile()
            
        
        elif select == '0':
            print("종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
        



