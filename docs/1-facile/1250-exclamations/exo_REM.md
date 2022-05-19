# Commentaires

{{ py('exo_corr') }}

- On initialise le nombre d'occurrences maximal ainsi que le courant, tous deux à zéro.
- On fait une boucle, sans avoir besoin de l'indice,
    - si le caractère correspond au motif, on incrémente le compteur courant, et on met à jour si nécessaire le maximum provisoire,
    - sinon on remet le compteur courant à 0
