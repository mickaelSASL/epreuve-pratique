def top_likes(likes):
    ...


# Tests
assert top_likes({'Bob': 102, 'Ada': 201, 'Alice': 103,
                  'Tim': 50}) == ('Ada', 201)
assert top_likes({'Alan': 222, 'Ada': 201, 'Eve': 222,
                  'Tim': 50}) == ('Alan', 222)
assert top_likes({'David': 222, 'Ada': 201, 'Alan': 222,
                  'Tim': 50}) == ('Alan', 222)