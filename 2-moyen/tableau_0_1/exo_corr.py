def separe(zeros_et_uns):
    """place tous les 0 de zeros_et_uns à gauche et tous les 1 à droite"""
    debut = 0  # indice de début
    fin = len(zeros_et_uns) - 1    # indice de fin
    while debut < fin:
        if zeros_et_uns[debut] == 0:
            debut = debut + 1
        else:
            zeros_et_uns[debut] = zeros_et_uns[fin]
            zeros_et_uns[fin] = 1
            fin = fin - 1


# tests

tableau1 = [0, 1, 0, 1, 0, 1, 0]
separe(tableau1)
assert tableau1 == [0, 0, 0, 0, 1, 1, 1]

tableau2 = [1, 1, 1, 0, 0, 0]
separe(tableau2)
assert tableau2 == [0, 0, 0, 1, 1, 1]
