def syracuse(n):
    suite = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        suite.append(n)
    return suite



# tests

assert syracuse(7) == [
    7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert syracuse(3) == [3, 10, 5, 16, 8, 4, 2, 1]
assert syracuse(1) == [1]
