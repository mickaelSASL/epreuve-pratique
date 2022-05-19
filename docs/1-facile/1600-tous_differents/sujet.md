---
author: Romain Janvier
title: Tous différents
tags:
  - boucle
---

# Tableau avec des éléments tous différents

Un tableau peut contenir plusieurs fois le même élément. C'est le cas du tableau `tableau1` ci-dessous :
```python
tableau1 = [1, 2, 3, 6, 2, 4, 5]
```
La valeur `2` est deux fois dans ce tableau.

Au contraire, dans le tableau `tableau2`, toutes les valeurs sont uniques :
```python
tableau2 = ['chien', 'chat', 'lion', 'poisson']
```

Écrire une fonction `tous_differents` qui prend un tableau `tableau` et renvoie un booléen indiquant si toutes les valeurs de `tableau` sont différentes ou non.

!!! info "Taille des tableaux"
    Pour limiter le temps de calcul, on se limitera à des tests avec des
    tableaux de moins de 100 éléments.

??? tip "Utilisation de `range(a, b)`"
    On pourra éventuellement utiliser `range(a, b)` qui renvoie toutes
    les valeurs entières allant de `a` à `b-1` inclus.

!!! example "Exemples"

    ```pycon
    >>> tableau1 = [1, 2, 3, 6, 2, 4, 5]
    >>> tous_differents(tableau1)
    False
    ```

    ```pycon
    >>> tableau2 = ['chien', 'chat', 'lion', 'poisson']
    >>> tous_differents(tableau2)
    True
    ```
    
{{ IDE('exo') }}

