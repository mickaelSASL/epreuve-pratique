# Tests
assert aplatir([[1, 2, 3, 4], [5, 6, 7, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert aplatir([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
assert aplatir([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
assert aplatir([[1], [2], [3], [4], [5], [6]]) == [1, 2, 3, 4, 5, 6]

# Tests supplémentaires
assert aplatir([[8, 7], [6, 5], [4, 3]]) == [8, 7, 6, 5, 4, 3]
assert aplatir([[1], [2], [3]]) == [1, 2, 3]
assert aplatir([[1, 1], [2, 2], [3, 3]]) == [1, 1, 2, 2, 3, 3]
assert aplatir([[1, 1]]) == [1, 1]