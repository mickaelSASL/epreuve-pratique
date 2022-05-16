def linspace(a, b, n, ferme):
    ...









# tests, à ne pas modifier

def sont_proches(resultat, attendu):
    if len(resultat) != len(attendu):
        return False
    for a, b in zip(resultat, attendu):
        if abs(a - b) > 10**-6:
            return False
    return True

resultat = linspace(2.0, 4.0, 5, True)
attendu = [2.0, 2.5, 3.0, 3.5, 4.0]
assert sont_proches(resultat, attendu) , "Erreur avec linspace(2.0, 4.0, 5, True)"

resultat = linspace(5.0, 9.5, 6, False)
attendu = [5.0, 5.75, 6.5, 7.25, 8.0, 8.75]
assert sont_proches(resultat, attendu) , "Erreur avec linspace(5.0, 9.5, 6, False)"

