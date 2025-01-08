import psutil
import time
import os

class TaskTeller:
    def __init__(self):
        self.tasks = {}
        self.refresh_interval = 5

    def track_tasks(self):
        print("Tracking tasks and system usage. Press Ctrl+C to stop.")
        try:
            while True:
                self.update_tasks()
                self.display_tasks()
                self.display_system_usage()
                time.sleep(self.refresh_interval)
        except KeyboardInterrupt:
            print("Stopped tracking tasks.")

    def update_tasks(self):
        self.tasks = {proc.pid: proc.info for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent'])}

    def display_tasks(self):
        print("\nActive Tasks:")
        print(f"{'PID':<10}{'Name':<30}{'CPU%':<10}{'Memory%':<10}")
        print("-" * 60)
        for pid, info in self.tasks.items():
            print(f"{pid:<10}{info['name']:<30}{info['cpu_percent']:<10.2f}{info['memory_percent']:<10.2f}")

    def display_system_usage(self):
        print("\nSystem Usage:")
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
        print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
        print("-" * 60)

if __name__ == "__main__":
    task_teller = TaskTeller()
    task_teller.track_tasks()