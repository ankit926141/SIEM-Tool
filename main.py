from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from parsers.basic_parser import parse_log
from storage.log_storage import store_log
from rules.detector import detect_threat
from alerts.store_alerts import save_alert
import time

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("system.log"):
            with open(event.src_path, "r") as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    parsed = parse_log(last_line)
                    if parsed:
                        store_log(parsed)
                        alerts = detect_threat(parsed)
                        for alert in alerts:
                            print(f"🚨 {alert}")
                            save_alert(alert)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(LogHandler(), path="logs", recursive=False)
    observer.start()
    print("👀 Watching logs/system.log for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
