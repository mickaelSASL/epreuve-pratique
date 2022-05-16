# tests

assert chemin_vers_arbre([1, -1]) == [[], []]

assert chemin_vers_arbre([2, -1, -1, 1, -1]) == [[], [], [[], []]]

# autres tests

assert chemin_vers_arbre([]) == []
assert chemin_vers_arbre([0]) == [[]]
assert chemin_vers_arbre([0, 0, 0, 0]) == [[[[[]]]]]
assert chemin_vers_arbre([2, -1, -1]) == [[], [], []]
assert chemin_vers_arbre([4, -1, -1, -1, -1]) == [[], [], [], [], []]
assert chemin_vers_arbre([2, 0, -1, 4, -1, -1, -1, 0, -1, -1]) == [[[]], [[], [], [], [[]], []], []]
