import shutil
import os
import time

def create_snapshot(src_dir, snapshot_dir):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    snapshot_path = os.path.join(snapshot_dir, f'snapshot_{timestamp}')
    try:
        shutil.copytree(src_dir, snapshot_path)
        print(f"Snapshot of {src_dir} created at {snapshot_path}")
    except Exception as e:
        print(f"Error creating snapshot: {e}")

def restore_snapshot(snapshot_path, restore_dir):
    try:
        if os.path.exists(restore_dir):
            shutil.rmtree(restore_dir)
        shutil.copytree(snapshot_path, restore_dir)
        print(f"Snapshot from {snapshot_path} restored to {restore_dir}")
    except Exception as e:
        print(f"Error restoring snapshot: {e}")