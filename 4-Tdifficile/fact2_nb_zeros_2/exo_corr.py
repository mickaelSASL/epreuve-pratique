def nb_zeros_factorielle(n):
    resultat = 0
    puiss_5 = 5
    while puiss_5 <= n:
        resultat += n // puiss_5
        puiss_5 *= 5
    return resultat



# tests

assert nb_zeros_factorielle(3) == 0

assert nb_zeros_factorielle(11) == 2

assert nb_zeros_factorielle(42) == 9
