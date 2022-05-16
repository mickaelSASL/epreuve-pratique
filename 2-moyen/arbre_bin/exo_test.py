# tests

nil = ArbreBinaire()
assert nil.est_vide()
assert nil.taille() == 0
assert nil.hauteur() == 0

noeud_1 = ArbreBinaire(nil, "1", nil)
assert not noeud_1.est_vide()
assert noeud_1.taille() == 1
assert noeud_1.hauteur() == 1

noeud_2 = ArbreBinaire(nil, "2", nil)

arbre_A1 = ArbreBinaire(noeud_1, "A1", noeud_2)
noeud_3 = ArbreBinaire(nil, "3", nil)
arbre_A2 = ArbreBinaire(arbre_A1, "A2", noeud_3)
assert not arbre_A2.est_vide()

assert arbre_A1.taille() == 3, f"{arbre_A1.taille()}"
assert arbre_A1.hauteur() == 2, f"{arbre_A1.hauteur()}"

assert arbre_A2.taille() == 5, f"{arbre_A2.taille()}"
assert arbre_A2.hauteur() == 3, f"{arbre_A2.hauteur()}"


# autres tests



nil = ArbreBinaire()
assert nil.est_vide()
assert nil.taille() == 0
assert nil.hauteur() == 0

noeud_1 = ArbreBinaire(nil, "machin", nil)
assert not noeud_1.est_vide()
assert noeud_1.taille() == 1
assert noeud_1.hauteur() == 1

noeud_2 = ArbreBinaire(nil, "chose", nil)

arbre_A1 = ArbreBinaire(noeud_2, "AA1", noeud_1)
noeud_3 = ArbreBinaire(nil, "3", nil)
arbre_A2 = ArbreBinaire(noeud_3, "AA2", arbre_A1)
assert not arbre_A2.est_vide()

assert arbre_A1.taille() == 3, f"{arbre_A1.taille()}"
assert arbre_A1.hauteur() == 2, f"{arbre_A1.hauteur()}"

assert arbre_A2.taille() == 5, f"{arbre_A2.taille()}"
assert arbre_A2.hauteur() == 3, f"{arbre_A2.hauteur()}"

