def extremes(valeurs):
    if valeurs == []:
        return {'min': None, 'max': None}
    else:
        mini = valeurs[0]
        maxi = valeurs[0]
        for x in valeurs:
            if x < mini:
                mini = x
            if x > maxi:
                maxi = x
        return {'min': mini, 'max': maxi}

# tests

assert extremes([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert extremes([]) == {'min': None, 'max': None}
