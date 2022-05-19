---
author: BNS2022-20.1, puis Franck Chambon
title: Liste des différences
tags:
  - boucle
---
# Tester si deux listes contiennent des valeurs différentes

Un laboratoire reçoit des résultats depuis deux sources différentes. Les résultats sont deux tableaux d'entiers `source_1` et `source_2` de même longueur.

Quand deux résultats concordent, on considère qu'il n'y aura pas à refaire l'expérience, on le codera par `False`, mais si les résultats sont différents, on considère qu'il faudra refaire cette expérience, on le codera par `True`.

Écrire une fonction telle que `differences(source_1, source_2)` renvoie un tableau de la longueur commune à `source_1` et `source_2` rempli de booléens.


!!! example "Exemples"
    ```pycon
    >>> differences([14, 87, 22, 5, 65], [14, 86, 27, 5, 65])
    [False, True, True, False, False]
    >>> differences([-54], [-54])
    [False]
    >>> differences([7, 8], [7, 11])
    [False, True]
    >>> differences([], [])
    []
    ```

{{ IDE('exo') }}
