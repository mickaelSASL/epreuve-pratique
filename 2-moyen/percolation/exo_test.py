# Tests
from copy import deepcopy

base_sol = [
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Test profondeur 0 (déjà atteinte)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 5, 0)
# Test profondeur 1 (atteignable)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 5, 1)
# Test profondeur 5 (atteignable)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 5, 5)
# Test profondeur 6 (non atteignable)
sol = deepcopy(base_sol)
assert not percolation(sol, 0, 5, 6)

# Tests supplémentaires
base_sol = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
]

# Test profondeur 0 (déjà atteinte)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 1, 0)
# Test profondeur 3 (atteignable)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 1, 1)
# Test profondeur 4 (non atteignable)
sol = deepcopy(base_sol)
assert not percolation(sol, 0, 1, 4)

base_sol = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Test profondeur 0 (déjà atteinte)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 1, 0)
# Test profondeur 3 (atteignable)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 1, 1)
# Test profondeur 6 (atteignable)
sol = deepcopy(base_sol)
assert percolation(sol, 0, 1, 1)
# Test profondeur 7 (non atteignable)
sol = deepcopy(base_sol)
assert not percolation(sol, 0, 1, 7)
