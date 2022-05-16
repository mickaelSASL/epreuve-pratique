# Tests
assert gelees([2, -3, -2, 0, 1, -1]) == 3
assert gelees([3, 2, 2]) == 0
assert gelees([]) == 0

# Tests supplémentaires
assert gelees([-2, -3, -2, 0, -1, -1]) == 6
assert gelees([0, 0, 0]) == 3
assert gelees([1]*1000+[-1]+[1]*1000) == 1
