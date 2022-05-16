def top_likes(likes):
    max_pseudo = ""
    max_likes = -1
    for pseudo in likes:
        if likes[pseudo] > max_likes:
            max_pseudo = pseudo
            max_likes = likes[pseudo]
        elif likes[pseudo] == max_likes and pseudo < max_pseudo:
            max_pseudo = pseudo
            max_likes = likes[pseudo]
    return (max_pseudo, max_likes)


# Tests
assert top_likes({'Bob': 102, 'Ada': 201, 'Alice': 103,
                  'Tim': 50}) == ('Ada', 201)
assert top_likes({'Alan': 222, 'Ada': 201, 'Eve': 222,
                  'Tim': 50}) == ('Alan', 222)
assert top_likes({'David': 222, 'Ada': 201, 'Alan': 222,
                  'Tim': 50}) == ('Alan', 222)