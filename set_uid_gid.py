import pwd
import grp
import os

def set_file_owner(file_path, user):
    try:
        # 사용자 이름으로 UID (사용자 ID) 가져오기
        uid = pwd.getpwnam(user).pw_uid
        # 현재 파일의 GID (그룹 ID)를 가져오기
        gid = os.stat(file_path).st_gid
        # 파일의 소유권을 지정된 사용자로 변경
        os.chown(file_path, uid, gid)
        print(f"파일 '{file_path}'의 소유자가 '{user}'으로 변경되었습니다.")
    except KeyError:
        raise ValueError(f"사용자 '{user}'을(를) 찾을 수 없습니다.")
    except FileNotFoundError:
        raise ValueError(f"파일 '{file_path}'을(를) 찾을 수 없습니다.")
    except PermissionError:
        raise ValueError(f"파일 '{file_path}'에 대한 소유자 변경 권한이 없습니다. 관리자 권한이 필요합니다.")
    except Exception as e:
        raise RuntimeError(f"예기치 못한 오류가 발생했습니다: {e}")

def set_file_group(file_path, group):
    try:
        # 그룹 이름으로 GID (그룹 ID) 가져오기
        gid = grp.getgrnam(group).gr_gid
        # 현재 파일의 UID (사용자 ID)를 가져오기
        uid = os.stat(file_path).st_uid
        # 파일의 소유권을 지정된 그룹으로 변경
        os.chown(file_path, uid, gid)
        print(f"파일 '{file_path}'의 그룹이 '{group}'으로 변경되었습니다.")
    except KeyError:
        raise ValueError(f"그룹 '{group}'을(를) 찾을 수 없습니다.")
    except FileNotFoundError:
        raise ValueError(f"파일 '{file_path}'을(를) 찾을 수 없습니다.")
    except PermissionError:
        raise ValueError(f"파일 '{file_path}'에 대한 그룹 변경 권한이 없습니다. 관리자 권한이 필요합니다.")
    except Exception as e:
        raise RuntimeError(f"예기치 못한 오류가 발생했습니다: {e}")

def set_file_permissions(file_path, permissions=0o700):
    try:
        # 파일의 권한을 설정
        os.chmod(file_path, permissions)
        print(f"파일 '{file_path}'의 권한이 '{oct(permissions)}'으로 변경되었습니다.")
    except FileNotFoundError:
        raise ValueError(f"파일 '{file_path}'을(를) 찾을 수 없습니다.")
    except PermissionError:
        raise ValueError(f"파일 '{file_path}'에 대한 권한 변경 권한이 없습니다. 관리자 권한이 필요합니다.")
    except Exception as e:
        raise RuntimeError(f"예기치 못한 오류가 발생했습니다: {e}")
