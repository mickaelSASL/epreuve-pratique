import drawSvg as draw

def largeur_gauche(arbre, base=1.0):
    if arbre == []:
        return 0
    if len(arbre) == 1:
        return largeur_gauche(arbre[0], base)
    return base + largeur_gauche(arbre[0], base/2)

def largeur_droite(arbre, base=1.0):
    if arbre == []:
        return 0
    if len(arbre) == 1:
        return largeur_droite(arbre[0], base)
    return base + largeur_droite(arbre[1], base/2)

def hauteur(arbre):
    if arbre == []:
        return 0
    return 1 + max(hauteur(t) for t in arbre)

def largeur(arbre):
    return largeur_gauche(arbre, 2.0) + largeur_droite(arbre, 2.0)

def gen_arbres(n):
    if n == 0:
        pass
    elif n == 1:
        yield []
    else:
        for central in gen_arbres(n-1):
            yield [central]
        for k in range(n):
            for gauche in gen_arbres(k):
                for droite in gen_arbres(n - 1 - k):
                    yield [gauche, droite]

""""
for t in gen_arbres(5):
    print(t, largeur(t))
exit(0)
"""

t = [[[[]]], []]

def dessine(arbre, x, y, base):
    trait_couleur = 'grey'
    noeud_couleur = 'red'
    h_branche = 40
    if len(arbre) == 1:
        xdx, ydy = x, y - h_branche
        d.append(draw.Lines(x, y, xdx, ydy,
        close=False, stroke_width=4, stroke=trait_couleur))
        dessine(arbre[0], xdx, ydy, base)
    if len(arbre) == 2:
        for indice, coef in [(0, -1), (1, +1)]:
            # sous-arbre à gauche, puis à droite
                xdx, ydy = x + coef * base, y - h_branche
                d.append(draw.Lines(x, y, xdx, ydy,
                close=False, stroke_width=4, stroke=trait_couleur))
                dessine(arbre[indice], xdx, ydy, base/2)

    d.append(draw.Circle(x, y, 6,
            fill=noeud_couleur, stroke_width=3, stroke=trait_couleur))



nb_noeud = 8

base = 40
marge = 10
for i, arbre in enumerate(gen_arbres(nb_noeud)):
        l_g = largeur_gauche(arbre, 1)
        l_d = largeur_droite(arbre, 1)
        d = draw.Drawing(
            (l_g + l_d) * base + 2*marge, 40*nb_noeud + marge,
            origin=(- base*l_g - marge, -40*nb_noeud + marge//2),
            displayInline=False
        )
        dessine(arbre, 0, 0, base)
        d.saveSvg(f'{nb_noeud}_arbre_{i}.svg')
        print(f'![](images/{nb_noeud}_arbre_{i}.svg)')
    

