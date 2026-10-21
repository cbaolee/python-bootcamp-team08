import csv
import json
from dataclasses import asdict
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    """Load a tasks csv file into a list of tasks"""
    tasks = []

    with open(path, mode='r', encoding='utf8') as file:
        reader = csv.reader(file)

        try:
            next(reader)
        except StopIteration:
            return tasks

        for line_number, row in enumerate(reader, start=2):
            if len(row) != 4:
                raise ValueError(f"Invalid number of columns at line {line_number}")

            str_title, str_imp, str_eff, str_dl = row

            try:
                int_imp = int(str_imp)
                float_eff = float(str_eff)
                date_dl = date.fromisoformat(str_dl)
            except ValueError:
                raise ValueError(f"Invalid data format at line {line_number}")

            tasks.append(Task(str_title, int_imp, float_eff, date_dl))

    return tasks

def save_json(tasks, path):
    with open(path, mode='w', encoding='utf8') as file:
        data = [asdict(task) for task in tasks]
        json.dump(data, file, indent=4, default=str)