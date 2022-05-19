# Commentaires

## Une solution possible

{{ IDE('exo_corr') }}


## Version fonctionnelle

Dans un style fonctionnel, on utilise `split` (mais c'était interdit justement pour cet exercice).

{{ IDE('exo_var2') }}

!!! tip "Remarque"

    - `discours.split(" ")` coupe `discours` uniquement aux espaces.
    - `discours.split()` coupe `discours` aux espaces, sauts de ligne, tabulations.

## Version avec `join`

Ici, la boucle pour construire un mot est courte ; dans le pire des cas on a des mots d'une vingtaine de lettres.

Mais dans **d'autres situations**, de longues boucles avec ajout de caractères dans une chaine de plus en plus grande, la chaine est recopiée intégralement à chaque tour (c'est un objet immuable). On aimerait éviter la recopie entière du début de la chaine.

Pour cela, on crée une liste vide, dans laquelle on ajoute tous les morceaux à chaque tour de boucle. Il n'y a pas de copie. À la fin, on colle les morceaux avec `join`.

{{ IDE('exo_var3') }}

Cette version est théoriquement meilleure, elle serait très utile dans un autre cadre.
