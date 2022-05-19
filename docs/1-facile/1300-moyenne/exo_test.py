# tests

def sont_proches(x, y):
    return abs(x - y) < 10**-6

assert sont_proches(moyenne([10, 20, 30, 40, 60, 110]), 45.0)
assert sont_proches(moyenne([1, 3]), 2.0)
assert sont_proches(moyenne([44, 51, 12, 72, 65, 34]), 46.333333333333336)

# autres tests

assert sont_proches(moyenne([69, 80, 43, 21, 42, 18]), 45.5)
assert sont_proches(moyenne([29, 94, 65, 77, 95, 31, 79]), 67.14285714285714)
assert sont_proches(moyenne([3, 1, 7, 6, 8]), 5.0)
