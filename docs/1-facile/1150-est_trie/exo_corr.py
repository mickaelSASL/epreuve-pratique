def est_trie(tableau):
    for i in range(1, len(tableau)):
        if tableau[i-1] > tableau[i]:
            return False
    return True
