def by_day(timetable: list[tuple[str, str]]) -> dict[str, str]:
    """Return a timetable based on course data"""
    result = {}
    
    for course, day in timetable:
        result.setdefault(day, []).append(course)
        
    return {day: sorted(courses) for day, courses in result.items()}