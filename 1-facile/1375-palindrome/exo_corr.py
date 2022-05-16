def cree_palindrome(mot, palindrome):
    sortie = mot + palindrome
    l = len(mot)
    for i in range(l):
        sortie += mot[l - 1 - i]
    return sortie



# tests

assert cree_palindrome("ka", "y") == 'kayak'
assert cree_palindrome("ser", "") == 'serres'
assert cree_palindrome("r", "ada") == 'radar'
assert cree_palindrome("ar", "fettttef") == 'arfettttefra'

