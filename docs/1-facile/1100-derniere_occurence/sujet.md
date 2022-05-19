---
author: BNS2022-36.1, puis Sébastien HOARAU
title: Dernière occurrence 
tags:
    - boucle
---

Programmer la fonction `derniere_occurrence`, prenant en paramètre un tableau non vide d'entiers et un entier `cible`, et qui renvoie l'indice de la **dernière** occurrence de `cible`. Si l'élément n'est pas présent, la fonction renvoie la longueur du tableau.

> On n'utilisera pas la fonction `index`

!!! example "Exemples"

    ```python
    >>> derniere_occurrence([5, 3], 1)
    2
    >>> derniere_occurrence([2, 4], 2)
    0
    >>> derniere_occurrence([2, 3, 5, 2, 4], 2)
    3
    ```

{{ IDE('exo') }}
