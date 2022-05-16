HEX_DEC = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
           'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def hex_int(seizaine, unite):
    """seizaine et unite sont les chiffres de l'écriture d'un 
    nombre en base 16 à 2 chiffres. Renvoie la valeur int en base 10"""
    return HEX_DEC[seizaine] * 16 + HEX_DEC[unite]

def html_vers_rvb(html):
    """html: str représente une couleur HTML
    renvoie le triplet représentant la couleur en RVB"""
    return hex_int(html[1], html[2]), hex_int(html[3], html[4]), hex_int(html[5], html[6])
    