def anniversaires(naissances, mois):
    return [prenom for prenom in naissances if naissances[prenom] == mois]

# Tests


assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 1)) == []
assert sorted(anniversaires({'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 10)) == [
    'Nicolas']
assert sorted(anniversaires({'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 7)) == [
    'Antoine', 'Camille']
assert sorted(anniversaires({}, 1)) == []
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 13)) == []
