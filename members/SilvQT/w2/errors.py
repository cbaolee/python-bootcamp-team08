from .models import Task

class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Infeasible plan: needed {needed_h}h, but only {available_h}h available.")

    def __str__(self) -> str:
        return f"Needed {self.needed_h} hours, but only {self.available_h} hours available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)