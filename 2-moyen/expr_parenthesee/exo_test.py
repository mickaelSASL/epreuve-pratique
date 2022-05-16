# autres tests

nombre = Noeud(None, 42, None)
assert expression_parenthesee(nombre) == '42'

somme = Noeud(Noeud(None, 1, None), '+', Noeud(None, 2, None))
assert expression_parenthesee(somme) == '(1+2)'

quotient = Noeud(Noeud(None, 3, None), '/', somme)
assert expression_parenthesee(quotient) == '(3/(1+2))'




# tests
somme_1 = Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))
somme_2 = Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None))
produit_1 = Noeud(Noeud(None, 3, None), '*', somme_1)
expression = Noeud(produit_1, '-', somme_2)

assert expression_parenthesee(expression) == '((3*(8+7))-(2+1))'

