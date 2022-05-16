delannoy_mem = dict()

def delannoy(n, m):
    if (n, m) not in delannoy_mem:
        if (n == 0) or (m == 0):
            resultat = 1
        else:
            resultat = (
                  delannoy(n - 1, m    )
                + delannoy(n,     m - 1)
                + delannoy(n - 1, m - 1)
            )
        delannoy_mem[(n, m)] = resultat
    return delannoy_mem[(n, m)]


# tests

assert delannoy(3, 3) == 63
assert delannoy(2, 1) == 5
