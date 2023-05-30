def rectangle_intersection(rectangle1, rectangle2):
    x1 = max(rectangle1[0], rectangle2[0])
    y1 = max(rectangle1[1], rectangle2[1])
    x2 = min(rectangle1[2], rectangle2[2])
    y2 = min(rectangle1[3], rectangle2[3])
    if x1 < x2 and y1 < y2:
        return True
    return False