def limite_amplitude(x, x_min, x_max):
   if x < x_min:
       return x_min
   elif x > x_max :
       return x_max
   else:
       return x

def ecrete(valeurs, x_min, x_max):
    valeurs_ecretees = []
    for x in valeurs:
        y = limite_amplitude(x, x_min, x_max)
        valeurs_ecretees.append(y)
    return valeurs_ecretees

# tests
valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
attendu = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur avec ecrete({valeurs})"
