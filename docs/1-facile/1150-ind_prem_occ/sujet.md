---
author: BNS2022-8.1, puis Franck Chambon
title: Indice première occurrence
tags:
  - boucle
---

# Indice de la première occurrence

Écrire une fonction `indice` qui prend en paramètres `element` un nombre entier, `tableau` un tableau de nombres entiers, et qui renvoie l'indice de la **première** occurrence de `element` dans `tableau`.

La fonction devra renvoyer `None` si `element` est absent de `tableau`.

> On n'utilisera pas ni la fonction `index`, ni la fonction `find`.

!!! example "Exemples"

    ```pycon
    >>> indice(1, [10, 12, 1, 56])
    2
    >>> indice(1, [1, 50, 1])
    0
    >>> indice(15, [8, 9, 10, 15])
    3
    >>> indice(1, [2, 3, 4]) is None
    True
    ```

{{ IDE('exo') }}
