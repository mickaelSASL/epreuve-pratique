def occurrences_mini(donnees):
    mini = donnees[0]
    indices = []
    for i in range(len(donnees)):
        valeur = donnees[i]
        if valeur == mini:
            indices.append(i)
        elif valeur < mini:
            mini = valeur
            indices = [i]
    return (mini, indices)


# tests

donnees = [+13, +49, +13, +5]
assert occurrences_mini(donnees) == (5, [3])

donnees = [-84, +75, -84, 0, +16]
assert occurrences_mini(donnees) == (-84, [0, 2])
