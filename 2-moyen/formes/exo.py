def dessine(lignes):
    """Affiche les rectangles et les triangles
    N'affiche pas les lignes ! Pour une ligne : utiliser print
    """
    for ligne in lignes:
        print(ligne)

def ligne_pleine(motif, nb_colonnes):
    return ...

def ligne_creuse(motif, nb_colonnes):
    if nb_colonnes == 1:
        return ...
    else:
        return motif + " " * (nb_colonnes - 2) + ...

def rectangle_plein(motif, nb_lignes, nb_colonnes):
    resultat = []
    for i in range(...):
        resultat.append(...)
    return resultat

def rectangle_creux(motif, nb_lignes, nb_colonnes):
    if nb_lignes == 1:
        return [ligne_pleine(...)]
    else:
        resultat = [...]
        for i in range(...):
            resultat.append(...)
        resultat.append(...)
        return resultat

def triangle_plein(motif, nb_lignes):
    ...

def triangle_creux(motif, nb_lignes):
    ...

# tests

assert ligne_pleine('M', 1) == "M"
assert ligne_pleine('#', 5) == "#####"

# Conseil : décommenter bloc par bloc les assertions
"""
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

"""
