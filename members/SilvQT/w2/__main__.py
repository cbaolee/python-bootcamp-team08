from pathlib import Path

from .io_utils import load_tasks

sample_path = Path("samples/tasks.csv")
if not sample_path.exists():
    sample_path = Path(__file__).resolve().parents[3] /"samples" /"tasks.csv"

tasks = load_tasks(sample_path)
for task in tasks:
    print(task)