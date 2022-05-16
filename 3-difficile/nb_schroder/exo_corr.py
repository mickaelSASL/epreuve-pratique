schroder_mem = [1, 2]

def schroder(n):
    if n >= len(schroder_mem):
        resultat =  (
                          (6*n - 3) * schroder(n - 1)
                        - (n  -  2) * schroder(n - 2)
                    ) // (n + 1)
        # ici schroder_mem est de longueur n garanti
        schroder_mem.append(resultat)
    return schroder_mem[n]




# tests

assert schroder(2) == 6
assert schroder(3) == 22
assert schroder(4) == 90
