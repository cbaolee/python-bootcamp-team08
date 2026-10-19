import argparse
import sys
from datetime import date
from members.paikabluu.w2.io_utils import load_tasks

def main() -> None:
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("csv_path", type=str, help="Path to the tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available hours")
    parser.add_argument("--today", type=str, default=date.today().isoformat(), help="Today's date (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    try:
        today_date = date.fromisoformat(args.today)
    except ValueError:
        print(f"Invalid --today format: {args.today}")
        sys.exit(1)
        
    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        print("Error: The specified CSV file was not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading tasks: {e}", file=sys.stderr)
        sys.exit(1)

    tasks.sort(key=lambda t: t.importance / max(t.days_left(today_date), 1), reverse=True)
    
    allocated: list[tuple] = []
    remaining = args.hours
    for t in tasks:
        if remaining <= 0:
            break
        hours_for_task = min(t.effort_h, remaining)
        allocated.append((t, hours_for_task))
        remaining -= hours_for_task
        
    total_allocated = args.hours - remaining
    print(f"Tonight ({total_allocated} h):")
    for i, (t, h) in enumerate(allocated, start=1):
        print(f"{i}. {t.title} .... {h} h")

if __name__ == "__main__":
    main()