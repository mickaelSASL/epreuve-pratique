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


# Autres tests

from random import sample
for i in range(10):
    nombres = list(sample(range(10**9), 100+i))
    attendu = sorted(nombres)
    tri_selection(nombres)
    assert len(nombres) == len(attendu), "Erreur, le tableau ne doit pas changer de taille"
    for a, b, in zip(nombres, attendu):
        assert a == b, "Erreur lors du tri"
