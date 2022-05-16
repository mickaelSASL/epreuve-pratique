from math import sqrt

def distance(point_1, point_2):
    """ Calcule et renvoie la distance euclidienne
    entre deux points. """
    # vous pouvez ajouter des lignes de code ici si besoin
    return sqrt(((...)**2 + (...)**2))

def plus_proche(points, depart):
    """ Renvoie le point du tableau points se trouvant à la plus 
    courte distance du point depart."""
    point_proche = points[0]
    dist_minimale = ...
    for i in range(1, ...):
        point = ...
        dist_courante = ...
        if dist_courante ...:
            point_proche = ...
            dist_minimale = ...
    return point_proche


# tests

assert plus_proche([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5)
assert plus_proche([(7, 9), (2, 5), (5, 2)], (7, 9)) == (7, 9)
