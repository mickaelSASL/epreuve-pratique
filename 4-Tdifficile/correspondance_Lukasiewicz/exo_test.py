# tests

assert arbre_vers_chemin([[], []]) == [1, -1]

assert arbre_vers_chemin([[], [], [[], []]]) == [2, -1, -1, 1, -1]

# autres tests

assert arbre_vers_chemin([]) == []
assert arbre_vers_chemin([[]]) == [0]
assert arbre_vers_chemin([[[[[]]]]]) == [0, 0, 0, 0]
assert arbre_vers_chemin([[], [], []]) == [2, -1, -1]
assert arbre_vers_chemin([[], [], [], [], []]) == [4, -1, -1, -1, -1]
assert arbre_vers_chemin([[[]], [[], [], [], [[]], []], []]) == [2, 0, -1, 4, -1, -1, -1, 0, -1, -1]
