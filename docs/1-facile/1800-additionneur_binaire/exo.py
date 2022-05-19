def additionneur(a, b, c):
    return (a & b) | (a & c) | (b & c), a ^ b ^ c


def addition_binaire(n1, n2):
    pass


assert additionneur(0, 0, 0) == (0, 0)
assert additionneur(1, 0, 0) == (0, 1)
assert additionneur(0, 1, 0) == (0, 1)
assert additionneur(0, 0, 1) == (0, 1)
assert additionneur(1, 1, 0) == (1, 0)
assert additionneur(0, 1, 1) == (1, 0)
assert additionneur(1, 0, 1) == (1, 0)
assert additionneur(1, 1, 1) == (1, 1)

assert addition_binaire([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 0]
assert addition_binaire([1, 0, 1, 0], [1]) == [1, 0, 1, 1]
assert addition_binaire([1, 0, 1, 0], [1,  1]) == [1, 1, 0, 1]
assert addition_binaire([1, 0, 1, 0], [1, 1, 0]) == [1, 0, 0, 0, 0]
assert addition_binaire([1, 0, 1, 0], [0]) == [1, 0, 1, 0]
assert addition_binaire([1, 0, 1, 0], [1, 0, 1, 0]) == [1, 0, 1, 0, 0]
assert addition_binaire([1, 0, 1, 0], [1, 0, 0, 0, 0]) == [1, 1, 0, 1, 0]
assert addition_binaire([1, 0, 1, 0], [1, 1, 1, 1, 1]) == [1, 0, 1, 0, 0, 1]
assert addition_binaire([1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0]) == [1, 1, 0, 1, 1, 0, 1, 1]
