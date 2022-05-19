---
author: Franck Chambon
title: arange
tags:
  - boucle
  - float
---
# Nombres espacés (2)

Pour construire la représentation graphique d'une fonction définie sur un intervalle, on calcule les images de plusieurs antécédents régulièrement espacés, ce qui permet de placer des points à relier. Encore faut-il disposer des antécédents. Comment les choisir ?

!!! example "Exemples"
    - Pour une fonction définie sur $[2.0, 4.0[$, avec des points régulièrement espacés par pas de $0.5$, on prend $2.0, 2.5, 3.0, 3.5$.
    - Pour une fonction définie sur $[5.0, 6.5[$, avec des points régulièrement espacés par pas de $0.25$, on prend $5.0, 5.25, 5.5, 5.75, 6.0, 6.25$.

En paramètre, on utilisera `debut`, `fin` et `pas` : des flottants ; `pas` est strictement positif. `debut` et `fin` décrivent l'intervalle dont on souhaite quelques éléments régulièrement espacés.

Écrire une fonction telle que `arange(debut, fin, pas)` renvoie une liste de flottants qui vérifie :
- les nombres sont tous strictement inférieurs à (`fin` moins $10^{-6}$) ;
- le premier, s'il existe, est `debut` ;
- les nombres sont rangés dans l'ordre croissant ;
- l'écart entre deux nombres consécutifs est `pas`.

!!! warning "Erreur relative"
    On rappelle qu'on ne fait pas de tests d'égalité entre flottants.
    
    La validation de **cet exercice** autorise des nombres avec une erreur relative de $10^{-6}$. **En contrepartie**, aucun nombre supérieur à (`fin` - $10^{-6}$) ne sera accepté dans la réponse.
    
    Concrètement, si vous devez écrire un test `#!py x < fin` alors vous devrez écrire `#!py x < fin - 10**-6` à la place.

!!! example "Exemples"

    ```pycon
    >>> arange(2.0, 4.0, 0.5)
    [2.0, 2.5, 3.0, 3.5]
    >>> arange(5.0, 6.5, 0.25)
    [5.0, 5.25, 5.5, 5.75, 6.0, 6.25]
    ```

{{ IDE('exo') }}
