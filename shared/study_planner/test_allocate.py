import sys
from pathlib import Path

CLASS_DIR = str(Path(__file__).resolve().parent.parent)

if CLASS_DIR not in sys.path:
    sys.path.append(CLASS_DIR)

from datetime import date

from allocate import allocate
from contract import Task


def test_allocate():
    task1 = Task(
        title="DS exam", importance=5, effort_h=3.0, deadline=date(2026, 10, 30)
    )
    task2 = Task(
        title="Assignment", importance=4, effort_h=2.0, deadline=date(2026, 10, 27)
    )
    task3 = Task(
        title="Read book", importance=2, effort_h=4.0, deadline=date(2026, 11, 5)
    )

    tasks = [task1, task2, task3]

    blocks_1 = allocate(tasks, hours=4.0)
    assert len(blocks_1) == 2
    assert blocks_1[0].hours == 3.0
    assert blocks_1[0].task.title == "DS exam"
    assert blocks_1[1].hours == 1.0
    assert blocks_1[1].task.title == "Assignment"

    blocks_2 = allocate(tasks, hours=10.0)
    assert len(blocks_2) == 3
    assert blocks_2[0].hours == 3.0
    assert blocks_2[1].hours == 2.0
    assert blocks_2[2].hours == 4.0
