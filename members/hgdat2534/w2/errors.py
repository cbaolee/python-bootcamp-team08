class InfeasiblePlan(Exception):
    """Raised when total task effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: needed {self.needed_h}h, "
            f"but only {self.available_h}h available."
        )


def check_feasible(tasks, available_h: float) -> None:
    """
    Checks whether the total effort_h of all tasks fits within available_h.
    Raises InfeasiblePlan if total needed hours exceed available hours.
    """
    needed_h = sum(t["effort_h"] if isinstance(t, dict) else t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
