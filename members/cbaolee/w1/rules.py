def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa) -> list[str]:
    reason: list[str] = []

    if credits < 120:
        reason.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reason.append("not enough gpa")

    return reason