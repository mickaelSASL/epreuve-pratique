# Commentaires

Le problème revient à filtrer les clés d'un dictionnaire selon un critère portant sur les valeurs.

On présente ci-dessous différentes solutions parcourant le dictionnaire de façons différentes ainsi qu'une dernière méthode plus "fonctionnelle".

## Une solution possible

{{ IDE('exo_corr') }}

On débute par la création d'une liste ayant vocation à contenir le prénom des personnes dont l'anniversaire tombe le mois passé en argument (ligne 2).

Ensuite on parcourt les clés du dictionnaire en faisant `for prenom in naissances:` (ligne 3). Celles-ci étant des prénoms de personnes, la variable parcourant ces clés est naturellement nommée `prenom`.

Pour chaque clé, on teste si la valeur associée (le mois de naissance) est égale au mois passé en argument (ligne 4). Si c'est le cas, on ajoute le prénom de la personne à la liste des résultats (ligne 5).

Enfin, on renvoie la liste des personnes dont l'anniversaire correspond.

## Autres méthodes de parcours d'un dictionnaire

Il est aussi possible de parcourir les clés d'un dictionnaire en faisant `for prenom in naissances.keys():`. Le reste du code ne change pas.

{{ IDE('exo_var1') }}

Enfin, une dernière méthode propre aux dictionnaires permet de parcourir directement les couples `(cle, valeur)`. On fait alors ` for prenom, naissance in naissances.items():`. Le test qui suit est alors plus lisible.

{{ IDE('exo_var2') }}

## En une ligne !

{{ IDE('exo_var3') }}

Dans cette méthode, on crée une liste par compréhension parcourant les couples `(cle, valeur)` comme dans la méthode précédente et testant immédiatement la validité du mois de naissance.

On rappelle que la concision d'un code n'est pas forcément signe de qualité ! On peut perdre en lisibilité.

