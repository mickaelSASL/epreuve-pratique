---
author: BNS2022-23.1, puis Nicolas Revéret
title: Top-Likes !
tags:
  - dictionnaire
  - boucle
---

# Top-Likes !

Sur le réseau social TipTop, on s'intéresse au nombre de « *like* » des abonnés. Les données sont stockées dans un dictionnaire où les clés sont les pseudos et les valeurs correspondantes sont les nombres de « *like* » comme ci-dessous :

```python
{'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
```

Écrire une fonction `top_likes` qui :

  * prend en paramètre un dictionnaire `likes` non-vide dont les clés sont des chaînes de caractères et les valeurs associées des entiers,
  
  * renvoie un tuple dont :
      * la première valeur est la clé du dictionnaire associée à la valeur maximale ; en cas d'égalité sur plusieurs clés, on choisira la plus petite suivant l'ordre alphabétique,
      * la seconde valeur est la valeur maximale présente dans le dictionnaire.

!!! example "Exemples"

    ```pycon
    >>> top_likes({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})
    ('Ada', 201)
    >>> top_likes({'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50})
    ('Alan', 222)
    >>> top_likes({'David': 222, 'Ada': 201, 'Alan': 222, 'Tim': 50})
    ('Alan', 222)
    ```

{{ IDE('exo') }}
