def eratosthene(n):
    crible = [True] * n
    if n > 0:
        crible[0] = False
    if n > 1:
        crible[1] = False
    for p in range(n):
        if crible[p] == True:
            # p est premier
            for kp in range(2*p, n, p):
                crible[kp] = False
    return crible

def premiers_inferieurs_a(n):
    crible = eratosthene(n)
    premiers = [p for p in range(n) if crible[p]]
    return premiers


# tests

assert eratosthene(5) == [False, False, True, True, False]
assert eratosthene(6) == [False, False, True, True, False, True]
assert premiers_inferieurs_a(5) == [2, 3]
assert premiers_inferieurs_a(7) == [2, 3, 5]
assert premiers_inferieurs_a(20) == [2, 3, 5, 7, 11, 13, 17, 19]

