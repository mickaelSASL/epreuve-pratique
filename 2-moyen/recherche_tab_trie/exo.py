def indice_rec(valeurs, cible, debut, fin):
    if debut > fin:
        return None
    milieu = (debut + fin) // ...
    if   valeurs[milieu] > ...:
        return indice_rec(valeurs, cible, ..., ...)
    elif ...:
        return indice_rec(valeurs, cible, ..., ...)
    else:
        return milieu

def indice(valeurs, cible):
    return ...(valeurs, cible, 0, len(valeurs) - 1)



# tests

#1
nombres = [2, 3, 5, 7, 11, 13, 17]
assert indice(nombres, 7) == 3
assert indice(nombres, 8) is None


#2

fruits = ["abricot", "kiwi", "mangue", "poire", "pomme"]
assert fruits == sorted(fruits)  # le tableau est bien trié
assert indice(fruits, "kiwi") == 1
assert indice(fruits, "cerise") is None
