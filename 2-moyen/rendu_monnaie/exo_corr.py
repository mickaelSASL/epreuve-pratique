pieces = [100, 50, 20, 10, 5, 2, 1]

def rendu_monnaie(a_rendre, i=0):
    if a_rendre == 0:
        return []
    p = pieces[i]
    if p <= a_rendre :
        return [p] + rendu_monnaie(a_rendre - p, i)
    else :
        return rendu_monnaie(a_rendre, i + 1)


# tests

assert rendu_monnaie(68) == [50, 10, 5, 2, 1]
assert rendu_monnaie(291) == [100, 100, 50, 20, 20, 1]
