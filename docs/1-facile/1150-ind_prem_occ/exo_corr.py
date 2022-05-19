def indice(element, tableau):
    for i in range(len(tableau)):
        if tableau[i] == element:
            return i



# tests

assert indice(1, [10, 12, 1, 56]) == 2
assert indice(1, [1, 50, 1]) == 0
assert indice(15, [8, 9, 10, 15]) == 3
assert indice(1, [2, 3, 4]) is None
