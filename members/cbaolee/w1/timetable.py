def by_day(timetable) -> dict[str, str]:
    result = {}
    
    for course, day in timetable:
        result.setdefault(day, []).append(course)
        
    return {day: sorted(courses) for day, courses in result.items()}