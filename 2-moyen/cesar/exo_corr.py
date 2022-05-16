def position_lettre(lettre):
    return ord(lettre) - ord('A')

def nouvelle_lettre(indice):
    return chr(ord('A') + indice)

def cesar(message, decalage):
    resultat = ''
    for caractere in message:
        if 'A' <= caractere <= 'Z':
            indice = (position_lettre(caractere) + decalage) % 26
            resultat = resultat + nouvelle_lettre(indice)
        else:
            resultat = resultat + caractere
    return resultat

# tests

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
