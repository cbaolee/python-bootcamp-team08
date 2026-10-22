import json
from dataclasses import asdict
from datetime import date

from ..contract import Block


def date_default(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Cannot serialize {type(obj).__name__}")


def export_json(blocks: list[Block], path: str) -> None:
    """Write a list of Block to a JSON file."""
    data = [asdict(block) for block in blocks]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2, default=date_default)