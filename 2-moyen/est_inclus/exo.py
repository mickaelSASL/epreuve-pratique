def est_inclus_a_partir_de(extrait, chaine, position):
    if ... > len(chaine):
        return False
    for i in range(len(extrait)):
        if chaine[position + ...] != ...:
            return ...
    return True

def est_inclus(brin, gene):
    l_gene = len(gene)
    l_brin = len(brin)
    for i in range(... - ... + 1):
        if est_inclus_a_partir_de(..., ..., ...):
            return True
    return False


# tests
assert     est_inclus("AATC", "GTACAAATCTTGCC")
assert not est_inclus("AGTC", "GTACAAATCTTGCC")
assert not est_inclus("AGTC", "GTACAAATCTTGCA")
assert     est_inclus("AGTC", "GTACAAATCTAGTC")
