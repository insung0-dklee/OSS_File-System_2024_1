import shutil
import os

def restore_snapshot(snapshot_path, restore_dir):
    try:
        if os.path.exists(restore_dir):
            shutil.rmtree(restore_dir)
        shutil.copytree(snapshot_path, restore_dir)
        print(f"Snapshot from {snapshot_path} restored to {restore_dir}")
    except Exception as e:
        print(f"Error restoring snapshot: {e}")
