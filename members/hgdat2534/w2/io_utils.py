import csv
import json
from dataclasses import asdict

from .models import Task


def load_tasks(path: str) -> list[Task]:
    """
    Reads a CSV file and returns a list of Task objects.
    Raises a ValueError with the line number if a row is invalid.
    """
    tasks = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        header = next(reader, None)
        if header != ["title", "importance", "effort_h", "deadline"]:
            raise ValueError(f"Invalid or missing header at line {reader.line_num}")

        for row in reader:
            if not row:
                continue
                
            if len(row) != 4:
                raise ValueError(f"Invalid row length at line {reader.line_num}")
            
            try:
                title = row[0].strip()
                importance = int(row[1])
                effort_h = float(row[2])
                deadline = row[3].strip()
                
                tasks.append(Task(title, importance, effort_h, deadline))
            except ValueError:
                raise ValueError(f"Invalid data types at line {reader.line_num}")
                
    return tasks

def save_json(tasks: list[Task], path: str) -> None:
    """
    Saves a list of Task objects to a JSON file.
    """
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump([asdict(task) for task in tasks], f, indent=4)