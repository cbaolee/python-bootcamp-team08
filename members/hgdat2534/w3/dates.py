from datetime import date, timedelta
import re

def parse_due(text: str, today: date) -> date:
    text_clean = text.strip()
    text_lower = text_clean.lower()

    try:
        return date.fromisoformat(text_clean)
    except ValueError:
        pass
        
    if text_lower == "tomorrow":
        return today + timedelta(days=1)
        
    match = re.match(r"^in\s+(\d+)\s+days?$", text_lower)
    if match:
        return today + timedelta(days=int(match.group(1)))
        
    weekdays = {
        "mon": 0, "monday": 0, "tue": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2, "thu": 3, "thursday": 3,
        "fri": 4, "friday": 4, "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6
    }
    
    if text_lower in weekdays:
        target_weekday = weekdays[text_lower]
        days_ahead = target_weekday - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7

        return today + timedelta(days=days_ahead)
        
    raise ValueError(f"Unknown date format: '{text}'")