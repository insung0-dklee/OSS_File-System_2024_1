import os
import re

"""
파일 이름 일괄 변경 코드
작성자 : 권혁준
학번 : 22311905
일자 : 2024-05-30
기능 : 여러 개의 파일을 선택해, 해당 파일의 이름을 번호 순으로 바꾸는 코드
      (000, 001, 002 ...)
"""

def file_namer():
    # 현재 작업 디렉토리의 파일 목록 출력
    files = os.listdir('.')
    print("현재 폴더의 파일 목록:\n")
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")

    # 이름을 변경할 파일의 번호 저장
    index_list = []
    input_string = input(
        """변경할 파일들의 번호를 변경하고 싶은 순서대로, 공백 문자 혹은 -로 구분해 입력 
        (ex: 1 3-20 21 22): """
    ).split()

    for x in input_string:
        if re.match(r'^\d+$|^\d+-\d+$', x):  # 숫자 또는 숫자-숫자 형식의 입력 검증
            if '-' in x:
                start, end = map(int, x.split('-'))
                if start > end:
                    print(f"잘못된 범위: {x}")
                    return
                index_list.extend(range(start, end + 1))
            else:
                index_list.append(int(x))
        else:
            print("입력된 파일 번호가 문자이거나 정상적이지 않습니다.")
            return

    # 인덱스 중복 검증
    if len(index_list) != len(set(index_list)):
        print("입력된 파일 목록이 중복되었습니다.")
        return

    # 파일 목록 저장 후 사용자에게 목록 출력
    rename_list = [files[index-1] for index in index_list]
    print("변경할 파일들은 아래와 같습니다.")
    for x in rename_list:
        print(x)

    # 변경할 파일의 새로운 이름을 입력
    print("""파일 이름을 입력하면 (입력한 파일명)_001 부터 차례대로 이름이 변경됩니다.
          실행 취소하려면 \"-1\"를 입력해주세요.
          파일이 변경 도중 중복되거나 존재하지 않을 경우 중단됩니다.""")
    new_filename = input("설정할 파일 이름을 입력: ")
    if new_filename == "-1":
        print("실행 취소되었습니다.")
        return

    # 파일명 변경
    try:
        for rename in range(len(rename_list)):
            _, file_extension = os.path.splitext(rename_list[rename])  # 파일 확장자 분리
            new_name = f"{new_filename}_{str(rename+1).rjust(3, '0')}{file_extension}"
            os.rename(renameList[rename], new_name)
        print("파일이 성공적으로 변경되었습니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없거나 실행 도중 파일이 변경되었습니다.")
    except FileExistsError:
        print("동일한 이름의 파일이 이미 존재합니다.")

if __name__ == "__main__":
    file_namer()
