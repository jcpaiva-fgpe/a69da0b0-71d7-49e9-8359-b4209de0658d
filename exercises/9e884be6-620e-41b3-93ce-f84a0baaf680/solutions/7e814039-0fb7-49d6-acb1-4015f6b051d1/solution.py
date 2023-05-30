def mix_colors(color1, color2):
    if color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
        return 'orange'
    elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
        return 'green'
    elif color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
        return 'purple'
    else:
        return 'Invalid color combination.'