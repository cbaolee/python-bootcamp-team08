"""Command-line study planner: python -m members.tuongvii2327.w3.cli tasks.csv --hours 2."""

import argparse
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def _priority(task: Task, today: date) -> float:
    """Higher score means do it sooner: importance divided by days left."""
    return task.importance / max(task.days_left(today), 1)


def build_plan(
    tasks: list[Task], hours: float, today: date
) -> list[tuple[Task, float]]:
    """Greedy plan: most urgent tasks first until the hours run out."""
    plan = []
    remaining = hours
    for task in sorted(tasks, key=lambda t: _priority(t, today), reverse=True):
        if remaining <= 0:
            break
        spent = min(task.effort_h, remaining)
        plan.append((task, spent))
        remaining -= spent
    return plan


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return the exit code."""
    parser = argparse.ArgumentParser(description="Plan tonight's study session.")
    parser.add_argument(
        "csv_path", type=Path, help="CSV with title,importance,effort_h,deadline"
    )
    parser.add_argument(
        "--hours", type=float, default=2.0, help="hours available tonight"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="YYYY-MM-DD (default: today)",
    )
    args = parser.parse_args(argv)

    today = args.today or date.today()
    if not args.csv_path.is_file():
        print(f"error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    try:
        tasks = load_tasks(args.csv_path)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    print(f"Tonight ({args.hours} h):")
    for i, (task, spent) in enumerate(build_plan(tasks, args.hours, today), start=1):
        print(f"    {i}. {task.title:.<20} {spent} h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
