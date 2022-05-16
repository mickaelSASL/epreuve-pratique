# tests

assert somme_premiers(5) == 5
assert somme_premiers(20) == 77



# autres tests

def EST_premier(n):
    if n < 2:
        return False
    for d in range(2, n):
        # 1 < d < n
        if n % d == 0:
            # d est un diviseur de n, autre que 1 et n
            return False
    return True

def SOMME_premiers(n):
    return sum(p for p in range(n) if EST_premier(p))


for n in range(100):
    attendu = SOMME_premiers(n)
    assert somme_premiers(n) == attendu, f"Erreur avec n = {n}"
