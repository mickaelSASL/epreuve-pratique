nb_chemins_mem = dict()

def nb_chemins(n, m):
    if (n, m) not in nb_chemins_mem:
        if (n == 0) or (...):
            resultat = ...
        else:
            resultat = (
                  nb_chemins(..., ...)
                + ...
            )
        nb_chemins_mem[(n, m)] = ...
    return ...


# tests

assert nb_chemins(3, 3) == 20
assert nb_chemins(4, 2) == 15
assert nb_chemins(4, 3) == 35
