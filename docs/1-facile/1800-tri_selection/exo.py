def tri_selection(tableau):
    ...


# tests

tab = [1, 52, 6, -9, 12]
tri_selection(tab)
assert tab == [-9, 1, 6, 12, 52], "Exemple 1"

tab_vide = []
tri_selection(tab_vide)
assert tab_vide == [], "Exemple 2"

singleton = [9]
tri_selection(singleton)
assert singleton == [9], "Exemple 3"
