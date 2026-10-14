import sys
from pathlib import Path

from .io_utils import load_tasks


def find_sample_csv() -> Path:
    """Locate tasks.csv from CLI args or standard bootcamp sample folders."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])

    # __file__ is members/<member>/w2/__main__.py -> parents[3] is bootcamp root
    bootcamp_root = Path(__file__).resolve().parents[3]
    candidates = [
        bootcamp_root / "samples" / "tasks.csv",
        bootcamp_root / "tests" / "samples" / "tasks.csv",
        Path(__file__).resolve().parent / "tasks.csv",
    ]
    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError("Could not locate sample tasks.csv")


def main() -> None:
    csv_path = find_sample_csv()
    tasks = load_tasks(csv_path)
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()