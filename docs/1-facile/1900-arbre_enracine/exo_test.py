def hauteur(arbre):
    if arbre == []:
        return 0
    else:
        return 1 + max(hauteur(sous_arbre) for sous_arbre in arbre)

def taille(arbre):
    if arbre == []:
        return 1
    else:
        return 1 + sum(taille(sous_arbre) for sous_arbre in arbre)


# tests

assert hauteur([]) == 0
assert hauteur([[], [], [[]]]) == 2

assert taille([]) == 1
assert taille([[], [], [[]]]) == 5

# autres tests

assert hauteur([[]]) == 1
assert hauteur([[], []]) == 1
assert hauteur([[], [], []]) == 1

assert hauteur([[], [[]], [[]], [], []]) == 2
assert hauteur([[], [[]], []]) == 2
assert hauteur([[[]], []]) == 2
assert hauteur([[], [[]]]) == 2
assert hauteur([[[]]]) == 2


branche = [[], [[[], []]]]
arbre = [[branche], [[branche], [[branche]]]]
assert hauteur(arbre) == 7


assert taille([[]]) == 2
assert taille([[], []]) == 3
assert taille([[], [], []]) == 4

assert taille([[], [[]], [[]], [], []]) == 8
assert taille([[], [[]], []]) == 5
assert taille([[[]], []]) == 4
assert taille([[], [[]]]) == 4
assert taille([[[]]]) == 3
