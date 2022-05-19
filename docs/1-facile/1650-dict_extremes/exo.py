def extremes(valeurs):
    ...





# tests

assert extremes([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert extremes([37, 37]) == {'min': 37, 'max': 37}
assert extremes([]) == {'min': None, 'max': None}
