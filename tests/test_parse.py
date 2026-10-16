import csv
import sys
from datetime import date
from pathlib import Path

import pytest

SHARED_DIR = str(Path(__file__).resolve().parent.parent)

if SHARED_DIR not in sys.path:
    sys.path.append(SHARED_DIR)

from contract import Task
from parse import parse_csv


def test_valid_multiple_rows(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
        "Learn Python,5,2.5,2026-10-20\n"
        "Unit Test Build,3,1,2026-10-25\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    result = parse_csv(csv_file)

    expected = [
        Task("Learn Python", 5, 2.5, date(2026, 10, 20)),
        Task("Unit Test Build", 3, 1.0, date(2026, 10, 25)),
    ]
    assert result == expected


def test_empty(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_file.write_text("", encoding="utf8")

    result = parse_csv(csv_file)

    assert result == []


def test_only_header(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    assert parse_csv(csv_file) == []


def test_too_few_columns(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
        "Miss Column Task,5,2.5\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    with pytest.raises(ValueError, match="Invalid number of columns at line 2"):
        parse_csv(csv_file)


def test_too_many_columns(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
        "Exceed Column Task,5,2.5,2026-10-20,extra\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    with pytest.raises(ValueError, match="Invalid number of columns at line 2"):
        parse_csv(csv_file)


def test_invalid_importance(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
        "Valid Task,5,2.0,2026-10-20\n"
        "Wrong Task,abc,2.5,2026-10-20\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    with pytest.raises(ValueError, match="Invalid data format at 3"):
        parse_csv(csv_file)


def test_invalid_effort(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
        "Wrong Task,5,two_hours,2026-10-20\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    with pytest.raises(ValueError, match="Invalid data format at 2"):
        parse_csv(csv_file)


def test_invalid_deadline(tmp_path):
    csv_file = tmp_path / "test_tasks.csv"
    csv_content = (
        "title,importance,effort_h,deadline\n"
        "Wrong Task,5,2.5,20-10-2026\n"
    )
    csv_file.write_text(csv_content, encoding="utf8")

    with pytest.raises(ValueError, match="Invalid data format at 2"):
        parse_csv(csv_file)