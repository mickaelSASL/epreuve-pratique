def compte_occurrences(caractere, mot):
    "version possible : itération avec indice"
    nb_occurrences = 0
    for i in range(len(mot)):
        if mot[i] == caractere:
            nb_occurrences += 1
    return nb_occurrences

def compte_occurrences(caractere, mot):
    "version recommandée : itération sans indice"
    nb_occurrences = 0
    for lettre in mot:
        if lettre == caractere:
            nb_occurrences += 1
    return nb_occurrences

def compte_occurrences(caractere, mot):
    "version interdite : avec facilité du langage Python"
    return mot.count(caractere)
