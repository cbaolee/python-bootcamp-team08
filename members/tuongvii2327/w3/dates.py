"""Parse human-friendly due dates."""

import re
from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Turn text like 'tomorrow', 'in 3 days', 'Fri' or '2026-10-30' into a date."""
    cleaned = text.strip().lower()
    if cleaned == "tomorrow":
        return today + timedelta(days=1)
    match = re.fullmatch(r"in (\d+) days?", cleaned)
    if match:
        return today + timedelta(days=int(match.group(1)))
    if cleaned in WEEKDAYS:
        # "or 7" makes the same weekday mean next week, not today
        ahead = (WEEKDAYS[cleaned] - today.weekday()) % 7 or 7
        return today + timedelta(days=ahead)
    try:
        return date.fromisoformat(cleaned)
    except ValueError as e:
        raise ValueError(f"cannot understand due date: {text!r}") from e
