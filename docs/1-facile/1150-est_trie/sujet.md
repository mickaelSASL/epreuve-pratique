---
author: BNS2022-37.1, puis Sébastien HOARAU
title: Est trié ? 
tags:
    - boucle
---

Programmer la fonction `est_trie` qui prend en paramètre un tableau de valeurs numériques et qui renvoie `True` si ce tableau est trié dans l'ordre croissant, `False` sinon.

!!! example "Exemples"

    ```pycon
    >>> est_trie([0, 5, 8, 8, 9])
    True
    >>> est_trie([8, 12, 4])
    False
    >>> est_trie([-1, 4])
    True
    >>> est_trie([5])
    True
    >>> est_trie([])
    True
    ```

{{ IDE('exo') }}
