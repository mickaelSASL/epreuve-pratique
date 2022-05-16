def sommet(tableau: list):
    gauche = 0
    droite = len(tableau) - 1
    while droite - gauche > 1:
        milieu = (gauche + droite) // 2
        if tableau[milieu - 1] < tableau[milieu] < tableau[milieu + 1]:
            gauche = milieu
        elif tableau[milieu - 1] > tableau[milieu] > tableau[milieu + 1]:
            droite = milieu
        else:
            return tableau[milieu]


# tests
assert sommet([1, 2, 1]) == 2
assert sommet([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5
assert sommet([1, 10, 9, 8, 7, 6, 5, 4]) == 10
assert sommet([1, 9, 8, 7]) == 9
assert sommet([1, 2, 3, 4, 5, 6, 7, 0]) == 7
assert sommet([1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == 4
assert sommet([4, 5, 7, 5, 3]) == 7
assert sommet([1, 10, 9, 8, 7, 6, 5, 4]) == 10
assert sommet([10, 100, 10, 9, 8, 7, 6]) == 100
assert sommet([1, 2, 4, 8, 4]) == 8
assert sommet([3, 4, 3, 2, 1, 0, -1, -2]) == 4

