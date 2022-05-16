import drawSvg as draw

def largeur_gauche(arbre, base=1.0):
    if arbre[0] == []:
        return base
    return base + largeur_gauche(arbre[0], base/2)

def largeur_droite(arbre, base=1.0):
    if arbre[1] == []:
        return base
    return base + largeur_droite(arbre[1], base/2)

def hauteur(arbre):
    if arbre == []:
        return 0
    return 1 + max(hauteur(arbre[0]), hauteur(arbre[1]))

def largeur(arbre):
    h = hauteur(arbre)
    return largeur_gauche(arbre, 2.0**(h-2)) + largeur_droite(arbre, 2.0**(h-2))

def gen_arbres(n):
    if n == 0:
        yield []
    else:
        for k in range(n):
            for gauche in gen_arbres(k):
                for droite in gen_arbres(n - 1 - k):
                    yield [gauche, droite]

def dessine(arbre, x, y, base):
    trait_couleur = 'grey'
    noeud_couleur = 'red'
    h_branche = 20
    for indice, coef in [(0, -1), (1, +1)]:
        # sous-arbre à gauche, puis à droite
        if arbre[indice]:
            xdx, ydy = x + coef * base, y - h_branche
            d.append(draw.Lines(x, y, xdx, ydy,
            close=False, stroke_width=4, stroke=trait_couleur))
            dessine(arbre[indice], xdx, ydy, base//2)
        else:
            xdx, ydy = x + coef * base * 4 //5 , y - h_branche * 4 // 5
            d.append(draw.Lines(x, y, xdx, ydy,
            close=False, stroke_width=2, stroke=trait_couleur))
            d.append(draw.Rectangle(xdx-3, ydy-3, 6, 6, fill='white', stroke_width=2, stroke=trait_couleur))

    d.append(draw.Circle(x, y, 6,
            fill=noeud_couleur, stroke_width=3, stroke=trait_couleur))


nb_noeud = 4

base = 4
marge = 10
for i, arbre in enumerate(gen_arbres(nb_noeud)):
    l_g = largeur_gauche(arbre, 2**nb_noeud)
    l_d = largeur_droite(arbre, 2**nb_noeud)
    h = nb_noeud + 1
    d = draw.Drawing(
        (l_g + l_d) * base + 2*marge, 20*h + marge,
        origin=(- base*l_g - marge, -20*h + marge//2),
        displayInline=False
    )
    dessine(arbre, 0, 0, base * 2**nb_noeud)
    d.saveSvg(f'example{i}.svg')

