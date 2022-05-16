hipparque_mem = [None, 1, 1]

def hipparque(n):
    i = len(hipparque_mem)
    while n >= i:
        difference = (
              (6*i - 9) * hipparque_mem[i - 1]
            - (i - 3) * hipparque_mem[i - 2]
        )
        suivant = difference // i
        hipparque_mem.append(suivant)
        i += 1
    return hipparque_mem[n]


# tests

assert hipparque(3) == 3
assert hipparque(4) == 11
assert hipparque(5) == 45
