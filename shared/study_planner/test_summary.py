from datetime import date

from shared.contract import Block, Task
from shared.study_planner.summary import summarize


def test_summarize_empty_blocks() -> None:
    assert summarize([]) =={
        "block_count": 0,
        "task_count": 0,
        "total_hours": 0.0,
        "hours_by_task": {},
    }


def test_summarize_groups_hours_for_repeated_tasks() -> None:
    exam = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    assignment = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    blocks =[
        Block(exam, 1.5),
        Block(assignment, 1.0),
        Block(exam, 2.0),
    ]
    assert summarize(blocks) =={
        "block_count": 3,
        "task_count": 2,
        "total_hours": 4.5,
        "hours_by_task": {"DS exam": 3.5, "Assignment": 1.0},
    }
