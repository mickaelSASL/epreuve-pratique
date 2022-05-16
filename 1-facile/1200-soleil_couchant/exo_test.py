# autres tests
assert 0 == nb_batiments_eclaires([])
assert 0 == nb_batiments_eclaires([0])
assert 0 == nb_batiments_eclaires([0]*10)
assert 1 == nb_batiments_eclaires([1])
assert 1 == nb_batiments_eclaires([10, 5])
assert 2 == nb_batiments_eclaires([5, 10])
assert 1 == nb_batiments_eclaires([0, 10, 5, 0])
assert 2 == nb_batiments_eclaires([0, 5, 10, 0])
assert 2 == nb_batiments_eclaires([1, 10, 5, 1])
assert 3 == nb_batiments_eclaires([1, 5, 10, 1])
assert 1 == nb_batiments_eclaires([10]*5)
assert 1 == nb_batiments_eclaires([0, 10, 10, 10, 0])



# tests

assert 4 == nb_batiments_eclaires([2, 1, 2, 4, 0, 4, 5, 3, 5, 6])
assert 1 == nb_batiments_eclaires([0, 3, 1, 2])
