def code(lettre):
    "Renvoie le code suivant l'énoncé."
    return ord(lettre) - ord('A') + 1

def est_parfait(mot) :
    code_int_cumul = ...
    code_str_concatene = ""
    for lettre in mot:
        valeur = code(...)
        code_int_cumul = ...
        code_str_concatene = ...
    code_concatene = ... (code_str_concatene)
    mot_est_parfait = (... % ... == 0)  # un booléen
    return (code_int_cumul, code_concatene, mot_est_parfait)


# tests

assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)
