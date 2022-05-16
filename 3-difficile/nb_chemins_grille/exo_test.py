# tests

assert nb_chemins(3, 3) == 20
assert nb_chemins(4, 2) == 15
assert nb_chemins(4, 3) == 35

# autres tests

NB_CHEMINS = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, ],
    [1, 3, 6, 10, 15, 21, 28, 36, 45, ],
    [1, 4, 10, 20, 35, 56, 84, 120, 165, ],
    [1, 5, 15, 35, 70, 126, 210, 330, 495, ],
    [1, 6, 21, 56, 126, 252, 462, 792, 1287, ],
    [1, 7, 28, 84, 210, 462, 924, 1716, 3003, ],
    [1, 8, 36, 120, 330, 792, 1716, 3432, 6435, ],
    [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, ],
]

for n in range(9):
    for m in range(9):
        attendu = NB_CHEMINS[n][m]
        assert nb_chemins(n, m) == attendu, f"Erreur avec n = {n} et m = {m}."
