def fusion(liste_a, liste_b):
    taille_a = len(liste_a)
    taille_b = len(liste_b)
    liste_triee = []
    i_a = 0
    i_b = 0
    while (i_a < taille_a) and (i_b < taille_b):
        if liste_a[i_a] < liste_b[i_b]:
            liste_triee.append(liste_a[i_a])
            i_a += 1
        else:
            liste_triee.append(liste_b[i_b])
            i_b += 1
    while i_a < taille_a:
        liste_triee.append(liste_a[i_a])
        i_a += 1
    while i_b < taille_b:
        liste_triee.append(liste_b[i_b])
        i_b += 1
    return liste_triee



# tests
assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]

assert fusion([1, 6, 10], []) == [1, 6, 10]

assert fusion([], [0, 7, 8, 9]) == [0, 7, 8, 9]
