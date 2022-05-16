def chemin_vers_arbre(chemin):
    "correspondance de Łukasiewicz"
    def etape(temp, i):
        "Fonction récursive interne"
        if temp[i] == 0:
            return [], 1
        else:
            resultat = []
            taille_totale = 1
            for _ in range(temp[i]):
                sous_arbre, taille = etape(temp, i + taille_totale)
                taille_totale += taille
                resultat.append(sous_arbre)
        return resultat, taille_totale

    n = 1 + len(chemin)
    temp = [y + 1 for y in chemin] + [0]
    arbre, taille = etape(temp, 0)
    return arbre


# tests

assert chemin_vers_arbre([1, -1]) == [[], []]

assert chemin_vers_arbre([2, -1, -1, 1, -1]) == [[], [], [[], []]]
