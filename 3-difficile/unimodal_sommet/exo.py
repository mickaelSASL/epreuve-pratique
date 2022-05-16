def sommet(tableau: list):
    gauche = 0
    droite = len(tableau) - 1
    while droite - gauche > 1:
        milieu = (      ...       ) // 2
        if tableau[milieu - 1] < tableau[milieu] < tableau[milieu + 1]:
            gauche = ...
        elif tableau[milieu - 1] > ...   > ...:
            droite = milieu
        else:
            return tableau[ ... ]



# tests
assert sommet([1, 9, 8, 7]) == 9
assert sommet([1, 3, 5, 2]) == 5
assert sommet([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5
assert sommet([1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == 4
