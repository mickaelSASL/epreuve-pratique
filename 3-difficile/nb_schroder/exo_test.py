# tests

assert schroder(2) == 6
assert schroder(3) == 22
assert schroder(4) == 90


# autres tests

A006318 = [
    1, 2, 6, 22, 90, 394, 1806, 8558, 41586, 206098, 1037718, 5293446,
    27297738, 142078746, 745387038, 3937603038, 20927156706, 111818026018,
    600318853926, 3236724317174, 17518619320890, 95149655201962,
    518431875418926, 2832923350929742, 15521467648875090
]

for n, attendu in enumerate(A006318):
    resultat = schroder(n)
    assert isinstance(resultat, int), "Erreur, le résultat doit être entier"
    assert attendu == resultat, f"Erreur avec n = {n}"
