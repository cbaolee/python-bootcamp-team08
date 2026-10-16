from ..contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    blocks = []
    remaining_hours = hours

    for task in tasks:
        if remaining_hours <= 0:
            break
        allocated_time = min(task.effort_h, remaining_hours)
        block = Block(task=task, hours=allocated_time)
        blocks.append(block)

        remaining_hours -= allocated_time

    return blocks
