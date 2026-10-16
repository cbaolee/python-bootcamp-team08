from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_empty_blocks():
    assert render([]) == "No tasks scheduled."


def test_render_multiple_blocks():
    t1 = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    t2 = Task("DS exam", 5, 6.0, date(2026, 10, 30))

    blocks = [Block(t1, 1.5), Block(t2, 0.5)]

    expected_output = "Tonight (2.0 h):\n1. Assignment - 1.5 h\n2. DS exam - 0.5 h"

    assert render(blocks) == expected_output
