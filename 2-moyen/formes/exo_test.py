# tests

assert ligne_pleine('M', 1) == "M"
assert ligne_pleine('#', 5) == "#####"

assert ligne_creuse('Y', 1) == "Y"
assert ligne_creuse('X', 5) == "X   X"

assert rectangle_plein('B', 1, 5) == ["BBBBB"]
assert rectangle_plein('A', 3, 5) == [
    "AAAAA",
    "AAAAA",
    "AAAAA",
]

assert rectangle_creux('P', 1, 5) == ["PPPPP"]
assert rectangle_creux('O', 3, 5) == [
    "OOOOO",
    "O   O",
    "OOOOO",
]

assert triangle_plein('S', 1) == ["S"]
assert triangle_plein('T', 5) == [
    "T",
    "TT",
    "TTT",
    "TTTT",
    "TTTTT",
]

assert triangle_creux('G', 1) == ["G"]
assert triangle_creux('F', 5) == [
    "F",
    "FF",
    "F F",
    "F  F",
    "FFFFF",
]

# autres tests

assert ligne_pleine('P', 7) == "PPPPPPP"

assert ligne_creuse('P', 7) == "P     P"

assert rectangle_plein('1', 3, 1) == [
    "1",
    "1",
    "1",
]

assert rectangle_plein('8', 3, 8) == [
    "88888888",
    "88888888",
    "88888888",
]

assert rectangle_creux('C', 1, 7) == ["CCCCCCC"]
assert rectangle_creux('C', 3, 1) == [
    "C",
    "C",
    "C",
]
assert rectangle_creux('C', 4, 6) == [
    "CCCCCC",
    "C    C",
    "C    C",
    "CCCCCC",
]
