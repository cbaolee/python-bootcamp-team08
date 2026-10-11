def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]] :
    result = {}
    for course, day in courses:
        result.setdefault(day, []).append(course)

    for day, value in result.items():
        value.sort()

    return result