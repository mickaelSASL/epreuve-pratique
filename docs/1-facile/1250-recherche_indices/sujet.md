---
author: BNS2022-40.1, puis Sébastien HOARAU
title: Recherche d'indices 
tags:
    - boucle
---

# Recherche des positions d'un élément dans un tableau

Écrire une fonction `recherche_positions` qui prend en paramètres `element` un nombre et `tableau` un tableau de nombres, et qui renvoie la liste croissante des indices de `element` dans `tableau` et la liste vide `[]` si `element` n'apparaît pas dans `tableau`.

> On n'utilisera ni la méthode `index`.

!!! example "Exemples"

    ```pycon
    >>> recherche_positions(3, [3, 2, 1, 3, 2, 1])
    [0, 3]
    >>> recherche_positions(4, [1, 2, 3])
    []
    >>> recherche_positions(10, [2, 10, 3, 10, 4, 10, 5])
    [1, 3, 5]
    ```

{{ IDE('exo') }}

