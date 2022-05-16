def supprimheu(mots):
    discours = ""
    for mot in mots:
        if mot != "heu":
            if discours != "":
                # on a déjà mis un mot
                discours += " "
            discours += mot
    return discours


# tests

assert supprimheu(["je", "heu", "vais", "coder", "heu", "la", "fonction", "supprimheu"]) == 'je vais coder la fonction supprimheu'

assert supprimheu(["c", "est", "facile"]) == 'c est facile'
