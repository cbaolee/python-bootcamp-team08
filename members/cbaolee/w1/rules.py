def can_register_thesis(credits: int, gpa: float) -> bool:
    """Checking if credits and gpa are able to register thesis"""
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    """Return the reasons for being declined"""
    reason: list[str] = []

    if credits < 120:
        reason.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reason.append("not enough gpa")

    return reason