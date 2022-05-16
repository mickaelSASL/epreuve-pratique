# Initialisation da la suite des résultats
catalan_mem = [1]

def nb_arbres_binaires(n):
    if n >= len(catalan_mem):
        somme_cas = ...
        for i in range(...):
            somme_cas += nb_arbres_binaires(...) * ...
        # Ici, catalan_mem sera de longueur n
        catalan_mem.append(...)
    return catalan_mem[...]


# tests

assert nb_arbres_binaires(3) == 5
assert nb_arbres_binaires(4) == 14
assert nb_arbres_binaires(5) == 42
