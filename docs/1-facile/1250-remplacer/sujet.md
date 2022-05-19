---
author: Nicolas Revéret
title: Remplacer une valeur
tags:
    - boucle
status: validé par Quentin (qkzk), FNativel, Serge, Frank
---

# Remplacer une valeur

Écrire la fonction `remplacer` prenant en argument :

* une liste d'entiers `valeurs`
* un entier `valeur_cible`
* un entier `nouvelle_valeur`

et renvoyant une **nouvelle** liste contenant les mêmes valeurs que `valeurs`, dans le même ordre, sauf `valeur_cible` qui a été remplacé par `nouvelle_valeur`. 

**La liste passée en paramètre ne doit pas être modifiée**.

!!! example "Exemples"

    ```pycon
    >>> valeurs = [3, 8, 7]
    >>> remplacer(valeurs, 3, 0)
    [0, 8, 7]
    >>> valeurs
    [3, 8, 7]
    ```

    ```pycon
    >>> valeurs = [3, 8, 3, 5]
    >>> remplacer(valeurs, 3, 0)
    [0, 8, 0, 5]
    >>> liste
    [3, 8, 3, 5]
    ```

{{ IDE('exo') }}