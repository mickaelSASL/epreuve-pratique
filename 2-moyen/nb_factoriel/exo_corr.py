factorielle_mem = [1]

def factorielle(n):
    i = len(factorielle_mem)
    while n >= i:
        fact_im1 = factorielle_mem[i - 1]
        fact_i = fact_im1 * i
        factorielle_mem.append(fact_i)
        i += 1
    return factorielle_mem[n]

# tests

assert factorielle(5) == 120
assert factorielle(10) == 3628800
