import os
import matplotlib.pyplot as plt

def get_directory_size(directory):
    """디렉토리의 총 크기를 재귀적으로 계산"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # 심볼릭 링크는 무시
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def get_directory_sizes(directory):
    """디렉토리 내 각 서브디렉토리 및 파일의 크기를 계산"""
    dir_sizes = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        # 각 서브디렉토리의 크기 계산
        for d in dirnames:
            sub_dir_path = os.path.join(dirpath, d)
            dir_sizes[sub_dir_path] = get_directory_size(sub_dir_path)
        # 각 파일의 크기 계산
        for f in filenames:
            file_path = os.path.join(dirpath, f)
            # 심볼릭 링크는 무시
            if not os.path.islink(file_path):
                dir_sizes[file_path] = os.path.getsize(file_path)
    return dir_sizes

def plot_directory_sizes(directory):
    """디렉토리 및 파일의 크기를 파이 차트로 시각화"""
    dir_sizes = get_directory_sizes(directory)
    labels = []
    sizes = []

    for path, size in dir_sizes.items():
        labels.append(os.path.basename(path))
        sizes.append(size)

    # 큰 사이즈 순으로 정렬
    sizes, labels = zip(*sorted(zip(sizes, labels), reverse=True))

    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # 동그랗게 그리기
    plt.title(f"Disk Usage in '{directory}'")
    plt.show()
