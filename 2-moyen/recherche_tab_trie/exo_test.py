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


# autres tests

valeurs = [2*i for i in range(8)]
for i in range(8):
    cible = 2*i
    attendu = i
    assert indice(valeurs, cible) == attendu, f"Erreur avec {cible} dans {valeurs}"
for i in range(9):
    cible = 2*i - 1
    assert indice(valeurs, cible) is None, f"Erreur avec {cible} dans {valeurs}"

txt = [chr(ord('A') + i) for i in range(26)]
for i in range(26):
    cible = chr(ord('A') + i)
    attendu = i
    assert indice(txt, cible) == attendu, f"1.Erreur avec {cible} dans {txt}"
    cible = chr(ord('A') + i) + "!"
    assert indice(txt, cible) is None, f"2.Erreur avec {cible} dans {txt}"
    cible = "!" + chr(ord('A') + i)
    assert indice(txt, cible) is None, f"3.Erreur avec {cible} dans {txt}"
cible = ""
assert indice(txt, cible) is None, f"4.Erreur avec {cible} dans {txt}"
