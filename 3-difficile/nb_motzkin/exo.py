motzkin_mem = [1]

def motzkin(n):
    if n >= len(motzkin_mem):
        resultat = motzkin(...)
        for i in range(...):
            resultat += motzkin(...) ... motzkin(...)
        # motzkin_mem est ici de longueur n
        motzkin_mem.append(resultat)
        # et là de longueur n + 1
    return motzkin_mem[n]


# tests

assert motzkin(4) == 9
assert motzkin(5) == 21
