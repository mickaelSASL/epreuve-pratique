---
author: BNS2022-4.1, puis Franck Chambon
title: Nombres puis double
tags:
  - boucle
---
# Double du précédent dans un tableau

Écrire une fonction `nombres_puis_double` qui prend en paramètre un tableau de nombres entiers, et qui renvoie la liste (éventuellement vide) des couples d'entiers `(a, b)` qu'il peut y avoir dans le tableau tel que `b` suit `a` et `b = 2 * a`.

!!! example "Exemples"

    ```pycon
    >>> nombres_puis_double([1, 4, 2, 5])
    []
    >>> nombres_puis_double([1, 3, 6, 7])
    [(3, 6)]
    >>> nombres_puis_double([7, 1, 2, 5, 3, 6])
    [(1, 2), (3, 6)]
    >>> nombres_puis_double([5, 1, 2, 4, 8, -5, -10, 7])
    [(1, 2), (2, 4), (4, 8), (-5, -10)]
    ```

{{ IDE('exo') }}
