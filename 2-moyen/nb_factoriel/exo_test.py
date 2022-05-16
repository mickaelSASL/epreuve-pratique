# tests

assert factorielle(5) == 120
assert factorielle(10) == 3628800

# autres tests

from math import factorial
for n in [0, 1, 2, 3, 4, 17, 42, 11, 42, 31]:
    assert factorial(n) == factorielle(n), "Erreur avec n = {n}"
