def redimensionner(tab, nouvelle_largeur, nouvelle_hauteur):
    ...


# Tests
tab1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tab2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
tab3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
assert redimensionner(tab1, 6, 2) == tab2
assert redimensionner(tab1, 3, 4) == tab3
