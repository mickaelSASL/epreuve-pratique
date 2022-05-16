# tests

assert extremes([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert extremes([37, 37]) == {'min': 37, 'max': 37}
assert extremes([]) == {'min': None, 'max': None}


# autres tests

assert extremes([42]) == {'min': 42, 'max': 42}
assert extremes([-42]) == {'min': -42, 'max': -42}
assert extremes([10, -10]) == {'min': -10, 'max': 10}
assert extremes([-10, 10]) == {'min': -10, 'max': 10}
assert extremes([-10, 100, 10]) == {'min': -10, 'max': 100}
assert extremes([-10, -100, 10]) == {'min': -100, 'max': 10}
assert extremes([10, 100, -10]) == {'min': -10, 'max': 100}
assert extremes([10, -100, -10]) == {'min': -100, 'max': 10}
