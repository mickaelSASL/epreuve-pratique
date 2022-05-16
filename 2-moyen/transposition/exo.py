def nb_lignes(grille):
    return len(...)

def ligne(grille, i):
    return ...

def nb_colonnes(grille):
    return ...

def colonne(grille, j):
    return [grille[...][...] for i in range(...)]

def transposition(tableau):
    return [... for j in range(...)]



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
