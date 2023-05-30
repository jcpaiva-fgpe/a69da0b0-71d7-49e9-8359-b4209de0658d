def converter(value, unit):
  if unit == 'inch':
    result = value * 2.54
  elif unit == 'cm':
    result = value / 2.54
  return round(result, 2)