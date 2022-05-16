# tests

def max(*args, **kwargs):
    assert False, "Interdit d'utiliser max."



assert sommet([4, 5, 7, 5, 3]) == 7
assert sommet([1, 10, 9, 8, 7, 6, 5, 4]) == 10
assert sommet([10, 100, 10, 9, 8, 7, 6]) == 100
assert sommet([1, 2, 4, 8, 4]) == 8
assert sommet([3, 4, 3, 2, 1, 0, -1, -2]) == 4


for i in range(1, 10):
    for j in range(1, 10):
        l = list(range(i)) + list(range(i + j, i - 1, -1))
        assert sommet(l) == i + j



class IntSurcharge():
    __compteur_comparaison = 0


    def __init__(self, x):
        self.__valeur = x

    def __lt__(self, autre):
        IntSurcharge.__compteur_comparaison += 1
        return self.__valeur < autre.__valeur

    def __gt__(self, autre):
        IntSurcharge.__compteur_comparaison += 1
        return self.__valeur > autre.__valeur

    def __ne__(self, autre):
        IntSurcharge.__compteur_comparaison += 1
        return self.__valeur != autre.__valeur

    def __eq__(self, autre):
        IntSurcharge.__compteur_comparaison += 1
        return self.__valeur == autre.__valeur

    def __le__(self, autre):
        IntSurcharge.__compteur_comparaison += 1
        return self.__valeur <= autre.__valeur

    def __ge__(self, autre):
        IntSurcharge.__compteur_comparaison += 1
        return self.__valeur >= autre.__valeur

    @property
    def compteur(self):
        return IntSurcharge.__compteur_comparaison

    @property
    def valeur(self):
        return self.__valeur

unimodal = [IntSurcharge(i) for i in range(10000)]
unimodal.extend([IntSurcharge(i) for i in range(10000, 543, -1)])

resultat = sommet(unimodal)

valeur = resultat.valeur
compteur = resultat.compteur
assert valeur == 10000
assert compteur < 200, "Vous avez utilisé une méthode interdite"

