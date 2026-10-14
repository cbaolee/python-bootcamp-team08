import csv
import json
from datetime import date

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None) 
        for i, row in enumerate(reader, start=2):
            try:
                title = row[0]
                importance = int(row[1])
                effort_h = float(row[2])
                deadline = date.fromisoformat(row[3])
                tasks.append(Task(title, importance, effort_h, deadline))
            except Exception as e:
                raise ValueError(f"Invalid data at line {i}") from e
    return tasks

def save_json(tasks: list[Task], path):
    data = []
    for t in tasks:
        data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()
        })
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)