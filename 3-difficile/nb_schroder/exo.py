schroder_mem = [...]

def schroder(n):
    if n >= len(schroder_mem):
        resultat = ... # ... schroder(n - 1) ...
        # ici schroder_mem est de longueur n garanti
        schroder_mem.append(...)
    return schroder_mem[...]




# tests

assert schroder(2) == 6
assert schroder(3) == 22
assert schroder(4) == 90
