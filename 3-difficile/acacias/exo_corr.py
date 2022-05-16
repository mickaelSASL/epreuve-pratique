def max_manger(feuilles):
    n = len(feuilles)
    if n == 0:
        return 0
    maxi_sans_i, maxi_avec_i = 0, feuilles[0]
    for i in range(1, n):
        maxi_sans_i, maxi_avec_i = (
            max(maxi_avec_i, maxi_sans_i),
            feuilles[i] + maxi_sans_i
        )
    return max(maxi_avec_i, maxi_sans_i)



# tests

feuilles = [4, 25, 20, 8, 17]
assert max_manger(feuilles) == 42


feuilles = [4, 6, 5, 7, 4]
assert max_manger(feuilles) == 13
