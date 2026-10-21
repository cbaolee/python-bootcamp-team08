from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(self.__str__())

    def __str__(self):
        return f"Infeasible plan, need {self.needed_h} hours but only has {self.available_h}"

def check_feasible(tasks: list[Task], available_h: float):
    """Check infeasibility of a plan"""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)

    return True