# Tests
assert top_likes({'Bob': 102, 'Ada': 201, 'Alice': 103,
                  'Tim': 50}) == ('Ada', 201)
assert top_likes({'Alan': 222, 'Ada': 201, 'Eve': 222,
                  'Tim': 50}) == ('Alan', 222)
assert top_likes({'David': 222, 'Ada': 201, 'Alan': 222,
                  'Tim': 50}) == ('Alan', 222)

# Tests supplémentaires
assert top_likes({'David': 12, 'DaviD': 12, 'david': 12}) == ('DaviD', 12)
assert top_likes({'David': 1, 'Charles': 2, 'Bertrand': 3}) == ('Bertrand', 3)
assert top_likes({'David': 1, 'Bertrand': 3, 'Charles': 2}) == ('Bertrand', 3)
assert top_likes({'David': 10, 'Bertrand': 3, 'Charles': 2}) == ('David', 10)
assert top_likes({'David': 0, 'Ada': 0, 'Alan': 0, 'Tim': 0}) == (
    'Ada', 0), """Erreur si personne n'a de "like"."""
