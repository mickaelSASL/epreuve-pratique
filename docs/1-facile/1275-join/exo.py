def supprimheu(mots):
    ...




# tests

assert supprimheu(["je", "heu", "vais", "coder", "heu", "la",
 "fonction", "supprimheu"]) == 'je vais coder la fonction supprimheu'

assert supprimheu(["c", "est", "facile"]) == 'c est facile'
