def recherche_positions(element, tableau):
    return [i for i in range(len(tableau)) if tableau[i] == element]


assert recherche_positions(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert recherche_positions(4, [1, 2, 3]) == []
assert recherche_positions(1, [1, 1, 1, 1]) == [0, 1, 2, 3]
assert recherche_positions(5, [0, 0, 5]) == [2]
