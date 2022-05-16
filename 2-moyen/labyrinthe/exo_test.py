# tests

labyrinthe  = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

chemin_1 = "EEEEES"
chemin_2 = "SSSSSEENNNEEEEEEESSOOOOSSSEEEESS"

import copy
labyrinthe_1 = copy.deepcopy(labyrinthe)
labyrinthe_2 = copy.deepcopy(labyrinthe)

assert not verifie(labyrinthe_1, chemin_1)
assert     verifie(labyrinthe_2, chemin_2)

# autres tests
import copy

# test minimaliste

lab2 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

assert   verifie(lab2, "")

assert not verifie(lab2, "N")
assert not verifie(lab2, "S")
assert not verifie(lab2, "E")
assert not verifie(lab2, "O")


# test 4×3

lab3 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
]

lab = copy.deepcopy(lab3)
assert     verifie(lab, "S")

lab = copy.deepcopy(lab3)
assert not verifie(lab, "SNS")

lab = copy.deepcopy(lab3)
assert not verifie(lab, "N")
lab = copy.deepcopy(lab3)
assert not verifie(lab, "E")
lab = copy.deepcopy(lab3)
assert not verifie(lab, "O")


# test 3×4

lab3 = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]

lab = copy.deepcopy(lab3)
assert     verifie(lab, "E")

lab = copy.deepcopy(lab3)
assert not verifie(lab, "EOE")

lab = copy.deepcopy(lab3)
assert not verifie(lab, "N")
lab = copy.deepcopy(lab3)
assert not verifie(lab, "S")
lab = copy.deepcopy(lab3)
assert not verifie(lab, "O")

