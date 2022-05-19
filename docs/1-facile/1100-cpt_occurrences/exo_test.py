# tests
assert compte_occurrences("e", "sciences") == 2, 'Erreur sur ce test'
assert compte_occurrences("i", "mississippi") == 4, 'Erreur sur ce test'
assert compte_occurrences("a", "mississippi") == 0, 'Erreur sur ce test'

# autres tests
assert compte_occurrences("a", "") == 0
assert compte_occurrences("a", "a") == 1
assert compte_occurrences("a", "b") == 0
assert compte_occurrences("a", "b"*1000) == 0
assert compte_occurrences("a", "a"*1000) == 1000
