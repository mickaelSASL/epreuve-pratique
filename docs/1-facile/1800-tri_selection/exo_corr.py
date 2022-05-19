def position_minimum(tableau, i):
    """recherche et renvoie l'indice du minimum à partir de l'indice i"""
    ind_mini = i
    for j in range(i + 1, len(tableau)):
        if tableau[j] < tableau[ind_mini]:
            ind_mini = j
    return ind_mini

def echange(tableau, i, j):
    tableau[i], tableau[j] = tableau[j], tableau[i]

def tri_selection(tableau):
    for i in range(len(tableau)):
        indice_minimum = position_minimum(tableau, i)
        echange(tableau, indice_minimum, i)
