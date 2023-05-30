def rotate_matrix(matrix):
    return [list(x)[::-1] for x in zip(*matrix)]