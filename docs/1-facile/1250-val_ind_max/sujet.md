---
author: BNS2022-6.1, puis Franck Chambon
title: Valeur et indice du max
tags:
  - boucle
  - tuple
---
# Maximum d'un tableau : valeur et indice

Écrire une fonction `valeur_et_indice_du_max` qui prend en paramètre une liste de nombres entiers `valeurs` et renvoie un couple donnant le plus grand élément de cette liste, ainsi que l'indice de la **première apparition** de ce maximum dans la liste. Pour une liste vide, la fonction renvoie `#!python (None, None)`

!!! example "Exemples"

    ```pycon
    >>> valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
    (9, 3)
    >>> valeur_et_indice_du_max([1, 1, 1, 99, 99])
    (99, 3)
    >>> valeur_et_indice_du_max([10])
    (10, 0)
    >>> valeur_et_indice_du_max([])
    (None, None)
    ```

{{ IDE('exo') }}
