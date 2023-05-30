def swap_two_numbers(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return str(num1) + ',' + str(num2)