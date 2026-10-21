import argparse
import sys
from datetime import date
from pathlib import Path
from members.SilvQT.w2.io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    """Constructs the command-line interface argument parser."""
    parser = argparse.ArgumentParser(
        description="Schedule study tasks given available hours."
    )
    parser.add_argument(
        "csv_path",
        type=Path,
        help="Path to the CSV file containing tasks.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Total hours available tonight.",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Override current date (YYYY-MM-DD format).",
    )
    return parser


def main() -> None:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args()

    if not args.csv_path.exists():
        print(f"Error: CSV file '{args.csv_path}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = load_tasks(args.csv_path)
    except Exception as err:
        print(f"Error loading tasks: {err}", file=sys.stderr)
        sys.exit(1)

    sorted_tasks = sorted(
        tasks,
        key=lambda t: (t.days_left(args.today), -t.importance),
    )

    allocated_tasks: list[tuple[str, float]] = []
    remaining_hours = args.hours

    for task in sorted_tasks:
        if remaining_hours <= 0:
            break
        hours_to_do = min(task.effort_h, remaining_hours)
        allocated_tasks.append((task.title, hours_to_do))
        remaining_hours -= hours_to_do

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, (title, hrs) in enumerate(allocated_tasks, start=1):
        left_str = f" {idx}. {title} "
        right_str = f" {hrs:.1f} h"
        dots_count = max(1, 25 - len(left_str) - len(right_str))
        print(f"{left_str}{'.' * dots_count}{right_str}")


if __name__ == "__main__":
    main()