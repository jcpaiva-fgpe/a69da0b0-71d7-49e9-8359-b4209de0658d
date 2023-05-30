def reverse_number(num):
    num_str = str(abs(num))
    reverse_str = num_str[::-1]
    reverse_num = int(reverse_str)
    if num<0:
        return reverse_num*-1
    else:
        return reverse_num