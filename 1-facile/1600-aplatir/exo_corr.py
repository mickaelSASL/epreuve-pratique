def aplatir(tableau):
    resultat = []
    for ligne in tableau:
        for valeur in ligne:
            resultat.append(valeur)

    return resultat


# Tests
assert aplatir([[1, 2, 3, 4], [5, 6, 7, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert aplatir([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
assert aplatir([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
assert aplatir([[1], [2], [3], [4], [5], [6]]) == [1, 2, 3, 4, 5, 6]
