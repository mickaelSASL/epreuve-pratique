def pascal(n):
    triangle = [[1]]
    for k in range(1, ...):
        ligne_k = [...]
        for i in range(1, k):
            ligne_k.append(triangle[...][i - 1] + triangle[...][...])
        ligne_k.append(...)
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
