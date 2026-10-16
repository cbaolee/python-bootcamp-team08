import json
from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.export import export_json


def make_blocks():
    exam_task = Task(
        title="DS exam",
        importance=5,
        effort_h=6.0,
        deadline=date(2026, 10, 30),
    )
    assignment_task = Task(
        title="Assignment",
        importance=4,
        effort_h=1.5,
        deadline=date(2026, 10, 27),
    )

    exam_block = Block(task=exam_task, hours=2.0)
    assignment_block = Block(task=assignment_task, hours=1.5)

    return [exam_block, assignment_block]


def test_creates_file(tmp_path):
    out = tmp_path / "plan.json"
    export_json(make_blocks(), str(out))
    assert out.exists()


def test_content_is_correct(tmp_path):
    out = tmp_path / "plan.json"
    export_json(make_blocks(), str(out))
    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert data[0]["hours"] == 2.0
    assert data[0]["task"]["title"] == "DS exam"


def test_date_is_iso_string(tmp_path):
    out = tmp_path / "plan.json"
    export_json(make_blocks(), str(out))
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data[0]["task"]["deadline"] == "2026-10-30"


def test_empty_list(tmp_path):
    out = tmp_path / "plan.json"
    export_json([], str(out))
    assert json.loads(out.read_text(encoding="utf-8")) == []


def test_overwrites_existing_file(tmp_path):
    out = tmp_path / "plan.json"
    out.write_text("old content", encoding="utf-8")

    export_json(make_blocks(), str(out))

    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data) == 2


def test_missing_directory_raises(tmp_path):
    out = tmp_path / "no_such_dir" / "plan.json"

    with pytest.raises(FileNotFoundError):
        export_json(make_blocks(), str(out))


def test_invalid_item_raises_type_error(tmp_path):
    out = tmp_path / "plan.json"

    with pytest.raises(TypeError):
        export_json(["not a block"], str(out))
