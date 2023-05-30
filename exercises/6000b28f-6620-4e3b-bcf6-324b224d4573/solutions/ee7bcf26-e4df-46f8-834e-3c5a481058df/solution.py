def is_email_valid(email):
    if '@' in email and '.' in email:
        at_index = email.index('@')
        dot_index = email.index('.')
        if at_index > 0 and dot_index > at_index+1 and dot_index+1<len(email):
            return 'Valid'
    return 'Invalid'