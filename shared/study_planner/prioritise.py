import sys
from pathlib import Path

CLASS_DIR = str(Path(__file__).resolve().parent.parent)
if CLASS_DIR not in sys.path:
    sys.path.append(CLASS_DIR)

from contract import Task


def prioritise(tasks, today) -> list[Task]:
    """
    Sorts tasks based on priority score: importance ÷ days_left.
    Tasks with higher scores are prioritized first.
    Tasks due today or in the past are given highest priority.
    """
    def calculate_score(task: Task) -> tuple[float, int]:
        days_left = (task.deadline - today).days
        
        if days_left <= 0:
            score = float('inf')
        else:
            score = task.importance / days_left
            
        return (score, task.importance)

    return sorted(tasks, key=calculate_score, reverse=True) 
