def password_checker(password):
    if len(password) < 8:
        return 'Invalid'
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for c in password:
        if c.isupper():
            has_uppercase = True
        elif c.islower():
            has_lowercase = True
        elif c.isdigit():
            has_digit = True
        if has_uppercase and has_lowercase and has_digit:
            return 'Valid'
    return 'Invalid'