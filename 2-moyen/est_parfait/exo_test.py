# tests

assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)

# autres tests

def EST_PARFAIT(mot) :
    code_int_cumul = 0
    code_str_concatene = ""
    for lettre in mot:
        valeur = ord(lettre) - ord('A') + 1
        code_int_cumul += valeur
        code_str_concatene += str(valeur)
    code_concatene = int(code_str_concatene)
    mot_est_parfait = (code_concatene % code_int_cumul == 0)  # un booléen
    return (code_int_cumul, code_concatene, mot_est_parfait)

for i in range(26):
    mot = chr(ord('A') + i)
    resultat = est_parfait(mot)
    attendu = EST_PARFAIT(mot)
    assert attendu == resultat, f"Erreur avec le mot {mot}"

for j in range(26):
    for j in range(26):
        mot = chr(ord('A') + i) + chr(ord('A') + j)
        resultat = est_parfait(mot)
        attendu = EST_PARFAIT(mot)
        assert attendu == resultat, f"Erreur avec le mot {mot}"


