# tests

donnees = [+13, +49, +13, +5]
assert occurrences_mini(donnees) == (5, [3])

donnees = [-84, +75, -84, 0, +16]
assert occurrences_mini(donnees) == (-84, [0, 2])

# autres tests

donnees = [0] * 4 + [1] * 4
attendu = (0, list(range(4)))
assert occurrences_mini(donnees) == attendu, f"Erreur avec {donnees}"

donnees = [1] * 4 + [0] * 4
attendu = (0, list(range(4, 8)))
assert occurrences_mini(donnees) == attendu, f"Erreur avec {donnees}"

donnees = [10] * 3 + [-5] * 4 + [1] * 4
attendu = (-5, list(range(3, 7)))
assert occurrences_mini(donnees) == attendu, f"Erreur avec {donnees}"

donnees = [10] * 4 + [-5] * 4 + [1] * 3
attendu = (-5, list(range(4, 8)))
assert occurrences_mini(donnees) == attendu, f"Erreur avec {donnees}"
