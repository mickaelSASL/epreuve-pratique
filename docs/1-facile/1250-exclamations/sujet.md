---
author: Franck Chambon
title: Exclamations
tags:
  - boucle
  - string
---
# Nombre d'exclamations consécutives !!!

Dans une phrase !!! écrite !!! certains utilisateurs abusent des points d'exclamations !! Ce pour différentes raisons ! Bref.

Écrire une fonction `nb_max_consecutifs` qui prend un caractère `motif` (une chaine de caractères de longueur 1), et une chaine de caractères `phrase` à analyser. La fonction renvoie le nombre maximal d'occurrences consécutives de `motif` dans `phrase`.

!!! example "Exemples"

    ```pycon
    >>> phrase = "Dans une phrase !!! écrite !!! certains utilisateurs abusent des points d'exclamations !! Ce pour différentes raisons ! Bref."
    >>> nb_max_consecutifs("!", phrase)
    3
    ```

    ```pycon
    >>> phrase = "Un mot    puis        un        autre avec espaces."
    >>> nb_max_consecutifs(" ", phrase)
    8
    ```

    ```pycon
    >>> expression = "((2 * x + 3) / (x + 1))"
    >>> nb_max_consecutifs("(", expression)
    2
    >>> nb_max_consecutifs("-", expression)
    0
    ```


{{ IDE('exo') }}

