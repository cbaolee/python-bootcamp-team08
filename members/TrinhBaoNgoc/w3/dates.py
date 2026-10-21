from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a date string into a date object."""
    text = text.lower()
    if text == "tomorrow":
        return today + timedelta(days=1)
    elif text == "in 3 days":
        return today + timedelta(days=3)
    elif text in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]:
        days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        target_idx = days.index(text)
        today_idx = today.weekday()
        days_ahead = target_idx - today_idx
        if days_ahead <= 0: # Target is next week
            days_ahead += 7
        return today + timedelta(days=days_ahead)
    else:
        try:
            return date.fromisoformat(text)
        except ValueError:
            raise ValueError(f"Unknown text format: {text}")