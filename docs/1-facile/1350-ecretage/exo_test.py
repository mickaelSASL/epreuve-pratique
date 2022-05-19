# tests
valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
attendu = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur avec ecrete({valeurs})"

# autres tests

# Question 1 :

assert limite_amplitude(-15, -10, 10) == -10, "-15 est trop petit (pas entre -10 et 10), on écrête"
assert limite_amplitude(-10, -10, 10) == -10
assert limite_amplitude( -8, -10, 10) == -8
assert limite_amplitude(  7, -10, 10) == 7
assert limite_amplitude( 10, -10, 10) == 10
assert limite_amplitude( 18, -10, 10) == 10, "18 est trop grand (pas entre -10 et 10), on écrête"

assert limite_amplitude(209, 210, 220) == 210, "209 est trop petit (pas entre 210 et 220), on écrête"
assert limite_amplitude(210, 210, 220) == 210
assert limite_amplitude(215, 210, 220) == 215
assert limite_amplitude(220, 210, 220) == 220
assert limite_amplitude(221, 210, 220) == 220, "221 est trop grand (pas entre 210 et 220), on écrête"


# Question 2 :

valeurs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
attendu = [5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10]
resultat = ecrete(valeurs, 5, 10)
assert resultat == attendu, f"Erreur avec {valeurs}"

valeurs = [-13, -4,  6,  5,  8, -3, -12, -3,  0,  6,  7]
attendu = [-10, -5, -5, -5, -5, -5, -10, -5, -5, -5, -5]
resultat = ecrete(valeurs, -10, -5)
assert resultat == attendu, f"Erreur avec {valeurs}"

valeurs = [7, 8, 3, 9, 8, 7, 2, 4, 8, 9, 0, 1, 5, 8, 8, 8, 4, 5, 4, 5]
attendu = [7, 8, 3, 9, 8, 7, 2, 4, 8, 9, 0, 1, 5, 8, 8, 8, 4, 5, 4, 5]
resultat = ecrete(valeurs, 0, 10)
assert resultat == attendu, f"Erreur avec {valeurs}"

valeurs = []
attendu = []
resultat = ecrete(valeurs, 0, 10)
assert resultat == attendu, f"Erreur avec {valeurs}"
