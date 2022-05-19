def rendu(somme_a_rendre):
    n_5 = somme_a_rendre // 5
    somme_a_rendre -= 5 * n_5

    n_2 = somme_a_rendre // 2
    somme_a_rendre -= 2 * n_2

    n_1 = somme_a_rendre
    
    return (n_5, n_2, n_1)




# tests

assert tuple(rendu( 7)) == (1, 1, 0)
assert tuple(rendu(10)) == (2, 0, 0)
assert tuple(rendu(13)) == (2, 1, 1)
assert tuple(rendu(32)) == (6, 1, 0)
