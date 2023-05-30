def validate_password(password):
    length = len(password)
    upper = False
    lower = False
    digit = False
    special = False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
            special = True
    return length >= 8 and upper and lower and digit and special