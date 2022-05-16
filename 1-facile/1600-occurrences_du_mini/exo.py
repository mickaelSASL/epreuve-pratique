def occurrences_mini(donnees):
    ...



# tests

donnees = [+13, +49, +13, +5]
assert occurrences_mini(donnees) == (5, [3])

donnees = [-84, +75, -84, 0, +16]
assert occurrences_mini(donnees) == (-84, [0, 2])
