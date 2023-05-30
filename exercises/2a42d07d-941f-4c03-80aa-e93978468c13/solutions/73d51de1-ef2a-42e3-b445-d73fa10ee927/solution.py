def multiplication_table(n):
    table = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = i * j
    return table