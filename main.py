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