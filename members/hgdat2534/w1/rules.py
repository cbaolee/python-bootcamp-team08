def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa) -> list[str]:
    requirements = []
    if credits < 120:
        requirements.append("need " + str(120 - credits) + " more credits")
    if gpa < 2.0:
        requirements.append("Need " + str(round(2.0 - gpa, 2)) + " more GPA points")
    return requirements