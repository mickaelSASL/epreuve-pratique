def nb_max_consecutifs(motif, phrase):
    nb_max = 0
    nb_courant = 0
    for caractere in phrase:
        if caractere == motif:
            nb_courant += 1
            if nb_courant > nb_max:
                nb_max = nb_courant
        else:
            nb_courant = 0
    return nb_max



# tests

phrase = "Dans une phrase !!! écrite !!! certains utilisateurs abusent des points d'exclamations !! Ce pour différentes raisons ! Bref."
assert nb_max_consecutifs("!", phrase) == 3

phrase = "Un mot    puis        un        autre avec espaces."
assert nb_max_consecutifs(" ", phrase) == 8

expression = "((2 * x + 3) / (x + 1))"
assert nb_max_consecutifs("(", expression) == 2
assert nb_max_consecutifs("-", expression) == 0
