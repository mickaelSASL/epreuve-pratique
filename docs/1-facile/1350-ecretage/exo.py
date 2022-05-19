def limite_amplitude(x, x_min, x_max):
   ...

def ecrete(valeurs, x_min, x_max):
    valeurs_ecretees = ...
    for ...:
        y = limite_amplitude(...)
        valeurs_ecretees.append(...)
    return valeurs_ecretees


# tests
valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
attendu = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur avec ecrete({valeurs})"
