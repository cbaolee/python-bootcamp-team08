# group the courses by day, return a dict with day is key and list of courses is value.
# The courses in each day is sorted by alphabet.
def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    days = {}
    for course, day in courses:
        days.setdefault(day, []).append(course)
    for names in days.values():
        names.sort()
    return days
