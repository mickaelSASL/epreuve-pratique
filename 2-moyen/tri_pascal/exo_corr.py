def pascal(n):
    triangle = [[1]]
    for k in range(1, n + 1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k - 1][i - 1] + triangle[k - 1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle


# tests

assert pascal(4) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
]


assert pascal(5) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
]
