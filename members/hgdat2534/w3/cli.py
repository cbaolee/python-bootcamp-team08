import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

from members.hgdat2534.w2 import Task, load_tasks


def parse_due(text: str, today: date) -> date:
    """Convert a deadline string into a date object relative to today."""
    if isinstance(text, date):
        return text

    text_clean = text.strip()
    text_lower = text_clean.lower()

    try:
        return date.fromisoformat(text_clean)
    except ValueError:
        pass

    if text_lower == "tomorrow":
        return today + timedelta(days=1)

    match = re.match(r"^in\s+(\d+)\s+days?$", text_lower)
    if match:
        return today + timedelta(days=int(match.group(1)))

    weekdays = {
        "mon": 0, "monday": 0, "tue": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2, "thu": 3, "thursday": 3,
        "fri": 4, "friday": 4, "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6,
    }
    if text_lower in weekdays:
        days_ahead = weekdays[text_lower] - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: '{text}'")


def select_tasks_for_tonight(
    tasks: list[Task], available_h: float, today: date
) -> list[Task]:
    """
    Sort tasks by urgency (days_left ascending), then importance (descending),
    and greedily pick tasks that fit within available_h.
    """
    ranked = sorted(
        tasks,
        key=lambda t: (t.days_left(today), -t.importance, t.effort_h, t.title),
    )

    selected = []
    remaining_h = available_h
    for task in ranked:
        if task.effort_h <= remaining_h + 1e-9:
            selected.append(task)
            remaining_h -= task.effort_h

    return selected


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Schedule tasks for tonight.")
    parser.add_argument("csv_path", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available hours tonight",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.today is not None:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            print(f"Error: Invalid --today date '{args.today}'. Expected YYYY-MM-DD.", file=sys.stderr)
            sys.exit(1)
    else:
        today = date.today()

    csv_path = Path(args.csv_path)
    if not csv_path.is_file():
        print(f"Error: File not found: '{args.csv_path}'", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = load_tasks(str(csv_path))
        for task in tasks:
            task.deadline = parse_due(task.deadline, today)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    tonight_tasks = select_tasks_for_tonight(tasks, args.hours, today)

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, task in enumerate(tonight_tasks, start=1):
        dots = "." * max(2, 17 - len(task.title))
        print(f"{idx}. {task.title} {dots} {task.effort_h:.1f} h")


if __name__ == "__main__":
    main()