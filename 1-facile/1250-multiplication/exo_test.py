from itertools import product

# Tests
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(3, -4) == -12
assert multiplication(-2, 0) == 0

# Tests supplémentaires
from itertools import product

premiers = [a for a in range(-10, 11)]
seconds = [a for a in range(-10, 11)]
for a, b in product(premiers, seconds):
    assert multiplication(a, b) == a*b, f"Erreur sur le produit {a}*{b}"
