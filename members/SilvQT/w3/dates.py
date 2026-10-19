from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parses a due date string into a date object relative to `today`."""
    clean_text = text.strip().lower()
    if clean_text == "today":
        return today

    if clean_text == "tomorrow":
        return today + timedelta(days=1)

    if clean_text.startswith("in "):
        parts = clean_text.split()  
        if len(parts) == 3 and parts[2] in ("day", "days"):
            try:
                days = int(parts[1])
                return today + timedelta(days=days)
            except ValueError:
                pass

    weekdays ={
        "mon": 0, "monday": 0,
        "tue": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2,
        "thu": 3, "thursday": 3,
        "fri": 4, "friday": 4,
        "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6,
    }
    
    if clean_text in weekdays:
        target_weekday = weekdays[clean_text]
        current_weekday = today.weekday()
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0: 
            days_ahead += 7
        return today + timedelta(days=days_ahead)


    try:
        return date.fromisoformat(text.strip())
    except ValueError as err:
        raise ValueError(f"Unknown due date format: {text!r}") from err