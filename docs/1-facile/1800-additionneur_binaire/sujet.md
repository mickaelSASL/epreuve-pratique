---
title: Additionneur binaire
author: Vincent-Xavier Jumel
---
# Additionner deux nombres binaires

Dans cet exercice, les nombres binaires sont représentés par des listes où
les bits de poids forts sont situés en tête et les bits de poids faibles à
la fin. Ainsi la liste `[1, 0, 1, 1]` représente l'entier $1×2^3 + 0×2^2 +
1×2^2 + 1×2^0 = 11$. **On ne demande pas de convertir les nombres dans cet
exercice.**

On rappelle que l'addition  de nombres binaires se fait chiffre à chiffre (ici
bit à bit), sans oublier l'éventuelle retenue. Ainsi la somme de 1 et 1
renvoie 0 et conserve 1 en retenue. On peut par exemple écrire :

```
retenues :    1   1 1
-----------
            1 0 1 0 1 1 0 1
          + 0 0 1 0 1 1 1 0
            ---------------
            1 1 0 1 1 0 1 1
```
Écrire une fonction `addition_binaire` qui prends deux listes de bits en
entrée et qui renvoie une liste de bits en sortie, correspondant à
l'addition binaire des deux nombres.

> On n'utilisera ni la fonction `bin` ni les opérateurs `+`, `//` ou `%`.

Une fonction `additionneur` est fournie. Elle prend en entrée trois valeurs
et renvoie deux nombres, le premier étant le chiffre de poids fort de la
somme et le second le chiffre de poids faible. Le premier chiffre peut-être
interprété comme une retenue. Cette fonction simule les circuits
électroniques usuellement présents dans un additionneur binaire. Ces circuits
sont habituellement codés avec des portes logiques correspondant aux
opérateurs `xor` (ou exclusif), `or` (ou), `and` (et) et `nand` (non et)

![](Schema_logique_additionneur_complet.gif)

!!! example "Exemples"
    ```pycon
    >>> additionneur(1, 1, 0)
    (1, 0)
    >>> addition_binaire([1, 1, 1], [1, 1, 1])
    [1, 1, 1, 0]
    >>> addition_binaire([1, 0, 1, 0], [1])
    [1, 0, 1, 1]
    >>> addition_binaire([1, 0, 1, 0], [1,  1])
    [1, 1, 0, 1]
    >>> addition_binaire([1, 0, 1, 0], [1, 1, 0])
    [1, 0, 0, 0, 0]
    >>> addition_binaire([1, 0, 1, 0], [0])
    [1, 0, 1, 0]
    >>> addition_binaire([1, 0, 1, 0], [1, 0, 1, 0])
    [1, 0, 1, 0, 0]
    >>> addition_binaire([1, 0, 1, 0], [1, 0, 0, 0, 0])
    [1, 1, 0, 1, 0]
    >>> addition_binaire([1, 0, 1, 0], [1, 1, 1, 1, 1])
    [1, 0, 1, 0, 0, 1]
    >>> addition_binaire([1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0])
    [1, 1, 0, 1, 1, 0, 1, 1]
    ```

{{ IDE('exo') }}

!!! tip "Aide"
    On peut afficher la liste des retenues pour s'aider dans le
    développement de la fonction.
