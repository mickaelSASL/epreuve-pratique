def remplacer(valeurs, valeur_cible, nouvelle_valeur):
    resultat = []
    for val in valeurs:
        if val == valeur_cible:
            resultat.append(nouvelle_valeur)
        else:
            resultat.append(val)

    return resultat


# Tests
# 1er test
valeurs = [3, 8, 7]
assert remplacer(valeurs, 3, 0) == [0, 8, 7]
assert valeurs == [
    3, 8, 7], "Il ne faut pas modifier les valeurs données en entrée"
# 2nd test
valeurs = [3, 8, 3, 5]
assert remplacer(valeurs, 3, 0) == [0, 8, 0, 5]
assert valeurs == [
    3, 8, 3, 5], "Il ne faut pas modifier les valeurs données en entrée"
