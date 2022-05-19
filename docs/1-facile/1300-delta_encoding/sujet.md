---
author: BNS2022-3.1, puis Franck Chambon
title: Codage par différence
tags:
  - boucle
  - tuple
---
# _Delta encoding_

Le codage par différence (_delta encoding_ en anglais) permet de compresser un tableau de données en indiquant pour chaque donnée, sa différence avec la précédente (plutôt que la donnée elle-même). On se retrouve alors avec un tableau de données assez petites nécessitant moins de place en mémoire. Cette méthode se révèle efficace lorsque les valeurs consécutives sont proches. 

Programmer la fonction `delta_encoding` qui prend en paramètre un tableau non vide de nombres entiers et qui renvoie un tuple à deux éléments comprenant :

- En premier, la valeur initiale
- En second, le tableau des différences, contenant les valeurs entières compressées à l'aide de cette technique.

!!! example "Exemples"

    ```python
    >>> delta_encoding([1_000_000, 1_000_042, 1_000_040, 1_000_055, 1_000_010])
    (1000000, [42, -2, 15, -45])
    >>> delta_encoding([42])
    (42, [])
    ```

    Afin de gagner en lisibilité, Python autorise de placer un tiret-bas pour séparer les chiffres par paquets de trois. Ainsi `1_000_000` correspond bien à un million, et est plus lisible que `1000000`. En revanche, l'affichage en console d'un résultat ne l'utilise pas.

{{ IDE('exo') }}
