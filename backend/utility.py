import string
import random
from datetime import datetime, timezone

def create_short_code(length=7):
    """Generate a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_datetime():
    dt = datetime.now(timezone.utc)
    return dt.isoformat(timespec='seconds').replace('+00:00', 'Z')
