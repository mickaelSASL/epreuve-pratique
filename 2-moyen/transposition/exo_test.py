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


# autres tests


une_colonne = [
    [(1, 2, 9)],
    [(3, 4, 9)],
    [(5, 6, 9)],
    [(7, 8, 9)],
]
une_ligne = [
    [(1, 2, 9), (3, 4, 9), (5, 6, 9), (7, 8, 9)],
]
assert nb_lignes(une_colonne) == len(une_colonne)
assert nb_colonnes(une_colonne) == len(une_colonne[0])
assert ligne(une_colonne, 0) == une_colonne[0]
assert colonne(une_colonne, 0) == [une_colonne[i][0] for i in range(len(une_colonne))]
assert transposition(une_ligne) == une_colonne
assert transposition(une_colonne) == une_ligne

