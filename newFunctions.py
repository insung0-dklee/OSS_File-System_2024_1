import os
import zipfile
import time
from PIL import Image
import matplotlib.pyplot as plt

def compress_file(file_path):
    """
    사용자가 파일경로를 입력하면 해당파일을 zip으로 압축합니다.
    
    매개변수 file_path (str): 압축할 파일의 경로
    """
    if not os.path.isfile(file_path):
        print(f"파일이 존재하지 않습니다: {file_path}")
        return

    try:
        file_dir = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        output_zip = os.path.join(file_dir, f"{file_name}.zip")
        
        # 파일 이름 중복 방지
        counter = 1
        while os.path.exists(output_zip):
            output_zip = os.path.join(file_dir, f"{file_name}_{counter}.zip")
            counter += 1

        with zipfile.ZipFile(output_zip, 'w') as zipf:
            zipf.write(file_path, file_name)
        print(f"파일이 성공적으로 압축되었습니다: {output_zip}")
    except Exception as e:
        print(f"파일 압축 중 오류가 발생했습니다: {e}")

def preview_text(file_path, num_lines=5):
    """
    텍스트 파일의 처음 몇 줄을 미리보기합니다.
    
    매개변수 file_path (str): 미리보기할 텍스트 파일의 경로
    매개변수 num_lines (int): 미리볼 줄 수, 기본값은 5줄
    """
    if not os.path.isfile(file_path):
        print(f"파일이 존재하지 않습니다: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [next(file) for _ in range(num_lines)]
        for line in lines:
            print(line, end='')
    except StopIteration:
        # 파일이 num_lines보다 적은 줄을 가지고 있을 때 남은 줄 출력
        print("파일의 줄 수가 지정된 줄 수보다 적습니다. 남은 줄을 모두 출력합니다:")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    print(line, end='')
        except Exception as e:
            print(f"텍스트 미리보기 중 오류가 발생했습니다: {e}")
    except Exception as e:
        print(f"텍스트 미리보기 중 오류가 발생했습니다: {e}")

# 예시 사용법
# compress_file('test.txt')
# preview_text('test.txt')
