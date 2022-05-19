def nb_batiments_eclaires(hauteurs):
    resultat = 0
    plafond = 0
    for h in hauteurs:
        if h > plafond:
            plafond = h
            resultat += 1
    return resultat




# tests

assert 4 == nb_batiments_eclaires([2, 1, 2, 4, 0, 4, 5, 3, 5, 6])
assert 1 == nb_batiments_eclaires([0, 3, 1, 2])
