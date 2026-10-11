def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    res = {}
    
    for course, day in timetable:
        if day not in res:
            res[day] = []
        res[day].append(course)
        
    for day in res:
        res[day].sort()
    
    return res