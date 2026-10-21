from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """
    Parses a string into a date object.
    Accepts ISO format, 'tomorrow', 'in X days', or short weekday names like 'Fri'.
    """
    text = text.lower().strip()

    if text == "tomorrow":
        return today + timedelta(days=1)

    if text.startswith("in ") and text.endswith(" days"):
        try:
            days = int(text[3:-5].strip())
            return today + timedelta(days=days)
        except ValueError:
            pass

    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    if text in weekdays:
        target = weekdays.index(text)
        current = today.weekday()
        days_ahead = target - current
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(text)
    except ValueError as e:
        raise ValueError(f"Unknown date format: {text}") from e
