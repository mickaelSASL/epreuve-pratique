def propager(M, i, j, intensite):
    if M[i][j] == ...:
        # ...
        return

    intensite_origine = ...

    M[i][j] = intensite

    if (i - 1) >= 0 and M[i - 1][j] == ...:
        # l'élément au-dessus fait partie de la composante
        propager(M, i - 1, j, intensite)

    if (...) < len(M) and M[i + 1][j] == 1:
        # l'élément au-dessous fait partie de la composante
        propager(M, ..., j, intensite)

    if (...) >= 0 and M[i][j - 1] == 1:
        # l'élément à gauche fait partie de la composante
        ...

    if ...:
        # ...
        ...





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
