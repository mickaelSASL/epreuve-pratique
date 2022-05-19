def remplacer(valeurs, valeur_cible, nouvelle_valeur):
    ...


# Tests
# 1er test
valeurs = [3, 8, 7]
assert remplacer([3, 8, 7], 3, 0) == [0, 8, 7]
assert valeurs == [3, 8, 7]
# 2nd test
valeurs = [3, 8, 3, 5]
assert remplacer([3, 8, 3, 5], 3, 0) == [0, 8, 0, 5]
assert valeurs == [3, 8, 3, 5]
