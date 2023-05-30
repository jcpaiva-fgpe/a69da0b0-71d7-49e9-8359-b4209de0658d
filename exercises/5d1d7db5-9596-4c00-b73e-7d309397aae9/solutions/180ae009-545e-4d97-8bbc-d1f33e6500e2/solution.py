def validate_phone_number(phone_number):
    if len(phone_number) != 14:
        return 'Invalid'
    if not (phone_number[0:3]+phone_number[4:7]+phone_number[8:]).isdigit():
        return 'Invalid'
    if phone_number[3] != '-' or phone_number[7] != '-':
        return 'Invalid'
    return 'Valid'
