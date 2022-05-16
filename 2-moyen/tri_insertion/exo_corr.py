def tri_insertion(entiers):
    n = len(entiers)
    for i in range(1, n):
        j = i
        valeur_a_inserer = entiers[i]
        while j > 0 and valeur_a_inserer < entiers[j - 1]:
            entiers[j] = entiers[j - 1]
            j = j - 1
        entiers[j] = valeur_a_inserer
