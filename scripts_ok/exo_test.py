assert compte_occurrences("e", "sciences") == 2, 'Erreur sur ce test'
assert compte_occurrences("i", "mississippi") == 4, 'Erreur sur ce test'
assert compte_occurrences("a", "mississippi") == 0, 'Erreur sur ce test'

test_1 = compte_occurrences("a", "") == 0
test_2 = compte_occurrences("a", "a") == 1
test_3 = compte_occurrences("a", "b") == 0
test_4 = compte_occurrences("a", "b"*1000) == 0
test_5 = compte_occurrences("a", "a"*1000) == 1000
secret = all([test_1, test_2, test_3, test_4, test_5])
assert secret, "Erreur sur un test secret"
