---
author: BNS2022-38.1, puis Sébastien HOARAU
title: Tri par sélection 
tags:
    - tri
    - boucle
---

Écrire une fonction `tri_selection` qui prend en paramètre un tableau `tableau` de nombres entiers et qui trie ce tableau **en place** (c'est-à-dire que le tableau est modifié) par ordre croissant des valeurs.

On utilisera l’algorithme suivant :

- On parcourt le tableau de gauche à droite :
    - on recherche le minimum du tableau entre cette position courante et la fin du tableau 
    - on échange alors les 2 valeurs

!!! example "Exemples"

    ```pycon
    >>> tab = [1, 52, 6, -9, 12]
    >>> tri_selection(tab)
    >>> tab
    [-9, 1, 6, 12, 52]
    ```

    ```pycon
    >>> tab_vide = []
    >>> tri_selection(tab_vide)
    >>> tab_vide
    []
    ``` 

    ```pycon
    >>> singleton = [9]
    >>> tri_selection(singleton)
    >>> singleton
    [9]
    ```

{{ IDE('exo') }}
