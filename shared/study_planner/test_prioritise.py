import sys
from datetime import date
from pathlib import Path

CLASS_DIR = str(Path(__file__).resolve().parent.parent)
if CLASS_DIR not in sys.path:
    sys.path.append(CLASS_DIR)

from contract import Task
from prioritise import prioritise


def test_prioritise_standard_calculation():
    """Tasks should be sorted by importance / days_left descending."""
    today = date(2026, 10, 20)

    t1 = Task("Low Priority", importance=2, effort_h=1.0, deadline=date(2026, 10, 22))
    t2 = Task("High Priority", importance=4, effort_h=2.0, deadline=date(2026, 10, 22))
    t3 = Task(
        "Important but far", importance=5, effort_h=5.0, deadline=date(2026, 10, 30)
    )

    tasks = [t1, t2, t3]
    assert prioritise(tasks, today) == [t2, t1, t3]


def test_prioritise_due_today_and_overdue():
    """Tasks due today or in the past should get float('inf') score and sit at the top."""
    today = date(2026, 10, 20)

    t_future = Task("Future", importance=5, effort_h=1.0, deadline=date(2026, 10, 21))
    t_today = Task("Due Today", importance=3, effort_h=1.0, deadline=date(2026, 10, 20))
    t_past = Task("Overdue", importance=4, effort_h=1.0, deadline=date(2026, 10, 19))

    tasks = [t_future, t_today, t_past]
    assert prioritise(tasks, today) == [t_past, t_today, t_future]


def test_prioritise_tie_breaking():
    """Tasks with identical scores should tie-break by raw importance."""
    today = date(2026, 10, 20)

    t1 = Task("A", importance=2, effort_h=1.0, deadline=date(2026, 10, 21))
    t2 = Task("B", importance=4, effort_h=1.0, deadline=date(2026, 10, 22))

    tasks = [t1, t2]
    assert prioritise(tasks, today) == [t2, t1]


def test_prioritise_empty_list():
    """Function should handle empty lists without crashing."""
    assert prioritise([], date(2026, 10, 20)) == []
