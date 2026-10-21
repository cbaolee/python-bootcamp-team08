import argparse
import sys
from datetime import date
from pathlib import Path

from members.cbaolee.w2.io_utils import load_tasks
from members.cbaolee.w2.models import Task


def main():
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    
    parser.add_argument("file_path", help="Đường dẫn đến file CSV (VD: tasks.csv)")
    parser.add_argument("--hours", type=float, required=True, help="Số giờ dự định học")
    parser.add_argument("--today", type=str, default=date.today().isoformat(), 
                        help="Ngày hiện tại định dạng YYYY-MM-DD (Mặc định: hôm nay)")
    
    args = parser.parse_args()

    try:
        current_date = date.fromisoformat(args.today)
    except ValueError:
        print("Lỗi: --today phải đúng định dạng YYYY-MM-DD.")
        sys.exit(1)

    if not Path(args.file_path).is_file():
        print(f"Lỗi: Không tìm thấy file '{args.file_path}'.")
        sys.exit(1)

    try:
        tasks = load_tasks(args.file_path)
    except ValueError as e:
        print(f"Lỗi khi đọc CSV: {e}")
        sys.exit(1)

    def get_priority(t: Task) -> float:
        dl = t.days_left(current_date)
        if dl <= 0:
            return float('inf')
        return t.importance / dl

    tasks_to_do = sorted(tasks, key=get_priority, reverse=True)
    
    allocated_blocks = []
    remaining_hours = args.hours
    
    for task in tasks_to_do:
        if remaining_hours <= 0:
            break
            
        allocated_time = min(task.effort_h, remaining_hours)
        allocated_blocks.append((task, allocated_time))
        
        remaining_hours -= allocated_time

    print(f"Tonight ({args.hours:.1f} h):")
    for i, (task, time_spent) in enumerate(allocated_blocks, start=1):
        title_part = f"{i}. {task.title} "
        
        dot_count = max(0, 20 - len(title_part))
        dots = "." * dot_count
        
        print(f"  {title_part}{dots} {time_spent:.1f} h")

if __name__ == "__main__":
    main()