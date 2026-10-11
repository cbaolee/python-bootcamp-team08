# return true if credits ≥ 120 and gpa ≥ 2.0
def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


# return a list of reasons why the student can not register thesis.
# Empty list if the student is enough condition.
def missing(credits, gpa) -> list[str]:
    miss = []
    if not can_register_thesis(credits, gpa):
        more_cre = 120 - credits
        more_gpa = 2.0 - gpa
        if more_cre > 0:
            miss.append(f"need {more_cre} more credits")
        if more_gpa > 0:
            miss.append(f"need {more_gpa} more gpa")
    return miss
