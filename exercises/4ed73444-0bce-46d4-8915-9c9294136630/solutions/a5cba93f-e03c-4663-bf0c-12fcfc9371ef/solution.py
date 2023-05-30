def temperature_converter(unit, value):
    if unit.lower() == 'celsius':
        return round((value * 9/5) + 32, 2)
    elif unit.lower() == 'fahrenheit':
        return round((value - 32) * 5/9, 2)