catalan_mem = [1]

def catalan(n):
    i = len(catalan_mem)
    while n >= i:
        catalan_im1 = ...
        catalan_i = ... // (i + 1)
        catalan_mem.append(...)
        i = ...
    # ici n < len(catalan_mem)
    return ...

# tests
assert catalan(2) == 2
assert catalan(3) == 5
assert catalan(5) == 42

