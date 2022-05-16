# tests

assert recherche_positions(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert recherche_positions(4, [1, 2, 3]) == []
assert recherche_positions(10, [2, 10, 3, 10, 4, 10, 5]) == [1, 3, 5]

# autres tests

assert recherche_positions(1, [1, 1, 1, 1]) == [0, 1, 2, 3]
assert recherche_positions(5, [0, 0, 5]) == [2]
assert recherche_positions(-1, [-1, 0, -1, 0, -1, 0, -1]) == [0, 2, 4, 6]
