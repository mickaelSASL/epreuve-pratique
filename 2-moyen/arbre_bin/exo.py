class ArbreBinaire():

    def __init__(self, gauche=None, etiquette=None, droite=None):
        self.gauche = gauche
        self.etiquette = etiquette
        self.droite = droite
    
    def est_vide(self):
        return self.etiquette is None
    
    def hauteur(self):
        if self.est_vide():
            return 0
        else:
            return ...
    
    def taille(self):
        ...



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
