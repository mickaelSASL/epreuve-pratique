def occurrence_lettres(phrase):
    occurrences = dict()
    for caractere in phrase:
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            occurrences[caractere] = 1
    return occurrences




# tests

assert occurrence_lettres("Bonjour à tous !") == {
    'B': 1, 'o': 3, 'n': 1, 'j': 1, 'u': 2, 'r': 1,
    ' ': 3, 'à': 1, 't': 1, 's': 1, '!': 1
}

assert occurrence_lettres("ababbab") == {"a": 3, "b": 4}
