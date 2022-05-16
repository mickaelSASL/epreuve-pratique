def conway_suivante(ligne):
    precedent = ligne[0]
    nb_consecutifs = 0
    resultat = []
    for chiffre in ligne:
        if chiffre == precedent:
            nb_consecutifs += 1
        else:
            resultat.append(nb_consecutifs)
            resultat.append(precedent)
            precedent = chiffre
            nb_consecutifs = 1
    resultat.append(nb_consecutifs)
    resultat.append(precedent)
    return resultat



# tests

LIGNE_6 = [3, 1, 2, 2, 1, 1]
LIGNE_7 = [1, 3, 1, 1, 2, 2, 2, 1]
LIGNE_8 = [1, 1, 1, 3, 2, 1, 3, 2, 1, 1]
assert conway_suivante(LIGNE_6) == LIGNE_7
assert conway_suivante(LIGNE_7) == LIGNE_8
