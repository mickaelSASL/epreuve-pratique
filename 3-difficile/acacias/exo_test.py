# tests

feuilles = [4, 25, 20, 8, 17]
assert max_manger(feuilles) == 42


feuilles = [4, 6, 5, 7, 4]
assert max_manger(feuilles) == 13

# autres tests

assert max_manger([9]) == 9
assert max_manger([]) == 0

feuilles = [0, 1] * 100
assert max_manger(feuilles) == 100
feuilles = [2, 1] * 100
assert max_manger(feuilles) == 200

feuilles = [1, 2, 1] * 20
assert max_manger(feuilles) == 40

feuilles = [1, 2, 3] * 20
assert max_manger(feuilles) == 61

