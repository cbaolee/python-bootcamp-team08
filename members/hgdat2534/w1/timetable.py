def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for course, day in courses:
        result.setdefault(day,  []).append(course)
    return {day: sorted(course) for day, course in result.items()}