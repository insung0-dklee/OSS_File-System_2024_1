import os
from create_directory import create_directory
from list_directory_contents import list_directory_contents
from delete_file_or_directory import delete_file_or_directory

def display_menu():
    print("1. 디렉토리 생성")
    print("2. 디렉토리 내용물 확인")
    print("3. 파일 또는 디렉토리 삭제")
    print("4. 종료")

def main():
    while True:
        display_menu()
        choice = input("선택할 기능을 입력하세요: ")

        if choice == "1":
            dir_name = input("생성할 디렉토리 이름을 입력하세요: ")
            create_directory(dir_name)

        elif choice == "2":
            dir_path = input("내용물을 확인할 디렉토리 경로를 입력하세요 (비워두면 현재 디렉토리): ")
            list_directory_contents(dir_path)

        elif choice == "3":
            path = input("삭제할 파일 또는 디렉토리 경로를 입력하세요: ")
            delete_file_or_directory(path)

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()