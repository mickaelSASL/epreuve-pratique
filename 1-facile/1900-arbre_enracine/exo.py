def hauteur(arbre):
    ...

def taille(arbre):
    ...


# tests

assert hauteur([]) == 0
assert hauteur([[], [], [[]]]) == 2

assert taille([]) == 1
assert taille([[], [], [[]]]) == 5
