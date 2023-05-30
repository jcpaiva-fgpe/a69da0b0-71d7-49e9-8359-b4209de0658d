def word_to_digit(sentence):
    digits = []
    words = sentence.split()
    for word in words:
        if word.isdigit():
            digits.append(word)
        elif word == 'zero':
            digits.append('0')
        elif word == 'one':
            digits.append('1')
        elif word == 'two':
            digits.append('2')
        elif word == 'three':
            digits.append('3')
        elif word == 'four':
            digits.append('4')
        elif word == 'five':
            digits.append('5')
        elif word == 'six':
            digits.append('6')
        elif word == 'seven':
            digits.append('7')
        elif word == 'eight':
            digits.append('8')
        elif word == 'nine':
            digits.append('9')
    return ''.join(digits)