assert hex_int('B', '5') == 181, "Échec hex_int exemple 1 de l'énoncé"
assert hex_int('0', '0') == 0, "Échec hex_int exemple 2 de l'énoncé"


assert html_vers_rvb("#C0392B'") == (192, 57, 43), "Échec html_vers_rvb exemple 1"
assert html_vers_rvb("#00FF00") == (0, 255, 0), "Échec html_vers_rvb exemple 2"
assert html_vers_rvb("#000000") == (0, 0, 0), 'Échec html_vers_rvb exemple 3'


assert html_vers_rvb("#FFFFFF") == (255, 255, 255), "Échec html_vers_rvb autre exemple 1"
assert html_vers_rvb("#888888") == (136, 136, 136), "Échec html_vers_rvb autre exemple 2"
assert html_vers_rvb("#760017") == (118, 0, 23), "Échec html_vers_rvb autre exemple 3"

