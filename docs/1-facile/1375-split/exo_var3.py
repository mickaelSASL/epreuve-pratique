def decoupe_mots(discours):
    mots = list()
    lettres = list()
    for caractere in discours:
        if caractere != " ":
            lettres.append(caractere)
        else:
            if len(lettres) >= 4:
                mots.append("".join(lettres))
            lettres = list()
    return mots
