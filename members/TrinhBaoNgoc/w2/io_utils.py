import csv
import json
from datetime import datetime

from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []

    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row["title"]
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = datetime.strptime(row["deadline"], "%Y-%m-%d").date()

                tasks.append(Task(title, importance, effort_h, deadline))

            except (ValueError, KeyError) as e:
                raise ValueError(f"Invalid data at line {line_num} : {e}")

    return tasks


def save_json(tasks, path) -> None:
    tasks_data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.strftime("%Y-%m-%d"),
        }
        for task in tasks
    ]

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(tasks_data, f, indent=4)
