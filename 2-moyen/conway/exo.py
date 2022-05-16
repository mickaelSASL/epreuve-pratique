def conway_suivante(ligne):
    precedent = ligne[0]
    nb_consecutifs = 0
    resultat = ...
    for chiffre in ligne:
        if chiffre == precedent:
            nb_consecutifs = ...
        else:
            resultat.append(...)
            resultat.append(...)
            precedent = ...
            nb_consecutifs = ...
    resultat.append(...)
    resultat.append(...)
    return ...



# tests

LIGNE_6 = [3, 1, 2, 2, 1, 1]
LIGNE_7 = [1, 3, 1, 1, 2, 2, 2, 1]
LIGNE_8 = [1, 1, 1, 3, 2, 1, 3, 2, 1, 1]
assert conway_suivante(LIGNE_6) == LIGNE_7
assert conway_suivante(LIGNE_7) == LIGNE_8
