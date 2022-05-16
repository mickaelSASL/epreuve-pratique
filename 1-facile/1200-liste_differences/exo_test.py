# tests

assert differences([14, 87, 22, 5, 65],
                   [14, 86, 27, 5, 65]) == [False, True, True, False, False]

assert differences([-54], [-54]) == [False]
assert differences([7, 8], [7, 11]) == [False, True]
assert differences([], []) == []

# autres tests

source_1 = list(range(20))
source_2 = list(range(20))
assert differences(source_1, source_2) == [False] * 20

source_1 = list(range(20))
source_2 = list(range(1, 21))
assert differences(source_1, source_2) == [True] * 20

source_1 = list(range(21))
source_2 = list(range(20, -1, -1))
assert differences(source_1, source_2) == [True] * 10 + [False] + [True] * 10

for i in range(20):
    source_1 = list(range(20))
    source_2 = list(range(20))
    source_2[i] = -1
    attendu = [False] * 20
    attendu[i] = True
    assert differences(source_1, source_2) == attendu
