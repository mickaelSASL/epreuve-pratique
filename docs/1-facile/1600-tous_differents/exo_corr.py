def tous_differents(tableau):
    n = len(tableau)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tableau[i] == tableau[j]:
                return False
    return True


# tests

tableau1 = [1, 2, 3, 6, 2, 4, 5]
assert tous_differents(tableau1) == False

tableau2 = ['chien', 'chat', 'lion', 'poisson']
assert tous_differents(tableau2) == True

