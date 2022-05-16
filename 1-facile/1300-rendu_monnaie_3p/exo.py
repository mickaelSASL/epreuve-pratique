def rendu(somme_a_rendre):
    ...




# tests

assert tuple(rendu( 7)) == (1, 1, 0)
assert tuple(rendu(10)) == (2, 0, 0)
assert tuple(rendu(13)) == (2, 1, 1)
assert tuple(rendu(32)) == (6, 1, 0)
