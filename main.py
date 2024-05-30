import os

def getParentDir(path):
    return os.path.dirname(path)

"""

    주어진 경로에 폴더를 생성합니다. 상위 디렉토리가 없으면 생성합니다.

    @param path 생성할 폴더의 경로
    @return None
    @exception FileNotFoundError 상위 디렉토리가 존재하지 않을 때 발생합니다. 이 경우 상위 디렉토리를 생성하려 시도합니다.
    @exception PermissionError 폴더를 생성할 권한이 없을 때 발생합니다.
    @exception FileExistsError 폴더가 이미 존재할 때 발생합니다.
    @exception Exception 기타 모든 예외 상황에 대해 발생합니다.

"""
def MakeDir(path):
    try:
        os.mkdir(path)
        print(f"폴더 '{path}'가 성공적으로 생성되었습니다.")
    except FileNotFoundError:
	try:
            os.makedirs(path)
            print(f"상위 디렉토리와 폴더 '{path}'가 성공적으로 생성되었습니다.")
        except PermissionError:
            print(f"폴더 '{path}'를 생성할 권한이 없습니다.")
        except Exception as e:
            print(f"폴더를 생성하는 동안 오류가 발생했습니다: {e}")    
    except PermissionError:
        print(f"폴더 '{path}'를 생성할 권한이 없습니다.")
    except FileExistsError:
        print(f"폴더 '{path}'가 이미 존재합니다.")
    except Exception as e:
        print(f"폴더를 생성하는 동안 오류가 발생했습니다: {e}")