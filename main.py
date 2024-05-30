import os

def getParentDir(path):
    return os.path.dirname(path)

def renameFile(old_path, new_name):
    """
    이 함수는 주어진 파일의 이름을 새로운 이름으로 변경합니다.

    :param old_path: 기존 파일의 전체 경로
    :param new_name: 새 파일 이름
    :return: 새 파일의 전체 경로
    """
    parent_dir = getParentDir(old_path)
    new_path = os.path.join(parent_dir, new_name)
    
    try:
        os.rename(old_path, new_path)
        print(f"파일 이름이 {old_path}에서 {new_path}(으)로 변경되었습니다.")
        return new_path
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {old_path}")
    except PermissionError:
        print(f"파일 이름을 변경할 권한이 없습니다: {old_path}")
    except Exception as e:
        print(f"파일 이름 변경 중 오류가 발생했습니다: {e}")
