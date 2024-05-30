
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


# 파일 분할
"""
지정한 파일을 지정된 크기로 분할.

@Param
    file_path : 분할할 원본 파일의 경로.
    setSize : 분할될 파일 한개의 크기 (바이트 단위).
        
@Return
    None
"""

def Partition_file(file_path, setSize):
    file_num = 0
    with open(file_path, 'rb') as infile:
        while True:
            size = infile.read(setSize)
            if not size:
                break
            with open(f"{file_path}_part{file_num}", 'wb') as chunk_file:
                chunk_file.write(size)
            file_num += 1
    print(f"File is partitioned to {file_num} parts.")
    
    # delete original file
    os.remove(file_path)


# 파일 병합
"""
분할된 파일들을 하나의 파일로 병합합니다.

@Param
    output_path : 병합된 파일을 저장할 위치
    input_paths : 병합할 분할된 파일들의 경로.
    
@Return
    None
"""

def Merge_files(output_path, input_paths):
    with open(output_path, 'wb') as outfile:
        for file_path in input_paths:
            with open(file_path, 'rb') as infile:
                outfile.write(infile.read())
    print("Files are Merged to =>", output_path)
    
    # delete partitioned files
    for file_path in input_paths:
        os.remove(file_path)
        print(f"Delete Complete {file_path}.")



"""
Using example

분할
Partition_file('test.txt', 2048)

병합
input_files = [f'test.txt_part{i}' for i in range(분할 파일개수)]
Merge_files('test.txt', input_files)
"""


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


    elif func == "분할":
        file_path = input("복사할 파일의 경로를 입력하세요 : ")
        setSize = int(input("분할될 크기를 입력하세요(byte) : "))
        Partition_file(file_path, setSize)
        
    elif func == "병합":
        output_path = input("병합될 경로를 지정하세요 : ")
        input_path = input("분할된 파일의 경로를 입력하세요(_part까지 입력 | 분할숫자 입력x) : ")
        count_part = int(input("분할된 파일의 개수를 입력하세요 : "))
        input_paths = [f'{input_path}{i}' for i in range(count_part)]
        Merge_files(output_path, input_paths)



    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")







