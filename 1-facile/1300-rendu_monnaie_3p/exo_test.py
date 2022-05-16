# tests

assert tuple(rendu( 7)) == (1, 1, 0)
assert tuple(rendu(10)) == (2, 0, 0)
assert tuple(rendu(13)) == (2, 1, 1)
assert tuple(rendu(32)) == (6, 1, 0)


# autres tests

def RENDU(somme_a_rendre):
    n_5 = somme_a_rendre // 5
    somme_a_rendre -= 5 * n_5

    n_2 = somme_a_rendre // 2
    somme_a_rendre -= 2 * n_2

    n_1 = somme_a_rendre
    
    return (n_5, n_2, n_1)

for somme_a_rendre in range(50):
    attendu = RENDU(somme_a_rendre)
    assert tuple(rendu(somme_a_rendre)) == attendu, f"Erreur avec le rendu de {somme_a_rendre}"
