from datetime import datetime, timezone, timedelta

def get_current_time():
    """
    Returns the current time in UTC+7 timezone."""
    return datetime.now(timezone(timedelta(hours=7)))