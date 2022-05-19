def sont_proches(x, y):
    return abs(x - y) < 10**-6


# Votre fonction moyenne ici



# tests

assert sont_proches(moyenne([10, 20, 30, 40, 60, 110]), 45.0)
assert sont_proches(moyenne([1, 3]), 2.0)
assert sont_proches(moyenne([44, 51, 12, 72, 65, 34]), 46.333333333333336)
