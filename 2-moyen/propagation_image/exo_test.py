# tests

M = [
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
]

propager(M, i=2, j=1, intensite=3)

M_attendu = [
    [0, 0, 1, 0],
    [0, 3, 0, 1],
    [3, 3, 3, 0],
    [0, 3, 3, 0],
]

assert M == M_attendu


# autres tests

M = [
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
]

propager(M, i=0, j=0, intensite=5)

M_attendu = [
    [5, 5, 1, 0],
    [5, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
]

assert M == M_attendu
