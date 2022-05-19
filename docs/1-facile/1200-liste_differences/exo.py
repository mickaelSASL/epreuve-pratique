def differences(source_1, source_2):
    ...



# tests

assert differences([14, 87, 22, 5, 65],
                   [14, 86, 27, 5, 65]) == [False, True, True, False, False]

assert differences([-54], [-54]) == [False]
assert differences([7, 8], [7, 11]) == [False, True]
assert differences([], []) == []

