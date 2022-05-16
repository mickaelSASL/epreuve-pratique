def sont_proches(x, y):
    return abs(x - y) < 10**-6

def moyenne(tableau):
    n = len(tableau)
    somme = 0
    for valeur in tableau:
        somme += valeur
    return somme / n
