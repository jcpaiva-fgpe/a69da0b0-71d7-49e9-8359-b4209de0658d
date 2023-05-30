def password_validator(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    special_chars = {'@', '#', '$', '%', '&', '*' }
    if not any(char in special_chars for char in password):
        return False
    return True