from math import sqrt

def distance(point_1, point_2):
    """ Calcule et renvoie la distance euclidienne
    entre deux points. """
    # vous pouvez ajouter des lignes de code ici si besoin
    x1, y1 = point_1
    x2, y2 = point_2
    return sqrt(((x1 - x2)**2 + (y1 - y2)**2))

def plus_proche(points, depart):
    """ Renvoie le point du tableau points se trouvant à la plus 
    courte distance du point depart."""
    point_proche = points[0]
    dist_minimale = distance(point_proche, depart)
    for i in range(1, len(points)):
        point = points[i]
        dist_courante = distance(point, depart)
        if dist_courante < dist_minimale:
            point_proche = point
            dist_minimale = dist_courante
    return point_proche
