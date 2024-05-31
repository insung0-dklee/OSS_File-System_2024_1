# 파일 비교 기능 추가
def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
            content1 = file1.read()
            content2 = file2.read()
        
        if content1 == content2:
            print("두 파일은 동일합니다.")
        else:
            print("두 파일은 다릅니다.")
    
    except Exception as e:
        print(f"파일 비교 중 오류가 발생했습니다: {e}")

# 사용자 입력을 받기 전에 func 변수 정의
func = input("기능 입력 (? 입력시 도움말) : ")

# 사용자 정의 명령어 기능 실행을 위한 분기 추가
if func.lower() == "파일 비교":
    file1_path = input("비교할 첫 번째 파일의 경로를 입력하세요: ")
    file2_path = input("비교할 두 번째 파일의 경로를 입력하세요: ")
    compare_files(file1_path, file2_path)
