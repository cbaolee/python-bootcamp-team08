import csv
import sys
from datetime import date
from pathlib import Path

SHARED_DIR = str(Path(__file__).resolve().parent.parent)

if SHARED_DIR not in sys.path:
    sys.path.append(SHARED_DIR)

from contract import Task


def parse_csv(path) -> list[Task]:
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
                raise ValueError(f"Invalid data format at {line_number}")

            tasks.append(Task(str_title, int_imp, float_eff, date_dl))

        return tasks