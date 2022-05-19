---
author: Franck Chambon
title: Palindrome
tags:
  - boucle
  - string
---
# Création de palindrome

Un palindrome est un mot qui se lit lettre par lettre, de gauche à droite, exactement comme de droite à gauche.

!!! example "Exemples"

    - `"kayak"`, `"radar"`, `"rdtxtdr"` sont des palindromes de longueur impaire.
    - `"elle"`, `"serres"`, `"afeefa"` sont des palindromes de longueur paire.

On peut construire un palindrome à partir d'une chaine de caractères et d'un **autre palindrome**, en concaténant la chaine, le palindrome et la chaine renversée.

1. `"kayak"` peut s'obtenir avec `"ka", "y", "ak"`
2. `"radar"` peut s'obtenir avec `"r", "ada", "r"`
3. `"rdtxtdr"` peut s'obtenir avec `"rd", "txt", "dr"`
4. `"elle"` peut s'obtenir avec `"e", "ll", "e"`
5. `"serres"` peut s'obtenir avec `"ser", "", "res"`
6. `"arfettttefra"` peut s'obtenir avec `"ar", "fettttef", "ra"`

Écrire une fonction `cree_palindrome` qui prend deux paramètres : une chaine de caractères `mot` et une chaine de caractères qui sera `palindrome`. La fonction renvoie le palindrome créé en concaténant `mot`, `palindrome`, et le renversement de `mot`.

!!! example "Exemples"

    ```pycon
    >>> cree_palindrome("ka", "y")
    'kayak'
    >>> cree_palindrome("ser", "")
    'serres'
    >>> cree_palindrome("r", "ada")
    'radar'
    >>> cree_palindrome("ar", "fettttef")
    'arfettttefra'
    ```

> - **On n'utilisera pas** les tranches de chaines de caractères !
> - On garantit que `palindrome` est bien un palindrome, il sera inutile de le vérifier.

{{ IDE('exo') }}
