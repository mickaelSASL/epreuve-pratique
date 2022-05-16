def arbre_vers_chemin(arbre):
    def etape(arbre):
        "Fonction récursive interne"
        resultat = [len(arbre)]
        for sous_arbre in arbre:
            resultat.extend(etape(sous_arbre))
        return resultat

    chemin = [y - 1 for y in etape(arbre)]
    chemin.pop()
    return chemin


# tests

assert arbre_vers_chemin([[], []]) == [1, -1]
assert arbre_vers_chemin([[], [], [[], []]]) == [2, -1, -1, 1, -1]

