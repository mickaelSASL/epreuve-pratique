VOYELLES = ['a', 'e', 'i', 'o', 'u', 'y']

def dentiste(texte):
    resultat = ''
    for lettre in texte:
        if lettre in VOYELLES:
            resultat = resultat + lettre
    return resultat

# tests

assert dentiste("j'ai mal") == 'aia'
assert dentiste("il fait chaud") == 'iaiau'
assert dentiste("") == ''
