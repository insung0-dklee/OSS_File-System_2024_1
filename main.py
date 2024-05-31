class NotificationHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"파일이 생성되었습니다: {event.src_path}")
        elif event.event_type == 'modified':
            print(f"파일이 수정되었습니다: {event.src_path}")
        elif event.event_type == 'deleted':
            print(f"파일이 삭제되었습니다: {event.src_path}")

# 파일 시스템 변경을 모니터링할 경로 입력
path_to_monitor = input("파일 시스템 변경을 감지할 디렉토리 경로를 입력하세요: ")

# 알림 핸들러 인스턴스 생성
notification_handler = NotificationHandler()

# 파일 시스템 이벤트 모니터링 시작
observer = Observer()
observer.schedule(notification_handler, path_to_monitor, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
