def verifie(labyrinthe, chemin):
    DECALAGE = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'O': (0, -1)}
    MARQUE_LIBRE = 0
    MARQUE_BUISSON = 1
    MARQUE_VU = 2

    i_entree, j_entree = 1, 1
    i_sortie, j_sortie = len(labyrinthe) - 2, len(labyrinthe[0]) - 2

    i, j = i_entree, j_entree
    for direction in chemin:
        labyrinthe[i][j] = MARQUE_VU
        di, dj = DECALAGE[direction]
        i, j = i + di, j + dj
        if labyrinthe[i][j] != MARQUE_LIBRE:
            return False
    return (i, j) == (i_sortie, j_sortie)


# tests

labyrinthe  = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

chemin_1 = "EEEEES"
chemin_2 = "SSSSSEENNNEEEEEEESSOOOOSSSEEEESS"

import copy
labyrinthe_1 = copy.deepcopy(labyrinthe)
labyrinthe_2 = copy.deepcopy(labyrinthe)

assert not verifie(labyrinthe_1, chemin_1)
assert     verifie(labyrinthe_2, chemin_2)
