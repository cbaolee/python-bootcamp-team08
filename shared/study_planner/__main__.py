import argparse
import sys
from datetime import date
from pathlib import Path

from ..errors import InfeasiblePlan
from .allocate import allocate
from .parse import parse_csv
from .prioritise import prioritise
from .render import render


def main():
    parser = argparse.ArgumentParser(description="Team Study Planner CLI")
    parser.add_argument("file_path", help="Path to CSV file contains Task")
    parser.add_argument("--hours", type=float, required=True, help="Planned hours for studying")
    parser.add_argument("--today", type=str, default=date.today().isoformat(),
                        help="Today in format YYYY-MM-DD")


    args = parser.parse_args()


    try:
        current_date = date.fromisoformat(args.today)
    except ValueError:
        print("Error: --today must have correct form YYYY-MM-DD")
        sys.exit(1)

    file_path = Path(args.file_path)
    if not file_path.exists():
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = parse_csv(args.file_path)

        if not tasks:
            print("Error: CSV file is empty or has no data rows", file=sys.stderr)
            sys.exit(1)

        sorted_tasks = prioritise(tasks, current_date)

        blocks = allocate(sorted_tasks, args.hours)

        output_text = render(blocks)

        print(output_text)


    except InfeasiblePlan as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
