# tests

assert occurrence_lettres("Bonjour à tous !") == {
    'B': 1, 'o': 3, 'n': 1, 'j': 1, 'u': 2, 'r': 1,
    ' ': 3, 'à': 1, 't': 1, 's': 1, '!': 1
}

assert occurrence_lettres("ababbab") == {"a": 3, "b": 4}


# autres tests

assert occurrence_lettres("") == dict()
assert occurrence_lettres("d") == {'d': 1}
assert occurrence_lettres("d" * 100) == {'d': 100}
assert occurrence_lettres("d" * 100 + "r" * 50) == {'d': 100, 'r': 50}
