# 타임스탬프를 사용하여 디렉토리의 스냅샷을 생성하고 복원하는 기능

import shutil
import os
import time

"""
    주어진 소스 디렉토리(src_dir)의 스냅샷을 지정된 스냅샷 디렉토리(snapshot_dir)에 생성합니다.
    스냅샷은 현재 시간의 타임스탬프를 사용하여 이름이 지정됩니다.

    Parameters:
    src_dir (str): 스냅샷을 생성할 소스 디렉토리의 경로.
    snapshot_dir (str): 스냅샷을 저장할 디렉토리의 경로.
"""
def create_snapshot(src_dir, snapshot_dir):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    snapshot_path = os.path.join(snapshot_dir, f'snapshot_{timestamp}')
    try:
        shutil.copytree(src_dir, snapshot_path)
        print(f"Snapshot of {src_dir} created at {snapshot_path}")
    except Exception as e:
        print(f"Error creating snapshot: {e}")
       
"""
    주어진 스냅샷 경로(snapshot_path)로부터 지정된 복원 디렉토리(restore_dir)에 스냅샷을 복원합니다.
    복원 디렉토리에 이미 데이터가 있는 경우 삭제하고 스냅샷을 복원합니다.

    Parameters:
    snapshot_path (str): 복원할 스냅샷의 경로.
    restore_dir (str): 스냅샷을 복원할 디렉토리의 경로.
"""

def restore_snapshot(snapshot_path, restore_dir):
    try:
        if os.path.exists(restore_dir):
            shutil.rmtree(restore_dir)
        shutil.copytree(snapshot_path, restore_dir)
        print(f"Snapshot from {snapshot_path} restored to {restore_dir}")
    except Exception as e:
        print(f"Error restoring snapshot: {e}")