import os
import re
from datetime import datetime


def clean_text(text):
    """Remove extra spaces from text."""
    if not text:
        return ""

    return " ".join(text.strip().split())


def is_empty(text):
    """Check whether text is empty."""
    return not clean_text(text)


def get_current_time():
    """Return current time."""
    return datetime.now().strftime("%I:%M %p")


def get_current_date():
    """Return current date."""
    return datetime.now().strftime("%d %B %Y")


def is_valid_username(username):
    """Validate username."""
    if not username:
        return False

    return bool(
        re.fullmatch(
            r"[A-Za-z0-9_]{3,30}",
            username
        )
    )


def ensure_folder(folder_name):
    """Create a folder if it doesn't exist."""

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


def file_exists(file_path):
    """Check whether a file exists."""
    return os.path.isfile(file_path)


def safe_filename(filename):
    """Remove unsafe characters from a filename."""

    return re.sub(
        r'[<>:"/\\|?*]',
        "_",
        filename
    )


def get_timestamp():
    """Return current timestamp."""
    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )