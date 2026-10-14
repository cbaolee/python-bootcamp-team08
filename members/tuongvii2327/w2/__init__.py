"""Week 2 package: Task model, CSV/JSON io and feasibility check."""

from datetime import date
from pathlib import Path

from .io_utils import load_tasks

SAMPLE_CSV = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    """Load the sample CSV and print every task."""
    today = date.today()
    for task in load_tasks(SAMPLE_CSV):
        print(
            f"{task.title}: importance={task.importance}, "
            f"effort={task.effort_h} h, deadline={task.deadline}, "
            f"{task.days_left(today)} days left"
        )
