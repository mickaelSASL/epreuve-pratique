def nb_chemins(n, m):
    numerateur = 1
    for i in range(n + 1, n + m + 1):
        numerateur *= i
    denominateur = 1
    for i in range(1, m + 1):
        denominateur *= i
    return numerateur // denominateur


# tests

assert nb_chemins(3, 3) == 20
assert nb_chemins(4, 2) == 15
assert nb_chemins(4, 3) == 35
