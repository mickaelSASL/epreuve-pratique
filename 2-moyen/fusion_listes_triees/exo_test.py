# tests
assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]

assert fusion([1, 6, 10], []) == [1, 6, 10]

assert fusion([], [0, 7, 8, 9]) == [0, 7, 8, 9]

# autres tests

import random
exemple_a = sorted(random.sample(range(10**9), 100))
exemple_b = sorted(random.sample(range(10**9), 100))
attendu = exemple_a + exemple_b
attendu.sort()
resultat = fusion(exemple_a[:], exemple_b[:])
for a, b in zip(resultat, attendu):
    assert a == b, "Erreur dans la fusion de grandes listes"

resultat = fusion(exemple_a, [])
for a, b in zip(resultat, exemple_a):
    assert a == b, "Erreur dans la fusion quand la seconde est vide"

resultat = fusion([], exemple_b)
for a, b in zip(resultat, exemple_b):
    assert a == b, "Erreur dans la fusion quand la seconde est vide"

