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


assert decoupe_mots("") == []
assert decoupe_mots(" ") == []
assert decoupe_mots("a b c d ") == []
assert decoupe_mots("a bc def ghij ") == ["ghij"]
assert decoupe_mots("abcd efg hi j ") == ["abcd"]
assert decoupe_mots("     abcd     abcd     ") == ["abcd", "abcd"]


