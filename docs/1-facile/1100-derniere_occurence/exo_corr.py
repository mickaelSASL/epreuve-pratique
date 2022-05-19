def derniere_occurrence(tableau, cible):
    indice_dernier = len(tableau)
    for i in range(len(tableau)):
        if tableau[i] == cible:
            indice_dernier = i
    return indice_dernier
