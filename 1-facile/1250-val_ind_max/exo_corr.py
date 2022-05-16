def valeur_et_indice_du_max(valeurs):
    if valeurs == []:
        return (None, None)
    else:
        valeur_maxi = valeurs[0]
        indice_maxi = 0
        for i in range(1, len(valeurs)):
            x = valeurs[i]
            if x > valeur_maxi:
                valeur_maxi = x
                indice_maxi = i
        return (valeur_maxi, indice_maxi)



# tests
assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert valeur_et_indice_du_max([1, 1, 1, 99, 99]) == (99, 3)
assert valeur_et_indice_du_max([10]) == (10, 0)
assert valeur_et_indice_du_max([]) == (None, None)
