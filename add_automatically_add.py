import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RuleBasedAutomationHandler(FileSystemEventHandler):
    def __init__(self, rules):
        self.rules = rules

    def on_created(self, event):
        self.process_event(event)

    def on_modified(self, event):
        self.process_event(event)

    def process_event(self, event):
        if event.is_directory:
            return

        for rule in self.rules:
            if rule["condition"](event):
                rule["action"](event)

def monitor_directory(path, rules):
    event_handler = RuleBasedAutomationHandler(rules)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

rules = [
    {
        "condition": lambda event: event.src_path.endswith(".txt"),
        "action": lambda event: shutil.move(event.src_path, "/path/to/text_files")
    },
    {
        "condition": lambda event: event.src_path.endswith((".jpg", ".png")),
        "action": lambda event: shutil.copy(event.src_path, "/path/to/image_backups")
    },
]







