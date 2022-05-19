# Commentaires

{{ py('exo_corr', 0, '# TESTS') }}

Il s'agit d'une recherche de maximum. On initialise le pseudo ayant le plus de « *like* » à `""` et la variable `max_likes` à `-1`. On prend soin dès la première itération de la boucle de remplacer ces valeurs par celle associées au premier pseudo contenu dans le dictionnaire.

Lors du parcours de pseudos, on compare le nombre de « *like* » associé à la valeur conservée jusqu'à maintenant. Si elle est plus importante on met à jour. Si les nombres de « *like* » sont égaux, on ne met à jour que si l'on a aussi `pseudo < max_pseudo`.

