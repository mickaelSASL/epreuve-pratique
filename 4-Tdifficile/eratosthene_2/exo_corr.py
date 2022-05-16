def est_premier(n):
    if n < 2:
        return False
    for d in range(2, n):
        # 1 < d < n
        if n % d == 0:
            # d est un diviseur de n, autre que 1 et n
            return False
    return True

def eratosthene(n):
    crible = [True] * n
    if n > 0:
        crible[0] = False  # 0 n'est pas premier
    if n > 1:
        crible[1] = False  # 1 n'est pas premier
    for p in range(2, n):
        if crible[p]:
            # p est premier
            for kp in range(2*p, n, p):
                # kp est un multiple de p, donc non premier
                crible[kp] = False
    return crible

def eratosthene_V2(n):
    crible = [True] * n
    if n > 0:
        crible[0] = False  # 0 n'est pas premier
    if n > 1:
        crible[1] = False  # 1 n'est pas premier
    p = 2
    while p * p < n:
        if crible[p]:
            # p est premier
            for kp in range(p*p, n, p):
                # kp est un multiple de p, donc non premier
                crible[kp] = False
        p += 1
    return crible

def eratosthene_V3(n):
    crible = bytearray([True]) * n
    if n > 0:
        crible[0] = False  # 0 n'est pas premier
    if n > 1:
        crible[1] = False  # 1 n'est pas premier
    p = 2
    while p * p < n:
        if crible[p]:
            crible[p*p:n:p] = bytearray([False]) * len(crible[p*p:n:p])
        p += 1
    return crible

from itertools import compress

def somme_premiers(n):
    if n < 2:
        return 0
    primalite = eratosthene_V2(n)
    return sum(compress(range(n), primalite))




# tests

assert somme_premiers(5) == 5
assert somme_premiers(20) == 77


# tests à créer

for limite in range(20):
    primalite = eratosthene(limite)
    primalite_V3 = eratosthene_V3(limite)
    primalite_brute = [est_premier(i) for i in range(limite)]
    assert list(primalite_V3) == primalite == primalite_brute, f"{limite}, {list(primalite_V3)} {primalite}"


