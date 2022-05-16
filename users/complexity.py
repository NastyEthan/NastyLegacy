import re

# check password complexity

def password_check(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return False
    elif re.search(r"\d", password) is None or re.search(r"[a-z]", password) is None or re.search(r"[A-Z]", password) is None or re.search(r"[!@#$%^&*()_+\-=\[\]{};':,./<>?]", password) is None:
        print("Password must contain at least one number, one lowercase letter, one uppercase letter, and one special character")
        return False
    elif re.search(r" ", password) is not None:
        print("Password cannot contain spaces")
        return False
    else:
        return True
