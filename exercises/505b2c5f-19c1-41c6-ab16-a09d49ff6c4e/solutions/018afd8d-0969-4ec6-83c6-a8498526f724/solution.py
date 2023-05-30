def number_to_words(number):
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if number == 0:
        return "zero"
    elif number < 0:
        return "minus " + number_to_words(abs(number))
    elif number < 10:
        return digits[number]
    elif number < 20:
        return teens[number-10]
    elif number < 100:
        if number % 10 == 0:
            return tens[number // 10]
        else:
            return tens[number // 10] + "-" + digits[number % 10]
    elif number < 1000:
        if number % 100 == 0:
            return digits[number // 100] + " hundred"
        else:
            return digits[number // 100] + " hundred and " + number_to_words(number % 100)
    elif number < 1000000:
        if number % 1000 == 0:
            return number_to_words(number // 1000) + " thousand"
        else:
            return number_to_words(number // 1000) + " thousand " + number_to_words(number % 1000)