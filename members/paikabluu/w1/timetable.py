def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    res = {}
    for course, day in schedule:
        res.setdefault(day, []).append(course)
    
    for day in res:
        res[day].sort()
        
    return res