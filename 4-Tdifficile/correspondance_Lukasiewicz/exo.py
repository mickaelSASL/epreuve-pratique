def arbre_vers_chemin(arbre):
    ...

# tests

assert arbre_vers_chemin([[], []]) == [1, -1]
assert arbre_vers_chemin([[], [], [[], []]]) == [2, -1, -1, 1, -1]
