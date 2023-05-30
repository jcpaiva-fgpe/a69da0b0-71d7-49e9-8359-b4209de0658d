def sorting_hat(num):
    if num % 4 == 0:
        return 'Gryffindor'
    elif num % 3 == 0:
        return 'Hufflepuff'
    elif num % 2 == 0:
        return 'Ravenclaw'
    else:
        return 'Slytherin'