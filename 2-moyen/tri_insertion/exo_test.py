# tests

tableau_0 = [9, 5, 8, 7, 6] 
tri_insertion(tableau_0)
assert tableau_0 == [5, 6, 7, 8, 9]

tableau_1 = [2, 5, -1, 7, 0, 28]
tri_insertion(tableau_1)
assert tableau_1 == [-1, 0, 2, 5, 7, 28]

tableau_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
tri_insertion(tableau_2)
assert tableau_2 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

un_seul = [9]
tri_insertion(un_seul)
assert un_seul == [9]

tableau_vide = []
tri_insertion(tableau_vide)
assert tableau_vide == []

# Autres tests

from random import sample
for i in range(10):
    nombres = list(sample(range(10**9), 100+i))
    attendu = sorted(nombres)
    tri_insertion(nombres)
    assert len(nombres) == len(attendu), "Erreur, le tableau ne doit pas changer de taille"
    assert nombres == attendu, "Erreur lors du tri"
