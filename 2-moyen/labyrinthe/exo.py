def verifie(labyrinthe, chemin):
    DECALAGE = {'N': (-1, 0), 'S': ...}
    MARQUE_LIBRE = 0
    MARQUE_BUISSON = 1
    MARQUE_VU = 2
    
    i_entree, j_entree = 1, 1
    i_sortie, j_sortie = ..., ...

    i, j = i_entree, j_entree
    for direction in chemin:
        labyrinthe[i][j] = MARQUE_VU
        di, dj = DECALAGE[...]
        i, j = ..., ...
        if labyrinthe[i][j] != ...:
            return ...
    return (i, j) == ...


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
