import shutil
import os
import time

#지정된 디렉토리의 스냅샷을 만들어 타임스탬프를 포함한 이름으로 저장
def create_snapshot(src_dir, snapshot_dir):
    #타임스탬프 생성, 현재시간에 기반하여 생성
    timestamp = time.strftime("%Y%m%d%H%M%S")
    #스냅샷 경로 설정 
    snapshot_path = os.path.join(snapshot_dir, f'snapshot_{timestamp}')
    try:
        #원본 디렉토리를 스냅샷 경로로 복사
        shutil.copytree(src_dir, snapshot_path)
        print(f"Snapshot of {src_dir} created at {snapshot_path}")
        #복사 중 오류가 발생한경우, 예외를 처리하고 오류 메시지 출력
    except Exception as e:
        print(f"Error creating snapshot: {e}")
#저장된 스냅샷 복원
def restore_snapshot(snapshot_path, restore_dir):
    try:
        if os.path.exists(restore_dir): #존재여부 확인후 삭제
            shutil.rmtree(restore_dir) 
         #스냅샷 디렉토리를 복원 디렉토리로 복사   
        shutil.copytree(snapshot_path, restore_dir)
        print(f"Snapshot from {snapshot_path} restored to {restore_dir}")
    #예외처리
    except Exception as e:
        print(f"Error restoring snapshot: {e}")