def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(effectifs_votes):
    nb_votes_max = 0
    for candidat in effectifs_votes:
        nb_voix = effectifs_votes[candidat] 
        if nb_voix > nb_votes_max:
            nb_votes_max = nb_voix
    gagnants = [nom for nom in effectifs_votes if effectifs_votes[nom] == nb_votes_max]
    return gagnants
