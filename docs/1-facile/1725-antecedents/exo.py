def antecedents(dico):
    ...



# tests

def trier(d): return {k: list(sorted(d[k])) for k in d}

assert trier(antecedents({'a': 5, 'b': 7})) == {5: ['a'], 7: ['b']}, "exemple 1"
assert trier(antecedents({'a': 5, 'b': 7, 'c': 5})) == {5: ['a', 'c'], 7: ['b']}, "exemple 2"
assert trier(antecedents({"Paris": "P", "Lyon": "L", "Nantes": "N", "Lille": "L"})) == \
                         {"P": ["Paris"], "L": ["Lille", "Lyon"], "N": ["Nantes"]}, "exemple 3"
