---
author: Charles Poulmaire et Franck Chambon
title: Écrêtage
tags:
  - boucle
---

# Écrêtage des valeurs d'un tableau

L'écrêtage d'un signal consiste à limiter l'amplitude du signal entre deux valeurs `x_min` et `x_max`. On peut également appliquer cela aux valeurs d'un tableau. Voici par exemple un tableau `valeurs` que l'on a écrêté entre $-150$ et $150$ pour donner le tableau `valeurs_ecretees` :

```python
valeurs          = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
valeurs_ecretees = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
```

*Question 1 :*

Compléter une fonction `limite_amplitude` qui prend en paramètre un nombre `x` ainsi que deux nombres `x_min` et `x_max` avec `x_min <= x_max` et qui renvoie :

- `x` si `x` est compris entre `x_min` et `x_max`,
- `x_min` si `x` est plus petit que `x_min`,
- `x_max` si `x` est plus grand que `x_max`.

!!! example "Exemple"

    ```pycon
    >>> limite_amplitude(34, -150, 150)
    34
    >>> limite_amplitude(-187, -150, 150)
    -150
    ```


*Question 2 :*

Compléter la fonction `ecrete` ci-dessous qui prend en paramètre un tableau de `valeurs` ainsi que `x_min` et `x_max` avec `x_min <= x_max` et renvoie un tableau des valeurs écrêtées entre `x_min` et `x_max`.

!!! example "Exemple"

    ```pycon
    >>> valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
    >>> ecrete(valeurs, -150, 150)
    [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
    ```

{{ IDE('exo') }}
