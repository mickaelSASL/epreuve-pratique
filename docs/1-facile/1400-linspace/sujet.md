---
author: Franck Chambon
title: linspace
tags:
  - boucle
  - float
---
# Nombres espacés

Pour construire la représentation graphique d'une fonction définie sur un intervalle,
on calcule les images de plusieurs antécédents régulièrement espacés, ce qui permet de placer des points à relier. Encore faut-il disposer des antécédents. Comment les choisir ?

!!! example "Exemples"
    - Pour une fonction définie sur $[2.0, 4.0]$, avec 5 points régulièrement espacés, on prend $2.0, 2.5, 3.0, 3.5, 4.0$.
    - Pour une fonction définie sur $[5.0, 6.5[$, avec 6 points régulièrement espacés, on prend $5.0, 5.25, 5.5, 5.75, 6.0, 6.25$.

Dans notre exercice, on se limite aux intervalles de type fermé $[a\,;\,b]$ ou non fermé $[a\,;\,b[$ pour lesquels on souhaite proposer $n$ nombres régulièrement espacés, où $n$ est un nombre entier au moins égal à 2.

- Si l'intervalle est de type $[a\,;\,b]$, on part de $a$ et on avance par pas de $\dfrac{b-a}{n-1}$.
- Si l'intervalle est de type $[a\,;\,b[$, on part de $a$ et on avance par pas de $\dfrac{b-a}{n}$.

Écrire une fonction telle que `linspace(a, b, n, ferme)` renvoie une liste de $n$ nombres flottants régulièrement espacés en partant de `a`, où `a` et `b` sont des flottants, `n` est un entier au moins égal à 2, et `ferme` est un booléen.

- Si le booléen `ferme` est égal à `True`, on choisira un pas adapté à l'intervalle fermé $[a\,;\,b]$. 
- Si le booléen `ferme` est égal à `False`, on choisira un pas adapté à l'intervalle non fermé $[a\,;\,b[$. 

> On garantit que $a$ et $b$ sont compris entre $-10^9$ et $10^9$, et que la différence $b-a$ est supérieure à $10^{-9}$. On garantit que $n$ est inférieur à $1000$.

!!! example "Exemples"

    ```pycon
    >>> linspace(2.0, 4.0, 5, True)
    [2.0, 2.5, 3.0, 3.5, 4.0]
    >>> linspace(5.0, 9.5, 6, False)
    [5.0, 5.75, 6.5, 7.25, 8.0, 8.75]
    ```

{{ IDE('exo') }}
