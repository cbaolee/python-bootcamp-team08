import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) ->list[Task]:
    tasks = []
    with open(path, mode = "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        next(reader, None)
        
        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue
            try:
                if len(row)!=4:
                    raise ValueError("Invalid columns number")
                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(
                    title = title,
                    importance = importance,
                    effort_h = effort_h,
                    deadline = deadline
                )
                tasks.append(task)
                
                
            except Exception as err:
                raise ValueError(f"Invalid row at line {line_num}: {err}"
                        ) from err
    return tasks
            


def save_json(tasks: list[Task], path:str):
    task_list = []
    for i in tasks:
        task_holder = {
            "title": i.title,
            "importance" : i.importance,
            "effort_h": i.effort_h,
            "deadline": i.deadline.isoformat()
        }
        task_list.append(task_holder)
    
    
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(task_list, file, indent = 0)