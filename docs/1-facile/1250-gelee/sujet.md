---
author: Nicolas Revéret
title: Gelées
tags:
    - boucle
---

# Plus longue période de gelées

Un météorologue a relevé les températures au lever du jour dans sa rue.
Il souhaite déterminer la durée de la plus longue période de gelées consécutives durant ces relevés.

Vous devez écrire une fonction `gelees(temperatures)` qui renvoie la longueur de la plus longue séquence de nombres négatifs ou nuls consécutifs dans la liste.

Les températures sont données sous forme d'une liste de nombres :

```python
temperatures = [2, -3, -2, 0, 1, -1]
```

Si la liste est vide, la fonction renverra la valeur `0`.

On rappelle que l'eau gèle à partir de 0°C inclus.

!!! example "Exemples"

    ```pycon
    >>> gelees([2, -3, -2, 0, 1, -1])
    3
    >>> gelees([3, 2, 2])
    0
    >>> gelees([])
    0
    ```

{{ IDE('exo') }}