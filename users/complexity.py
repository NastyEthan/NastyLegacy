import re

# check password complexity

def password_check(password):
    if len(password) < 8 or re.search(r"\d", password) is None or re.search(r"[a-z]", password) is None or re.search(r"[A-Z]", password) is None or re.search(r"[!@#$%^&*()_+\-=\[\]{};':,./<>?]", password) is None:
        return False
    else:
        return True
