"""Command-line tool to schedule tasks for tonight based on urgency and hours."""

import argparse
import sys
from collections.abc import Sequence
from datetime import date
from pathlib import Path

for parent in Path(__file__).resolve().parents:
    if (parent / "members").is_dir():
        if str(parent) not in sys.path:
            sys.path.insert(0, str(parent))
        break

try:
    from members.minh_nv.w2 import Task, load_tasks
except ModuleNotFoundError:
    from ..w2 import Task, load_tasks

try:
    from members.minh_nv.w3.dates import parse_due
except ModuleNotFoundError:
    from .dates import parse_due

try:
    from contract import Block
except ModuleNotFoundError:
    try:
        from .contract import Block
    except ImportError:
        from dataclasses import dataclass

        @dataclass
        class Block:
            """Allocated time slice for a specific task."""

            task: Task
            hours: float


def plan_tonight(tasks: list[Task], available_h: float, today: date) -> list[Block]:
    """Rank tasks by urgency and importance and allocate blocks up to available_h."""
    ranked = sorted(
        tasks,
        key=lambda t: (t.days_left(today), -t.importance, t.title),
    )

    blocks: list[Block] = []
    remaining_h = available_h

    for task in ranked:
        if remaining_h <= 1e-9:
            break
        allocated = min(task.effort_h, remaining_h)
        if allocated > 0:
            blocks.append(Block(task=task, hours=allocated))
            remaining_h -= allocated

    return blocks


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the CLI."""
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


def main(argv: Sequence[str] | None = None) -> None:
    """Parse CLI arguments, load tasks, and print tonight's schedule."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.today is not None:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            print(
                f"Error: Invalid --today date '{args.today}'. Expected YYYY-MM-DD.",
                file=sys.stderr,
            )
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
            task.deadline = parse_due(str(task.deadline), today)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    blocks = plan_tonight(tasks, args.hours, today)

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, block in enumerate(blocks, start=1):
        dots = "." * max(2, 17 - len(block.task.title))
        print(f"{idx}. {block.task.title} {dots} {block.hours:.1f} h")


if __name__ == "__main__":
    main()