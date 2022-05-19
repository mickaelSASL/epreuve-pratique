# tests

def sont_proches(a, b):
    return abs(b - a) < 10**-6

resultat = arange(2.0, 4.0, 0.5)
attendu = [2.0, 2.5, 3.0, 3.5]
assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
for a, b in zip(resultat, attendu):
    assert sont_proches(a, b), f"Erreur avec {a} qui n'est pas proche de {b} dans arange(2.0, 4.0, 0.5)"

resultat = arange(5.0, 6.5, 0.25)
attendu = [5.0, 5.25, 5.5, 5.75, 6.0, 6.25]
assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
for a, b in zip(resultat, attendu):
    assert sont_proches(a, b), f"Erreur avec {a} qui n'est pas proche de {b} dans arange(5.0, 6.5, 0.25)"



# autres tests

def pro_arange(debut, fin, pas):
    resultat = []
    x = debut
    while x < fin - 10**-6:
        resultat.append(x)
        x += pas
    return resultat


for n in range(1, 30):
    debut, fin, pas = 4.0 + 5*n, 1.0 + 8*n, 1/n
    resultat = arange(debut, fin, pas)
    attendu = pro_arange(debut, fin, pas)
    assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
    for a, b in zip(resultat, attendu):
        assert sont_proches(a, b), f"Erreur avec {a} qui n'est pas proche de {b} dans arange({debut}, {fin}, {pas})"


