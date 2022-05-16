from copy import deepcopy
import numpy as np
import drawSvg as draw


def dessiner(figure, fichier):
    w, h = TAILLE_CASE*(len(grille[0])+2), TAILLE_CASE*(len(grille)+2)
    d = draw.Drawing(w, h, origin=(0, 0))

    r = draw.Rectangle(0, 0, w, h, fill='white')
    d.append(r)

    for y in range(len(figure)):
        for x in range(len(figure[y])):
            r = draw.Rectangle(TAILLE_CASE+x*TAILLE_CASE,
                               TAILLE_CASE+h-(y+3)*TAILLE_CASE,
                               TAILLE_CASE, TAILLE_CASE, fill=couleurs[figure[y][x]],
                               strokewidth=2,
                               stroke=COULEUR_GRILLE)
            d.append(r)

    for y in range(len(figure)):
        d.append(draw.Text(str(y),
                           TAILLE_POLICE,
                           (4*TAILLE_CASE)//5,
                           h-(y+1.5)*TAILLE_CASE,
                           text_anchor='end',
                           valign='middle'))

    for x in range(len(figure[0])):
        d.append(draw.Text(str(x),
                           TAILLE_POLICE,
                           1.5*TAILLE_CASE+x*TAILLE_CASE,
                           h-0.5*TAILLE_CASE,
                           text_anchor='middle',
                           valign='middle'))

    d.saveSvg(f'{fichier}.svg')


def percolation(grille: list[list[int]], x: int, y: int, prof_max: int) -> bool:
    """Inonde la grille. Renvoie vrai si on arrive à la ligne de prof_max, Faux sinon

    Args:
        grille (list[list[int]]): la grille dans laquelle on évolue
        x (int): l'abscisse position de la goutte
        y (int): l'ordonnée de la goutte
        prof_max (int): la profondeur maximale à atteindre

    Returns:
        bool: [description]
    """
    global etape
    etape += 1
    dessiner(figure, f"percolation{etape}")

    if y == prof_max:
        return True
    else:
        explo_bas = False
        if grille[y+1][x] == VIDE and (x, y+1) not in visites:
            figure[y+1][x] = EAU
            visites.append((x, y+1))
            explo_bas = percolation(grille, x, y+1, prof_max)
            if explo_bas:
                return True

        explo_gauche = False
        if grille[y][x-1] == VIDE and (x-1, y) not in visites:
            figure[y][x-1] = EAU
            visites.append((x-1, y))
            explo_gauche = percolation(grille, x-1, y, prof_max)

        explo_droite = False
        if grille[y][x+1] == VIDE and (x+1, y) not in visites:
            figure[y][x+1] = EAU
            visites.append((x+1, y))
            explo_droite = percolation(grille, x+1, y, prof_max)

        return explo_gauche or explo_gauche or explo_droite


TERRE = 1
COULEUR_TERRE = "#cd853f"
VIDE = 0
COULEUR_VIDE = "#ffffff"
EAU = 2
COULEUR_EAU = "#1e90ff"
couleurs = {EAU: COULEUR_EAU, TERRE: COULEUR_TERRE, VIDE: COULEUR_VIDE}
COULEUR_GRILLE = "#444"
TAILLE_CASE = 40
TAILLE_POLICE = 20

grille = [
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
x_depart = 5
y_depart = 0

figure = deepcopy(grille)

depart = (5, 0)
visites = [depart]
figure[depart[1]][depart[0]] = EAU
etape = 0
print(percolation(grille, *depart, 5))
print(np.asmatrix(figure))
print(visites)
