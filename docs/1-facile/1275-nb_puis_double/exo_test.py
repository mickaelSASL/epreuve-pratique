# tests

assert nombres_puis_double([1, 4, 2, 5]) == []
assert nombres_puis_double([1, 3, 6, 7]) == [(3, 6)]
assert nombres_puis_double([7, 1, 2, 5, 3, 6]) == [(1, 2), (3, 6)]
assert nombres_puis_double(
    [5, 1, 2, 4, 8, -5, -10, 7]) == [(1, 2), (2, 4), (4, 8), (-5, -10)]


# corner case
assert nombres_puis_double([10, 4, 2, 5]) == [], "Attention aux indices"
