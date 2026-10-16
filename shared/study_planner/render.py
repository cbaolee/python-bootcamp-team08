import sys
from pathlib import Path

CLASS_DIR = str(Path(__file__).resolve().parent.parent)
if CLASS_DIR not in sys.path:
    sys.path.append(CLASS_DIR)

from contract import Block


def render(blocks: list[Block]) -> str:
    if not blocks:
        return "No tasks scheduled."

    total_hours = sum(b.hours for b in blocks)
    lines = [f"Tonight ({total_hours} h):"]

    for i, block in enumerate(blocks, start=1):
        lines.append(f"{i}. {block.task.title} - {block.hours} h")

    return "\n".join(lines)
