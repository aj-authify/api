import re


def is_valid(website):
    pattern = r"^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, website))
