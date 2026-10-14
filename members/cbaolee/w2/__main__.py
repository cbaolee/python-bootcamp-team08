from pathlib import Path

from .io_utils import load_tasks

ROOT = Path(__file__).resolve().parent.parent.parent.parent


def print_tasks(path):
    try:
        tasks = load_tasks(path)
    except ValueError as error:
        print(f"The CSV file in {path} has a bad format: {error}")
        return

    print(f"The CSV file in {path} includes:")
    for task in tasks:
        print(task)


if __name__ == "__main__":
    print_tasks(ROOT / 'samples' / 'tasks.csv')
