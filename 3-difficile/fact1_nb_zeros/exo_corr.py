nb_zeros_factorielle = [0]

def nb_zeros(n):
    resultat = 0
    while n % 10 == 0:
        n //= 10
        resultat += 1
    return resultat

factorielle = 1
for n in range(1, 1000):
    factorielle *= n
    suivant = nb_zeros(factorielle)
    nb_zeros_factorielle.append(suivant)


# tests

assert nb_zeros_factorielle[3] == 0

assert nb_zeros_factorielle[11] == 2

assert nb_zeros_factorielle[42] == 9

assert len(nb_zeros_factorielle) >= 1000
