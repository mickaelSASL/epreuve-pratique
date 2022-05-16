# tests

assert nb_chemins(3, 3) == 20
assert nb_chemins(4, 2) == 15
assert nb_chemins(4, 3) == 35

# autres tests

def FACT(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

for (n, m) in [(13, 17), (13, 18), (14, 17), (14, 18), (200, 221)]:
    attendu = FACT(n + m) // FACT(n) // FACT(m)
    assert nb_chemins(n, m) == attendu, f"Erreur avec n = {n} et m = {m}"
