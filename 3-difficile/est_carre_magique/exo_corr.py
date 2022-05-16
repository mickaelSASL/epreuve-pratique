def est_carre_magique(carre):
    n = len(carre)
    somme = n * (n*n + 1) // 2

    # test des lignes
    for i in range(n):
        somme_i = sum(carre[i][j] for j in range(n))
        if somme_i != somme:
            return False

    # test des colonnes
    for j in range(n):
        somme_j = sum(carre[i][j] for i in range(n))
        if somme_j != somme:
            return False

    # test des diagonales
    somme_d1 = sum(carre[i][i] for i in range(n))
    if somme_d1 != somme:
        return False
    somme_d2 = sum(carre[i][n - 1 - i] for i in range(n))
    if somme_d2 != somme:
        return False

    # test présence unique
    deja_vu = [False] * (n*n + 1)
    for i in range(n):
        for j in range(n):
            if not(1 <= carre[i][j] <= n*n):
                return False

            if deja_vu[carre[i][j]]:
                return False
            deja_vu[carre[i][j]] = True

    return True



# tests

ex_ordre_3 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8],
]
assert est_carre_magique(ex_ordre_3)

contre_ex_ordre_2 = [
    [2, 2],
    [2, 2],
]
assert not est_carre_magique(contre_ex_ordre_2)

ex_ordre_4 = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1], 
]
assert est_carre_magique(ex_ordre_4)


