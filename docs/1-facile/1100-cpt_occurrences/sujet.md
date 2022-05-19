---
author: BNS2022-1.1, puis Franck Chambon
title: Compte d'occurrences
tags:
  - boucle
  - string
---

# Occurrences d'un caractère dans un mot

Écrire une fonction `compte_occurrences` qui prend en paramètres `caractere`, un caractère (une chaine de caractères de longueur 1), et `mot`, une chaine de caractères, et qui renvoie le nombre d'occurrences de `caractere` dans `mot`, c'est-à-dire le nombre de fois où `caractere` apparait dans `mot`.

> On n'utilisera pas la méthode `count`.

!!! example "Exemples"

    ```pycon
    >>> compte_occurrences("e", "sciences")
    2
    >>> compte_occurrences("i", "mississippi")
    4
    >>> compte_occurrences("a", "mississippi")
    0
    ```

{{ IDE('exo') }}
