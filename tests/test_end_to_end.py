"""End-to-end tests for the shared study planner pipeline (T-W3)."""

from datetime import date
import json
from pathlib import Path

import pytest

from shared.errors import InfeasiblePlan, check_feasible
from shared.study_planner.allocate import allocate
from shared.study_planner.export import export_json
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render
from shared.study_planner.summary import summarize


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Create a sample CSV file matching the W2/W3 task specification."""
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )
    return csv_file


def test_e2e_full_pipeline(sample_csv: Path) -> None:
    """Test parse_csv -> prioritise -> allocate -> render end-to-end."""
    today = date(2026, 10, 26)
    available_hours = 2.0

    # 1. Parse CSV
    tasks = parse_csv(sample_csv)
    assert len(tasks) == 2

    # 2. Prioritise: Assignment (4 / 1 = 4.0) > DS exam (5 / 4 = 1.25)
    sorted_tasks = prioritise(tasks, today)
    assert [t.title for t in sorted_tasks] == ["Assignment", "DS exam"]

    # 3. Allocate greedily within 2.0 hours
    blocks = allocate(sorted_tasks, available_hours)
    assert len(blocks) == 2
    assert blocks[0].task.title == "Assignment"
    assert blocks[0].hours == pytest.approx(1.5)
    assert blocks[1].task.title == "DS exam"
    assert blocks[1].hours == pytest.approx(0.5)

    # 4. Render plan string
    output_text = render(blocks)
    expected_output = (
        "Tonight (2.0 h):\n"
        "1. Assignment - 1.5 h\n"
        "2. DS exam - 0.5 h"
    )
    assert output_text == expected_output


def test_e2e_summary_and_export_json(
    sample_csv: Path, tmp_path: Path
) -> None:
    """Test pipeline integration with summarize() and export_json()."""
    today = date(2026, 10, 26)
    json_path = tmp_path / "plan.json"

    tasks = parse_csv(sample_csv)
    sorted_tasks = prioritise(tasks, today)
    blocks = allocate(sorted_tasks, 2.0)

    # Verify summary output
    summary = summarize(blocks)
    assert summary == {
        "block_count": 2,
        "task_count": 2,
        "total_hours": pytest.approx(2.0),
        "hours_by_task": {
            "Assignment": pytest.approx(1.5),
            "DS exam": pytest.approx(0.5),
        },
    }

    # Verify JSON export
    export_json(blocks, str(json_path))
    assert json_path.exists()

    exported = json.loads(json_path.read_text(encoding="utf-8"))
    assert len(exported) == 2
    assert exported[0] == {
        "task": {
            "title": "Assignment",
            "importance": 4,
            "effort_h": 1.5,
            "deadline": "2026-10-27",
        },
        "hours": 1.5,
    }
    assert exported[1] == {
        "task": {
            "title": "DS exam",
            "importance": 5,
            "effort_h": 6.0,
            "deadline": "2026-10-30",
        },
        "hours": 0.5,
    }


def test_e2e_empty_csv(tmp_path: Path) -> None:
    """Test pipeline behavior when the CSV file is empty."""
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("", encoding="utf-8")

    tasks = parse_csv(empty_csv)
    assert tasks == []

    blocks = allocate(prioritise(tasks, date(2026, 10, 26)), 2.0)
    assert blocks == []
    assert render(blocks) == "No tasks scheduled."


def test_e2e_infeasible_plan_error(sample_csv: Path) -> None:
    """Test check_feasible raises InfeasiblePlan on parsed tasks."""
    tasks = parse_csv(sample_csv)

    with pytest.raises(InfeasiblePlan) as exc_info:
        check_feasible(tasks, available_h=2.0)

    assert exc_info.value.needed_h == pytest.approx(7.5)
    assert exc_info.value.available_h == pytest.approx(2.0)
    assert str(exc_info.value) == (
        "Infeasible plan: need 7.5 h but only 2.0 h available"
    )


def test_e2e_invalid_csv_raises_value_error(tmp_path: Path) -> None:
    """Test parse_csv raises ValueError with line number on malformed rows."""
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text(
        "title,importance,effort_h,deadline\n"
        "Broken Task,abc,2.0,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Invalid data format at 2"):
        parse_csv(bad_csv)