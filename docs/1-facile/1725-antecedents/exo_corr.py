def antecedents(dico):
    dico_antecedents = {}
    for cle, valeur in dico.items():
        if valeur not in dico_antecedents:
            dico_antecedents[valeur] = [cle]
        else:
            dico_antecedents[valeur].append(cle)
    return dico_antecedents


# tests

def trier(d): return {k: list(sorted(d[k])) for k in d}

assert trier(antecedents({'a': 5, 'b': 7})) == {5: ['a'], 7: ['b']}, "exemple 1"
assert trier(antecedents({'a': 5, 'b': 7, 'c': 5})) == {5: ['a', 'c'], 7: ['b']}, "exemple 2"
assert trier(antecedents({"Paris": "P", "Lyon": "L", "Nantes": "N", "Lille": "L"})) == \
                         {"P": ["Paris"], "L": ["Lille", "Lyon"], "N": ["Nantes"]}, "exemple 3"
