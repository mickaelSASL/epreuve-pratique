import drawSvg as draw


def dessiner(tab, multiples, premiers, nouveaux, nom_fichier):
    n = len(tab)
    nb_lignes = n // 10
    w, h = 12*LARGEUR_CASE, (2+nb_lignes)*LARGEUR_CASE
    d = draw.Drawing(w, h, origin=(0, 0))

    r = draw.Rectangle(0, 0, w, h, fill='white')
    d.append(r)

    for i, valeur in enumerate(tab):
        couleur = COULEUR_COMPOSE if (
            i in multiples or not tab[i]) else COULEUR_PREMIER if i in premiers else COULEUR_BASE
        ligne = i//10
        colonne = i % 10
        r = draw.Rectangle(LARGEUR_CASE+colonne*LARGEUR_CASE,
                           h-(ligne+2)*LARGEUR_CASE,
                           LARGEUR_CASE,
                           LARGEUR_CASE,
                           fill=couleur,
                           strokewidth=2,
                           stroke=CONTOUR_BARRE)
        d.append(r)

        d.append(draw.Text(str(i),
                           TAILLE_POLICE,
                           1.5*LARGEUR_CASE+colonne*LARGEUR_CASE,
                           h-(ligne+1.5)*LARGEUR_CASE,
                           text_anchor='middle',
                           valign='middle'))
        if i in nouveaux:
            d.append(draw.Line(LARGEUR_CASE+colonne*LARGEUR_CASE,
                               h-(ligne+2)*LARGEUR_CASE,
                               LARGEUR_CASE+(colonne+1)*LARGEUR_CASE,
                               h-(ligne+1)*LARGEUR_CASE,
                               fill=couleur,
                               stroke_width=2,
                               stroke=CONTOUR_BARRE))

    d.saveSvg(f'{nom_fichier}.svg')


def crible(n):
    premiers = []
    multiples = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    figure = 0
    nouveaux = []
    for i in range(2, n):
        dessiner(tab, multiples, premiers, nouveaux, figure)
        if tab[i] == True:
            nouveaux = []
            premiers.append(i)
            figure += 1
            dessiner(tab, multiples, premiers, nouveaux, figure)
            for multiple in range(2*i, n, i):
                tab[multiple] = False
                multiples.append(multiple)
                nouveaux.append(multiple)
        figure += 1
    return premiers


LARGEUR_CASE = 30
COULEUR_BASE = '#ddd'
COULEUR_PREMIER = '#90ee90'
COULEUR_COMPOSE = '#ff6666'
CONTOUR_BARRE = '#555'
COULEUR_NOUVEAUX = '#555'
TAILLE_POLICE = 20

print(crible(30))
