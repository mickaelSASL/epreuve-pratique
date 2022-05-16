def nb_sommes(n):
    def nb_k_sommes(n, k):
        if n < k:
            return 0
        elif k == 1:
            return 1
        else:
            return nb_k_sommes(n - 1, k - 1) + nb_k_sommes(n - k, k)
    
    return sum(nb_k_sommes(n, k) for k in range(1, 1 + n))


# tests

assert nb_sommes(3) == 3
assert nb_sommes(5) == 7


# autres tests

assert nb_sommes(1) == 1
assert nb_sommes(2) == 2
assert nb_sommes(4) == 5
assert nb_sommes(10) == 42
assert nb_sommes(42) == 53174

