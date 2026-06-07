import string
import random

def create_short_code(length=7):
    """Generate a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
