import drawSvg as draw

cumul_chemins = {-1:[], 0:[[]], 1:[[1, 2], [0]]}

def schroder(n):
    HORIZONTAL = 0
    DIAGONAL_H = 1
    DIAGONAL_B = 2
    if n in cumul_chemins:
        return cumul_chemins[n]
    else:
        ans = (
              [[DIAGONAL_H] + chemin_g + [DIAGONAL_B] + chemin_d for k in range(n+1) for chemin_g in schroder(k-1) for chemin_d in schroder(n-k)]
            + [[HORIZONTAL] + chemin for chemin in schroder(n-1)]
        )
        cumul_chemins[n] = ans
    return cumul_chemins[n]


def ajoute_grille(d, n, m):
    for i in range(n + 1):
        d.append(draw.Lines(
             0*m, 20*i,
            20*m, 20*i,
            close=False,
            stroke_width=2,
            stroke='grey')
        )
        d.append(draw.Circle(0*m,  20*i, 0.5,
                fill='grey', stroke_width=1, stroke='grey'))
        d.append(draw.Circle(20*m, 20*i, 0.5,
                fill='grey', stroke_width=1, stroke='grey'))

    for j in range(m + 1):
        d.append(draw.Lines(
            20*j,  0*n,
            20*j, 20*n,
            close=False,
            stroke_width=2,
            stroke='grey')
        )
        d.append(draw.Circle(20*j,  0*n, 0.5,
                fill='grey', stroke_width=1, stroke='grey'))
        d.append(draw.Circle(20*j, 20*n, 0.5,
                fill='grey', stroke_width=1, stroke='grey'))



large = 20
marge = 8
for n in range(2, 4):
    for i, chemin in enumerate(schroder(n)):
        d = draw.Drawing(
            2*n * large + 2*marge,
            n * large + 2*marge,
            origin=(-marge, -marge),
            displayInline=False
        )
        ajoute_grille(d, n, 2*n)
        d.append(draw.Circle(0, 0, 3,
                fill='red', stroke_width=3, stroke='red'))
        x1, y1 = 0, 0
        for v in chemin:
            if   v == 0:
                dx, dy = 2*large,  0
            elif v == 1:
                dx, dy =  large, +large
            elif v == 2:
                dx, dy = large, -large
            x2, y2 = x1 + dx, y1 + dy
            d.append(draw.Lines(
                x1, y1, x2, y2,
                close=False,
                fill='none',
                stroke_width=4,
                stroke='red')
            )
            d.append(draw.Circle(x2, y2, 3,
                    fill='red', stroke_width=3, stroke='red'))
            x1, y1 = x2, y2
            
        d.saveSvg(f'{n}_chemin_{i}.svg')
        print(f"![](images/{n}_chemin_{i}.svg)")
