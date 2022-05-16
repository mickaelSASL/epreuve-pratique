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

# autres tests

# ordre 3
assert     est_carre_magique([[2, 7, 6], [9, 5, 1], [4, 3, 8],])
assert not est_carre_magique([[1, 6, 5], [8, 4, 0], [3, 2, 7],]), "0 est présent ; interdit"
assert not est_carre_magique([[3, 8, 7], [10, 6, 2], [5, 4, 9],]), "1 est absent ; interdit"
assert not est_carre_magique([[1, 1, 1], [1, 1, 1], [1, 1, 1],]), "beaucoup d'absents ; interdit"
assert not est_carre_magique([[4, 3, 8], [2, 7, 6], [9, 5, 1],]), "erreur avec les diagonales"
assert not est_carre_magique([[7, 6, 2], [5, 1, 9], [3, 8, 4],]), "erreur avec les diagonales"

# ordre 1
assert est_carre_magique([[1]])
assert not est_carre_magique([[0]])
assert not est_carre_magique([[-1]])
assert not est_carre_magique([[2]])
assert not est_carre_magique([[128]])

# ordre n impair
def magique_f(i, j, n):
    assert n%2 == 1
    return n * ((i + j + (n-3)//2)%n) + ((i + 2*j - 2) % n) + 1

def rotation(carre):
    n = len(carre)
    carre = [[carre[n-1-j][i] for j in range(n)] for i in range(n)]

def switch(carre):
    # on inverse deux lignes extremes et deux colonnes extremes
    n = len(carre)
    carre[0], carre[-1] = carre[-1], carre[0]
    for i in range(n):
        carre[i][0], carre[i][-1] = carre[i][-1], carre[i][0]

for n in range(3, 21, 2):
    carre = [[magique_f(i, j, n) for j in range(1, n+1)] for i in range(1, 1+n)]
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    switch(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    carre[0][-1] += 1
    carre[0][-2] -= 1
    carre[1][-1] -= 1
    carre[1][-2] += 1
    carre[-1][0] -= 1
    carre[-1][1] += 1
    carre[-2][0] += 1
    carre[-2][1] -= 1
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
    switch(carre)
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"

# ordre n pair

soleil = [
    [ 6, 32,  3, 34, 35,  1],
    [ 7, 11, 27, 28,  8, 30],
    [19, 14, 16, 15, 23, 24],
    [18, 20, 22, 21, 17, 13],
    [25, 29, 10,  9, 26, 12],
    [36,  5, 33,  4,  2, 31],
]
assert est_carre_magique(soleil), "Erreur avec le carré dit 'du Soleil'"

franklin = [
    [52, 61,  4, 13, 20, 29, 36, 45],
    [14,  3, 62, 51, 46, 35, 30, 19],
    [53, 60,  5, 12, 21, 28, 37, 44],
    [11,  6, 59, 54, 43, 38, 27, 22],
    [55, 58,  7, 10, 23, 26, 39, 42],
    [ 9,  8, 57, 56, 41, 40, 25, 24],
    [50, 63,  2, 15, 18, 31, 34, 47],
    [16,  1, 64, 49, 48, 33, 32, 17],
]
assert est_carre_magique(soleil), "Erreur avec le carré de Benjamin Franklin"

def magique_4(n):
    assert n%4 == 0

    def case(i, j):
        if ((i + j + 1) % 4 == 0) or ((i - j) % 4 == 0):
            return 1 + i + n*j
        else:
            return n * n - (i + n*j)

    return [[case(i, j) for j in range(n)] for i in range(n)]

for n in range(4, 21, 4):
    carre = magique_4(n)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    switch(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert est_carre_magique(carre), f"Erreur avec n = {n}"
    carre[0][-1] += 1
    carre[0][-2] -= 1
    carre[1][-1] -= 1
    carre[1][-2] += 1
    carre[-1][0] -= 1
    carre[-1][1] += 1
    carre[-2][0] += 1
    carre[-2][1] -= 1
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
    switch(carre)
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
    rotation(carre)
    assert not est_carre_magique(carre), f"Erreur avec n = {n}"
