
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

"""상위 파일 하나를 만들고, 그 파일에 만들고자 하는 파일을 바로 만들 수 있는 프로그램입니다.
즉, 하나의 폴더 안에 여러 파일을 생성할 수 있는 장점이 있습니다."""
"""
    main_file = input('상위 폴더의 폴더명을 적으시오: ')     -> 여러 파일을 모아둘 하나의 파일명을 정하도록 하였습니다.
    main = [] #하위 폴더들의 주소를 저장할 배열              -> 하위 폴더들의 주소를 하나씩 저장하고 후에 한번에 출력하도록 하기 위하여 main 배열을 만들었습니다.
    main_path = os.path.join(os.getcwd(), main_file)   -> 여러 경로를 하나의 주소로 붙여주는 os.path.join 을 사용한 것입니다. os.getcwd()는 현재 작업하고 있는 파일 주소를 불러올 때 사용되며, 
                                                        main_file을 os.getcwd()에 붙여줌으로써 현재 작업하고 있는 파일에 상위 폴더를 만들어주었습니다.
    num = int(input("만들 하위파일들의 개수를 적으시오: "))   -> 사용자가 원하는만큼 파일 개수를 만들 수 있도록 num이라는 변수에 입력을 받고 후에 입력받은 수만큼 for문을 반복하도록 하였습니다.
    print("만들 하위파일들의 이름을 적으시오: ")              -> 하위 파일들의 이름을 적으라고 사용자에게 알려주기 위해 작성하였습니다.
    for i in range(0, num):                             -> 입력받은 num번만큼 반복하도록 for문을 작성하였습니다.
        path = input()                                  -> path 변수는 하위 폴더들의 이름을 받기 위해 사용하였습니다. input()을 사용하여 사용자가 직접 파일 명을 정할 수 있습니다.
        fin_path=os.path.join(main_path,path)           -> fin_path변수는 최종 하위 폴더의 경로를 나타내며 main_path와 입력받은 하위 폴더의 path를 합쳐 나타냈습니다.
        os.makedirs(fin_path, exist_ok=True)      -> 새로운 폴더를 만드는 함수인 os.makedirs을 사용하였습니다. exist_ok=True는 이미 동일한 폴더가 존재하더라도 에러 없이 넘어갈 수 있습니다.
        main.append(fin_path)                          -> main 배열에 주소 스트링값을 추가해주는 작업입니다.
    print("모아진 폴더들의 주소입니다")                     -> 하위 폴더들의 주소를 나타내준다는 뜻을 사용자에게 알리기 위해 작성하였습니다.
    for i in range(0, num):                            -> main 배열에 num번만큼 값이 저장됐으므로 num번만큼 반복되도록 for문을 사용하였습니다.
        print(main[i])                                  -> 배열의 값 0부터 num번까지 출력하도록 사용하였습니다.
"""

def createFile():
    main_file = input('상위 폴더의 폴더명을 적으시오: ')
    main = []
    main_path = os.path.join(os.getcwd(), main_file)
    print(main_path)
    num = int(input("만들 하위파일들의 개수를 적으시오: "))
    print("만들 하위파일들의 이름을 적으시오: ")
    for i in range(0, num):
        path = input()
        fin_path=os.path.join(main_path,path)
        os.makedirs(fin_path, exist_ok=True)
        main.append(fin_path)
    print("모아진 폴더들의 주소입니다")
    for i in range(0, num):
        print(main[i])