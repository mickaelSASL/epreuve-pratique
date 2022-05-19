---
author: Sébastien Hoarau, Mireille Coilhac, Franck Chambon
title: Rendu de monnaie
tags:
  - maths
---
# Rendu de monnaie avec 3 types de pièces

On s'intéresse au problème du rendu d'une quantité `somme_a_rendre` de monnaie.

On suppose qu'on dispose

- d'un nombre infini de billets de 5 euros,
- de pièces de 2 euros
- et de pièces de 1 euro.

Le but est d'écrire une fonction nommée `rendu` dont le paramètre est un entier positif `somme_a_rendre` qui renvoie un tuple de trois entiers qui correspondent aux nombres de billets de 5 euros de pièces de 2 euros et de pièces de 1 euro à rendre afin que le total rendu soit égal à `somme_a_rendre`.

On commencera par rendre le nombre maximal de billets de 5 euros, puis celui des pièces de 2 euros et enfin celui des pièces de 1 euro.


!!! example "Exemples"
    
    - Pour rendre 7 €, on rend 1 billet de 5 €, 1 pièce de 2 € et 0 pièce de 1 €.

    ```pycon
    >>> rendu(7)
    (1, 1, 0)
    ```

    - Pour rendre 10 €, on rend 2 billets de 5 €.
    - Pour rendre 13 €, on rend 2 billets de 5 €, une pièce de 2 € et une pièce de 1 €.
    - Pour rendre 32 €, on rend 6 billets de 5 € et une pièce de 2 €.
    
    ```pycon
    >>> rendu(10)
    (2, 0, 0)
    >>> rendu(13)
    (2, 1, 1)
    >>> rendu(32)
    (6, 1, 0)
    ```

{{ IDE('exo') }}
