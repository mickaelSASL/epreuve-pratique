nb_chemins_mem = dict()

def nb_chemins(n, m):
    if (n, m) not in nb_chemins_mem:
        if (n == 0) or (m == 0):
            resultat = 1
        else:
            resultat = (
                  nb_chemins(n - 1, m    )
                + nb_chemins(n,     m - 1)
            )
        nb_chemins_mem[(n, m)] = resultat
    return nb_chemins_mem[(n, m)]


# tests

assert nb_chemins(4, 3) == 35
assert nb_chemins(3, 3) == 20
