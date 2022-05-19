# Tests
# 1er test
valeurs = [3, 8, 7]
assert remplacer(valeurs, 3, 0) == [0, 8, 7]
assert valeurs == [3, 8, 7], "Il ne faut pas modifier les valeurs données en entrée"
# 2nd test
valeurs = [3, 8, 3, 5]
assert remplacer(valeurs, 3, 0) == [0, 8, 0, 5]
assert valeurs == [3, 8, 3, 5], "Il ne faut pas modifier les valeurs données en entrée"


# Tests supplémentaires
# Valeurs identiques à l'entrée
valeurs = [5] * 8
assert remplacer(valeurs, 5, 10) == [10] * 8
assert valeurs == [5] * 8, "Il ne faut pas modifier les valeurs données en entrée"
# Valeurs identiques à la sortie
valeurs = [5] * 8 + [10] * 2
assert remplacer(valeurs, 10, 5) == [5] * 10
assert valeurs == [5] * 8 + [10] * 2, "Il ne faut pas modifier les valeurs données en entrée"
# Cible non présente
valeurs = [5] * 8
assert remplacer(valeurs, 10, 1) == [5] * 8
assert valeurs == [5] * 8, "Il ne faut pas modifier les valeurs données en entrée"
# liste vide
valeurs = []
assert remplacer(valeurs, 10, 1) == []
assert valeurs == [], "Il ne faut pas modifier les valeurs données en entrée"
