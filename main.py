import os

def getParentDir(path):          
    return os.path.dirname(path)

def add_to_favorites(file_name):               #file_name: 즐겨찾기에 추가할 파일의 이름을 입력받습니다. 
                                               #파일 이름을 FAVORITES_FILE에 추가합니다. 이미 즐겨찾기에 추가된 파일이라도 중복 저장되지 않도록 할 수 있습니다.
    try:
        with open(FAVORITES_FILE, 'a') as f:
            f.write(file_name + '\n')
        print(f"'{file_name}' 파일이 즐겨찾기에 추가되었습니다.")
    except Exception as e:
        print(f"즐겨찾기에 파일을 추가하는 중 오류가 발생했습니다: {e}")

def remove_from_favorites(file_name):
    try:
        if os.path.exists(FAVORITES_FILE):
            with open(FAVORITES_FILE, 'r') as f:
                lines = f.readlines()
            with open(FAVORITES_FILE, 'w') as f:
                for line in lines:
                    if line.strip() != file_name:
                        f.write(line)
            print(f"'{file_name}' 파일이 즐겨찾기에서 제거되었습니다.")
        else:
            print("즐겨찾기 파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"즐겨찾기에서 파일을 제거하는 중 오류가 발생했습니다: {e}")

def list_favorites():
    try:
        if os.path.exists(FAVORITES_FILE):
            with open(FAVORITES_FILE, 'r') as f:
                favorites = f.readlines()
            if favorites:
                print("즐겨찾기 파일 목록:")
                for favorite in favorites:
                    print(favorite.strip())
            else:
                print("즐겨찾기 목록이 비어 있습니다.")
        else:
            print("즐겨찾기 파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"즐겨찾기 파일을 읽는 중 오류가 발생했습니다: {e}")
