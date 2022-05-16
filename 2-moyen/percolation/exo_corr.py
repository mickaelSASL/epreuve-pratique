TERRE = 1
VIDE = 0
EAU = 2


def percolation(sol, i, j, prof_max):
    sol[i][j] = EAU

    if i == prof_max:
        return True
    else:
        if sol[i+1][j] == VIDE:
            if percolation(sol, i+1, j, prof_max):
                return True

        if sol[i][j-1] == VIDE:
            if percolation(sol, i, j-1, prof_max):
                return True

        if sol[i][j+1] == VIDE:
            if percolation(sol, i, j+1, prof_max):
                return True

        return False


# Tests
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

from copy import deepcopy
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
