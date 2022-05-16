def dessine(lignes):
    """Affiche les rectangles et les triangles
    N'affiche pas les lignes ! Pour une ligne : utiliser print
    """
    for ligne in lignes:
        print(ligne)

def ligne_pleine(motif, nb_colonnes):
    return motif * nb_colonnes

def ligne_creuse(motif, nb_colonnes):
    if nb_colonnes == 1:
        return motif
    else:
        return motif + " " * (nb_colonnes - 2) + motif

def rectangle_plein(motif, nb_lignes, nb_colonnes):
    resultat = []
    for i in range(nb_lignes):
        resultat.append(ligne_pleine(motif, nb_colonnes))
    return resultat

def rectangle_creux(motif, nb_lignes, nb_colonnes):
    if nb_lignes == 1:
        return [ligne_pleine(motif, nb_colonnes)]
    else:
        resultat = [ligne_pleine(motif, nb_colonnes)]
        for i in range(nb_lignes - 2):
            resultat.append(ligne_creuse(motif, nb_colonnes))
        resultat.append(ligne_pleine(motif, nb_colonnes))
        return resultat

def triangle_plein(motif, nb_lignes):
    resultat = []
    for i in range(nb_lignes):
        resultat.append(ligne_pleine(motif, i + 1))
    return resultat

def triangle_creux(motif, nb_lignes):
    if nb_lignes == 1:
        return [motif]
    else:
        resultat = [motif]
        for i in range(nb_lignes - 2):
            resultat.append(ligne_creuse(motif, i + 2))
        resultat.append(ligne_pleine(motif, nb_lignes))
        return resultat

# tests

assert ligne_pleine('M', 1) == "M"
assert ligne_pleine('#', 5) == "#####"

assert ligne_creuse('Y', 1) == "Y"
assert ligne_creuse('X', 5) == "X   X"

assert rectangle_plein('B', 1, 5) == ["BBBBB"]
assert rectangle_plein('A', 3, 5) == [
    "AAAAA",
    "AAAAA",
    "AAAAA",
]

assert rectangle_creux('P', 1, 5) == ["PPPPP"]
assert rectangle_creux('O', 3, 5) == [
    "OOOOO",
    "O   O",
    "OOOOO",
]

assert triangle_plein('S', 1) == ["S"]
assert triangle_plein('T', 5) == [
    "T",
    "TT",
    "TTT",
    "TTTT",
    "TTTTT",
]

assert triangle_creux('G', 1) == ["G"]
assert triangle_creux('F', 5) == [
    "F",
    "FF",
    "F F",
    "F  F",
    "FFFFF",
]
