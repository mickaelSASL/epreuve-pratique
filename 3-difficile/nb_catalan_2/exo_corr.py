# Initialisation da la suite des résultats
catalan_mem = [1]

def nb_arbres_binaires(n):
    if n >= len(catalan_mem):
        somme_cas = 0
        for i in range(n):
            somme_cas += nb_arbres_binaires(i) * nb_arbres_binaires(n - 1 - i)
        # Ici, catalan_mem sera de longueur n
        catalan_mem.append(somme_cas)
    return catalan_mem[n]


# tests

assert nb_arbres_binaires(3) == 5
assert nb_arbres_binaires(4) == 14
assert nb_arbres_binaires(5) == 42
