---
author: BNS2022-5.1, puis Franck Chambon
title: Valeurs extrêmes
tags:
  - dictionnaire
  - boucle
---

# Dictionnaire de valeurs extrêmes

Écrire une fonction `extremes` qui prend en paramètre un tableau `valeurs` de nombres non triés, et qui renvoie la plus petite ainsi que la plus grande valeur du tableau sous la forme d'un dictionnaire à deux clés `'min'` et `'max'`. Si les extrêmes n'existent pas, on utilisera `None` pour chacun.

> On n'utilisera pas les fonctions `min` et `max` fournies par le langage.

!!! example "Exemples"

    ```pycon
    >>> valeurs = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
    >>> resultat = extremes(valeurs)
    >>> resultat
    {'min': -2, 'max': 9}
    ```

    ```pycon
    >>> valeurs = [37, 37]
    >>> resultat = extremes(valeurs)
    >>> resultat
    {'min': 37, 'max': 37}
    ```

    ```pycon
    >>> valeurs = []
    >>> resultat = extremes(valeurs)
    >>> resultat
    {'min': None, 'max': None}
    ```


{{ IDE('exo') }}
