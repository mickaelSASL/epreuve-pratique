def supprime_premier(chaine, cible):
    assert len(cible) == 1, "caractere doit être une chaîne de longueur 1"

    pass


def anagrammes(chaine1, chaine2):
    assert len(chaine1) == len(
        chaine2), "Les deux chaînes doivent avoir la même taille"

    pass

# Tests


assert supprime_premier('ukulélé', 'u') == (True, 'kulélé')
assert supprime_premier('ukulélé', 'é') == (True, 'ukullé')
assert supprime_premier('ukulélé', 'a') == (False, 'ukulélé')
assert anagrammes('chien', 'niche')
assert anagrammes('énergie noire', 'reine ignorée')
assert not anagrammes('louve', 'poule')
