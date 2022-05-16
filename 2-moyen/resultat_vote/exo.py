def depouille(urne):
    resultat = ...
    for bulletin in urne:
        if ...:
            resultat[bulletin] = ...
        else:
            ...
    return resultat

def vainqueur(effectifs_votes):
    nb_votes_max = 0
    for candidat in effectifs_votes:
        nb_voix = ... 
        if ... > ...:
            nb_votes_max = ...
    gagnants = [nom for nom in effectifs_votes if effectifs_votes[nom] == ...]
    return ...

urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit']

urne_2 = ['Poons', 'DrRed', 'Soleran', 'Mimeen', 'Poons', 'Soleran', 'Mimeen', 'Zajy', 'Soleran', 'DrRed', 'Zajy', 'Kashur', 'Mimeen']

# tests

assert vainqueur(depouille(urne)) == ['Extra Vomit']
assert sorted(vainqueur(depouille(urne_2))) == ['Mimeen', 'Soleran']
