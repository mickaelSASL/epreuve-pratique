# tests

nb_premiers = [2, 11, 3, 7, 5]
nb_premiers_trie = [2, 3, 5, 7, 11]
tri_bulles(nb_premiers)
assert len(nb_premiers) == len(nb_premiers_trie), "Erreur, le tableau ne doit pas changer de taille"
for a, b, in zip(nb_premiers, nb_premiers_trie):
    assert a == b, "Erreur lors du tri de [2, 11, 3, 7, 5]"


seul = [42]
seul_trie = [42]
tri_bulles(seul)
assert len(seul) == 1, "Erreur, le tableau [42] ne doit pas changer de taille"
assert seul[0] == 42, "Erreur, un élément seul est déjà trié"

# autres tests

from random import sample
for i in range(10):
    nombres = list(sample(range(10**9), 100+i))
    attendu = sorted(nombres)
    tri_bulles(nombres)
    assert len(nombres) == len(attendu), "Erreur, le tableau ne doit pas changer de taille"
    for a, b, in zip(nombres, attendu):
        assert a == b, "Erreur lors du tri"
