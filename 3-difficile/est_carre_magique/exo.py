def est_carre_magique(carre):
    ...





# tests

ex_ordre_3 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8],
]
assert est_carre_magique(ex_ordre_3)

contre_ex_ordre_2 = [
    [2, 2],
    [2, 2],
]
assert not est_carre_magique(contre_ex_ordre_2)

ex_ordre_4 = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1], 
]
assert est_carre_magique(ex_ordre_4)

