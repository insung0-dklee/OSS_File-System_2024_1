import os
import re

def file_namer():
    """
    현재 작업 디렉토리의 파일 이름을 사용자가 지정한 순서대로 번호를 매겨 변경합니다.
    """
    # 현재 작업 디렉토리의 파일 목록 출력
    files = os.listdir('.')
    print("현재 폴더의 파일 목록:\n")
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")

    # 사용자 입력 처리
    try:
        index_list = parse_user_input(input("변경할 파일들의 번호를 변경하고 싶은 순서대로, 공백 문자 혹은 -로 구분해 입력하세요 (ex: 1 3-20 21 22): "))
    except ValueError as e:
        print(e)
        return

    # 파일 목록 저장 후 사용자에게 목록 출력
    rename_list = [files[index-1] for index in index_list if index <= len(files)]
    print("변경할 파일들은 아래와 같습니다.")
    for file in rename_list:
        print(file)

    # 변경할 파일의 새로운 이름 입력
    new_filename = input("설정할 파일 이름을 입력하세요. 실행 취소하려면 \"-1\"를 입력해주세요: ")
    if new_filename == "-1":
        print("실행 취소되었습니다.")
        return

    # 파일명 변경
    rename_files(rename_list, new_filename)

def parse_user_input(input_str):
    """
    사용자 입력을 파싱하여 파일 인덱스 목록을 반환합니다.
    """
    index_list = []
    for x in input_str.split():
        if '-' in x:
            start, end = map(int, x.split('-'))
            index_list.extend(range(start, end+1))
        else:
            index_list.append(int(x))

    if len(index_list) != len(set(index_list)):
        raise ValueError("입력된 파일 목록이 중복되었습니다.")

    return index_list

def rename_files(files, new_filename):
    """
    주어진 파일 목록의 이름을 새 이름으로 변경합니다.
    """
    for i, file in enumerate(files, start=1):
        _, file_extension = os.path.splitext(file)
        new_name = f"{new_filename}_{str(i).zfill(3)}{file_extension}"

        try:
            os.rename(file, new_name)
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file}")
            break
        except FileExistsError:
            print(f"동일한 이름의 파일이 이미 존재합니다: {new_name}")
            break
    else:
        print("모든 파일이 성공적으로 변경되었습니다.")

if __name__ == "__main__":
    file_namer()