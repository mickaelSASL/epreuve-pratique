# tests

assert est_trie([0, 5, 8, 8, 9])
assert not est_trie([8, 12, 4])
assert est_trie([-1, 4])
assert est_trie([5])
assert est_trie([])


# Autres tests

assert not est_trie([5, 4, 3, 2, 1, 0])
assert not est_trie([1, 2, 3, 4, 0])
assert est_trie([10, 10, 10, 10])
assert est_trie([-9, -9, -8, -6, -3, -2, 0, 4, 6, 7, 7, 7])
