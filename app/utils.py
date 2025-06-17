from datetime import datetime, timezone, timedelta

def get_current_time():
    """
    Returns the current time in UTC+7 timezone."""
    return datetime.now(timezone(timedelta(hours=7)))

def apply_common_fields(obj, request, is_create=True):
    now = get_current_time()
    user_id = request.state.user_id
    ip = request.state.ip_address

    obj.updated_at = now
    obj.updated_by_user_id = user_id
    obj.ip_address = ip

    if is_create:
        obj.created_at = now
        obj.created_by_user_id = user_id