"""Date parsing utilities for relative and exact deadline strings."""

import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Convert a deadline string into a date object relative to today.

    Supports ISO dates ('YYYY-MM-DD'), 'tomorrow', 'in N day(s)',
    and weekday names (e.g., 'Fri' or 'Friday', returning the next occurrence).
    Raises ValueError for unknown formats.
    """
    if isinstance(text, date):
        return text

    text_clean = text.strip()
    text_lower = text_clean.lower()

    # 1. Exact Date (YYYY-MM-DD)
    try:
        return date.fromisoformat(text_clean)
    except ValueError:
        pass

    # 2. "tomorrow"
    if text_lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. "in X days"
    match = re.match(r"^in\s+(\d+)\s+days?$", text_lower)
    if match:
        return today + timedelta(days=int(match.group(1)))

    # 4. Weekday Name (Next occurrence)
    weekdays: dict[str, int] = {
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

    if text_lower in weekdays:
        days_ahead = weekdays[text_lower] - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: '{text}'")