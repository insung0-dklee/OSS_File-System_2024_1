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
    try:
        file_dir = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        output_zip = os.path.join(file_dir, f"{file_name}.zip")

        with zipfile.ZipFile(output_zip, 'w') as zipf:
            zipf.write(file_path, file_name)
        print(f"파일이 성공적으로 압축되었습니다: {output_zip}")
    except Exception as e:
        print(f"파일 압축 중 오류가 발생했습니다: {e}")

def list_file_creation_times(directory):
    """
    사용자가 입력한 디렉토리 내부의 모든 파일들의 생성 시간을 출력합니다.
    
    매개변수 directory: 파일 생성 시간을 출력할 디렉토리의 경로
    """
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                created_time = os.path.getctime(file_path)
                created_time_readable = time.ctime(created_time)
                print(f"{filename}: 생성 시간 - {created_time_readable}")
    except Exception as e:
        print(f"파일 생성 시간 출력 중 오류가 발생했습니다: {e}")

def preview_image(file_path):
    """
    이미지 파일을 미리보기합니다.
    
    매개변수 file_path (str): 미리보기할 이미지 파일의 경로
    """
    try:
        with Image.open(file_path) as img:
            plt.imshow(img)
            plt.axis('off')
            plt.show()
    except Exception as e:
        print(f"이미지 미리보기 중 오류가 발생했습니다: {e}")

def preview_text(file_path, num_lines=5):
    """
    텍스트 파일의 처음 몇 줄을 미리보기합니다.
    
    매개변수 file_path (str): 미리보기할 텍스트 파일의 경로
    매개변수 num_lines (int): 미리볼 줄 수, 기본값은 5줄
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [next(file) for _ in range(num_lines)]
        for line in lines:
            print(line, end='')
    except Exception as e:
        print(f"텍스트 미리보기 중 오류가 발생했습니다: {e}")
