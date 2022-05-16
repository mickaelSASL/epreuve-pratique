catalan_mem = [1]

def catalan(n):
    i = len(catalan_mem)
    while n >= i:
        catalan_im1 = catalan_mem[i - 1]
        catalan_i = catalan_im1 * 2 * (2*i - 1) // (i + 1)
        catalan_mem.append(catalan_i)
        i += 1
    # ici n < len(catalan_mem)
    return catalan_mem[n]

# tests
assert catalan(2) == 2
assert catalan(3) == 5
assert catalan(5) == 42

