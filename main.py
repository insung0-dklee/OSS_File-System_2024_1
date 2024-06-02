import os

def getParentDir(path):
    return os.path.dirname(path)

import os
import ctypes

def set_desktop_background(image_path):
    """
    바탕화면 배경을 지정된 이미지 파일로 설정합니다.
    
    @param
        image_path: 바탕화면 배경으로 설정할 이미지 파일의 경로
    """
    try:
        # SPI_SETDESKWALLPAPER 상수를 사용하여 바탕화면 배경 이미지 설정
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        print("바탕화면 배경이 설정되었습니다.")
    except Exception as e:
        print(f"바탕화면 배경 설정 중 오류가 발생했습니다: {e}")

def get_desktop_files():
    """
    바탕화면의 파일 목록을 반환합니다.
    """
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.listdir(desktop_path)

def main():
    # 바탕화면의 파일 목록 가져오기
    desktop_files = get_desktop_files()

    # 이미지 파일 목록 필터링
    image_files = [file for file in desktop_files if file.endswith((".jpg", ".png", ".bmp", ".gif"))]

    if image_files:
        print("바탕화면의 이미지 파일 목록:")
        for i, file in enumerate(image_files):
            print(f"{i+1}. {file}")

        file_index = int(input("바탕화면 배경으로 설정할 이미지 파일 번호를 입력하세요: "))
        selected_file = os.path.join(os.path.expanduser("~"), "Desktop", image_files[file_index-1])
        set_desktop_background(selected_file)
    else:
        print("바탕화면에 이미지 파일이 없습니다.")

if __name__ == "__main__":
    main()

