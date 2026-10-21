from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Due date from today based on text parameter"""
    week_day = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }

    if text == "tomorrow":
        return today + timedelta(days=1)
    
    elif text in week_day:
        if week_day[text] <= today.weekday():
            dt = 7 - today.weekday() + week_day[text]
            return today + timedelta(days=dt)
        else:
            dt = week_day[text] - today.weekday()
            return today + timedelta(days=dt)

    elif text.startswith("in ") and text.endswith(" days"):
        try:
            days_to_add = int(text.split()[1])
            return today + timedelta(days=days_to_add)
        except ValueError:
            raise ValueError("Unknown text format")
        
    else:
        try:
            return date.fromisoformat(text)
        except ValueError:
            raise ValueError("Unknown text format")