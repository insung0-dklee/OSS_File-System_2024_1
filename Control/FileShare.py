import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from . import FileControl
import os

def file_share():
    finish = False

    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print("도움말")
            print(" '이메일 전송'           입력시파일을 이메일을 통해 전송")
            print(" '종료'                  입력시 프로그램을 종료할 수 있습니다.")
        
        elif select == '이메일 전송':
            print("\n(이미지, 사운드 등 특수 파일을 제외한 plain file만 첨부 가능)")
            recevier = input("파일을 전송할 이메일을 입력하세요: ")
            subject = input("이메일 제목을 간단하게 입력하세요: ")
            content = input("이메일 내용을 간단하게 입력하세요: ")
            file_path = input("전송할 파일의 경로를 입력하세요: ")
            try:
                send_email(recevier, subject, content, file_path)
                print(f"{recevier}님께 성공적으로 이메일을 전송했습니다.\n")
            except Exception as e:
                print(f"email 전송 중 error 발생, 다시 요청해주세요.\n{e}\n")

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요. : ")


def attach_file(msg, file_path):
    file = FileControl.read_file(file_path)
    #첨부파일의 정보를 헤더로 추가
    attachment = MIMEApplication(file)
    attachment.add_header('Content-Disposition','attachment', filename=os.path.basename(file_path)) 
    msg.attach(attachment)

def send_email(receiver, subject, content, file_path):
    """
    특정 파일을 메일을 통해 빠르게 공유하기 위한 기능
    (sender email POP3/SMTP 설정 필요)
    :param recevier: 파일을 공유할 대상의 이메일
    :param subject: 이메일 제목
    :param content: 이메일 내용
    :param file_path: 공유할 파일의 경로
    :return: none
    """

    # email, password 수정 후 빌드
    sender = "your-email@naver.com"
    passwod = "your-password"

    # 이메일 생성
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.attach(MIMEText(content))
    try:
        # 파일 첨부
        attach_file(msg, file_path)
        
        # 이메일 서버에 연결
        server = smtplib.SMTP('smtp.naver.com', 587)
        server.starttls()
        server.login(sender, passwod)

        # 이메일 보내기
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
    except Exception as e:
        raise e
