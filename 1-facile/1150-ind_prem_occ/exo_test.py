# tests

assert indice(1, [10, 12, 1, 56]) == 2
assert indice(1, [1, 50, 1]) == 0
assert indice(15, [8, 9, 10, 15]) == 3
assert indice(1, [2, 3, 4]) is None


# autre tests

assert indice(1, [10, 11, 12, 13]) is None
assert indice(10, [10, 11, 12, 13]) == 0
assert indice(11, [10, 11, 12, 13]) == 1
assert indice(12, [10, 11, 12, 13]) == 2
assert indice(13, [10, 11, 12, 13]) == 3
assert indice(14, [10, 11, 12, 13]) is None

assert indice(1, [13, 12, 11, 10]) is None
assert indice(10, [13, 12, 11, 10]) == 3
assert indice(11, [13, 12, 11, 10]) == 2
assert indice(12, [13, 12, 11, 10]) == 1
assert indice(13, [13, 12, 11, 10]) == 0
assert indice(14, [13, 12, 11, 10]) is None

