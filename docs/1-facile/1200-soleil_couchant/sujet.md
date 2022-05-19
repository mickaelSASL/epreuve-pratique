---
author: Franck Chambon
title: Soleil couchant
tags:
  - boucle
  - adhoc
---
# Soleil couchant sur les bâtiments

Lorsque des bâtiments sont alignés, ils se font de l'ombre les uns les autres. Dans cet exercice, nous sommes au soleil couchant, les rayons du soleil sont donc supposés horizontaux.

![](images/soleil-couchant.svg)

Le schéma ci-dessus illustre un soleil couchant qui éclaire 9 bâtiments, les rayons du soleil sont représentés par des flèches horizontales.

- Les bâtiments aux indices `0` et `3` reçoivent des rayons de soleil alors que les bâtiments aux indices `1` et `2` sont masqués.
- Les **4** bâtiments aux indices `[0, 3, 6, 9]` reçoivent des rayons de soleil sur au moins un étage et sont donc éclairés, alors que les autres ne le sont pas.
- Il n'y a pas de bâtiment à l'indice `4`.


Écrire une fonction `nb_batiments_eclaires` qui prend en argument la liste `hauteurs` des bâtiments et qui renvoie le nombre de bâtiments éclairés.

- La hauteur des bâtiments (en nombre d'étages) est donnée par une liste d'entiers positifs. Une hauteur de zéro étage signifie l'absence de bâtiment à l'endroit désigné.
    - Pour l'exemple ci-dessus, cette liste est `[2, 1, 2, 4, 0, 4, 5, 3, 5, 6]`. 


!!! example "Exemples"

    ```pycon
    >>> nb_batiments_eclaires([2, 1, 2, 4, 0, 4, 5, 3, 5, 6])
    4
    >>> nb_batiments_eclaires([0, 3, 1, 2])
    1
    ```

{{ IDE('exo') }}
