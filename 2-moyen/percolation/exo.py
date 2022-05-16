TERRE = 1
VIDE = 0
EAU = 2


def percolation(sol, i, j, prof_max):
    sol[i][j] = ...

    if ... == ...:
        return True
    else:
        if ... == VIDE:
            if percolation(sol, ..., ..., prof_max):
                return True

        ...

        ...

        return False


# Tests
# Test profondeur 0 (déjà atteinte)
sol = nouveau_sol()
assert percolation(sol, 0, 5, 0)
# Test profondeur 1 (atteignable)
sol = nouveau_sol()
assert percolation(sol, 0, 5, 1)
# Test profondeur 5 (atteignable)
sol = nouveau_sol()
assert percolation(sol, 0, 5, 5)
# Test profondeur 6 (non atteignable)
sol = nouveau_sol()
assert not percolation(sol, 0, 5, 6)
