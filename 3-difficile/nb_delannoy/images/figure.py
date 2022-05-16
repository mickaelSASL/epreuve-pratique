import drawSvg as draw

chemins = {(0, 0): [[]]}

def delannoy(n, m):
    HORIZONTAL = 0
    VERTICAL   = 1
    DIAGONAL   = 2
    if (n, m) in chemins:
        return chemins[(n, m)]
    if n == 0:
        chemins[(0, m)] = [[HORIZONTAL] * m]
    elif m == 0:
        chemins[(n, 0)] = [[ VERTICAL ] * n]
    else:
        ans = (
              [c + [HORIZONTAL] for c in delannoy(n,     m - 1)]
            + [c + [ VERTICAL ] for c in delannoy(n - 1, m    )]
            + [c + [ DIAGONAL ] for c in delannoy(n - 1, m - 1)]
        )
        chemins[(n, m)] = ans
    return chemins[(n, m)]


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

n, m = 3, 3
large = 20
marge = 8

for i, chemin in enumerate(delannoy(n, m)):
    d = draw.Drawing(
        n * large + 2*marge,
        m * large + 2*marge,
        origin=(-marge, -marge),
        displayInline=False
    )
    ajoute_grille(d, n, m)
    d.append(draw.Circle(0, 0, 2,
            fill='red', stroke_width=2, stroke='red'))
    x1, y1 = 0, 0
    for v in chemin:
        if   v == 0:
            dx, dy = large,  0
        elif v == 1:
            dx, dy =  0, large
        elif v == 2:
            dx, dy = large, large
        x2, y2 = x1 + dx, y1 + dy
        d.append(draw.Lines(
            x1, y1, x2, y2,
            close=False,
            fill='none',
            stroke_width=4,
            stroke='red')
        )
        d.append(draw.Circle(x2, y2, 2,
                fill='red', stroke_width=2, stroke='red'))
        x1, y1 = x2, y2
        
    d.saveSvg(f'chemin_{i}.svg')
    print(f"![](images/chemin_{i}.svg)")
