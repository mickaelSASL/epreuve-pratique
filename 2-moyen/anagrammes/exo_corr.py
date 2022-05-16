def supprime_premier(chaine: str, cible: str) -> str:
    assert len(cible) == 1, "caractere doit être une chaîne de longueur 1"

    resultat = ""
    present = False
    for caractere in chaine:
        if caractere != cible:
            resultat += caractere
        elif not present:
            present = True
        else:
            resultat += caractere

    return (present, resultat)


def anagrammes(chaine1: str, chaine2: str) -> bool:
    assert len(chaine1) == len(
        chaine2), "Les deux chaînes doivent avoir la même taille"

    if len(chaine1) == 1:
        return chaine1 == chaine2
    else:
        cible = chaine1[0]
        vrai, chaine1_sans_cible = supprime_premier(chaine1, cible)
        cible_dans_2, chaine2_sans_cible = supprime_premier(chaine2, cible)
        if cible_dans_2:
            return anagrammes(chaine1_sans_cible, chaine2_sans_cible)
        else:
            return False


# Tests
assert supprime_premier('ukulélé', 'u') == (True, 'kulélé')
assert supprime_premier('ukulélé', 'é') == (True, 'ukullé')
assert supprime_premier('ukulélé', 'a') == (False, 'ukulélé')
assert anagrammes('chien', 'niche')
assert anagrammes('énergie noire', 'reine ignorée')
assert not anagrammes('louve', 'poule')

# Tests supplémentaires
assert supprime_premier('mississippi', 'm') == (True, 'ississippi')
assert supprime_premier('mississippi', 'a') == (False, 'mississippi')
assert anagrammes('nsi', 'isn')
assert not anagrammes('nsi', 'snt')
assert anagrammes('clint  eastwood', 'old west action')
assert anagrammes('astronomers ', 'moon starers')
assert not anagrammes('astronome', 'metronome')
