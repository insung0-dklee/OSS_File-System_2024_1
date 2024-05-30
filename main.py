import os

def getParentDir(path):
    return os.path.dirname(path)


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
        



