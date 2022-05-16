def anniversaires(naissances, mois):
    personnes_anniversaire = []
    for prenom, mois_naissance in naissances.items():
        if mois_naissance == mois:
            personnes_anniversaire.append(prenom)
    return personnes_anniversaire

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
