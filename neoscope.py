import psutil
import time
import datetime
import os

class NeoScope:
    def __init__(self, log_interval=5):
        self.log_interval = log_interval
        self.log_file = "neoscope_log.txt"
        self.start_monitoring()

    def log_system_stats(self):
        with open(self.log_file, "a") as log:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            log.write(f"{current_time} | CPU: {cpu_usage}% | RAM Usage: {memory_info.percent}% | Disk Usage: {disk_usage.percent}%\n")

    def display_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{'Time':<20}{'CPU Usage':<15}{'RAM Usage':<15}{'Disk Usage':<15}")
        with open(self.log_file, 'r') as log:
            lines = log.readlines()
            for line in lines[-10:]:  # Display last 10 entries
                print(line.strip())

    def start_monitoring(self):
        print("NeoScope is monitoring your system. Press Ctrl+C to stop.")
        try:
            while True:
                self.log_system_stats()
                self.display_stats()
                time.sleep(self.log_interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")

if __name__ == "__main__":
    NeoScope(log_interval=5)