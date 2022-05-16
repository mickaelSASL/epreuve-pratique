def additionneur(a, b, c):
    return (a & b) | (a & c) | (b & c), a ^ b ^ c


def addition_binaire(n1, n2):
    difference = len(n1) - len(n2)
    if difference > 0:
        n2 = [0] * difference + n2
    else:
        n1 = [0] * (-difference) + n1
    retenue: int = 0
    resultat: list[int] = []
    for i in range(len(n1)):
        retenue, bit = additionneur(n1[len(n1) - 1 - i], n2[len(n1) - 1 - i], retenue)
        resultat = [bit] + resultat
    if retenue == 1:
        resultat = [retenue] + resultat
    return resultat


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
