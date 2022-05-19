# tests

tableau1 = [1, 2, 3, 6, 2, 4, 5]
assert tous_differents(tableau1) == False

tableau2 = ['chien', 'chat', 'lion', 'poisson']
assert tous_differents(tableau2) == True

# autres tests
assert tous_differents([]) == True
assert tous_differents([1, 1]) == False
assert tous_differents([9, 6, 7, 3, 2, 1, 1]) == False
assert tous_differents(range(100)) == True
assert tous_differents(['v', 'o', 'i', 't', 'u', 'r', 'e']) == True
assert tous_differents(['a', 'a', 'b', 'c', 'd', 'e']) == False
assert tous_differents([1, 2, 3, 4, 1]) == False
assert tous_differents([5, 9, 1, 2, 1, 3, 7]) == False
assert tous_differents([1, 2, 3, 4, 3, 2, 1]) == False
assert tous_differents(['a', 'a', 1, 1, "truc", "truc"]) == False
assert tous_differents(["bob"]) == True
