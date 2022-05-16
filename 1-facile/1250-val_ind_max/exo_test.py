# tests

assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert valeur_et_indice_du_max([1, 1, 1, 99, 99]) == (99, 3)
assert valeur_et_indice_du_max([10]) == (10, 0)
assert valeur_et_indice_du_max([]) == (None, None)


# autres tests

assert valeur_et_indice_du_max([100, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (100, 0)
assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 800]) == (800, 9)
assert valeur_et_indice_du_max([1, 1, 1, 199, 199, 5]) == (199, 3)
assert valeur_et_indice_du_max([100]) == (100, 0)

