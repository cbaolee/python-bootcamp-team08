import sys
from pathlib import Path

CLASS_DIR = str(Path(__file__).resolve().parent.parent)

if CLASS_DIR not in sys.path:
    sys.path.append(CLASS_DIR)
    
from contract import Task, Block

def allocate(tasks: list[Task],hours : float) -> list[Block] :
    blocks = []
    remaining_hours = hours
    
    for task in tasks:
        if remaining_hours <= 0:
            break
        allocated_time = min(task.effort_h, remaining_hours)
        block = Block(task = task, hours = allocated_time)
        blocks.append(block)
        
        remaining_hours -= allocated_time
    
    return blocks