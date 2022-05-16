factorielle_mem = [1]

def factorielle(n):
    i = len(factorielle_mem)
    while n >= i:
        fact_im1 = ...
        fact_i = ...
        factorielle_mem.append(...)
        i = ...
    return ...

# tests

assert factorielle(5) == 120
assert factorielle(10) == 3628800
