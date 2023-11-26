def convert_to_24_hour(hour, minute, period):
    if not (1 <= hour <= 12) or not (0 <= minute < 60) or period not in ["am", "pm"]:
        return "Invalid input"

    if hour == 12:
        hour = 0 if period == "am" else 12
    elif period == "pm":
        hour += 12

    return f"{hour:02d}{minute:02d}"