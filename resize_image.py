from PIL import Image

def resize_image(image_path, output_path, size):
    """
    주어진 경로의 이미지를 지정한 크기로 리사이즈하여 저장합니다.

    :param image_path: 원본 이미지 파일 경로
    :param output_path: 리사이즈된 이미지 파일을 저장할 경로
    :param size: 리사이즈할 크기 (너비, 높이)
    """
    try:
        with Image.open(image_path) as img:
            # 이미지를 지정한 크기로 리사이즈
            img = img.resize(size, Image.ANTIALIAS)
            # 리사이즈된 이미지를 저장
            img.save(output_path)
            print(f'Image saved to {output_path}')
    except Exception as e:
        print(f'Error resizing image: {e}')

