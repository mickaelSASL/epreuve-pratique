assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 1)) == []
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 10)) == ['Nicolas']
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 7)) == ['Antoine', 'Camille']
assert sorted(anniversaires(dict(), 1)) == []
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 13)) == []


# Tests supplémentaires
# Dictionnaire vide
assert sorted(anniversaires({}, 13)) == []
# Tous nés le mois cherché
assert sorted(anniversaires(
    {'Nicolas': 1, 'Antoine': 1, 'Camille': 1}, 1)) == ['Antoine', 'Camille', 'Nicolas']
# Tous nés un mois non cherché
assert sorted(anniversaires(
    {'Nicolas': 1, 'Antoine': 1, 'Camille': 1}, 10)) == []
