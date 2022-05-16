# tests

def trier(d): return {k: list(sorted(d[k])) for k in d}

assert trier(antecedents({'a': 5, 'b': 7})) == {5: ['a'], 7: ['b']}, "exemple 1"
assert trier(antecedents({'a': 5, 'b': 7, 'c': 5})) == {5: ['a', 'c'], 7: ['b']}, "exemple 2"
assert trier(antecedents({"Paris": "P", "Lyon": "L", "Nantes": "N", "Lille": "L"})) == \
                         {"P": ["Paris"], "L": ["Lille", "Lyon"], "N": ["Nantes"]}, "exemple 3"

# autres tests

assert trier(antecedents({"Paris": "Tour Eiffel", "Rome": "Colisée", "Berlin": "Reichtag", "Londres": "Big Ben"})) == \
    {'Tour Eiffel': ['Paris'], 'Colisée': ['Rome'], 'Reichtag': ['Berlin'], 'Big Ben': ['Londres']}, \
    "test 4"
assert trier(antecedents({})) == {}, "test 5"
assert trier(antecedents({'a': 'a'})) == {'a': ['a']}, "test 6"
assert trier(antecedents({c:0 for c in "abcdef"})) == {0: list("abcdef")}, "test 7"
