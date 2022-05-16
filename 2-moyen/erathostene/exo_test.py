# tests

assert eratosthene(5) == [False, False, True, True, False]
assert eratosthene(6) == [False, False, True, True, False, True]
assert premiers_inferieurs_a(5) == [2, 3]
assert premiers_inferieurs_a(7) == [2, 3, 5]
assert premiers_inferieurs_a(20) == [2, 3, 5, 7, 11, 13, 17, 19]


# autres tests

def est_premier(n):
    if n < 2: return False
    for d in range(2, n):
        if n%d == 0: return False
    return True

for n in range(37):
    attendu = [est_premier(p) for p in range(n)]
    assert eratosthene(n) == attendu, f"Erreur avec n = {n}"
for n in range(100):
    attendu = [p for p in range(n) if est_premier(p)]
    assert premiers_inferieurs_a(n) == attendu, f"Erreur avec n = {n}"
