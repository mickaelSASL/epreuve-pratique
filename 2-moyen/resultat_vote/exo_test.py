# Tests

urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit']

urne_2 = ['Poons', 'DrRed', 'Soleran', 'Mimeen', 'Poons', 'Soleran', 'Mimeen', 'Zajy', 'Soleran', 'DrRed', 'Zajy', 'Kashur', 'Mimeen']


assert vainqueur(depouille(urne)) == ['Extra Vomit']
assert sorted(vainqueur(depouille(urne_2))) == ['Mimeen', 'Soleran']



# Autres tests

urne_3 = ['Soleran', 'Kashur', 'Poons', 'DrRed', 'Kashur', 'DrRed', 'Mimeen', 'Mimeen', 'Mimeen', 'Zajy', 'Mimeen', 'Poons', 'Soleran', 'Poons', 'Kashur', 'Zajy', 'DrRed', 'Soleran', 'DrRed', 'Kashur', 'Mimeen', 'Kashur', 'Mimeen', 'Kashur', 'Zajy', 'Poons', 'Kashur', 'Poons', 'Zajy', 'Soleran', 'DrRed', 'Mimeen', 'Zajy', 'DrRed', 'DrRed']

urne_4 = ['Poons', 'Kashur', 'Poons', 'DrRed', 'Kashur', 'DrRed', 'Mimeen', 'Mimeen', 'Mimeen', 'Poons', 'Mimeen', 'Poons', 'Soleran', 'Poons', 'Kashur', 'Zajy', 'DrRed', 'Soleran', 'DrRed', 'Kashur', 'Mimeen', 'Kashur', 'Mimeen', 'Kashur', 'Zajy', 'Poons', 'Kashur', 'Poons', 'Zajy', 'Soleran', 'DrRed', 'Mimeen', 'Zajy', 'DrRed', 'DrRed']

assert sorted(vainqueur(depouille(urne_3))) == ['DrRed', 'Kashur', 'Mimeen']
assert sorted(vainqueur(depouille(urne_4))) == ['DrRed', 'Kashur', 'Mimeen', 'Poons']
