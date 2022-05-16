# tests

assert rendu_monnaie(68) == [50, 10, 5, 2, 1], "Erreur sur ce test"
assert rendu_monnaie(291) == [100, 100, 50, 20, 20, 1], "Erreur sur ce test"


# autres tests

assert rendu_monnaie(0) == []
assert rendu_monnaie(1) == [1]
assert rendu_monnaie(2) == [2]
assert rendu_monnaie(sum(pieces)) == pieces
assert rendu_monnaie(4) == [2, 2]
assert rendu_monnaie(500) == [100, 100, 100, 100, 100]
