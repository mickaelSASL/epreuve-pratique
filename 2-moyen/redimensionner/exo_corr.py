def redimensionner(tab, nouvelle_largeur, nouvelle_hauteur):
    nouveau_tab = [[0]*nouvelle_largeur for _ in range(nouvelle_hauteur)]

    numero_ligne, numero_colonne = 0, -1
    for ligne in tab:
        for valeur in ligne:
            numero_colonne += 1
            if numero_colonne == nouvelle_largeur:
                numero_ligne += 1
                numero_colonne = 0
            nouveau_tab[numero_ligne][numero_colonne] = valeur
    return nouveau_tab


# Tests
tab1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tab2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
tab3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
assert redimensionner(tab1, 6, 2) == tab2
assert redimensionner(tab1, 3, 4) == tab3
