"""
Copyright Franck CHAMBON
CC 4.0 BY SA
Pas d'utilisation commerciale
"""

import drawSvg as draw

def ajoute_grille(dessin, n, m, pas):
    def ajoute_ligne(x1, y1, x2, y2):
        dessin.append(draw.Lines(x1, y1, x2, y2,
            close=False, stroke_width=2, stroke='grey'))

        for x, y in [(x1, y1), (x2, y2)]:
            dessin.append(draw.Circle(x, y, 0.5,
                fill='grey', stroke_width=1, stroke='grey'))

    for i in range(n + 1):
        ajoute_ligne(0*pas, i*pas, m*pas, i*pas)
    for j in range(m + 1):
        ajoute_ligne(j*pas, 0*pas, j*pas, n*pas)

def ajoute_chemin_lukasiewicz(dessin, chemin, pas):
    x1, y1 = 0, 0
    dessin.append(draw.Circle(x1, y1, 3,
            fill='red', stroke_width=2, stroke='red'))
    dx = 1
    for dy in chemin:
        x2, y2 = x1 + pas*dx, y1 + pas*dy
        dessin.append(draw.Lines(
            x1, y1, x2, y2,
            close=False, fill='none', stroke_width=4, stroke='red'))
        dessin.append(draw.Circle(x2, y2, 3,
                fill='red', stroke_width=2, stroke='red'))
        x1, y1 = x2, y2


def arbre_vers_chemin(arbre):
    "correspondance de Łukasiewicz"
    def etape(arbre):
        "Fonction récursive interne"
        resultat = [len(arbre)]
        for sous_arbre in arbre:
            resultat.extend(etape(sous_arbre))
        return resultat

    chemin = [y - 1 for y in etape(arbre)]
    chemin.pop()
    return chemin


def chemin_vers_arbre(chemin):
    "correspondance de Łukasiewicz"
    def etape(temp, i):
        "Fonction récursive interne"
        if temp[i] == 0:
            return [], 1
        else:
            resultat = []
            taille_totale = 1
            for _ in range(temp[i]):
                sous_arbre, taille = etape(temp, i + taille_totale)
                taille_totale += taille
                resultat.append(sous_arbre)
        return resultat, taille_totale

    n = 1 + len(chemin)
    temp = [y + 1 for y in chemin] + [0]
    arbre, taille = etape(temp, 0)
    return arbre


bulle, dx, dy = 4, 16, 32
def largeur(arbre):
    if arbre == []:
        return bulle
    else:
        return (
            sum(largeur(sous_arbre) for sous_arbre in arbre)
            + dx * (len(arbre) - 1)
        )

def hauteur(arbre):
    if arbre == []:
        # c'est une feuille, pas un arbre vide !!!
        return 0
    else:
        return dy + max(hauteur(sous_arbre) for sous_arbre in arbre)

def ajoute_arbre(dessin, arbre, x1, y1):
    dessin.append(draw.Circle(x1, y1, bulle,
            fill='red', stroke_width=2, stroke='red'))
    x2 = x1 - largeur(arbre) // 2
    y2 = y1 - dy
    for sous_arbre in arbre:
        x2 += largeur(sous_arbre) // 2
        dessin.append(draw.Lines(
            x1, y1, x2, y2,
            close=False, fill='none', stroke_width=4, stroke='red'))
        dessin.append(draw.Circle(x2, y2, bulle,
                fill='red', stroke_width=2, stroke='red'))
        ajoute_arbre(dessin, sous_arbre, x2, y2)
        x2 += largeur(sous_arbre) // 2 + dx

def ajoute_arbre_bin(dessin, arbre, x1, y1):
    x2 = x1 - largeur(arbre) // 2
    y2 = y1 - dy
    for sous_arbre in arbre:
        if sous_arbre == []:
            couleur = 'lightblue'
        else:
            couleur = 'red'
        x2 += largeur(sous_arbre) // 2
        dessin.append(draw.Lines(
            x1, y1, x2, y2,
            close=False, fill='none', stroke_width=4, stroke=couleur))
        dessin.append(draw.Circle(x2, y2, bulle,
                fill=couleur, stroke_width=2, stroke=couleur))
        ajoute_arbre_bin(dessin, sous_arbre, x2, y2)
        x2 += largeur(sous_arbre) // 2 + dx
    if arbre == []:
        couleur = 'lightblue'
    else:
        couleur = 'red'
    dessin.append(draw.Circle(x1, y1, bulle,
            fill=couleur, stroke_width=2, stroke=couleur))

def gen_arbres(n):
    if n == 0:
        yield []
    else:
        for k in range(n):
            for gauche in gen_arbres(k):
                for droite in gen_arbres(n - 1 - k):
                    yield [gauche, droite]




nb_noeud = 4
for i, arbre in enumerate(gen_arbres(nb_noeud)):
    pas = 16
    marge = 8
    l = largeur(arbre)
    h = hauteur(arbre)

    d = draw.Drawing(
        l + 2*marge,
        h + 2*marge,
        origin=(-l // 2 - marge, - marge),
        displayInline=False
    )

    ajoute_arbre_bin(d, arbre, 0, h)
    d.saveSvg(f'arbre_{i}.svg')
    print(f"![](images/arbre_{i}.svg)")


