# tests
exemple_1 = [1, 2, 4, 5]
insere(3, exemple_1)
assert exemple_1 == [1, 2, 3, 4, 5]

exemple_2 = [1, 2, 7, 12, 14, 25]
insere(7, exemple_2)
assert exemple_2 == [1, 2, 7, 7, 12, 14, 25]

exemple_3 = [2, 3, 4]
insere(1, exemple_3)
assert exemple_3 == [1, 2, 3, 4]


# autres tests

nombres = []

insere(-101, nombres)
assert nombres == [-101], "Erreur insertion dans liste vide"

insere(11, nombres)
assert nombres == [-101, 11], "Erreur insertion singleton"

insere(0, nombres)
assert nombres == [-101, 0, 11], "Erreur insertion élément nul"

insere(-200, nombres)
assert nombres == [-200, -101, 0, 11], "Erreur insertion à gauche"

insere(200, nombres)
assert nombres == [-200, -101, 0, 11, 200], "Erreur insertion à droite"

