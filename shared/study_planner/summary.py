from ..contract import Block


def summarize(blocks: list[Block]) -> dict:
    hours_by_task = {}
    block_count = 0
    total_hours = 0.0

    for block in blocks:
        block_count += 1
        total_hours += block.hours
        title = block.task.title

        if title not in hours_by_task:
            hours_by_task[title] = 0.0
        hours_by_task[title] += block.hours

    return {
        "block_count": block_count,
        "task_count": len(hours_by_task),
        "total_hours": total_hours,
        "hours_by_task": hours_by_task,
    }