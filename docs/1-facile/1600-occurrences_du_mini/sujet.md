---
author: BNS2022-18.1, puis Franck Chambon
title: Occurrences du minimum
tags:
  - boucle
---
# Occurrences du minimum

On dispose d'un tableau **non vide** `donnees` d'entiers : les mesures d'un phénomène étudié.

Écrire une fonction telle que `occurrences_mini(donnees)` renvoie un tuple composé de deux parties :

- la valeur minimale du phénomène étudié ;
- la liste des indices qui sont associés à la valeur minimale

!!! example "Exemples"
    ```pycon
    >>> donnees = [+13, +49, +13, +5]
    >>> occurrences_mini(donnees)
    (5, [3])
    ```

    ```pycon
    >>> donnees = [-84, +75, -84, 0, +16]
    >>> occurrences_mini(donnees)
    (-84, [0, 2])
    ```

{{ IDE('exo') }}
