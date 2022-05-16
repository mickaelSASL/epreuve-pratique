def moyenne(notes_ponderes):
    ...





# tests

def sont_proches(x, y):
    "Renvoie un booléen : les nombres x et y sont-ils proches ?"
    return abs(x - y) < 10**-6

assert sont_proches(moyenne([(15.0, 2)]), 15.0)
assert sont_proches(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]), 12.5)
