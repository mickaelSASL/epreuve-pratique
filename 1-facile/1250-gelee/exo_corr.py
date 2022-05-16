def gelees(temperatures):
    plus_longue_periode = 0
    periode = 0
    for temp in temperatures:
        if temp <= 0:
            periode += 1
            if periode > plus_longue_periode:
                plus_longue_periode = periode
        else:
            periode = 0
    return plus_longue_periode


# Tests
assert gelees([2, -3, -2, 0, 1, -1]) == 3
assert gelees([3, 2, 2]) == 0
assert gelees([]) == 0
