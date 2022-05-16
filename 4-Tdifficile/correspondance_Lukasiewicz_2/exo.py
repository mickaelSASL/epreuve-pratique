def chemin_vers_arbre(chemin):
    "correspondance de Łukasiewicz"
    ...





# tests

assert chemin_vers_arbre([1, -1]) == [[], []]

assert chemin_vers_arbre([2, -1, -1, 1, -1]) == [[], [], [[], []]]
