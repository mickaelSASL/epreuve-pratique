def inverse_chaine(chaine):
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbr_palindrome(nombre):
    chaine = str(nombre)
    return est_palindrome(chaine)


# tests

assert inverse_chaine('bac') == 'cab'

assert not est_palindrome('NSI')

assert est_palindrome('ISN-NSI')

assert not est_nbr_palindrome(214312)

assert est_nbr_palindrome(213312)
