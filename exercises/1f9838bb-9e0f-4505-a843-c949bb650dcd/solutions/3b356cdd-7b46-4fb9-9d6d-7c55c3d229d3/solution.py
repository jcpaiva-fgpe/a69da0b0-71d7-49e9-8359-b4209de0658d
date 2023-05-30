def age_checker(birth_year):
  age = 2022 - birth_year
  if age >= 18:
    return 'Of legal age'
  else:
    return 'Not of legal age'