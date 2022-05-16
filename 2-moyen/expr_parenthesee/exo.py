class Noeud:
    """
    Classe implémentant un nœud d'arbre binaire disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre à gauche.
    - droite : le sous-arbre à droite.
    """
    def __init__(self, gauche, valeur, droite):
        self.gauche = gauche
        self.valeur = valeur
        self.droite = droite
    
    def est_feuille(self):
        "Renvoie un booléen, la réponse à : le nœud est-il une feuille ?"
        return self.gauche is None and self.droite is None


def expression_parenthesee(e):
    if e.est_feuille():
        return str(...)
    else:
        return '(' + expression_parenthesee(...) + ...



# tests
feuille = Noeud(None, 5, None)
assert expression_parenthesee(feuille) == '5'

somme_1 = Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))
somme_2 = Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None))
produit_1 = Noeud(Noeud(None, 3, None), '*', somme_1)
expression = Noeud(produit_1, '-', somme_2)

assert expression_parenthesee(expression) == '((3*(8+7))-(2+1))'
