class Noeud:
    def __init__(self, gauche, element, droite):
        self.gauche = gauche
        self.element = element
        self.droite = droite

class ABR:
    """Classe ABR ; sans doublon
    """
    def __init__(self):
        self.racine = None
    
    def est_vide(self):
        return self.racine is None
    
    def insere(self, element):
        if self.est_vide():
            self.racine = Noeud(ABR(), element, ABR())
        elif element < self.racine.element:
            self.racine.gauche.insere(element)
        elif element > self.racine.element:
            ...
        else:
            # cas d'égalité
            pass  # donc pas de doublon !
    
    def est_present(self, element):
        if self.est_vide():
            return ...
        elif element < self.racine.element:
            return self.racine.gauche.est_present(element)
        elif ...:
            ...
        else:
            # cas d'égalité
            return True
    
    def affichage_infixe(self):
        if self.est_vide():
            return "|"
        else:
            return (
                  self.racine.gauche.affichage_infixe()
                + str(self.racine. ...)
                + self.racine. ...
            )


# tests

#1
nombres = ABR()
assert nombres.est_vide()
for x in [1, 3, 7, 9, 9]:
    nombres.insere(x)
assert not nombres.est_vide()

assert nombres.affichage_infixe() == '|1|3|7|9|'

assert nombres.est_present(7)
assert not nombres.est_present(8)

#2
fruits_ranges = ABR()
assert fruits_ranges.est_vide()

panier = ["kiwi", "pomme", "abricot", "mangue", "poire"]
for fruit in panier:
    fruits_ranges.insere(fruit)
assert not fruits_ranges.est_vide()

assert fruits_ranges.affichage_infixe() == '|abricot|kiwi|mangue|poire|pomme|'

assert fruits_ranges.est_present("pomme")
assert not fruits_ranges.est_present("cerise")
