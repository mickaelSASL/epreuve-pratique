# test de la fonction donnée
assert additionneur(0, 0, 0) == (0, 0)
assert additionneur(1, 0, 0) == (0, 1)
assert additionneur(0, 1, 0) == (0, 1)
assert additionneur(0, 0, 1) == (0, 1)
assert additionneur(1, 1, 0) == (1, 0)
assert additionneur(0, 1, 1) == (1, 0)
assert additionneur(1, 0, 1) == (1, 0)
assert additionneur(1, 1, 1) == (1, 1)

# test de l'exemple
assert addition_binaire([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 0]
assert addition_binaire([1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0]) == [1, 1, 0, 1, 1, 0, 1, 1]

# test basique
assert addition_binaire([1, 0, 1, 0], [1]) == [1, 0, 1, 1]
assert addition_binaire([1, 0, 1, 0], [1,  1]) == [1, 1, 0, 1]
assert addition_binaire([1, 0, 1, 0], [1, 1, 0]) == [1, 0, 0, 0, 0]
assert addition_binaire([1, 0, 1, 0], [0]) == [1, 0, 1, 0]

# test ordre des nombres
assert addition_binaire([1, 0, 1, 0], [1, 0, 1, 0]) == [1, 0, 1, 0, 0]
assert addition_binaire([1, 0, 1, 0], [1, 0, 0, 0, 0]) == [1, 1, 0, 1, 0]
assert addition_binaire([1, 0, 1, 0], [1, 1, 1, 1, 1]) == [1, 0, 1, 0, 0, 1]
