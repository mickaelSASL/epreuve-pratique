def nb_lignes(grille):
    return len(grille)

def ligne(grille, i):
    return grille[i]

def nb_colonnes(grille):
    return len(grille[0])

def colonne(grille, j):
    return [grille[i][j] for i in range(nb_lignes(grille))]

def transposition(tableau):
    return [colonne(tableau, j) for j in range(nb_colonnes(tableau))]



# tests

grille = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
]
assert nb_lignes(grille) == 3
assert ligne(grille, 0) == [0, 1, 1, 1]
assert nb_colonnes(grille) == 4
assert colonne(grille, 1) == [1, 0, 0]
t_grille = [
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 1],
]
assert transposition(grille) == t_grille
assert transposition(t_grille) == grille

grille = [
    ['#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#'],
    ['.', '.', '#', '#', '#'],
    ['#', '.', '#', '#', '#'],
]
assert nb_lignes(grille) == 4
assert ligne(grille, 3) == ['#', '.', '#', '#', '#']
assert nb_colonnes(grille) == 5
assert colonne(grille, 0) == ['#', '#', '.', '#']
t_grille = [
    ['#', '#', '.', '#'],
    ['#', '#', '.', '.'],
    ['#', '#', '#', '#'],
    ['#', '#', '#', '#'],
    ['#', '#', '#', '#'],
]
assert transposition(grille) == t_grille
assert transposition(t_grille) == grille
