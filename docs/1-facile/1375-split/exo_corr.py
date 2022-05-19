def decoupe_mots(discours):
    mots = list()
    mot = ""
    for caractere in discours:
        if caractere != " ":
            mot += caractere
        else:
            if len(mot) >= 4:
                mots.append(mot)
            mot = ""
    return mots

# tests

discours = "je peux vous dire aujourd hui mes amis qu en depit des difficultes et des frustrations actuelles j ai quand meme fait un reve c est un reve profondement enracine dans le reve americain "

assert decoupe_mots(discours) == [
    'peux', 'vous', 'dire', 'aujourd', 'amis', 'depit',
    'difficultes', 'frustrations', 'actuelles', 'quand',
    'meme', 'fait', 'reve', 'reve', 'profondement',
    'enracine', 'dans', 'reve', 'americain'
]

test_2 = "abcd azerty  xyz   azerty     "

assert decoupe_mots(test_2) == ["abcd", "azerty", "azerty"]
