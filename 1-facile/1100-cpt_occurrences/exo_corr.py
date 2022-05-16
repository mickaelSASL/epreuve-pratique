def compte_occurrences(caractere, mot):
    nb_occurrences = 0
    for lettre in mot:
        if lettre == caractere:
            nb_occurrences += 1
    return nb_occurrences

# tests
assert compte_occurrences("e", "sciences") == 2, 'Erreur sur ce test'
assert compte_occurrences("i", "mississippi") == 4, 'Erreur sur ce test'
assert compte_occurrences("a", "mississippi") == 0, 'Erreur sur ce test'
