def password_strength(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    digits = [char for char in password if char.isdigit()]
    special_chars = [char for char in password if char in '!@#$%^&*']
    if len(password) < 8:
        return 'Weak'
    elif len(upper) == 0 or len(lower) == 0 or len(digits) == 0 or len(special_chars) == 0:
        return 'Moderate'
    elif len(upper) >= 1 and len(lower) >= 1 and len(digits) >= 1 and len(special_chars) >= 1:
        return 'Strong'
    else:
        return 'Very Strong'