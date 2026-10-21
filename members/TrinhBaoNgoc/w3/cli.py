
import argparse
import sys
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise


def main() -> None:
    """Run the study planner CLI."""
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("file", help="CSV tasks file path")
    parser.add_argument("--hours", type=float, default=2.0, help="Hours available")
    parser.add_argument(
        "--today",
        type=str,
        default=str(date.today()),
        help="Today's date (YYYY-MM-DD)",
    )

    args = parser.parse_args()

    try:
        tasks = parse_csv(args.file)
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.", file=sys.stderr)
        sys.exit(1)

    today = date.fromisoformat(args.today)
    ranked = prioritise(tasks, today)
    blocks = allocate(ranked, args.hours)

    for block in blocks:
        print(f"{block.task.title} — {block.hours:.1f}h")


if __name__ == "__main__":
    main()