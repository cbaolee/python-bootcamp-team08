from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int       # 1-5
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        delta_days = self.deadline - today
        return delta_days.days