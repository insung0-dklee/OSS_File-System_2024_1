import os
from dirsync import sync

def synchronize_directories(source_dir, target_dir, action="sync"):

    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"원본 디렉토리 '{source_dir}'를 찾을 수 없습니다.")

    os.makedirs(target_dir, exist_ok=True)

    sync(source_dir, target_dir, action)
    print(f"동기화 완료: {source_dir} -> {target_dir}")

if __name__ == "__main__":
    source_dir = input("원본 디렉토리 경로: ")
    target_dir = input("대상 디렉토리 경로: ")

    while True:
        action = input("동기화 작업을 선택하세요 (sync, copy, update, 기본값: sync): ")
        if action in ["sync", "copy", "update", ""]:
            break
        else:
            print("잘못된 작업 종류입니다. 다시 입력하세요.")

    if action == "":
        action = "sync"

    synchronize_directories(source_dir, target_dir, action)