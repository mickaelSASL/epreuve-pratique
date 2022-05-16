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


# autres tests

def permutations(objets):
    n = len(objets)
    if n == 0:
        return [[]]
    resultat = []
    for i in range(n):
        objets_sans_i = [objets[j] for j in range(n) if i != j]
        for perm in permutations(objets_sans_i):
            perm.append(objets[i])
            resultat.append(perm)
    return resultat


for perm in permutations([1, 2, 3, 4, 5]):
    abr = ABR()
    assert abr.est_vide()
    for x in perm: abr.insere(x)
    for x in range(-5, 10):
        attendu = 1 <= x < 6
        assert abr.est_present(x) == attendu
    assert abr.affichage_infixe() == '|1|2|3|4|5|'
