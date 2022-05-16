def maximum(nombres):
    ...


def tri_denombrement(nombres):
    maxi = ...

    effectifs = [0] * (maxi + 1)

    for nb in nombres:
        ...

    # On crée une nouvelle liste
    # pour stocker les nombres triés
    nombres_tries = []
    for n in range(maxi + 1):
        for i in ...:
            ...

    return nombres_tries


# Tests
liste = [4, 5, 4, 2]
tri_denombrement(liste)
assert liste == [2, 4, 4, 5]
liste = [3, 8, 7, 3, 5]
tri_denombrement(liste)
assert liste == [3, 3, 5, 7, 8]
liste = [1, 2, 3, 4, 5]
tri_denombrement(liste)
assert liste == [1, 2, 3, 4, 5]
liste = [5, 4, 3, 2, 1]
tri_denombrement(liste)
assert liste == [1, 2, 3, 4, 5]
liste = []
tri_denombrement(liste)
assert liste == []
